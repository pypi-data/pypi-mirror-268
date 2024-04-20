-- # Class: "TestEntityParameter" Description: "A single 'tag = value' pair (where 'value' is a simple string)."
--     * Slot: id Description: 
--     * Slot: parameter Description: Name of a TestParameter.
--     * Slot: value Description: (String) value of a TestParameter.
--     * Slot: TestMetadata_id Description: Autocreated FK slot
--     * Slot: TestRunSession_id Description: Autocreated FK slot
-- # Class: "Qualifier" Description: ""
--     * Slot: id Description: 
--     * Slot: parameter Description: The 'parameter' of a Qualifier should be a `qualifier` slot name from the Biolink Model ('biolink' namespace) 'biolink:qualifier' hierarchy.
--     * Slot: value Description: The 'value' of should be a suitable value generally drawn from an applicable Biolink Model ("Enum") value set of the specified Qualifier.
--     * Slot: TestAsset_id Description: Autocreated FK slot
--     * Slot: AcceptanceTestAsset_id Description: Autocreated FK slot
--     * Slot: TestEdgeData_id Description: Autocreated FK slot
--     * Slot: TestCase_id Description: Autocreated FK slot
--     * Slot: AcceptanceTestCase_id Description: Autocreated FK slot
--     * Slot: QuantitativeTestCase_id Description: Autocreated FK slot
-- # Class: "TestEntity" Description: "Abstract global 'identification' class shared as a parent with all major model classes within the data model for Translator testing."
--     * Slot: id Description: A unique identifier for a Test Entity
--     * Slot: name Description: A human-readable name for a Test Entity
--     * Slot: description Description: A human-readable description for a Test Entity
--     * Slot: TestRunSession_id Description: Autocreated FK slot
-- # Class: "TestMetadata" Description: "Represents metadata related to (external SME, SMURF, Translator feedback,  large scale batch, etc.) like the provenance of test assets, cases and/or suites."
--     * Slot: test_source Description: Provenance of a specific set of test assets, cases and/or suites.  Or, the person who cares about this,  know about this.  We would like this to be an ORCID eventually, but currently it is just a string.
--     * Slot: test_reference Description: Document URL where original test source particulars are registered (e.g. Github repo)
--     * Slot: test_objective Description: Testing objective behind specified set of test particulars (e.g. acceptance pass/fail; benchmark; quantitative; standards compliance; graph navigation integrity)
--     * Slot: id Description: A unique identifier for a Test Entity
--     * Slot: name Description: A human-readable name for a Test Entity
--     * Slot: description Description: A human-readable description for a Test Entity
-- # Class: "TestAsset" Description: "Represents a Test Asset, which is a single specific instance of TestCase-agnostic semantic parameters representing the specification of a Translator test target with inputs and (expected) outputs."
--     * Slot: input_id Description: 
--     * Slot: input_name Description: 
--     * Slot: input_category Description: 
--     * Slot: predicate_id Description: 
--     * Slot: predicate_name Description: 
--     * Slot: output_id Description: 
--     * Slot: output_name Description: 
--     * Slot: output_category Description: 
--     * Slot: association Description: Specific Biolink Model association 'category' which applies to the test asset defined knowledge statement
--     * Slot: expected_output Description: 
--     * Slot: test_issue Description: 
--     * Slot: semantic_severity Description: 
--     * Slot: in_v1 Description: 
--     * Slot: well_known Description: 
--     * Slot: test_reference Description: Document URL where original test source particulars are registered (e.g. Github repo)
--     * Slot: id Description: A unique identifier for a Test Entity
--     * Slot: name Description: A human-readable name for a Test Entity
--     * Slot: description Description: A human-readable description for a Test Entity
--     * Slot: TestCase_id Description: Autocreated FK slot
--     * Slot: QuantitativeTestCase_id Description: Autocreated FK slot
--     * Slot: test_metadata_id Description: Test metadata describes the external provenance, cross-references and objectives for a given test.
-- # Class: "AcceptanceTestAsset" Description: "Model derived from Jenn's test asset design and Shervin's runner JSON here as an example."
--     * Slot: must_pass_date Description: The date by which this test must pass
--     * Slot: must_pass_environment Description: The deployment environment within which this test must pass.
--     * Slot: scientific_question Description: The full human-readable scientific question a SME would ask, which is encoded into the test asset.
--     * Slot: string_entry Description: The object of the core triple to be tested
--     * Slot: direction Description: The direction of the expected query result triple
--     * Slot: answer_informal_concept Description: An answer that is returned from the test case, note: this must be combined with the expected_result to form a complete answer.  It might make sense to couple these in their own object instead of strictly sticking to the flat schema introduced by the spreadsheet here: https://docs.google.com/spreadsheets/d/1yj7zIchFeVl1OHqL_kE_pqvzNLmGml_FLbHDs-8Yvig/edit#gid=0
--     * Slot: expected_result Description: The expected result of the query
--     * Slot: top_level Description: The answer must return in these many results
--     * Slot: query_node Description: The node of the (templated) TRAPI query to replace
--     * Slot: notes Description: The notes of the query
--     * Slot: input_id Description: 
--     * Slot: input_name Description: 
--     * Slot: input_category Description: 
--     * Slot: predicate_id Description: 
--     * Slot: predicate_name Description: 
--     * Slot: output_id Description: 
--     * Slot: output_name Description: 
--     * Slot: output_category Description: 
--     * Slot: association Description: Specific Biolink Model association 'category' which applies to the test asset defined knowledge statement
--     * Slot: expected_output Description: 
--     * Slot: test_issue Description: 
--     * Slot: semantic_severity Description: 
--     * Slot: in_v1 Description: 
--     * Slot: well_known Description: 
--     * Slot: test_reference Description: Document URL where original test source particulars are registered (e.g. Github repo)
--     * Slot: id Description: A unique identifier for a Test Entity
--     * Slot: name Description: A human-readable name for a Test Entity
--     * Slot: description Description: A human-readable description for a Test Entity
--     * Slot: AcceptanceTestCase_id Description: Autocreated FK slot
--     * Slot: test_metadata_id Description: Test metadata describes the external provenance, cross-references and objectives for a given test.
-- # Class: "TestEdgeData" Description: "Represents a single Biolink Model compliant instance of a subject-predicate-object edge that can be used for testing."
--     * Slot: input_id Description: 
--     * Slot: input_name Description: 
--     * Slot: input_category Description: 
--     * Slot: predicate_id Description: 
--     * Slot: predicate_name Description: 
--     * Slot: output_id Description: 
--     * Slot: output_name Description: 
--     * Slot: output_category Description: 
--     * Slot: association Description: Specific Biolink Model association 'category' which applies to the test asset defined knowledge statement
--     * Slot: expected_output Description: 
--     * Slot: test_issue Description: 
--     * Slot: semantic_severity Description: 
--     * Slot: in_v1 Description: 
--     * Slot: well_known Description: 
--     * Slot: test_reference Description: Document URL where original test source particulars are registered (e.g. Github repo)
--     * Slot: id Description: A unique identifier for a Test Entity
--     * Slot: name Description: A human-readable name for a Test Entity
--     * Slot: description Description: A human-readable description for a Test Entity
--     * Slot: test_metadata_id Description: Test metadata describes the external provenance, cross-references and objectives for a given test.
-- # Class: "Precondition" Description: "Represents a precondition for a TestCase"
--     * Slot: id Description: A unique identifier for a Test Entity
--     * Slot: name Description: A human-readable name for a Test Entity
--     * Slot: description Description: A human-readable description for a Test Entity
-- # Class: "TestCase" Description: "Represents a single enumerated instance of Test Case, derived from a  given collection of one or more TestAsset instances (the value of the 'test_assets' slot) which define the 'inputs' and 'outputs' of the TestCase, used to probe a particular test condition."
--     * Slot: query_type Description: Type of TestCase query.
--     * Slot: trapi_template Description: A template for a query, which can be used to generate a query for a test case.  note: the current enumerated values for this slot come from the Benchmarks repo config/benchmarks.json "templates" collection and refer to the "name" field of each template.  Templates themselves are currently stored in the config/[source_name]/templates directory.
--     * Slot: test_case_objective Description: Testing objective behind specified set of test particulars (e.g. acceptance pass/fail; benchmark; quantitative; standards compliance; graph navigation integrity)
--     * Slot: test_case_source Description: Provenance of a specific set of test assets, cases and/or suites.  Or, the person who cares about this,  know about this.  We would like this to be an ORCID eventually, but currently it is just a string.
--     * Slot: test_case_predicate_name Description: 
--     * Slot: test_case_predicate_id Description: 
--     * Slot: test_case_input_id Description: 
--     * Slot: input_category Description: 
--     * Slot: output_category Description: 
--     * Slot: test_env Description: Deployment environment within which the associated TestSuite is run.
--     * Slot: id Description: A unique identifier for a Test Entity
--     * Slot: name Description: A human-readable name for a Test Entity
--     * Slot: description Description: A human-readable description for a Test Entity
--     * Slot: TestSuite_id Description: Autocreated FK slot
--     * Slot: AcceptanceTestSuite_id Description: Autocreated FK slot
--     * Slot: StandardsComplianceTestSuite_id Description: Autocreated FK slot
--     * Slot: OneHopTestSuite_id Description: Autocreated FK slot
-- # Class: "AcceptanceTestCase" Description: "See AcceptanceTestAsset above for more details."
--     * Slot: query_type Description: Type of TestCase query.
--     * Slot: trapi_template Description: A template for a query, which can be used to generate a query for a test case.  note: the current enumerated values for this slot come from the Benchmarks repo config/benchmarks.json "templates" collection and refer to the "name" field of each template.  Templates themselves are currently stored in the config/[source_name]/templates directory.
--     * Slot: test_case_objective Description: Testing objective behind specified set of test particulars (e.g. acceptance pass/fail; benchmark; quantitative; standards compliance; graph navigation integrity)
--     * Slot: test_case_source Description: Provenance of a specific set of test assets, cases and/or suites.  Or, the person who cares about this,  know about this.  We would like this to be an ORCID eventually, but currently it is just a string.
--     * Slot: test_case_predicate_name Description: 
--     * Slot: test_case_predicate_id Description: 
--     * Slot: test_case_input_id Description: 
--     * Slot: input_category Description: 
--     * Slot: output_category Description: 
--     * Slot: test_env Description: Deployment environment within which the associated TestSuite is run.
--     * Slot: id Description: A unique identifier for a Test Entity
--     * Slot: name Description: A human-readable name for a Test Entity
--     * Slot: description Description: A human-readable description for a Test Entity
-- # Class: "QuantitativeTestCase" Description: "Assumed additional model from Shervin's runner JSON here as an example.  This schema is not yet complete."
--     * Slot: query_type Description: Type of TestCase query.
--     * Slot: trapi_template Description: A template for a query, which can be used to generate a query for a test case.  note: the current enumerated values for this slot come from the Benchmarks repo config/benchmarks.json "templates" collection and refer to the "name" field of each template.  Templates themselves are currently stored in the config/[source_name]/templates directory.
--     * Slot: test_case_objective Description: Testing objective behind specified set of test particulars (e.g. acceptance pass/fail; benchmark; quantitative; standards compliance; graph navigation integrity)
--     * Slot: test_case_source Description: Provenance of a specific set of test assets, cases and/or suites.  Or, the person who cares about this,  know about this.  We would like this to be an ORCID eventually, but currently it is just a string.
--     * Slot: test_case_predicate_name Description: 
--     * Slot: test_case_predicate_id Description: 
--     * Slot: test_case_input_id Description: 
--     * Slot: input_category Description: 
--     * Slot: output_category Description: 
--     * Slot: test_env Description: Deployment environment within which the associated TestSuite is run.
--     * Slot: id Description: A unique identifier for a Test Entity
--     * Slot: name Description: A human-readable name for a Test Entity
--     * Slot: description Description: A human-readable description for a Test Entity
-- # Class: "TestSuiteSpecification" Description: "Parameters for a Test Case instances either dynamically generated from some external source of Test Assets."
--     * Slot: test_data_file_locator Description: An web accessible file resource link to test entity data (e.g. a web accessible text file of Test Asset entries)
--     * Slot: test_data_file_format Description: File format of test entity data (e.g. TSV, YAML or JSON)
--     * Slot: id Description: A unique identifier for a Test Entity
--     * Slot: name Description: A human-readable name for a Test Entity
--     * Slot: description Description: A human-readable description for a Test Entity
-- # Class: "TestSuite" Description: "Specification of a set of Test Cases, one of either with a static list of 'test_cases' or a dynamic 'test_suite_specification' slot values. Note: at least one slot or the other, but generally not both(?) needs to be present."
--     * Slot: test_persona Description: A Test persona describes the user or operational context of a given test.
--     * Slot: id Description: A unique identifier for a Test Entity
--     * Slot: name Description: A human-readable name for a Test Entity
--     * Slot: description Description: A human-readable description for a Test Entity
--     * Slot: test_metadata_id Description: Test metadata describes the external provenance, cross-references and objectives for a given test.
--     * Slot: test_suite_specification_id Description: Declarative specification of a Test Suite of Test Cases whose generation is deferred, (i.e. within a Test Runner) or whose creation is achieved by stream processing of an external data source.
-- # Class: "AcceptanceTestSuite" Description: ""
--     * Slot: test_persona Description: A Test persona describes the user or operational context of a given test.
--     * Slot: id Description: A unique identifier for a Test Entity
--     * Slot: name Description: A human-readable name for a Test Entity
--     * Slot: description Description: A human-readable description for a Test Entity
--     * Slot: test_metadata_id Description: Test metadata describes the external provenance, cross-references and objectives for a given test.
--     * Slot: test_suite_specification_id Description: Declarative specification of a Test Suite of Test Cases whose generation is deferred, (i.e. within a Test Runner) or whose creation is achieved by stream processing of an external data source.
-- # Class: "BenchmarkTestSuite" Description: "JsonObj(is_a='TestSuite')"
--     * Slot: id Description: 
-- # Class: "StandardsComplianceTestSuite" Description: "Test suite for testing Translator components against releases of standards like TRAPI and the Biolink Model."
--     * Slot: test_persona Description: A Test persona describes the user or operational context of a given test.
--     * Slot: id Description: A unique identifier for a Test Entity
--     * Slot: name Description: A human-readable name for a Test Entity
--     * Slot: description Description: A human-readable description for a Test Entity
--     * Slot: test_metadata_id Description: Test metadata describes the external provenance, cross-references and objectives for a given test.
--     * Slot: test_suite_specification_id Description: Declarative specification of a Test Suite of Test Cases whose generation is deferred, (i.e. within a Test Runner) or whose creation is achieved by stream processing of an external data source.
-- # Class: "OneHopTestSuite" Description: "Test case for testing the integrity of "One Hop" knowledge graph retrievals sensa legacy SRI_Testing harness."
--     * Slot: test_persona Description: A Test persona describes the user or operational context of a given test.
--     * Slot: id Description: A unique identifier for a Test Entity
--     * Slot: name Description: A human-readable name for a Test Entity
--     * Slot: description Description: A human-readable description for a Test Entity
--     * Slot: test_metadata_id Description: Test metadata describes the external provenance, cross-references and objectives for a given test.
--     * Slot: test_suite_specification_id Description: Declarative specification of a Test Suite of Test Cases whose generation is deferred, (i.e. within a Test Runner) or whose creation is achieved by stream processing of an external data source.
-- # Class: "TestCaseResult" Description: "The outcome of a TestRunner run of one specific TestCase."
--     * Slot: test_suite_id Description: CURIE id of a TestSuite registered in the system.
--     * Slot: test_case_result Description: Encoded result of a single test run of a given test case
--     * Slot: id Description: A unique identifier for a Test Entity
--     * Slot: name Description: A human-readable name for a Test Entity
--     * Slot: description Description: A human-readable description for a Test Entity
--     * Slot: TestRunSession_id Description: Autocreated FK slot
--     * Slot: test_case_id Description: Slot referencing a single TestCase.
-- # Class: "TestRunSession" Description: "Single run of a TestRunner in a given environment, with a specified set of test_entities (generally, one or more instances of TestSuite)."
--     * Slot: test_env Description: Deployment environment within which the associated TestSuite is run.
--     * Slot: test_runner_name Description: Global system name of a TestRunner.
--     * Slot: timestamp Description: Date time when a given entity was created.
--     * Slot: id Description: A unique identifier for a Test Entity
--     * Slot: name Description: A human-readable name for a Test Entity
--     * Slot: description Description: A human-readable description for a Test Entity
-- # Class: "TestOutput" Description: "The output of a TestRunner run of one specific TestCase."
--     * Slot: test_case_id Description: CURIE id of a TestCase registered in the system.
--     * Slot: id Description: A unique identifier for a Test Entity
--     * Slot: name Description: A human-readable name for a Test Entity
--     * Slot: description Description: A human-readable description for a Test Entity
-- # Class: "TestResultPKSet" Description: "Primary keys for a given ARA result set from a SmokeTest result for a given TestCase."
--     * Slot: parent_pk Description: 
--     * Slot: merged_pk Description: 
--     * Slot: aragorn Description: 
--     * Slot: arax Description: 
--     * Slot: unsecret Description: 
--     * Slot: bte Description: 
--     * Slot: improving Description: 
--     * Slot: id Description: A unique identifier for a Test Entity
--     * Slot: name Description: A human-readable name for a Test Entity
--     * Slot: description Description: A human-readable description for a Test Entity
-- # Class: "TestEntity_tags" Description: ""
--     * Slot: TestEntity_id Description: Autocreated FK slot
--     * Slot: tags Description: A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.
-- # Class: "TestEntity_test_runner_settings" Description: ""
--     * Slot: TestEntity_id Description: Autocreated FK slot
--     * Slot: test_runner_settings Description: Scalar parameters for the TestRunner processing a given TestEntity.
-- # Class: "TestMetadata_tags" Description: ""
--     * Slot: TestMetadata_id Description: Autocreated FK slot
--     * Slot: tags Description: A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.
-- # Class: "TestMetadata_test_runner_settings" Description: ""
--     * Slot: TestMetadata_id Description: Autocreated FK slot
--     * Slot: test_runner_settings Description: Scalar parameters for the TestRunner processing a given TestEntity.
-- # Class: "TestAsset_tags" Description: ""
--     * Slot: TestAsset_id Description: Autocreated FK slot
--     * Slot: tags Description: One or more 'tags' slot values (inherited from TestEntity) should generally be defined to specify TestAsset membership in a "Block List" collection
-- # Class: "TestAsset_test_runner_settings" Description: ""
--     * Slot: TestAsset_id Description: Autocreated FK slot
--     * Slot: test_runner_settings Description: Scalar settings for the TestRunner, e.g. "inferred"
-- # Class: "AcceptanceTestAsset_tags" Description: ""
--     * Slot: AcceptanceTestAsset_id Description: Autocreated FK slot
--     * Slot: tags Description: One or more 'tags' slot values (inherited from TestEntity) should generally be defined to specify TestAsset membership in a "Block List" collection
-- # Class: "AcceptanceTestAsset_test_runner_settings" Description: ""
--     * Slot: AcceptanceTestAsset_id Description: Autocreated FK slot
--     * Slot: test_runner_settings Description: Scalar settings for the TestRunner, e.g. "inferred"
-- # Class: "TestEdgeData_tags" Description: ""
--     * Slot: TestEdgeData_id Description: Autocreated FK slot
--     * Slot: tags Description: One or more 'tags' slot values (inherited from TestEntity) should generally be defined to specify TestAsset membership in a "Block List" collection
-- # Class: "TestEdgeData_test_runner_settings" Description: ""
--     * Slot: TestEdgeData_id Description: Autocreated FK slot
--     * Slot: test_runner_settings Description: Scalar settings for the TestRunner, e.g. "inferred"
-- # Class: "Precondition_tags" Description: ""
--     * Slot: Precondition_id Description: Autocreated FK slot
--     * Slot: tags Description: A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.
-- # Class: "Precondition_test_runner_settings" Description: ""
--     * Slot: Precondition_id Description: Autocreated FK slot
--     * Slot: test_runner_settings Description: Scalar parameters for the TestRunner processing a given TestEntity.
-- # Class: "TestCase_preconditions" Description: ""
--     * Slot: TestCase_id Description: Autocreated FK slot
--     * Slot: preconditions_id Description: 
-- # Class: "TestCase_components" Description: ""
--     * Slot: TestCase_id Description: Autocreated FK slot
--     * Slot: components Description: The component that this test case is intended to run against.  Most often this is the ARS for  acceptance tests, but for the Benchmarks repo integration, this can also be individual components of the system like Aragorn, or ARAX.
-- # Class: "TestCase_tags" Description: ""
--     * Slot: TestCase_id Description: Autocreated FK slot
--     * Slot: tags Description: One or more 'tags' slot values (slot inherited from TestEntity) should generally be defined as filters to specify TestAsset membership in a "Block List" collection.
-- # Class: "TestCase_test_runner_settings" Description: ""
--     * Slot: TestCase_id Description: Autocreated FK slot
--     * Slot: test_runner_settings Description: Scalar parameters for the TestRunner processing a given TestEntity.
-- # Class: "AcceptanceTestCase_preconditions" Description: ""
--     * Slot: AcceptanceTestCase_id Description: Autocreated FK slot
--     * Slot: preconditions_id Description: 
-- # Class: "AcceptanceTestCase_components" Description: ""
--     * Slot: AcceptanceTestCase_id Description: Autocreated FK slot
--     * Slot: components Description: The component that this test case is intended to run against.  Most often this is the ARS for  acceptance tests, but for the Benchmarks repo integration, this can also be individual components of the system like Aragorn, or ARAX.
-- # Class: "AcceptanceTestCase_tags" Description: ""
--     * Slot: AcceptanceTestCase_id Description: Autocreated FK slot
--     * Slot: tags Description: One or more 'tags' slot values (slot inherited from TestEntity) should generally be defined as filters to specify TestAsset membership in a "Block List" collection.
-- # Class: "AcceptanceTestCase_test_runner_settings" Description: ""
--     * Slot: AcceptanceTestCase_id Description: Autocreated FK slot
--     * Slot: test_runner_settings Description: Scalar parameters for the TestRunner processing a given TestEntity.
-- # Class: "QuantitativeTestCase_preconditions" Description: ""
--     * Slot: QuantitativeTestCase_id Description: Autocreated FK slot
--     * Slot: preconditions_id Description: 
-- # Class: "QuantitativeTestCase_components" Description: ""
--     * Slot: QuantitativeTestCase_id Description: Autocreated FK slot
--     * Slot: components Description: The component that this test case is intended to run against.  Most often this is the ARS for  acceptance tests, but for the Benchmarks repo integration, this can also be individual components of the system like Aragorn, or ARAX.
-- # Class: "QuantitativeTestCase_tags" Description: ""
--     * Slot: QuantitativeTestCase_id Description: Autocreated FK slot
--     * Slot: tags Description: One or more 'tags' slot values (slot inherited from TestEntity) should generally be defined as filters to specify TestAsset membership in a "Block List" collection.
-- # Class: "QuantitativeTestCase_test_runner_settings" Description: ""
--     * Slot: QuantitativeTestCase_id Description: Autocreated FK slot
--     * Slot: test_runner_settings Description: Scalar parameters for the TestRunner processing a given TestEntity.
-- # Class: "TestSuiteSpecification_tags" Description: ""
--     * Slot: TestSuiteSpecification_id Description: Autocreated FK slot
--     * Slot: tags Description: A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.
-- # Class: "TestSuiteSpecification_test_runner_settings" Description: ""
--     * Slot: TestSuiteSpecification_id Description: Autocreated FK slot
--     * Slot: test_runner_settings Description: Scalar parameters for the TestRunner processing a given TestEntity.
-- # Class: "TestSuite_tags" Description: ""
--     * Slot: TestSuite_id Description: Autocreated FK slot
--     * Slot: tags Description: A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.
-- # Class: "TestSuite_test_runner_settings" Description: ""
--     * Slot: TestSuite_id Description: Autocreated FK slot
--     * Slot: test_runner_settings Description: Scalar parameters for the TestRunner processing a given TestEntity.
-- # Class: "AcceptanceTestSuite_tags" Description: ""
--     * Slot: AcceptanceTestSuite_id Description: Autocreated FK slot
--     * Slot: tags Description: A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.
-- # Class: "AcceptanceTestSuite_test_runner_settings" Description: ""
--     * Slot: AcceptanceTestSuite_id Description: Autocreated FK slot
--     * Slot: test_runner_settings Description: Scalar parameters for the TestRunner processing a given TestEntity.
-- # Class: "StandardsComplianceTestSuite_tags" Description: ""
--     * Slot: StandardsComplianceTestSuite_id Description: Autocreated FK slot
--     * Slot: tags Description: A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.
-- # Class: "StandardsComplianceTestSuite_test_runner_settings" Description: ""
--     * Slot: StandardsComplianceTestSuite_id Description: Autocreated FK slot
--     * Slot: test_runner_settings Description: Scalar parameters for the TestRunner processing a given TestEntity.
-- # Class: "OneHopTestSuite_tags" Description: ""
--     * Slot: OneHopTestSuite_id Description: Autocreated FK slot
--     * Slot: tags Description: A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.
-- # Class: "OneHopTestSuite_test_runner_settings" Description: ""
--     * Slot: OneHopTestSuite_id Description: Autocreated FK slot
--     * Slot: test_runner_settings Description: Scalar parameters for the TestRunner processing a given TestEntity.
-- # Class: "TestCaseResult_tags" Description: ""
--     * Slot: TestCaseResult_id Description: Autocreated FK slot
--     * Slot: tags Description: A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.
-- # Class: "TestCaseResult_test_runner_settings" Description: ""
--     * Slot: TestCaseResult_id Description: Autocreated FK slot
--     * Slot: test_runner_settings Description: Scalar parameters for the TestRunner processing a given TestEntity.
-- # Class: "TestRunSession_components" Description: ""
--     * Slot: TestRunSession_id Description: Autocreated FK slot
--     * Slot: components Description: The component that this test case is intended to run against.  Most often this is the ARS for  acceptance tests, but for the Benchmarks repo integration, this can also be individual components of the system like Aragorn, or ARAX.
-- # Class: "TestRunSession_tags" Description: ""
--     * Slot: TestRunSession_id Description: Autocreated FK slot
--     * Slot: tags Description: A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.
-- # Class: "TestRunSession_test_runner_settings" Description: ""
--     * Slot: TestRunSession_id Description: Autocreated FK slot
--     * Slot: test_runner_settings Description: Scalar parameters for the TestRunner processing a given TestEntity.
-- # Class: "TestOutput_pks" Description: ""
--     * Slot: TestOutput_id Description: Autocreated FK slot
--     * Slot: pks_id Description: Primary keys for a given ARA result set from a SmokeTest result for a given TestCase.
-- # Class: "TestOutput_tags" Description: ""
--     * Slot: TestOutput_id Description: Autocreated FK slot
--     * Slot: tags Description: A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.
-- # Class: "TestOutput_test_runner_settings" Description: ""
--     * Slot: TestOutput_id Description: Autocreated FK slot
--     * Slot: test_runner_settings Description: Scalar parameters for the TestRunner processing a given TestEntity.
-- # Class: "TestResultPKSet_tags" Description: ""
--     * Slot: TestResultPKSet_id Description: Autocreated FK slot
--     * Slot: tags Description: A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.
-- # Class: "TestResultPKSet_test_runner_settings" Description: ""
--     * Slot: TestResultPKSet_id Description: Autocreated FK slot
--     * Slot: test_runner_settings Description: Scalar parameters for the TestRunner processing a given TestEntity.

CREATE TABLE "TestMetadata" (
	test_source VARCHAR(18), 
	test_reference TEXT, 
	test_objective VARCHAR(23), 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Precondition" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "AcceptanceTestCase" (
	query_type VARCHAR(6), 
	trapi_template VARCHAR(24), 
	test_case_objective VARCHAR(23), 
	test_case_source VARCHAR(18), 
	test_case_predicate_name TEXT, 
	test_case_predicate_id TEXT, 
	test_case_input_id TEXT, 
	input_category TEXT, 
	output_category TEXT, 
	test_env VARCHAR(4), 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "QuantitativeTestCase" (
	query_type VARCHAR(6), 
	trapi_template VARCHAR(24), 
	test_case_objective VARCHAR(23), 
	test_case_source VARCHAR(18), 
	test_case_predicate_name TEXT, 
	test_case_predicate_id TEXT, 
	test_case_input_id TEXT, 
	input_category TEXT, 
	output_category TEXT, 
	test_env VARCHAR(4), 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "TestSuiteSpecification" (
	test_data_file_locator TEXT, 
	test_data_file_format VARCHAR(4), 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "BenchmarkTestSuite" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "TestRunSession" (
	test_env VARCHAR(4), 
	test_runner_name TEXT, 
	timestamp DATETIME, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "TestOutput" (
	test_case_id TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "TestResultPKSet" (
	parent_pk TEXT, 
	merged_pk TEXT, 
	aragorn TEXT, 
	arax TEXT, 
	unsecret TEXT, 
	bte TEXT, 
	improving TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "TestEntityParameter" (
	id INTEGER NOT NULL, 
	parameter TEXT, 
	value TEXT, 
	"TestMetadata_id" TEXT, 
	"TestRunSession_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("TestMetadata_id") REFERENCES "TestMetadata" (id), 
	FOREIGN KEY("TestRunSession_id") REFERENCES "TestRunSession" (id)
);
CREATE TABLE "TestEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"TestRunSession_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("TestRunSession_id") REFERENCES "TestRunSession" (id)
);
CREATE TABLE "AcceptanceTestAsset" (
	must_pass_date DATE, 
	must_pass_environment VARCHAR(4), 
	scientific_question TEXT, 
	string_entry TEXT, 
	direction VARCHAR(9), 
	answer_informal_concept TEXT, 
	expected_result VARCHAR(12), 
	top_level INTEGER, 
	query_node VARCHAR(7), 
	notes TEXT, 
	input_id TEXT, 
	input_name TEXT, 
	input_category TEXT, 
	predicate_id TEXT, 
	predicate_name TEXT, 
	output_id TEXT, 
	output_name TEXT, 
	output_category TEXT, 
	association TEXT, 
	expected_output TEXT, 
	test_issue VARCHAR(20), 
	semantic_severity VARCHAR(13), 
	in_v1 BOOLEAN, 
	well_known BOOLEAN, 
	test_reference TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"AcceptanceTestCase_id" TEXT, 
	test_metadata_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("AcceptanceTestCase_id") REFERENCES "AcceptanceTestCase" (id), 
	FOREIGN KEY(test_metadata_id) REFERENCES "TestMetadata" (id)
);
CREATE TABLE "TestEdgeData" (
	input_id TEXT, 
	input_name TEXT, 
	input_category TEXT, 
	predicate_id TEXT, 
	predicate_name TEXT, 
	output_id TEXT, 
	output_name TEXT, 
	output_category TEXT, 
	association TEXT, 
	expected_output TEXT, 
	test_issue VARCHAR(20), 
	semantic_severity VARCHAR(13), 
	in_v1 BOOLEAN, 
	well_known BOOLEAN, 
	test_reference TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_metadata_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(test_metadata_id) REFERENCES "TestMetadata" (id)
);
CREATE TABLE "TestSuite" (
	test_persona VARCHAR(11), 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_metadata_id TEXT NOT NULL, 
	test_suite_specification_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(test_metadata_id) REFERENCES "TestMetadata" (id), 
	FOREIGN KEY(test_suite_specification_id) REFERENCES "TestSuiteSpecification" (id)
);
CREATE TABLE "AcceptanceTestSuite" (
	test_persona VARCHAR(11), 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_metadata_id TEXT NOT NULL, 
	test_suite_specification_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(test_metadata_id) REFERENCES "TestMetadata" (id), 
	FOREIGN KEY(test_suite_specification_id) REFERENCES "TestSuiteSpecification" (id)
);
CREATE TABLE "StandardsComplianceTestSuite" (
	test_persona VARCHAR(11), 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_metadata_id TEXT NOT NULL, 
	test_suite_specification_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(test_metadata_id) REFERENCES "TestMetadata" (id), 
	FOREIGN KEY(test_suite_specification_id) REFERENCES "TestSuiteSpecification" (id)
);
CREATE TABLE "OneHopTestSuite" (
	test_persona VARCHAR(11), 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_metadata_id TEXT NOT NULL, 
	test_suite_specification_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(test_metadata_id) REFERENCES "TestMetadata" (id), 
	FOREIGN KEY(test_suite_specification_id) REFERENCES "TestSuiteSpecification" (id)
);
CREATE TABLE "TestMetadata_tags" (
	"TestMetadata_id" TEXT, 
	tags TEXT, 
	PRIMARY KEY ("TestMetadata_id", tags), 
	FOREIGN KEY("TestMetadata_id") REFERENCES "TestMetadata" (id)
);
CREATE TABLE "TestMetadata_test_runner_settings" (
	"TestMetadata_id" TEXT, 
	test_runner_settings TEXT, 
	PRIMARY KEY ("TestMetadata_id", test_runner_settings), 
	FOREIGN KEY("TestMetadata_id") REFERENCES "TestMetadata" (id)
);
CREATE TABLE "Precondition_tags" (
	"Precondition_id" TEXT, 
	tags TEXT, 
	PRIMARY KEY ("Precondition_id", tags), 
	FOREIGN KEY("Precondition_id") REFERENCES "Precondition" (id)
);
CREATE TABLE "Precondition_test_runner_settings" (
	"Precondition_id" TEXT, 
	test_runner_settings TEXT, 
	PRIMARY KEY ("Precondition_id", test_runner_settings), 
	FOREIGN KEY("Precondition_id") REFERENCES "Precondition" (id)
);
CREATE TABLE "AcceptanceTestCase_preconditions" (
	"AcceptanceTestCase_id" TEXT, 
	preconditions_id TEXT, 
	PRIMARY KEY ("AcceptanceTestCase_id", preconditions_id), 
	FOREIGN KEY("AcceptanceTestCase_id") REFERENCES "AcceptanceTestCase" (id), 
	FOREIGN KEY(preconditions_id) REFERENCES "Precondition" (id)
);
CREATE TABLE "AcceptanceTestCase_components" (
	"AcceptanceTestCase_id" TEXT, 
	components VARCHAR, 
	PRIMARY KEY ("AcceptanceTestCase_id", components), 
	FOREIGN KEY("AcceptanceTestCase_id") REFERENCES "AcceptanceTestCase" (id)
);
CREATE TABLE "AcceptanceTestCase_tags" (
	"AcceptanceTestCase_id" TEXT, 
	tags TEXT, 
	PRIMARY KEY ("AcceptanceTestCase_id", tags), 
	FOREIGN KEY("AcceptanceTestCase_id") REFERENCES "AcceptanceTestCase" (id)
);
CREATE TABLE "AcceptanceTestCase_test_runner_settings" (
	"AcceptanceTestCase_id" TEXT, 
	test_runner_settings TEXT, 
	PRIMARY KEY ("AcceptanceTestCase_id", test_runner_settings), 
	FOREIGN KEY("AcceptanceTestCase_id") REFERENCES "AcceptanceTestCase" (id)
);
CREATE TABLE "QuantitativeTestCase_preconditions" (
	"QuantitativeTestCase_id" TEXT, 
	preconditions_id TEXT, 
	PRIMARY KEY ("QuantitativeTestCase_id", preconditions_id), 
	FOREIGN KEY("QuantitativeTestCase_id") REFERENCES "QuantitativeTestCase" (id), 
	FOREIGN KEY(preconditions_id) REFERENCES "Precondition" (id)
);
CREATE TABLE "QuantitativeTestCase_components" (
	"QuantitativeTestCase_id" TEXT, 
	components VARCHAR, 
	PRIMARY KEY ("QuantitativeTestCase_id", components), 
	FOREIGN KEY("QuantitativeTestCase_id") REFERENCES "QuantitativeTestCase" (id)
);
CREATE TABLE "QuantitativeTestCase_tags" (
	"QuantitativeTestCase_id" TEXT, 
	tags TEXT, 
	PRIMARY KEY ("QuantitativeTestCase_id", tags), 
	FOREIGN KEY("QuantitativeTestCase_id") REFERENCES "QuantitativeTestCase" (id)
);
CREATE TABLE "QuantitativeTestCase_test_runner_settings" (
	"QuantitativeTestCase_id" TEXT, 
	test_runner_settings TEXT, 
	PRIMARY KEY ("QuantitativeTestCase_id", test_runner_settings), 
	FOREIGN KEY("QuantitativeTestCase_id") REFERENCES "QuantitativeTestCase" (id)
);
CREATE TABLE "TestSuiteSpecification_tags" (
	"TestSuiteSpecification_id" TEXT, 
	tags TEXT, 
	PRIMARY KEY ("TestSuiteSpecification_id", tags), 
	FOREIGN KEY("TestSuiteSpecification_id") REFERENCES "TestSuiteSpecification" (id)
);
CREATE TABLE "TestSuiteSpecification_test_runner_settings" (
	"TestSuiteSpecification_id" TEXT, 
	test_runner_settings TEXT, 
	PRIMARY KEY ("TestSuiteSpecification_id", test_runner_settings), 
	FOREIGN KEY("TestSuiteSpecification_id") REFERENCES "TestSuiteSpecification" (id)
);
CREATE TABLE "TestRunSession_components" (
	"TestRunSession_id" TEXT, 
	components VARCHAR, 
	PRIMARY KEY ("TestRunSession_id", components), 
	FOREIGN KEY("TestRunSession_id") REFERENCES "TestRunSession" (id)
);
CREATE TABLE "TestRunSession_tags" (
	"TestRunSession_id" TEXT, 
	tags TEXT, 
	PRIMARY KEY ("TestRunSession_id", tags), 
	FOREIGN KEY("TestRunSession_id") REFERENCES "TestRunSession" (id)
);
CREATE TABLE "TestRunSession_test_runner_settings" (
	"TestRunSession_id" TEXT, 
	test_runner_settings TEXT, 
	PRIMARY KEY ("TestRunSession_id", test_runner_settings), 
	FOREIGN KEY("TestRunSession_id") REFERENCES "TestRunSession" (id)
);
CREATE TABLE "TestOutput_pks" (
	"TestOutput_id" TEXT, 
	pks_id TEXT, 
	PRIMARY KEY ("TestOutput_id", pks_id), 
	FOREIGN KEY("TestOutput_id") REFERENCES "TestOutput" (id), 
	FOREIGN KEY(pks_id) REFERENCES "TestResultPKSet" (id)
);
CREATE TABLE "TestOutput_tags" (
	"TestOutput_id" TEXT, 
	tags TEXT, 
	PRIMARY KEY ("TestOutput_id", tags), 
	FOREIGN KEY("TestOutput_id") REFERENCES "TestOutput" (id)
);
CREATE TABLE "TestOutput_test_runner_settings" (
	"TestOutput_id" TEXT, 
	test_runner_settings TEXT, 
	PRIMARY KEY ("TestOutput_id", test_runner_settings), 
	FOREIGN KEY("TestOutput_id") REFERENCES "TestOutput" (id)
);
CREATE TABLE "TestResultPKSet_tags" (
	"TestResultPKSet_id" TEXT, 
	tags TEXT, 
	PRIMARY KEY ("TestResultPKSet_id", tags), 
	FOREIGN KEY("TestResultPKSet_id") REFERENCES "TestResultPKSet" (id)
);
CREATE TABLE "TestResultPKSet_test_runner_settings" (
	"TestResultPKSet_id" TEXT, 
	test_runner_settings TEXT, 
	PRIMARY KEY ("TestResultPKSet_id", test_runner_settings), 
	FOREIGN KEY("TestResultPKSet_id") REFERENCES "TestResultPKSet" (id)
);
CREATE TABLE "TestCase" (
	query_type VARCHAR(6), 
	trapi_template VARCHAR(24), 
	test_case_objective VARCHAR(23), 
	test_case_source VARCHAR(18), 
	test_case_predicate_name TEXT, 
	test_case_predicate_id TEXT, 
	test_case_input_id TEXT, 
	input_category TEXT, 
	output_category TEXT, 
	test_env VARCHAR(4), 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"TestSuite_id" TEXT, 
	"AcceptanceTestSuite_id" TEXT, 
	"StandardsComplianceTestSuite_id" TEXT, 
	"OneHopTestSuite_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("TestSuite_id") REFERENCES "TestSuite" (id), 
	FOREIGN KEY("AcceptanceTestSuite_id") REFERENCES "AcceptanceTestSuite" (id), 
	FOREIGN KEY("StandardsComplianceTestSuite_id") REFERENCES "StandardsComplianceTestSuite" (id), 
	FOREIGN KEY("OneHopTestSuite_id") REFERENCES "OneHopTestSuite" (id)
);
CREATE TABLE "TestEntity_tags" (
	"TestEntity_id" TEXT, 
	tags TEXT, 
	PRIMARY KEY ("TestEntity_id", tags), 
	FOREIGN KEY("TestEntity_id") REFERENCES "TestEntity" (id)
);
CREATE TABLE "TestEntity_test_runner_settings" (
	"TestEntity_id" TEXT, 
	test_runner_settings TEXT, 
	PRIMARY KEY ("TestEntity_id", test_runner_settings), 
	FOREIGN KEY("TestEntity_id") REFERENCES "TestEntity" (id)
);
CREATE TABLE "AcceptanceTestAsset_tags" (
	"AcceptanceTestAsset_id" TEXT, 
	tags TEXT, 
	PRIMARY KEY ("AcceptanceTestAsset_id", tags), 
	FOREIGN KEY("AcceptanceTestAsset_id") REFERENCES "AcceptanceTestAsset" (id)
);
CREATE TABLE "AcceptanceTestAsset_test_runner_settings" (
	"AcceptanceTestAsset_id" TEXT, 
	test_runner_settings TEXT, 
	PRIMARY KEY ("AcceptanceTestAsset_id", test_runner_settings), 
	FOREIGN KEY("AcceptanceTestAsset_id") REFERENCES "AcceptanceTestAsset" (id)
);
CREATE TABLE "TestEdgeData_tags" (
	"TestEdgeData_id" TEXT, 
	tags TEXT, 
	PRIMARY KEY ("TestEdgeData_id", tags), 
	FOREIGN KEY("TestEdgeData_id") REFERENCES "TestEdgeData" (id)
);
CREATE TABLE "TestEdgeData_test_runner_settings" (
	"TestEdgeData_id" TEXT, 
	test_runner_settings TEXT, 
	PRIMARY KEY ("TestEdgeData_id", test_runner_settings), 
	FOREIGN KEY("TestEdgeData_id") REFERENCES "TestEdgeData" (id)
);
CREATE TABLE "TestSuite_tags" (
	"TestSuite_id" TEXT, 
	tags TEXT, 
	PRIMARY KEY ("TestSuite_id", tags), 
	FOREIGN KEY("TestSuite_id") REFERENCES "TestSuite" (id)
);
CREATE TABLE "TestSuite_test_runner_settings" (
	"TestSuite_id" TEXT, 
	test_runner_settings TEXT, 
	PRIMARY KEY ("TestSuite_id", test_runner_settings), 
	FOREIGN KEY("TestSuite_id") REFERENCES "TestSuite" (id)
);
CREATE TABLE "AcceptanceTestSuite_tags" (
	"AcceptanceTestSuite_id" TEXT, 
	tags TEXT, 
	PRIMARY KEY ("AcceptanceTestSuite_id", tags), 
	FOREIGN KEY("AcceptanceTestSuite_id") REFERENCES "AcceptanceTestSuite" (id)
);
CREATE TABLE "AcceptanceTestSuite_test_runner_settings" (
	"AcceptanceTestSuite_id" TEXT, 
	test_runner_settings TEXT, 
	PRIMARY KEY ("AcceptanceTestSuite_id", test_runner_settings), 
	FOREIGN KEY("AcceptanceTestSuite_id") REFERENCES "AcceptanceTestSuite" (id)
);
CREATE TABLE "StandardsComplianceTestSuite_tags" (
	"StandardsComplianceTestSuite_id" TEXT, 
	tags TEXT, 
	PRIMARY KEY ("StandardsComplianceTestSuite_id", tags), 
	FOREIGN KEY("StandardsComplianceTestSuite_id") REFERENCES "StandardsComplianceTestSuite" (id)
);
CREATE TABLE "StandardsComplianceTestSuite_test_runner_settings" (
	"StandardsComplianceTestSuite_id" TEXT, 
	test_runner_settings TEXT, 
	PRIMARY KEY ("StandardsComplianceTestSuite_id", test_runner_settings), 
	FOREIGN KEY("StandardsComplianceTestSuite_id") REFERENCES "StandardsComplianceTestSuite" (id)
);
CREATE TABLE "OneHopTestSuite_tags" (
	"OneHopTestSuite_id" TEXT, 
	tags TEXT, 
	PRIMARY KEY ("OneHopTestSuite_id", tags), 
	FOREIGN KEY("OneHopTestSuite_id") REFERENCES "OneHopTestSuite" (id)
);
CREATE TABLE "OneHopTestSuite_test_runner_settings" (
	"OneHopTestSuite_id" TEXT, 
	test_runner_settings TEXT, 
	PRIMARY KEY ("OneHopTestSuite_id", test_runner_settings), 
	FOREIGN KEY("OneHopTestSuite_id") REFERENCES "OneHopTestSuite" (id)
);
CREATE TABLE "TestAsset" (
	input_id TEXT, 
	input_name TEXT, 
	input_category TEXT, 
	predicate_id TEXT, 
	predicate_name TEXT, 
	output_id TEXT, 
	output_name TEXT, 
	output_category TEXT, 
	association TEXT, 
	expected_output TEXT, 
	test_issue VARCHAR(20), 
	semantic_severity VARCHAR(13), 
	in_v1 BOOLEAN, 
	well_known BOOLEAN, 
	test_reference TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"TestCase_id" TEXT, 
	"QuantitativeTestCase_id" TEXT, 
	test_metadata_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("TestCase_id") REFERENCES "TestCase" (id), 
	FOREIGN KEY("QuantitativeTestCase_id") REFERENCES "QuantitativeTestCase" (id), 
	FOREIGN KEY(test_metadata_id) REFERENCES "TestMetadata" (id)
);
CREATE TABLE "TestCaseResult" (
	test_suite_id TEXT, 
	test_case_result VARCHAR(7), 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"TestRunSession_id" TEXT, 
	test_case_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("TestRunSession_id") REFERENCES "TestRunSession" (id), 
	FOREIGN KEY(test_case_id) REFERENCES "TestCase" (id)
);
CREATE TABLE "TestCase_preconditions" (
	"TestCase_id" TEXT, 
	preconditions_id TEXT, 
	PRIMARY KEY ("TestCase_id", preconditions_id), 
	FOREIGN KEY("TestCase_id") REFERENCES "TestCase" (id), 
	FOREIGN KEY(preconditions_id) REFERENCES "Precondition" (id)
);
CREATE TABLE "TestCase_components" (
	"TestCase_id" TEXT, 
	components VARCHAR, 
	PRIMARY KEY ("TestCase_id", components), 
	FOREIGN KEY("TestCase_id") REFERENCES "TestCase" (id)
);
CREATE TABLE "TestCase_tags" (
	"TestCase_id" TEXT, 
	tags TEXT, 
	PRIMARY KEY ("TestCase_id", tags), 
	FOREIGN KEY("TestCase_id") REFERENCES "TestCase" (id)
);
CREATE TABLE "TestCase_test_runner_settings" (
	"TestCase_id" TEXT, 
	test_runner_settings TEXT, 
	PRIMARY KEY ("TestCase_id", test_runner_settings), 
	FOREIGN KEY("TestCase_id") REFERENCES "TestCase" (id)
);
CREATE TABLE "Qualifier" (
	id INTEGER NOT NULL, 
	parameter TEXT, 
	value TEXT, 
	"TestAsset_id" TEXT, 
	"AcceptanceTestAsset_id" TEXT, 
	"TestEdgeData_id" TEXT, 
	"TestCase_id" TEXT, 
	"AcceptanceTestCase_id" TEXT, 
	"QuantitativeTestCase_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("TestAsset_id") REFERENCES "TestAsset" (id), 
	FOREIGN KEY("AcceptanceTestAsset_id") REFERENCES "AcceptanceTestAsset" (id), 
	FOREIGN KEY("TestEdgeData_id") REFERENCES "TestEdgeData" (id), 
	FOREIGN KEY("TestCase_id") REFERENCES "TestCase" (id), 
	FOREIGN KEY("AcceptanceTestCase_id") REFERENCES "AcceptanceTestCase" (id), 
	FOREIGN KEY("QuantitativeTestCase_id") REFERENCES "QuantitativeTestCase" (id)
);
CREATE TABLE "TestAsset_tags" (
	"TestAsset_id" TEXT, 
	tags TEXT, 
	PRIMARY KEY ("TestAsset_id", tags), 
	FOREIGN KEY("TestAsset_id") REFERENCES "TestAsset" (id)
);
CREATE TABLE "TestAsset_test_runner_settings" (
	"TestAsset_id" TEXT, 
	test_runner_settings TEXT, 
	PRIMARY KEY ("TestAsset_id", test_runner_settings), 
	FOREIGN KEY("TestAsset_id") REFERENCES "TestAsset" (id)
);
CREATE TABLE "TestCaseResult_tags" (
	"TestCaseResult_id" TEXT, 
	tags TEXT, 
	PRIMARY KEY ("TestCaseResult_id", tags), 
	FOREIGN KEY("TestCaseResult_id") REFERENCES "TestCaseResult" (id)
);
CREATE TABLE "TestCaseResult_test_runner_settings" (
	"TestCaseResult_id" TEXT, 
	test_runner_settings TEXT, 
	PRIMARY KEY ("TestCaseResult_id", test_runner_settings), 
	FOREIGN KEY("TestCaseResult_id") REFERENCES "TestCaseResult" (id)
);