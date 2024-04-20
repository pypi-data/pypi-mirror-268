from __future__ import annotations 
from datetime import (
    datetime,
    date
)
from decimal import Decimal 
from enum import Enum 
import re
import sys
from typing import (
    Any,
    List,
    Literal,
    Dict,
    Optional,
    Union
)
from pydantic.version import VERSION  as PYDANTIC_VERSION 
if int(PYDANTIC_VERSION[0])>=2:
    from pydantic import (
        BaseModel,
        ConfigDict,
        Field,
        field_validator
    )
else:
    from pydantic import (
        BaseModel,
        Field,
        validator
    )

metamodel_version = "None"
version = "0.0.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass


class TestSourceEnum(str, Enum):
    # (External) Subject Matter Expert
    SME = "SME"
    # Subject Matter User Reasonably Familiar, generally Translator-internal biomedical science expert
    SMURF = "SMURF"
    # Git hub hosted issue from which a test asset/case/suite may be derived.
    GitHubUserFeedback = "GitHubUserFeedback"
    # Technical Advisory Committee, generally posting semantic use cases as Translator Feedback issues
    TACT = "TACT"
    # Curated benchmark tests
    BenchMark = "BenchMark"
    # Translator funded KP or ARA team generating test assets/cases/suites for their resources.
    TranslatorTeam = "TranslatorTeam"
    # Current SRI_Testing-like test data edges specific to KP or ARA components
    TestDataLocation = "TestDataLocation"


class TestObjectiveEnum(str, Enum):
    # Acceptance (pass/fail) test
    AcceptanceTest = "AcceptanceTest"
    # Semantic benchmarking
    BenchmarkTest = "BenchmarkTest"
    # Quantitative test
    QuantitativeTest = "QuantitativeTest"
    # Release-specific TRAPI and Biolink Model ("reasoner-validator") compliance validation
    StandardsValidationTest = "StandardsValidationTest"
    # Knowledge graph "One Hop" query navigation integrity
    OneHopTest = "OneHopTest"


class TestEnvEnum(str, Enum):
    """
    Testing environments within which a TestSuite is run by a TestRunner scheduled by the TestHarness.
    """
    # Development
    dev = "dev"
    # Continuous Integration
    ci = "ci"
    # Test
    test = "test"
    # Production
    prod = "prod"


class FileFormatEnum(str, Enum):
    """
    Text file formats for test data sources.
    """
    TSV = "TSV"
    YAML = "YAML"
    JSON = "JSON"


class ExpectedOutputEnum(str, Enum):
    """
    Expected output values for instances of Test Asset or Test Cases(?). (Note: does this Enum overlap with 'ExpectedResultsEnum' below?)
    """
    Acceptable = "Acceptable"
    BadButForgivable = "BadButForgivable"
    NeverShow = "NeverShow"
    TopAnswer = "TopAnswer"
    OverlyGeneric = "OverlyGeneric"


class TestIssueEnum(str, Enum):
    causes_not_treats = "causes not treats"
    # 'Text Mining Knowledge Provider' generated relationship?
    TMKP = "TMKP"
    category_too_generic = "category too generic"
    contraindications = "contraindications"
    chemical_roles = "chemical roles"
    test_issue = "test_issue"


class SemanticSeverityEnum(str, Enum):
    """
    From Jenn's worksheet, empty or ill defined (needs elaboration)
    """
    High = "High"
    Low = "Low"
    NotApplicable = "NotApplicable"


class DirectionEnum(str, Enum):
    increased = "increased"
    decreased = "decreased"


class ExpectedResultsEnum(str, Enum):
    """
    Does this Enum overlap with 'ExpectedOutputEnum' above?
    """
    # The query should return the result in this test case
    include_good = "include_good"
    # The query should not return the result in this test case
    exclude_bad = "exclude_bad"


class NodeEnum(str, Enum):
    """
    Target node of a Subject-Predicate-Object driven query
    """
    subject = "subject"
    object = "object"


class QueryTypeEnum(str, Enum):
    """
    Query
    """
    treats = "treats"


class TrapiTemplateEnum(str, Enum):
    ameliorates = "ameliorates"
    treats = "treats"
    three_hop = "three_hop"
    drug_treats_rare_disease = "drug_treats_rare_disease"
    drug_to_gene = "drug-to-gene"


class ComponentEnum(str):
    """
    Translator components are identified by their InfoRes identifiers.
    """
    pass


class TestPersonaEnum(str, Enum):
    """
    User persona context of a given test.
    """
    All = "All"
    # An MD or someone working in the clinical field.
    Clinical = "Clinical"
    # Looking for an answer for a specific patient.
    LookUp = "LookUp"
    # Someone working on basic biology questions or drug discoveries where the study of the biological mechanism.
    Mechanistic = "Mechanistic"


class TestCaseResultEnum(str, Enum):
    # test case result indicating success.
    PASSED = "PASSED"
    # test case result indicating failure.
    FAILED = "FAILED"
    # test case result indicating that the specified test was not run.
    SKIPPED = "SKIPPED"


class TestEntityParameter(ConfiguredBaseModel):
    """
    A single 'tag = value' pair (where 'value' is a simple string).
    """
    parameter: Optional[str] = Field(None, description="""Name of a TestParameter.""")
    value: Optional[str] = Field(None, description="""(String) value of a TestParameter.""")


class Qualifier(TestEntityParameter):
    parameter: Optional[str] = Field(None, description="""The 'parameter' of a Qualifier should be a `qualifier` slot name from the Biolink Model ('biolink' namespace) 'biolink:qualifier' hierarchy.""")
    value: Optional[str] = Field(None, description="""The 'value' of should be a suitable value generally drawn from an applicable Biolink Model (\"Enum\") value set of the specified Qualifier.""")


class TestEntity(ConfiguredBaseModel):
    """
    Abstract global 'identification' class shared as a parent with all major model classes within the data model for Translator testing.
    """
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    test_runner_settings: Optional[List[str]] = Field(default_factory=list, description="""Scalar parameters for the TestRunner processing a given TestEntity.""")


class TestMetadata(TestEntity):
    """
    Represents metadata related to (external SME, SMURF, Translator feedback,  large scale batch, etc.) like the provenance of test assets, cases and/or suites.
    """
    test_source: Optional[TestSourceEnum] = Field(None, description="""Provenance of a specific set of test assets, cases and/or suites.  Or, the person who cares about this,  know about this.  We would like this to be an ORCID eventually, but currently it is just a string.""")
    test_reference: Optional[str] = Field(None, description="""Document URL where original test source particulars are registered (e.g. Github repo)""")
    test_objective: Optional[TestObjectiveEnum] = Field(None, description="""Testing objective behind specified set of test particulars (e.g. acceptance pass/fail; benchmark; quantitative; standards compliance; graph navigation integrity)""")
    test_annotations: Optional[List[TestEntityParameter]] = Field(default_factory=list, description="""Metadata annotation.""")
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    test_runner_settings: Optional[List[str]] = Field(default_factory=list, description="""Scalar parameters for the TestRunner processing a given TestEntity.""")


class TestAsset(TestEntity):
    """
    Represents a Test Asset, which is a single specific instance of TestCase-agnostic semantic parameters representing the specification of a Translator test target with inputs and (expected) outputs.
    """
    input_id: Optional[str] = Field(None)
    input_name: Optional[str] = Field(None)
    input_category: Optional[str] = Field(None)
    predicate_id: Optional[str] = Field(None)
    predicate_name: Optional[str] = Field(None)
    output_id: Optional[str] = Field(None)
    output_name: Optional[str] = Field(None)
    output_category: Optional[str] = Field(None)
    association: Optional[str] = Field(None, description="""Specific Biolink Model association 'category' which applies to the test asset defined knowledge statement""")
    qualifiers: Optional[List[Qualifier]] = Field(default_factory=list, description="""Optional qualifiers which constrain to the test asset defined knowledge statement. Note that this field records such qualifier slots and values as tag=value pairs, where the tag is the Biolink Model qualifier slot named and the value is an acceptable (Biolink Model enum?) value of the said qualifier slot.""")
    expected_output: Optional[str] = Field(None)
    test_issue: Optional[TestIssueEnum] = Field(None)
    semantic_severity: Optional[SemanticSeverityEnum] = Field(None)
    in_v1: Optional[bool] = Field(None)
    well_known: Optional[bool] = Field(None)
    test_reference: Optional[str] = Field(None, description="""Document URL where original test source particulars are registered (e.g. Github repo)""")
    test_metadata: TestMetadata = Field(..., description="""Test metadata describes the external provenance, cross-references and objectives for a given test.""")
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""One or more 'tags' slot values (inherited from TestEntity) should generally be defined to specify TestAsset membership in a \"Block List\" collection""")
    test_runner_settings: Optional[List[str]] = Field(default_factory=list, description="""Scalar settings for the TestRunner, e.g. \"inferred\"""")


class AcceptanceTestAsset(TestAsset):
    """
    Model derived from Jenn's test asset design and Shervin's runner JSON here as an example.
    """
    must_pass_date: Optional[date] = Field(None, description="""The date by which this test must pass""")
    must_pass_environment: Optional[TestEnvEnum] = Field(None, description="""The deployment environment within which this test must pass.""")
    scientific_question: Optional[str] = Field(None, description="""The full human-readable scientific question a SME would ask, which is encoded into the test asset.""")
    string_entry: Optional[str] = Field(None, description="""The object of the core triple to be tested""")
    direction: Optional[DirectionEnum] = Field(None, description="""The direction of the expected query result triple""")
    answer_informal_concept: Optional[str] = Field(None, description="""An answer that is returned from the test case, note: this must be combined with the expected_result to form a complete answer.  It might make sense to couple these in their own object instead of strictly sticking to the flat schema introduced by the spreadsheet here: https://docs.google.com/spreadsheets/d/1yj7zIchFeVl1OHqL_kE_pqvzNLmGml_FLbHDs-8Yvig/edit#gid=0""")
    expected_result: Optional[ExpectedResultsEnum] = Field(None, description="""The expected result of the query""")
    top_level: Optional[int] = Field(None, description="""The answer must return in these many results""")
    query_node: Optional[NodeEnum] = Field(None, description="""The node of the (templated) TRAPI query to replace""")
    notes: Optional[str] = Field(None, description="""The notes of the query""")
    input_id: Optional[str] = Field(None)
    input_name: Optional[str] = Field(None)
    input_category: Optional[str] = Field(None)
    predicate_id: Optional[str] = Field(None)
    predicate_name: Optional[str] = Field(None)
    output_id: Optional[str] = Field(None)
    output_name: Optional[str] = Field(None)
    output_category: Optional[str] = Field(None)
    association: Optional[str] = Field(None, description="""Specific Biolink Model association 'category' which applies to the test asset defined knowledge statement""")
    qualifiers: Optional[List[Qualifier]] = Field(default_factory=list, description="""Optional qualifiers which constrain to the test asset defined knowledge statement. Note that this field records such qualifier slots and values as tag=value pairs, where the tag is the Biolink Model qualifier slot named and the value is an acceptable (Biolink Model enum?) value of the said qualifier slot.""")
    expected_output: Optional[str] = Field(None)
    test_issue: Optional[TestIssueEnum] = Field(None)
    semantic_severity: Optional[SemanticSeverityEnum] = Field(None)
    in_v1: Optional[bool] = Field(None)
    well_known: Optional[bool] = Field(None)
    test_reference: Optional[str] = Field(None, description="""Document URL where original test source particulars are registered (e.g. Github repo)""")
    test_metadata: TestMetadata = Field(..., description="""Test metadata describes the external provenance, cross-references and objectives for a given test.""")
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""One or more 'tags' slot values (inherited from TestEntity) should generally be defined to specify TestAsset membership in a \"Block List\" collection""")
    test_runner_settings: Optional[List[str]] = Field(default_factory=list, description="""Scalar settings for the TestRunner, e.g. \"inferred\"""")


class TestEdgeData(TestAsset):
    """
    Represents a single Biolink Model compliant instance of a subject-predicate-object edge that can be used for testing.
    """
    input_id: Optional[str] = Field(None)
    input_name: Optional[str] = Field(None)
    input_category: Optional[str] = Field(None)
    predicate_id: Optional[str] = Field(None)
    predicate_name: Optional[str] = Field(None)
    output_id: Optional[str] = Field(None)
    output_name: Optional[str] = Field(None)
    output_category: Optional[str] = Field(None)
    association: Optional[str] = Field(None, description="""Specific Biolink Model association 'category' which applies to the test asset defined knowledge statement""")
    qualifiers: Optional[List[Qualifier]] = Field(default_factory=list, description="""Optional qualifiers which constrain to the test asset defined knowledge statement. Note that this field records such qualifier slots and values as tag=value pairs, where the tag is the Biolink Model qualifier slot named and the value is an acceptable (Biolink Model enum?) value of the said qualifier slot.""")
    expected_output: Optional[str] = Field(None)
    test_issue: Optional[TestIssueEnum] = Field(None)
    semantic_severity: Optional[SemanticSeverityEnum] = Field(None)
    in_v1: Optional[bool] = Field(None)
    well_known: Optional[bool] = Field(None)
    test_reference: Optional[str] = Field(None, description="""Document URL where original test source particulars are registered (e.g. Github repo)""")
    test_metadata: TestMetadata = Field(..., description="""Test metadata describes the external provenance, cross-references and objectives for a given test.""")
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""One or more 'tags' slot values (inherited from TestEntity) should generally be defined to specify TestAsset membership in a \"Block List\" collection""")
    test_runner_settings: Optional[List[str]] = Field(default_factory=list, description="""Scalar settings for the TestRunner, e.g. \"inferred\"""")


class Precondition(TestEntity):
    """
    Represents a precondition for a TestCase
    """
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    test_runner_settings: Optional[List[str]] = Field(default_factory=list, description="""Scalar parameters for the TestRunner processing a given TestEntity.""")


class TestCase(TestEntity):
    """
    Represents a single enumerated instance of Test Case, derived from a  given collection of one or more TestAsset instances (the value of the 'test_assets' slot) which define the 'inputs' and 'outputs' of the TestCase, used to probe a particular test condition.
    """
    query_type: Optional[QueryTypeEnum] = Field(None, description="""Type of TestCase query.""")
    test_assets: List[TestAsset] = Field(default_factory=list, description="""One or more 'tags' slot values (inherited from TestEntity) should generally be defined as filters to specify TestAsset membership in 'test_assets' slot (\"Block List\") collection.""")
    preconditions: Optional[List[str]] = Field(default_factory=list)
    trapi_template: Optional[TrapiTemplateEnum] = Field(None, description="""A template for a query, which can be used to generate a query for a test case.  note: the current enumerated values for this slot come from the Benchmarks repo config/benchmarks.json \"templates\" collection and refer to the \"name\" field of each template.  Templates themselves are currently stored in the config/[source_name]/templates directory.""")
    test_case_objective: Optional[TestObjectiveEnum] = Field(None, description="""Testing objective behind specified set of test particulars (e.g. acceptance pass/fail; benchmark; quantitative; standards compliance; graph navigation integrity)""")
    test_case_source: Optional[TestSourceEnum] = Field(None, description="""Provenance of a specific set of test assets, cases and/or suites.  Or, the person who cares about this,  know about this.  We would like this to be an ORCID eventually, but currently it is just a string.""")
    test_case_predicate_name: Optional[str] = Field(None)
    test_case_predicate_id: Optional[str] = Field(None)
    test_case_input_id: Optional[str] = Field(None)
    qualifiers: Optional[List[Qualifier]] = Field(default_factory=list, description="""Optional qualifiers which constrain to the test asset defined knowledge statement. Note that this field records such qualifier slots and values as tag=value pairs, where the tag is the Biolink Model qualifier slot named and the value is an acceptable (Biolink Model enum?) value of the said qualifier slot.""")
    input_category: Optional[str] = Field(None)
    output_category: Optional[str] = Field(None)
    components: Optional[List[ComponentEnum]] = Field(default_factory=list, description="""The component that this test case is intended to run against.  Most often this is the ARS for  acceptance tests, but for the Benchmarks repo integration, this can also be individual components of the system like Aragorn, or ARAX.""")
    test_env: Optional[TestEnvEnum] = Field(None, description="""Deployment environment within which the associated TestSuite is run.""")
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""One or more 'tags' slot values (slot inherited from TestEntity) should generally be defined as filters to specify TestAsset membership in a \"Block List\" collection.""")
    test_runner_settings: Optional[List[str]] = Field(default_factory=list, description="""Scalar parameters for the TestRunner processing a given TestEntity.""")


class AcceptanceTestCase(TestCase):
    """
    See AcceptanceTestAsset above for more details.
    """
    query_type: Optional[QueryTypeEnum] = Field(None, description="""Type of TestCase query.""")
    test_assets: List[AcceptanceTestAsset] = Field(default_factory=list, description="""One or more 'tags' slot values (inherited from TestEntity) should generally be defined as filters to specify TestAsset membership in 'test_assets' slot (\"Block List\") collection.""")
    preconditions: Optional[List[str]] = Field(default_factory=list)
    trapi_template: Optional[TrapiTemplateEnum] = Field(None, description="""A template for a query, which can be used to generate a query for a test case.  note: the current enumerated values for this slot come from the Benchmarks repo config/benchmarks.json \"templates\" collection and refer to the \"name\" field of each template.  Templates themselves are currently stored in the config/[source_name]/templates directory.""")
    test_case_objective: Optional[TestObjectiveEnum] = Field(None, description="""Testing objective behind specified set of test particulars (e.g. acceptance pass/fail; benchmark; quantitative; standards compliance; graph navigation integrity)""")
    test_case_source: Optional[TestSourceEnum] = Field(None, description="""Provenance of a specific set of test assets, cases and/or suites.  Or, the person who cares about this,  know about this.  We would like this to be an ORCID eventually, but currently it is just a string.""")
    test_case_predicate_name: Optional[str] = Field(None)
    test_case_predicate_id: Optional[str] = Field(None)
    test_case_input_id: Optional[str] = Field(None)
    qualifiers: Optional[List[Qualifier]] = Field(default_factory=list, description="""Optional qualifiers which constrain to the test asset defined knowledge statement. Note that this field records such qualifier slots and values as tag=value pairs, where the tag is the Biolink Model qualifier slot named and the value is an acceptable (Biolink Model enum?) value of the said qualifier slot.""")
    input_category: Optional[str] = Field(None)
    output_category: Optional[str] = Field(None)
    components: Optional[List[ComponentEnum]] = Field(default_factory=list, description="""The component that this test case is intended to run against.  Most often this is the ARS for  acceptance tests, but for the Benchmarks repo integration, this can also be individual components of the system like Aragorn, or ARAX.""")
    test_env: Optional[TestEnvEnum] = Field(None, description="""Deployment environment within which the associated TestSuite is run.""")
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""One or more 'tags' slot values (slot inherited from TestEntity) should generally be defined as filters to specify TestAsset membership in a \"Block List\" collection.""")
    test_runner_settings: Optional[List[str]] = Field(default_factory=list, description="""Scalar parameters for the TestRunner processing a given TestEntity.""")


class QuantitativeTestCase(TestCase):
    """
    Assumed additional model from Shervin's runner JSON here as an example.  This schema is not yet complete.
    """
    query_type: Optional[QueryTypeEnum] = Field(None, description="""Type of TestCase query.""")
    test_assets: List[TestAsset] = Field(default_factory=list, description="""One or more 'tags' slot values (inherited from TestEntity) should generally be defined as filters to specify TestAsset membership in 'test_assets' slot (\"Block List\") collection.""")
    preconditions: Optional[List[str]] = Field(default_factory=list)
    trapi_template: Optional[TrapiTemplateEnum] = Field(None, description="""A template for a query, which can be used to generate a query for a test case.  note: the current enumerated values for this slot come from the Benchmarks repo config/benchmarks.json \"templates\" collection and refer to the \"name\" field of each template.  Templates themselves are currently stored in the config/[source_name]/templates directory.""")
    test_case_objective: Optional[TestObjectiveEnum] = Field(None, description="""Testing objective behind specified set of test particulars (e.g. acceptance pass/fail; benchmark; quantitative; standards compliance; graph navigation integrity)""")
    test_case_source: Optional[TestSourceEnum] = Field(None, description="""Provenance of a specific set of test assets, cases and/or suites.  Or, the person who cares about this,  know about this.  We would like this to be an ORCID eventually, but currently it is just a string.""")
    test_case_predicate_name: Optional[str] = Field(None)
    test_case_predicate_id: Optional[str] = Field(None)
    test_case_input_id: Optional[str] = Field(None)
    qualifiers: Optional[List[Qualifier]] = Field(default_factory=list, description="""Optional qualifiers which constrain to the test asset defined knowledge statement. Note that this field records such qualifier slots and values as tag=value pairs, where the tag is the Biolink Model qualifier slot named and the value is an acceptable (Biolink Model enum?) value of the said qualifier slot.""")
    input_category: Optional[str] = Field(None)
    output_category: Optional[str] = Field(None)
    components: Optional[List[ComponentEnum]] = Field(default_factory=list, description="""The component that this test case is intended to run against.  Most often this is the ARS for  acceptance tests, but for the Benchmarks repo integration, this can also be individual components of the system like Aragorn, or ARAX.""")
    test_env: Optional[TestEnvEnum] = Field(None, description="""Deployment environment within which the associated TestSuite is run.""")
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""One or more 'tags' slot values (slot inherited from TestEntity) should generally be defined as filters to specify TestAsset membership in a \"Block List\" collection.""")
    test_runner_settings: Optional[List[str]] = Field(default_factory=list, description="""Scalar parameters for the TestRunner processing a given TestEntity.""")


class TestSuiteSpecification(TestEntity):
    """
    Parameters for a Test Case instances either dynamically generated from some external source of Test Assets.
    """
    test_data_file_locator: Optional[str] = Field(None, description="""An web accessible file resource link to test entity data (e.g. a web accessible text file of Test Asset entries)""")
    test_data_file_format: Optional[FileFormatEnum] = Field(None, description="""File format of test entity data (e.g. TSV, YAML or JSON)""")
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    test_runner_settings: Optional[List[str]] = Field(default_factory=list, description="""Scalar parameters for the TestRunner processing a given TestEntity.""")


class TestSuite(TestEntity):
    """
    Specification of a set of Test Cases, one of either with a static list of 'test_cases' or a dynamic 'test_suite_specification' slot values. Note: at least one slot or the other, but generally not both(?) needs to be present.
    """
    test_metadata: TestMetadata = Field(..., description="""Test metadata describes the external provenance, cross-references and objectives for a given test.""")
    test_persona: Optional[TestPersonaEnum] = Field(None, description="""A Test persona describes the user or operational context of a given test.""")
    test_cases: Optional[Dict[str, TestCase]] = Field(default_factory=dict, description="""List of explicitly enumerated Test Cases.""")
    test_suite_specification: Optional[TestSuiteSpecification] = Field(None, description="""Declarative specification of a Test Suite of Test Cases whose generation is deferred, (i.e. within a Test Runner) or whose creation is achieved by stream processing of an external data source.""")
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    test_runner_settings: Optional[List[str]] = Field(default_factory=list, description="""Scalar parameters for the TestRunner processing a given TestEntity.""")


class AcceptanceTestSuite(TestSuite):
    test_metadata: TestMetadata = Field(..., description="""Test metadata describes the external provenance, cross-references and objectives for a given test.""")
    test_persona: Optional[TestPersonaEnum] = Field(None, description="""A Test persona describes the user or operational context of a given test.""")
    test_cases: Optional[Dict[str, TestCase]] = Field(default_factory=dict, description="""List of explicitly enumerated Test Cases.""")
    test_suite_specification: Optional[TestSuiteSpecification] = Field(None, description="""Declarative specification of a Test Suite of Test Cases whose generation is deferred, (i.e. within a Test Runner) or whose creation is achieved by stream processing of an external data source.""")
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    test_runner_settings: Optional[List[str]] = Field(default_factory=list, description="""Scalar parameters for the TestRunner processing a given TestEntity.""")


class BenchmarkTestSuite(ConfiguredBaseModel):
    """
    JsonObj(is_a='TestSuite')
    """
    pass


class StandardsComplianceTestSuite(TestSuite):
    """
    Test suite for testing Translator components against releases of standards like TRAPI and the Biolink Model.
    """
    test_metadata: TestMetadata = Field(..., description="""Test metadata describes the external provenance, cross-references and objectives for a given test.""")
    test_persona: Optional[TestPersonaEnum] = Field(None, description="""A Test persona describes the user or operational context of a given test.""")
    test_cases: Optional[Dict[str, TestCase]] = Field(default_factory=dict, description="""List of explicitly enumerated Test Cases.""")
    test_suite_specification: Optional[TestSuiteSpecification] = Field(None, description="""Declarative specification of a Test Suite of Test Cases whose generation is deferred, (i.e. within a Test Runner) or whose creation is achieved by stream processing of an external data source.""")
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    test_runner_settings: Optional[List[str]] = Field(default_factory=list, description="""Scalar parameters for the TestRunner processing a given TestEntity.""")


class OneHopTestSuite(TestSuite):
    """
    Test case for testing the integrity of \"One Hop\" knowledge graph retrievals sensa legacy SRI_Testing harness.
    """
    test_metadata: TestMetadata = Field(..., description="""Test metadata describes the external provenance, cross-references and objectives for a given test.""")
    test_persona: Optional[TestPersonaEnum] = Field(None, description="""A Test persona describes the user or operational context of a given test.""")
    test_cases: Optional[Dict[str, TestCase]] = Field(default_factory=dict, description="""List of explicitly enumerated Test Cases.""")
    test_suite_specification: Optional[TestSuiteSpecification] = Field(None, description="""Declarative specification of a Test Suite of Test Cases whose generation is deferred, (i.e. within a Test Runner) or whose creation is achieved by stream processing of an external data source.""")
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    test_runner_settings: Optional[List[str]] = Field(default_factory=list, description="""Scalar parameters for the TestRunner processing a given TestEntity.""")


class TestCaseResult(TestEntity):
    """
    The outcome of a TestRunner run of one specific TestCase.
    """
    test_suite_id: Optional[str] = Field(None, description="""CURIE id of a TestSuite registered in the system.""")
    test_case: Optional[TestCase] = Field(None, description="""Slot referencing a single TestCase.""")
    test_case_result: Optional[TestCaseResultEnum] = Field(None, description="""Encoded result of a single test run of a given test case""")
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    test_runner_settings: Optional[List[str]] = Field(default_factory=list, description="""Scalar parameters for the TestRunner processing a given TestEntity.""")


class TestRunSession(TestEntity):
    """
    Single run of a TestRunner in a given environment, with a specified set of test_entities (generally, one or more instances of TestSuite).
    """
    components: Optional[List[ComponentEnum]] = Field(default_factory=list, description="""The component that this test case is intended to run against.  Most often this is the ARS for  acceptance tests, but for the Benchmarks repo integration, this can also be individual components of the system like Aragorn, or ARAX.""")
    test_env: Optional[TestEnvEnum] = Field(None, description="""Deployment environment within which the associated TestSuite is run.""")
    test_runner_name: Optional[str] = Field(None, description="""Global system name of a TestRunner.""")
    test_run_parameters: Optional[List[TestEntityParameter]] = Field(default_factory=list, description="""Different TestRunners could expect additional global test configuration parameters, like the applicable TRAPI version (\"trapi_version\") or Biolink Model versions (\"biolink_version\").""")
    test_entities: Optional[Dict[str, TestEntity]] = Field(default_factory=dict, description="""Different TestRunners could expect specific kinds of TestEntity as an input.  These 'test_entities' are one or more instances of TestAsset, TestCase or (preferably?) TestSuite.""")
    test_case_results: Optional[Dict[str, TestCaseResult]] = Field(default_factory=dict, description="""One or more instances of TestCaseResult.""")
    timestamp: Optional[datetime ] = Field(None, description="""Date time when a given entity was created.""")
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    test_runner_settings: Optional[List[str]] = Field(default_factory=list, description="""Scalar parameters for the TestRunner processing a given TestEntity.""")


class TestOutput(TestEntity):
    """
    The output of a TestRunner run of one specific TestCase.
    """
    test_case_id: Optional[str] = Field(None, description="""CURIE id of a TestCase registered in the system.""")
    pks: Optional[List[str]] = Field(default_factory=list, description="""Primary keys for a given ARA result set from a SmokeTest result for a given TestCase.""")
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    test_runner_settings: Optional[List[str]] = Field(default_factory=list, description="""Scalar parameters for the TestRunner processing a given TestEntity.""")


class TestResultPKSet(TestEntity):
    """
    Primary keys for a given ARA result set from a SmokeTest result for a given TestCase.
    """
    parent_pk: Optional[str] = Field(None)
    merged_pk: Optional[str] = Field(None)
    aragorn: Optional[str] = Field(None)
    arax: Optional[str] = Field(None)
    unsecret: Optional[str] = Field(None)
    bte: Optional[str] = Field(None)
    improving: Optional[str] = Field(None)
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    test_runner_settings: Optional[List[str]] = Field(default_factory=list, description="""Scalar parameters for the TestRunner processing a given TestEntity.""")


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
TestEntityParameter.model_rebuild()
Qualifier.model_rebuild()
TestEntity.model_rebuild()
TestMetadata.model_rebuild()
TestAsset.model_rebuild()
AcceptanceTestAsset.model_rebuild()
TestEdgeData.model_rebuild()
Precondition.model_rebuild()
TestCase.model_rebuild()
AcceptanceTestCase.model_rebuild()
QuantitativeTestCase.model_rebuild()
TestSuiteSpecification.model_rebuild()
TestSuite.model_rebuild()
AcceptanceTestSuite.model_rebuild()
BenchmarkTestSuite.model_rebuild()
StandardsComplianceTestSuite.model_rebuild()
OneHopTestSuite.model_rebuild()
TestCaseResult.model_rebuild()
TestRunSession.model_rebuild()
TestOutput.model_rebuild()
TestResultPKSet.model_rebuild()

