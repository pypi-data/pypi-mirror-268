from urllib import response

from src.translator_testing_model.datamodel.pydanticmodel import TestAsset, TestCase, TestSuite, TestMetadata, Qualifier
import csv
import json
import requests
import yaml
import bmt

toolkit = bmt.Toolkit()
import enum


class SuiteNames(enum.Enum):
    pass_fail = "pass_fail"
    quantitative = "quantitative"
    full = "full"


def retrieve_predicate_mapping():
    # URL of the YAML file
    predicate_mapping_url = "https://w3id.org/biolink/predicate_mapping.yaml"

    # Fetch the content of the YAML file
    request_response = requests.get(predicate_mapping_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the YAML content into a Python dictionary
        predicate_mapping = yaml.safe_load(request_response.content)

        # Return the parsed dictionary
        return predicate_mapping
    else:
        # Handle errors or unsuccessful requests
        print(f"Failed to retrieve the file. HTTP Status Code: {request_response.status_code}")
        return None


def parse_tsv(filename):
    """
    Parse a TSV file and return a list of dictionaries.

    :param filename: The path to the TSV file.
    :return: A list of dictionaries, where each dictionary represents a row in the TSV.
    """
    with open(filename, newline='', encoding='utf-8') as tsvfile:
        # Use csv.DictReader, specifying the delimiter as a tab
        reader = csv.DictReader(tsvfile, delimiter='\t')

        # Convert the reader into a list of dictionaries
        return list(reader)


# Functions to create TestAssets, TestCases, and TestSuite
def create_test_assets_from_tsv(test_assets: list, suite_name: SuiteNames, toolkit):
    assets = []
    for row in test_assets:
        if row.get("Relationship") == "" or row.get("OutputID") == "" or row.get("InputID") == "":
            print("Skipping row with missing relationship, input or output ID", row.get("id"))
            continue
        if suite_name == SuiteNames.pass_fail:
            if get_expected_output(row) != "TopAnswer" and get_expected_output(row) != "NeverShow":
                continue
            else:
                ta = create_test_asset(row, toolkit)
                assets.append(ta)

        else:
            ta = create_test_asset(row, toolkit)
        assets.append(ta)
    return assets


def get_converted_predicate(specified_predicate, toolkit):
    if specified_predicate == "decreases abundance or activity of":
        specified_predicate = "decreases activity or abundance of"
    element = toolkit.get_element(specified_predicate)
    if element is not None:
        return element.name.replace(" ", "_"), "", "", "biolink:" + element.name
    else:
        for collection in toolkit.pmap.values():
            for item in collection:
                if item.get("mapped predicate") == specified_predicate:
                    return (
                        item.get("predicate").replace(" ", "_"),
                        item.get("object aspect qualifier"),
                        item.get("object direction qualifier"),
                        "biolink:" + item.get("qualified predicate"),
                    )
    return specified_predicate, "", "", ""


def get_category(prefixes, id):
    if id.startswith("NCBIGene:"):
        return 'biolink:Gene'
    elif id.startswith("MONDO:"):
        return 'biolink:Disease'
    elif id.startswith("UBERON:"):
        return 'biolink:AnatomicalEntity'
    elif id.startswith("HP:"):
        return 'biolink:PhenotypicFeature'
    elif id.startswith("DRUGBANK:") or id.startswith("CHEBI:") or any(id.startswith(prefix) for prefix in prefixes):
        return 'biolink:ChemicalEntity'
    return None


def get_expected_output(row):
    output = row.get("Expected Result / Suggested Comparator")
    if output in ["4_NeverShow", "3_BadButForgivable", "2_Acceptable", "1_TopAnswer", "5_OverlyGeneric"]:
        return output.split("_")[1]
    print(f"{row.get('id')} has invalid expected output: {output}")
    return None


def create_test_asset(row, toolkit):
    specified_predicate = row.get("Relationship").lower().strip()
    converted_predicate, biolink_object_aspect_qualifier, biolink_object_direction_qualifier, biolink_qualified_predicate = get_converted_predicate(specified_predicate, toolkit)

    expected_output = get_expected_output(row)
    if not expected_output:
        return None

    chem_prefixes = toolkit.get_element("chemical entity").id_prefixes
    input_category = get_category(chem_prefixes, row.get("InputID"))
    output_category = get_category(chem_prefixes, row.get("OutputID"))

    ta = TestAsset(
        id=row.get("id").replace(":", "_"),
        name=f"{expected_output}: {row.get('OutputName').strip()} {specified_predicate} {row.get('InputName').strip()}",
        description=f"{expected_output}: {row.get('OutputName').strip()} {specified_predicate} {row.get('InputName').strip()}",
        input_id=row.get("InputID").strip(),
        predicate_name=converted_predicate,
        predicate_id=f"biolink:{converted_predicate}",
        output_id=row.get("OutputID").strip(),
        output_name=row.get("OutputName").strip(),
        output_category=output_category,
        expected_output=expected_output.strip(),
        test_metadata=TestMetadata(
            id=1,
            test_source="SMURF",
            test_reference=row.get("Translator GitHubIssue").strip() if row.get("Translator GitHubIssue") else None,
            test_objective="AcceptanceTest"
        ),
        input_category=input_category,
    )
    ta.input_name = row.get("InputName").strip()
    ta.test_runner_settings = [row.get("Settings").lower()]

    if biolink_qualified_predicate:
        ta.qualifiers = [
            Qualifier(parameter="biolink_qualified_predicate", value=biolink_qualified_predicate),
            Qualifier(parameter="biolink_object_aspect_qualifier", value=biolink_object_aspect_qualifier.replace(" ", "_")),
            Qualifier(parameter="biolink_object_direction_qualifier", value=biolink_object_direction_qualifier),
        ]

    ta.well_known = row.get("Well Known") == "yes"

    return ta


def create_test_cases_from_test_assets(test_assets, test_case_model):
    # Group test assets based on input_id and relationship
    grouped_assets = {}
    for test_asset in test_assets:
        key = (test_asset.input_id, test_asset.predicate_name)
        if key not in grouped_assets:
            grouped_assets[key] = []
        grouped_assets[key].append(test_asset)

    # Create test cases from grouped test assets
    test_cases = []
    for idx, (key, assets) in enumerate(grouped_assets.items()):
        test_case_id = f"TestCase_{idx}"
        descriptions = '; '.join(asset.description for asset in assets)
        test_case = test_case_model(id=test_case_id,
                                    name="what " + key[1] + " " + key[0],
                                    description=descriptions,
                                    test_env="ci",
                                    components=["ars"],
                                    test_case_objective="AcceptanceTest",
                                    test_assets=assets,
                                    test_runner_settings=["inferred"]
                                    )
        if test_case.test_assets is None:
            print("test case has no assets", test_case)

        if test_case.test_case_objective == "AcceptanceTest":
            test_input_id = ""
            test_case_predicate_name = ""
            test_case_qualifiers = []
            input_category = ""
            output_category = ""
            for asset in assets:
                # these all assume group by applies to the same input_id and predicate_name
                test_input_id = asset.input_id
                test_case_predicate_name = asset.predicate_name
                test_case_qualifiers = asset.qualifiers
                input_category = asset.input_category
                output_category = asset.output_category

            test_case.test_case_input_id = test_input_id
            test_case.test_case_predicate_name = test_case_predicate_name
            test_case.test_case_predicate_id = "biolink:" + test_case_predicate_name
            test_case.qualifiers = test_case_qualifiers
            test_case.input_category = input_category
            test_case.output_category = output_category
            test_cases.append(test_case)

    return test_cases


def create_test_suite_from_test_cases(test_cases, test_suite_model):
    test_suite_id = "TestSuite_1"
    test_cases_dict = {test_case.id: test_case for test_case in test_cases}

    ci_test_case_collection = []
    stress_test_case_collection = []

    for i in range(len(test_cases)):
        if i % 10 == 9:  # If the index is a multiple of 10 (accounting for 0-indexing)
            ci_test_case_collection.append(test_cases[i])
        if i % 2 == 1:    # If the index is a multiple of 5 (accounting for 0-indexing)
            stress_test_case_collection.append(test_cases[i])
    test_cases_dict_ci = {test_case.id: test_case for test_case in ci_test_case_collection}
    test_cases_dict_stress = {test_case.id: test_case for test_case in stress_test_case_collection}
    print(len(stress_test_case_collection), "number_stress")
    print(len(test_cases_dict_ci), "number_ci")
    print(len(test_cases_dict), "number_total")

    # CI and DELTA have the same
    # number: https://docs.google.com/document/d/1UNX7Z4Wjwg0FPA58VBNMYducNCq44LykzQ6_JU7FEEo/edit
    print(len(test_cases_dict_ci), "number_delta")

    tmd = TestMetadata(id=1,
                       test_source="SMURF",
                       test_objective="AcceptanceTest")

    test_suite_ci_id = "TestSuite_2"
    ci_tmd = TestMetadata(id=2,
                          test_source="SMURF",
                          test_objective="AcceptanceTest")


    test_suite_stress_id = "TestSuite_3"
    stress_tmd = TestMetadata(id=3,
                              test_source="SMURF",
                              test_objective="AcceptanceTest")

    test_suite_delta_id = "TestSuite_4"
    delta_tmd = TestMetadata(id=4,
                             test_source="SMURF",
                             test_objective="AcceptanceTest")

    return (test_suite_model(id=test_suite_id, test_cases=test_cases_dict, test_metadata=tmd),
            test_suite_model(id=test_suite_ci_id, test_cases=test_cases_dict_ci, test_metadata=ci_tmd),
            test_suite_model(id=test_suite_stress_id, test_cases=test_cases_dict_stress, test_metadata=stress_tmd),
            test_suite_model(id=test_suite_delta_id, test_cases=test_cases_dict_ci, test_metadata=delta_tmd))


def create_benchmark_test_case(subset: bool) -> TestCase or list[TestCase]:
    url = 'https://raw.githubusercontent.com/TranslatorSRI/Benchmarks/main/benchmarks_runner/config/benchmarks.json'
    benchmark_cases = []
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response content as JSON
        data = response.json()
        for k, v in data.items():
            tmd = TestMetadata(id=1,
                               test_source="SMURF",
                               test_objective="QuantitativeTest")
            test_asset = TestAsset(id=k,
                                   name=k,
                                   description=k,
                                   test_metadata=tmd
                                   )
            test_case = TestCase(id=k,
                                 name=k,
                                 description=k,
                                 test_assets=[test_asset],
                                 test_env="ci",
                                 components=["ars"],
                                 test_case_objective="QuantitativeTest",
                                 test_runner_settings=["limit_queries"]
                                 )
            file_prefix = k
            if subset and k.startswith("DrugCentral_subset"):
                benchmark_cases.append(test_case)
                filename = f"{file_prefix}.json"
                with open(filename, 'w', encoding='utf-8') as file:
                    json.dump(test_case.dict(), file, ensure_ascii=False, indent=4)
                return test_case
            else:
                filename = f"{file_prefix}.json"
                with open(filename, 'w', encoding='utf-8') as file:
                    json.dump(test_case.dict(), file, ensure_ascii=False, indent=4)
                benchmark_cases.append(test_case)
        return benchmark_cases

    else:
        print(f'Failed to retrieve the file. Status code: {response.status_code}')


def dump_to_json(file_prefix):
    filename = f"{file_prefix.id}.json"
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(file_prefix.dict(), file, ensure_ascii=False, indent=4)


if __name__ == '__main__':

    # Reading the TSV file
    tsv_file_path = 'pf_test_assets_032224.tsv'
    tsv_data = parse_tsv(tsv_file_path)

    # Create TestAsset objects
    pf_test_assets = create_test_assets_from_tsv(tsv_data, SuiteNames.pass_fail, toolkit)

    # Create TestCase objects
    test_cases = create_test_cases_from_test_assets(pf_test_assets, TestCase)

    for i, item in enumerate(test_cases):
        identifier = item.id
        dump_to_json(item)

    for i, item in enumerate(pf_test_assets):
        identifier = item.id
        dump_to_json(item)

    # Create Benchmark Test Cases - subset for now
    benchmark_case = create_benchmark_test_case(subset=True)
    if isinstance(benchmark_case, list):
        test_cases.extend(benchmark_case)
    else:
        test_cases.append(benchmark_case)

    # Assemble into a TestSuite
    (test_suite_all, test_suite_CI, test_suite_STRESS, test_suite_DELTA) = create_test_suite_from_test_cases(test_cases, TestSuite)
    #

    # Convert to JSON and save to file
    test_suite_json_all = test_suite_all.json(indent=4)
    test_suite_json_CI = test_suite_CI.json(indent=4)
    test_suite_json_STRESS = test_suite_STRESS.json(indent=4)
    test_suite_json_DELTA = test_suite_DELTA.json(indent=4)


    suite_json_output_path = 'semantic_smoke_test_suite_TEST.json'

    with open(suite_json_output_path, 'w') as file:
        file.write(test_suite_json_all)

    sst_ci_json_output_path = 'semantic_smoke_test_suite_CI.json'

    with open(sst_ci_json_output_path, 'w') as file:
        file.write(test_suite_json_CI)

    suite_delta_json_output_path_prod = 'stress_test_PROD.json'

    with open(suite_delta_json_output_path_prod, 'w') as file:
        file.write(test_suite_json_STRESS)

    suite_delta_json_output_path_prod = 'semantic_delta_and_time_profiling_PROD.json'

    with open(suite_delta_json_output_path_prod, 'w') as file:
        file.write(test_suite_json_DELTA)
