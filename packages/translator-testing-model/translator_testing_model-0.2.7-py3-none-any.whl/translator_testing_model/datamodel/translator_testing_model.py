# Auto generated from translator_testing_model.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-04-19T10:26:22
# Schema: Translator-Testing-Model
#
# id: https://w3id.org/TranslatorSRI/TranslatorTestingModel
# description: Data model to formalize the structure of test assets, cases, suites and related metadata
#   applied to run the diverse polymorphic testing objectives for the Biomedical Data Translator system.
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate, XSDDateTime

metamodel_version = "1.7.0"
version = "0.0.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
TTM = CurieNamespace('ttm', 'https://w3id.org/TranslatorSRI/TranslatorTestingModel/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = TTM


# Types
class CategoryType(Uriorcurie):
    """ A primitive type in which the value denotes a class within the biolink model. The value must be a URI or a CURIE within the 'biolink' namespace. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "category_type"
    type_model_uri = TTM.CategoryType


class PredicateType(Uriorcurie):
    """ A CURIE from the Biolink Model ('biolink' namespace) 'biolink:related_to' hierarchy. For example, biolink:related_to, biolink:causes, biolink:treats. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "predicate_type"
    type_model_uri = TTM.PredicateType


class ConceptCategory(CategoryType):
    """ A category type within the Biolink Model ('biolink' namespace) 'biolink:NamedThing' hierarchy. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "concept_category"
    type_model_uri = TTM.ConceptCategory


class AssociationCategory(CategoryType):
    """ A category type within the Biolink Model ('biolink' namespace) 'biolink:Association' hierarchy. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "association_category"
    type_model_uri = TTM.AssociationCategory


# Class references
class TestEntityId(URIorCURIE):
    pass


class TestMetadataId(TestEntityId):
    pass


class TestAssetId(TestEntityId):
    pass


class AcceptanceTestAssetId(TestAssetId):
    pass


class TestEdgeDataId(TestAssetId):
    pass


class PreconditionId(TestEntityId):
    pass


class TestCaseId(TestEntityId):
    pass


class AcceptanceTestCaseId(TestCaseId):
    pass


class QuantitativeTestCaseId(TestCaseId):
    pass


class TestSuiteSpecificationId(TestEntityId):
    pass


class TestSuiteId(TestEntityId):
    pass


class AcceptanceTestSuiteId(TestSuiteId):
    pass


class StandardsComplianceTestSuiteId(TestSuiteId):
    pass


class OneHopTestSuiteId(TestSuiteId):
    pass


class TestCaseResultId(TestEntityId):
    pass


class TestRunSessionId(TestEntityId):
    pass


class TestOutputId(TestEntityId):
    pass


class TestResultPKSetId(TestEntityId):
    pass


@dataclass
class TestEntityParameter(YAMLRoot):
    """
    A single 'tag = value' pair (where 'value' is a simple string).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TTM["TestEntityParameter"]
    class_class_curie: ClassVar[str] = "ttm:TestEntityParameter"
    class_name: ClassVar[str] = "TestEntityParameter"
    class_model_uri: ClassVar[URIRef] = TTM.TestEntityParameter

    parameter: Optional[str] = None
    value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.parameter is not None and not isinstance(self.parameter, str):
            self.parameter = str(self.parameter)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass
class Qualifier(TestEntityParameter):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TTM["Qualifier"]
    class_class_curie: ClassVar[str] = "ttm:Qualifier"
    class_name: ClassVar[str] = "Qualifier"
    class_model_uri: ClassVar[URIRef] = TTM.Qualifier

    parameter: Optional[str] = None
    value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.parameter is not None and not isinstance(self.parameter, str):
            self.parameter = str(self.parameter)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass
class TestEntity(YAMLRoot):
    """
    Abstract global 'identification' class shared as a parent with all major model classes within the data model for
    Translator testing.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TTM["TestEntity"]
    class_class_curie: ClassVar[str] = "ttm:TestEntity"
    class_name: ClassVar[str] = "TestEntity"
    class_model_uri: ClassVar[URIRef] = TTM.TestEntity

    id: Union[str, TestEntityId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Union[str, List[str]]] = empty_list()
    test_runner_settings: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TestEntityId):
            self.id = TestEntityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.tags, list):
            self.tags = [self.tags] if self.tags is not None else []
        self.tags = [v if isinstance(v, str) else str(v) for v in self.tags]

        if not isinstance(self.test_runner_settings, list):
            self.test_runner_settings = [self.test_runner_settings] if self.test_runner_settings is not None else []
        self.test_runner_settings = [v if isinstance(v, str) else str(v) for v in self.test_runner_settings]

        super().__post_init__(**kwargs)


@dataclass
class TestMetadata(TestEntity):
    """
    Represents metadata related to (external SME, SMURF, Translator feedback, large scale batch, etc.) like the
    provenance of test assets, cases and/or suites.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TTM["TestMetadata"]
    class_class_curie: ClassVar[str] = "ttm:TestMetadata"
    class_name: ClassVar[str] = "TestMetadata"
    class_model_uri: ClassVar[URIRef] = TTM.TestMetadata

    id: Union[str, TestMetadataId] = None
    test_source: Optional[Union[str, "TestSourceEnum"]] = None
    test_reference: Optional[Union[str, URIorCURIE]] = None
    test_objective: Optional[Union[str, "TestObjectiveEnum"]] = None
    test_annotations: Optional[Union[Union[dict, TestEntityParameter], List[Union[dict, TestEntityParameter]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TestMetadataId):
            self.id = TestMetadataId(self.id)

        if self.test_source is not None and not isinstance(self.test_source, TestSourceEnum):
            self.test_source = TestSourceEnum(self.test_source)

        if self.test_reference is not None and not isinstance(self.test_reference, URIorCURIE):
            self.test_reference = URIorCURIE(self.test_reference)

        if self.test_objective is not None and not isinstance(self.test_objective, TestObjectiveEnum):
            self.test_objective = TestObjectiveEnum(self.test_objective)

        if not isinstance(self.test_annotations, list):
            self.test_annotations = [self.test_annotations] if self.test_annotations is not None else []
        self.test_annotations = [v if isinstance(v, TestEntityParameter) else TestEntityParameter(**as_dict(v)) for v in self.test_annotations]

        super().__post_init__(**kwargs)


@dataclass
class TestAsset(TestEntity):
    """
    Represents a Test Asset, which is a single specific instance of TestCase-agnostic semantic parameters representing
    the specification of a Translator test target with inputs and (expected) outputs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TTM["TestAsset"]
    class_class_curie: ClassVar[str] = "ttm:TestAsset"
    class_name: ClassVar[str] = "TestAsset"
    class_model_uri: ClassVar[URIRef] = TTM.TestAsset

    id: Union[str, TestAssetId] = None
    test_metadata: Union[dict, TestMetadata] = None
    input_id: Optional[Union[str, URIorCURIE]] = None
    input_name: Optional[str] = None
    input_category: Optional[Union[str, ConceptCategory]] = None
    predicate_id: Optional[Union[str, PredicateType]] = None
    predicate_name: Optional[str] = None
    output_id: Optional[Union[str, URIorCURIE]] = None
    output_name: Optional[str] = None
    output_category: Optional[Union[str, ConceptCategory]] = None
    association: Optional[Union[str, AssociationCategory]] = None
    qualifiers: Optional[Union[Union[dict, Qualifier], List[Union[dict, Qualifier]]]] = empty_list()
    expected_output: Optional[str] = None
    test_issue: Optional[Union[str, "TestIssueEnum"]] = None
    semantic_severity: Optional[Union[str, "SemanticSeverityEnum"]] = None
    in_v1: Optional[Union[bool, Bool]] = None
    well_known: Optional[Union[bool, Bool]] = None
    test_reference: Optional[Union[str, URIorCURIE]] = None
    tags: Optional[Union[str, List[str]]] = empty_list()
    test_runner_settings: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TestAssetId):
            self.id = TestAssetId(self.id)

        if self._is_empty(self.test_metadata):
            self.MissingRequiredField("test_metadata")
        if not isinstance(self.test_metadata, TestMetadata):
            self.test_metadata = TestMetadata(**as_dict(self.test_metadata))

        if self.input_id is not None and not isinstance(self.input_id, URIorCURIE):
            self.input_id = URIorCURIE(self.input_id)

        if self.input_name is not None and not isinstance(self.input_name, str):
            self.input_name = str(self.input_name)

        if self.input_category is not None and not isinstance(self.input_category, ConceptCategory):
            self.input_category = ConceptCategory(self.input_category)

        if self.predicate_id is not None and not isinstance(self.predicate_id, PredicateType):
            self.predicate_id = PredicateType(self.predicate_id)

        if self.predicate_name is not None and not isinstance(self.predicate_name, str):
            self.predicate_name = str(self.predicate_name)

        if self.output_id is not None and not isinstance(self.output_id, URIorCURIE):
            self.output_id = URIorCURIE(self.output_id)

        if self.output_name is not None and not isinstance(self.output_name, str):
            self.output_name = str(self.output_name)

        if self.output_category is not None and not isinstance(self.output_category, ConceptCategory):
            self.output_category = ConceptCategory(self.output_category)

        if self.association is not None and not isinstance(self.association, AssociationCategory):
            self.association = AssociationCategory(self.association)

        if not isinstance(self.qualifiers, list):
            self.qualifiers = [self.qualifiers] if self.qualifiers is not None else []
        self.qualifiers = [v if isinstance(v, Qualifier) else Qualifier(**as_dict(v)) for v in self.qualifiers]

        if self.expected_output is not None and not isinstance(self.expected_output, str):
            self.expected_output = str(self.expected_output)

        if self.test_issue is not None and not isinstance(self.test_issue, TestIssueEnum):
            self.test_issue = TestIssueEnum(self.test_issue)

        if self.semantic_severity is not None and not isinstance(self.semantic_severity, SemanticSeverityEnum):
            self.semantic_severity = SemanticSeverityEnum(self.semantic_severity)

        if self.in_v1 is not None and not isinstance(self.in_v1, Bool):
            self.in_v1 = Bool(self.in_v1)

        if self.well_known is not None and not isinstance(self.well_known, Bool):
            self.well_known = Bool(self.well_known)

        if self.test_reference is not None and not isinstance(self.test_reference, URIorCURIE):
            self.test_reference = URIorCURIE(self.test_reference)

        if not isinstance(self.tags, list):
            self.tags = [self.tags] if self.tags is not None else []
        self.tags = [v if isinstance(v, str) else str(v) for v in self.tags]

        if not isinstance(self.test_runner_settings, list):
            self.test_runner_settings = [self.test_runner_settings] if self.test_runner_settings is not None else []
        self.test_runner_settings = [v if isinstance(v, str) else str(v) for v in self.test_runner_settings]

        super().__post_init__(**kwargs)


@dataclass
class AcceptanceTestAsset(TestAsset):
    """
    Model derived from Jenn's test asset design and Shervin's runner JSON here as an example.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TTM["AcceptanceTestAsset"]
    class_class_curie: ClassVar[str] = "ttm:AcceptanceTestAsset"
    class_name: ClassVar[str] = "AcceptanceTestAsset"
    class_model_uri: ClassVar[URIRef] = TTM.AcceptanceTestAsset

    id: Union[str, AcceptanceTestAssetId] = None
    test_metadata: Union[dict, TestMetadata] = None
    must_pass_date: Optional[Union[str, XSDDate]] = None
    must_pass_environment: Optional[Union[str, "TestEnvEnum"]] = None
    scientific_question: Optional[str] = None
    string_entry: Optional[str] = None
    direction: Optional[Union[str, "DirectionEnum"]] = None
    answer_informal_concept: Optional[str] = None
    expected_result: Optional[Union[str, "ExpectedResultsEnum"]] = None
    top_level: Optional[int] = None
    query_node: Optional[Union[str, "NodeEnum"]] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcceptanceTestAssetId):
            self.id = AcceptanceTestAssetId(self.id)

        if self.must_pass_date is not None and not isinstance(self.must_pass_date, XSDDate):
            self.must_pass_date = XSDDate(self.must_pass_date)

        if self.must_pass_environment is not None and not isinstance(self.must_pass_environment, TestEnvEnum):
            self.must_pass_environment = TestEnvEnum(self.must_pass_environment)

        if self.scientific_question is not None and not isinstance(self.scientific_question, str):
            self.scientific_question = str(self.scientific_question)

        if self.string_entry is not None and not isinstance(self.string_entry, str):
            self.string_entry = str(self.string_entry)

        if self.direction is not None and not isinstance(self.direction, DirectionEnum):
            self.direction = DirectionEnum(self.direction)

        if self.answer_informal_concept is not None and not isinstance(self.answer_informal_concept, str):
            self.answer_informal_concept = str(self.answer_informal_concept)

        if self.expected_result is not None and not isinstance(self.expected_result, ExpectedResultsEnum):
            self.expected_result = ExpectedResultsEnum(self.expected_result)

        if self.top_level is not None and not isinstance(self.top_level, int):
            self.top_level = int(self.top_level)

        if self.query_node is not None and not isinstance(self.query_node, NodeEnum):
            self.query_node = NodeEnum(self.query_node)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass
class TestEdgeData(TestAsset):
    """
    Represents a single Biolink Model compliant instance of a subject-predicate-object edge that can be used for
    testing.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TTM["TestEdgeData"]
    class_class_curie: ClassVar[str] = "ttm:TestEdgeData"
    class_name: ClassVar[str] = "TestEdgeData"
    class_model_uri: ClassVar[URIRef] = TTM.TestEdgeData

    id: Union[str, TestEdgeDataId] = None
    test_metadata: Union[dict, TestMetadata] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TestEdgeDataId):
            self.id = TestEdgeDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Precondition(TestEntity):
    """
    Represents a precondition for a TestCase
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TTM["Precondition"]
    class_class_curie: ClassVar[str] = "ttm:Precondition"
    class_name: ClassVar[str] = "Precondition"
    class_model_uri: ClassVar[URIRef] = TTM.Precondition

    id: Union[str, PreconditionId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PreconditionId):
            self.id = PreconditionId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class TestCase(TestEntity):
    """
    Represents a single enumerated instance of Test Case, derived from a given collection of one or more TestAsset
    instances (the value of the 'test_assets' slot) which define the 'inputs' and 'outputs' of the TestCase, used to
    probe a particular test condition.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TTM["TestCase"]
    class_class_curie: ClassVar[str] = "ttm:TestCase"
    class_name: ClassVar[str] = "TestCase"
    class_model_uri: ClassVar[URIRef] = TTM.TestCase

    id: Union[str, TestCaseId] = None
    test_assets: Union[Dict[Union[str, TestAssetId], Union[dict, TestAsset]], List[Union[dict, TestAsset]]] = empty_dict()
    query_type: Optional[Union[str, "QueryTypeEnum"]] = None
    preconditions: Optional[Union[Union[str, PreconditionId], List[Union[str, PreconditionId]]]] = empty_list()
    trapi_template: Optional[Union[str, "TrapiTemplateEnum"]] = None
    test_case_objective: Optional[Union[str, "TestObjectiveEnum"]] = None
    test_case_source: Optional[Union[str, "TestSourceEnum"]] = None
    test_case_predicate_name: Optional[str] = None
    test_case_predicate_id: Optional[str] = None
    test_case_input_id: Optional[Union[str, URIorCURIE]] = None
    qualifiers: Optional[Union[Union[dict, Qualifier], List[Union[dict, Qualifier]]]] = empty_list()
    input_category: Optional[Union[str, ConceptCategory]] = None
    output_category: Optional[Union[str, ConceptCategory]] = None
    components: Optional[Union[Union[str, "ComponentEnum"], List[Union[str, "ComponentEnum"]]]] = empty_list()
    test_env: Optional[Union[str, "TestEnvEnum"]] = None
    tags: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TestCaseId):
            self.id = TestCaseId(self.id)

        if self._is_empty(self.test_assets):
            self.MissingRequiredField("test_assets")
        self._normalize_inlined_as_list(slot_name="test_assets", slot_type=TestAsset, key_name="id", keyed=True)

        if self.query_type is not None and not isinstance(self.query_type, QueryTypeEnum):
            self.query_type = QueryTypeEnum(self.query_type)

        if not isinstance(self.preconditions, list):
            self.preconditions = [self.preconditions] if self.preconditions is not None else []
        self.preconditions = [v if isinstance(v, PreconditionId) else PreconditionId(v) for v in self.preconditions]

        if self.trapi_template is not None and not isinstance(self.trapi_template, TrapiTemplateEnum):
            self.trapi_template = TrapiTemplateEnum(self.trapi_template)

        if self.test_case_objective is not None and not isinstance(self.test_case_objective, TestObjectiveEnum):
            self.test_case_objective = TestObjectiveEnum(self.test_case_objective)

        if self.test_case_source is not None and not isinstance(self.test_case_source, TestSourceEnum):
            self.test_case_source = TestSourceEnum(self.test_case_source)

        if self.test_case_predicate_name is not None and not isinstance(self.test_case_predicate_name, str):
            self.test_case_predicate_name = str(self.test_case_predicate_name)

        if self.test_case_predicate_id is not None and not isinstance(self.test_case_predicate_id, str):
            self.test_case_predicate_id = str(self.test_case_predicate_id)

        if self.test_case_input_id is not None and not isinstance(self.test_case_input_id, URIorCURIE):
            self.test_case_input_id = URIorCURIE(self.test_case_input_id)

        if not isinstance(self.qualifiers, list):
            self.qualifiers = [self.qualifiers] if self.qualifiers is not None else []
        self.qualifiers = [v if isinstance(v, Qualifier) else Qualifier(**as_dict(v)) for v in self.qualifiers]

        if self.input_category is not None and not isinstance(self.input_category, ConceptCategory):
            self.input_category = ConceptCategory(self.input_category)

        if self.output_category is not None and not isinstance(self.output_category, ConceptCategory):
            self.output_category = ConceptCategory(self.output_category)

        if self.test_env is not None and not isinstance(self.test_env, TestEnvEnum):
            self.test_env = TestEnvEnum(self.test_env)

        if not isinstance(self.tags, list):
            self.tags = [self.tags] if self.tags is not None else []
        self.tags = [v if isinstance(v, str) else str(v) for v in self.tags]

        super().__post_init__(**kwargs)


@dataclass
class AcceptanceTestCase(TestCase):
    """
    See AcceptanceTestAsset above for more details.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TTM["AcceptanceTestCase"]
    class_class_curie: ClassVar[str] = "ttm:AcceptanceTestCase"
    class_name: ClassVar[str] = "AcceptanceTestCase"
    class_model_uri: ClassVar[URIRef] = TTM.AcceptanceTestCase

    id: Union[str, AcceptanceTestCaseId] = None
    test_assets: Union[Dict[Union[str, AcceptanceTestAssetId], Union[dict, AcceptanceTestAsset]], List[Union[dict, AcceptanceTestAsset]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcceptanceTestCaseId):
            self.id = AcceptanceTestCaseId(self.id)

        if self._is_empty(self.test_assets):
            self.MissingRequiredField("test_assets")
        self._normalize_inlined_as_list(slot_name="test_assets", slot_type=AcceptanceTestAsset, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class QuantitativeTestCase(TestCase):
    """
    Assumed additional model from Shervin's runner JSON here as an example.  This schema is not yet complete.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TTM["QuantitativeTestCase"]
    class_class_curie: ClassVar[str] = "ttm:QuantitativeTestCase"
    class_name: ClassVar[str] = "QuantitativeTestCase"
    class_model_uri: ClassVar[URIRef] = TTM.QuantitativeTestCase

    id: Union[str, QuantitativeTestCaseId] = None
    test_assets: Union[Dict[Union[str, TestAssetId], Union[dict, TestAsset]], List[Union[dict, TestAsset]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuantitativeTestCaseId):
            self.id = QuantitativeTestCaseId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class TestSuiteSpecification(TestEntity):
    """
    Parameters for a Test Case instances either dynamically generated from some external source of Test Assets.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TTM["TestSuiteSpecification"]
    class_class_curie: ClassVar[str] = "ttm:TestSuiteSpecification"
    class_name: ClassVar[str] = "TestSuiteSpecification"
    class_model_uri: ClassVar[URIRef] = TTM.TestSuiteSpecification

    id: Union[str, TestSuiteSpecificationId] = None
    test_data_file_locator: Optional[Union[str, URIorCURIE]] = None
    test_data_file_format: Optional[Union[str, "FileFormatEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TestSuiteSpecificationId):
            self.id = TestSuiteSpecificationId(self.id)

        if self.test_data_file_locator is not None and not isinstance(self.test_data_file_locator, URIorCURIE):
            self.test_data_file_locator = URIorCURIE(self.test_data_file_locator)

        if self.test_data_file_format is not None and not isinstance(self.test_data_file_format, FileFormatEnum):
            self.test_data_file_format = FileFormatEnum(self.test_data_file_format)

        super().__post_init__(**kwargs)


@dataclass
class TestSuite(TestEntity):
    """
    Specification of a set of Test Cases, one of either with a static list of 'test_cases' or a dynamic
    'test_suite_specification' slot values. Note: at least one slot or the other, but generally not both(?) needs to
    be present.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TTM["TestSuite"]
    class_class_curie: ClassVar[str] = "ttm:TestSuite"
    class_name: ClassVar[str] = "TestSuite"
    class_model_uri: ClassVar[URIRef] = TTM.TestSuite

    id: Union[str, TestSuiteId] = None
    test_metadata: Union[dict, TestMetadata] = None
    test_persona: Optional[Union[str, "TestPersonaEnum"]] = None
    test_cases: Optional[Union[Dict[Union[str, TestCaseId], Union[dict, TestCase]], List[Union[dict, TestCase]]]] = empty_dict()
    test_suite_specification: Optional[Union[dict, TestSuiteSpecification]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TestSuiteId):
            self.id = TestSuiteId(self.id)

        if self._is_empty(self.test_metadata):
            self.MissingRequiredField("test_metadata")
        if not isinstance(self.test_metadata, TestMetadata):
            self.test_metadata = TestMetadata(**as_dict(self.test_metadata))

        if self.test_persona is not None and not isinstance(self.test_persona, TestPersonaEnum):
            self.test_persona = TestPersonaEnum(self.test_persona)

        self._normalize_inlined_as_dict(slot_name="test_cases", slot_type=TestCase, key_name="id", keyed=True)

        if self.test_suite_specification is not None and not isinstance(self.test_suite_specification, TestSuiteSpecification):
            self.test_suite_specification = TestSuiteSpecification(**as_dict(self.test_suite_specification))

        super().__post_init__(**kwargs)


@dataclass
class AcceptanceTestSuite(TestSuite):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TTM["AcceptanceTestSuite"]
    class_class_curie: ClassVar[str] = "ttm:AcceptanceTestSuite"
    class_name: ClassVar[str] = "AcceptanceTestSuite"
    class_model_uri: ClassVar[URIRef] = TTM.AcceptanceTestSuite

    id: Union[str, AcceptanceTestSuiteId] = None
    test_metadata: Union[dict, TestMetadata] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcceptanceTestSuiteId):
            self.id = AcceptanceTestSuiteId(self.id)

        super().__post_init__(**kwargs)


class BenchmarkTestSuite(YAMLRoot):
    """
    JsonObj(is_a='TestSuite')
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TTM["BenchmarkTestSuite"]
    class_class_curie: ClassVar[str] = "ttm:BenchmarkTestSuite"
    class_name: ClassVar[str] = "BenchmarkTestSuite"
    class_model_uri: ClassVar[URIRef] = TTM.BenchmarkTestSuite


@dataclass
class StandardsComplianceTestSuite(TestSuite):
    """
    Test suite for testing Translator components against releases of standards like TRAPI and the Biolink Model.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TTM["StandardsComplianceTestSuite"]
    class_class_curie: ClassVar[str] = "ttm:StandardsComplianceTestSuite"
    class_name: ClassVar[str] = "StandardsComplianceTestSuite"
    class_model_uri: ClassVar[URIRef] = TTM.StandardsComplianceTestSuite

    id: Union[str, StandardsComplianceTestSuiteId] = None
    test_metadata: Union[dict, TestMetadata] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StandardsComplianceTestSuiteId):
            self.id = StandardsComplianceTestSuiteId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class OneHopTestSuite(TestSuite):
    """
    Test case for testing the integrity of "One Hop" knowledge graph retrievals sensa legacy SRI_Testing harness.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TTM["OneHopTestSuite"]
    class_class_curie: ClassVar[str] = "ttm:OneHopTestSuite"
    class_name: ClassVar[str] = "OneHopTestSuite"
    class_model_uri: ClassVar[URIRef] = TTM.OneHopTestSuite

    id: Union[str, OneHopTestSuiteId] = None
    test_metadata: Union[dict, TestMetadata] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OneHopTestSuiteId):
            self.id = OneHopTestSuiteId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class TestCaseResult(TestEntity):
    """
    The outcome of a TestRunner run of one specific TestCase.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TTM["TestCaseResult"]
    class_class_curie: ClassVar[str] = "ttm:TestCaseResult"
    class_name: ClassVar[str] = "TestCaseResult"
    class_model_uri: ClassVar[URIRef] = TTM.TestCaseResult

    id: Union[str, TestCaseResultId] = None
    test_suite_id: Optional[Union[str, URIorCURIE]] = None
    test_case: Optional[Union[dict, TestCase]] = None
    test_case_result: Optional[Union[str, "TestCaseResultEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TestCaseResultId):
            self.id = TestCaseResultId(self.id)

        if self.test_suite_id is not None and not isinstance(self.test_suite_id, URIorCURIE):
            self.test_suite_id = URIorCURIE(self.test_suite_id)

        if self.test_case is not None and not isinstance(self.test_case, TestCase):
            self.test_case = TestCase(**as_dict(self.test_case))

        if self.test_case_result is not None and not isinstance(self.test_case_result, TestCaseResultEnum):
            self.test_case_result = TestCaseResultEnum(self.test_case_result)

        super().__post_init__(**kwargs)


@dataclass
class TestRunSession(TestEntity):
    """
    Single run of a TestRunner in a given environment, with a specified set of test_entities (generally, one or more
    instances of TestSuite).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TTM["TestRunSession"]
    class_class_curie: ClassVar[str] = "ttm:TestRunSession"
    class_name: ClassVar[str] = "TestRunSession"
    class_model_uri: ClassVar[URIRef] = TTM.TestRunSession

    id: Union[str, TestRunSessionId] = None
    components: Optional[Union[Union[str, "ComponentEnum"], List[Union[str, "ComponentEnum"]]]] = empty_list()
    test_env: Optional[Union[str, "TestEnvEnum"]] = None
    test_runner_name: Optional[str] = None
    test_run_parameters: Optional[Union[Union[dict, TestEntityParameter], List[Union[dict, TestEntityParameter]]]] = empty_list()
    test_entities: Optional[Union[Dict[Union[str, TestEntityId], Union[dict, TestEntity]], List[Union[dict, TestEntity]]]] = empty_dict()
    test_case_results: Optional[Union[Dict[Union[str, TestCaseResultId], Union[dict, TestCaseResult]], List[Union[dict, TestCaseResult]]]] = empty_dict()
    timestamp: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TestRunSessionId):
            self.id = TestRunSessionId(self.id)

        if self.test_env is not None and not isinstance(self.test_env, TestEnvEnum):
            self.test_env = TestEnvEnum(self.test_env)

        if self.test_runner_name is not None and not isinstance(self.test_runner_name, str):
            self.test_runner_name = str(self.test_runner_name)

        if not isinstance(self.test_run_parameters, list):
            self.test_run_parameters = [self.test_run_parameters] if self.test_run_parameters is not None else []
        self.test_run_parameters = [v if isinstance(v, TestEntityParameter) else TestEntityParameter(**as_dict(v)) for v in self.test_run_parameters]

        self._normalize_inlined_as_dict(slot_name="test_entities", slot_type=TestEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="test_case_results", slot_type=TestCaseResult, key_name="id", keyed=True)

        if self.timestamp is not None and not isinstance(self.timestamp, XSDDateTime):
            self.timestamp = XSDDateTime(self.timestamp)

        super().__post_init__(**kwargs)


@dataclass
class TestOutput(TestEntity):
    """
    The output of a TestRunner run of one specific TestCase.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TTM["TestOutput"]
    class_class_curie: ClassVar[str] = "ttm:TestOutput"
    class_name: ClassVar[str] = "TestOutput"
    class_model_uri: ClassVar[URIRef] = TTM.TestOutput

    id: Union[str, TestOutputId] = None
    test_case_id: Optional[str] = None
    pks: Optional[Union[Union[str, TestResultPKSetId], List[Union[str, TestResultPKSetId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TestOutputId):
            self.id = TestOutputId(self.id)

        if self.test_case_id is not None and not isinstance(self.test_case_id, str):
            self.test_case_id = str(self.test_case_id)

        if not isinstance(self.pks, list):
            self.pks = [self.pks] if self.pks is not None else []
        self.pks = [v if isinstance(v, TestResultPKSetId) else TestResultPKSetId(v) for v in self.pks]

        super().__post_init__(**kwargs)


@dataclass
class TestResultPKSet(TestEntity):
    """
    Primary keys for a given ARA result set from a SmokeTest result for a given TestCase.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TTM["TestResultPKSet"]
    class_class_curie: ClassVar[str] = "ttm:TestResultPKSet"
    class_name: ClassVar[str] = "TestResultPKSet"
    class_model_uri: ClassVar[URIRef] = TTM.TestResultPKSet

    id: Union[str, TestResultPKSetId] = None
    parent_pk: Optional[str] = None
    merged_pk: Optional[str] = None
    aragorn: Optional[str] = None
    arax: Optional[str] = None
    unsecret: Optional[str] = None
    bte: Optional[str] = None
    improving: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TestResultPKSetId):
            self.id = TestResultPKSetId(self.id)

        if self.parent_pk is not None and not isinstance(self.parent_pk, str):
            self.parent_pk = str(self.parent_pk)

        if self.merged_pk is not None and not isinstance(self.merged_pk, str):
            self.merged_pk = str(self.merged_pk)

        if self.aragorn is not None and not isinstance(self.aragorn, str):
            self.aragorn = str(self.aragorn)

        if self.arax is not None and not isinstance(self.arax, str):
            self.arax = str(self.arax)

        if self.unsecret is not None and not isinstance(self.unsecret, str):
            self.unsecret = str(self.unsecret)

        if self.bte is not None and not isinstance(self.bte, str):
            self.bte = str(self.bte)

        if self.improving is not None and not isinstance(self.improving, str):
            self.improving = str(self.improving)

        super().__post_init__(**kwargs)


# Enumerations
class TestSourceEnum(EnumDefinitionImpl):

    SME = PermissibleValue(
        text="SME",
        description="(External) Subject Matter Expert")
    SMURF = PermissibleValue(
        text="SMURF",
        description="""Subject Matter User Reasonably Familiar, generally Translator-internal biomedical science expert""")
    GitHubUserFeedback = PermissibleValue(
        text="GitHubUserFeedback",
        description="Git hub hosted issue from which a test asset/case/suite may be derived.")
    TACT = PermissibleValue(
        text="TACT",
        description="""Technical Advisory Committee, generally posting semantic use cases as Translator Feedback issues""")
    BenchMark = PermissibleValue(
        text="BenchMark",
        description="Curated benchmark tests")
    TranslatorTeam = PermissibleValue(
        text="TranslatorTeam",
        description="Translator funded KP or ARA team generating test assets/cases/suites for their resources.")
    TestDataLocation = PermissibleValue(
        text="TestDataLocation",
        description="Current SRI_Testing-like test data edges specific to KP or ARA components")

    _defn = EnumDefinition(
        name="TestSourceEnum",
    )

class TestObjectiveEnum(EnumDefinitionImpl):

    AcceptanceTest = PermissibleValue(
        text="AcceptanceTest",
        description="Acceptance (pass/fail) test")
    BenchmarkTest = PermissibleValue(
        text="BenchmarkTest",
        description="Semantic benchmarking")
    QuantitativeTest = PermissibleValue(
        text="QuantitativeTest",
        description="Quantitative test")
    StandardsValidationTest = PermissibleValue(
        text="StandardsValidationTest",
        description="Release-specific TRAPI and Biolink Model (\"reasoner-validator\") compliance validation")
    OneHopTest = PermissibleValue(
        text="OneHopTest",
        description="Knowledge graph \"One Hop\" query navigation integrity")

    _defn = EnumDefinition(
        name="TestObjectiveEnum",
    )

class TestEnvEnum(EnumDefinitionImpl):
    """
    Testing environments within which a TestSuite is run by a TestRunner scheduled by the TestHarness.
    """
    dev = PermissibleValue(
        text="dev",
        description="Development")
    ci = PermissibleValue(
        text="ci",
        description="Continuous Integration")
    test = PermissibleValue(
        text="test",
        description="Test")
    prod = PermissibleValue(
        text="prod",
        description="Production")

    _defn = EnumDefinition(
        name="TestEnvEnum",
        description="Testing environments within which a TestSuite is run by a TestRunner scheduled by the TestHarness.",
    )

class FileFormatEnum(EnumDefinitionImpl):
    """
    Text file formats for test data sources.
    """
    TSV = PermissibleValue(text="TSV")
    YAML = PermissibleValue(text="YAML")
    JSON = PermissibleValue(text="JSON")

    _defn = EnumDefinition(
        name="FileFormatEnum",
        description="Text file formats for test data sources.",
    )

class ExpectedOutputEnum(EnumDefinitionImpl):
    """
    Expected output values for instances of Test Asset or Test Cases(?). (Note: does this Enum overlap with
    'ExpectedResultsEnum' below?)
    """
    Acceptable = PermissibleValue(text="Acceptable")
    BadButForgivable = PermissibleValue(text="BadButForgivable")
    NeverShow = PermissibleValue(text="NeverShow")
    TopAnswer = PermissibleValue(text="TopAnswer")
    OverlyGeneric = PermissibleValue(text="OverlyGeneric")

    _defn = EnumDefinition(
        name="ExpectedOutputEnum",
        description="""Expected output values for instances of Test Asset or Test Cases(?). (Note: does this Enum overlap with 'ExpectedResultsEnum' below?)""",
    )

class TestIssueEnum(EnumDefinitionImpl):

    TMKP = PermissibleValue(
        text="TMKP",
        description="'Text Mining Knowledge Provider' generated relationship?")
    contraindications = PermissibleValue(text="contraindications")
    test_issue = PermissibleValue(text="test_issue")

    _defn = EnumDefinition(
        name="TestIssueEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "causes not treats",
            PermissibleValue(text="causes not treats"))
        setattr(cls, "category too generic",
            PermissibleValue(text="category too generic"))
        setattr(cls, "chemical roles",
            PermissibleValue(text="chemical roles"))

class SemanticSeverityEnum(EnumDefinitionImpl):
    """
    From Jenn's worksheet, empty or ill defined (needs elaboration)
    """
    High = PermissibleValue(text="High")
    Low = PermissibleValue(text="Low")
    NotApplicable = PermissibleValue(text="NotApplicable")

    _defn = EnumDefinition(
        name="SemanticSeverityEnum",
        description="From Jenn's worksheet, empty or ill defined (needs elaboration)",
    )

class DirectionEnum(EnumDefinitionImpl):

    increased = PermissibleValue(text="increased")
    decreased = PermissibleValue(text="decreased")

    _defn = EnumDefinition(
        name="DirectionEnum",
    )

class ExpectedResultsEnum(EnumDefinitionImpl):
    """
    Does this Enum overlap with 'ExpectedOutputEnum' above?
    """
    include_good = PermissibleValue(
        text="include_good",
        description="The query should return the result in this test case")
    exclude_bad = PermissibleValue(
        text="exclude_bad",
        description="The query should not return the result in this test case")

    _defn = EnumDefinition(
        name="ExpectedResultsEnum",
        description="Does this Enum overlap with 'ExpectedOutputEnum' above?",
    )

class NodeEnum(EnumDefinitionImpl):
    """
    Target node of a Subject-Predicate-Object driven query
    """
    subject = PermissibleValue(text="subject")
    object = PermissibleValue(text="object")

    _defn = EnumDefinition(
        name="NodeEnum",
        description="Target node of a Subject-Predicate-Object driven query",
    )

class QueryTypeEnum(EnumDefinitionImpl):
    """
    Query
    """
    treats = PermissibleValue(text="treats")

    _defn = EnumDefinition(
        name="QueryTypeEnum",
        description="Query",
    )

class TrapiTemplateEnum(EnumDefinitionImpl):

    ameliorates = PermissibleValue(text="ameliorates")
    treats = PermissibleValue(text="treats")
    three_hop = PermissibleValue(text="three_hop")
    drug_treats_rare_disease = PermissibleValue(text="drug_treats_rare_disease")

    _defn = EnumDefinition(
        name="TrapiTemplateEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "drug-to-gene",
            PermissibleValue(text="drug-to-gene"))

class ComponentEnum(EnumDefinitionImpl):
    """
    Translator components are identified by their InfoRes identifiers.
    """
    _defn = EnumDefinition(
        name="ComponentEnum",
        description="Translator components are identified by their InfoRes identifiers.",
    )

class TestPersonaEnum(EnumDefinitionImpl):
    """
    User persona context of a given test.
    """
    All = PermissibleValue(text="All")
    Clinical = PermissibleValue(
        text="Clinical",
        description="An MD or someone working in the clinical field.")
    LookUp = PermissibleValue(
        text="LookUp",
        description="Looking for an answer for a specific patient.")
    Mechanistic = PermissibleValue(
        text="Mechanistic",
        description="""Someone working on basic biology questions or drug discoveries where the study of the biological mechanism.""")

    _defn = EnumDefinition(
        name="TestPersonaEnum",
        description="User persona context of a given test.",
    )

class TestCaseResultEnum(EnumDefinitionImpl):

    PASSED = PermissibleValue(
        text="PASSED",
        description="test case result indicating success.")
    FAILED = PermissibleValue(
        text="FAILED",
        description="test case result indicating failure.")
    SKIPPED = PermissibleValue(
        text="SKIPPED",
        description="test case result indicating that the specified test was not run.")

    _defn = EnumDefinition(
        name="TestCaseResultEnum",
    )

# Slots
class slots:
    pass

slots.parent_pk = Slot(uri=TTM.parent_pk, name="parent_pk", curie=TTM.curie('parent_pk'),
                   model_uri=TTM.parent_pk, domain=None, range=Optional[str])

slots.merged_pk = Slot(uri=TTM.merged_pk, name="merged_pk", curie=TTM.curie('merged_pk'),
                   model_uri=TTM.merged_pk, domain=None, range=Optional[str])

slots.aragorn = Slot(uri=TTM.aragorn, name="aragorn", curie=TTM.curie('aragorn'),
                   model_uri=TTM.aragorn, domain=None, range=Optional[str])

slots.arax = Slot(uri=TTM.arax, name="arax", curie=TTM.curie('arax'),
                   model_uri=TTM.arax, domain=None, range=Optional[str])

slots.unsecret = Slot(uri=TTM.unsecret, name="unsecret", curie=TTM.curie('unsecret'),
                   model_uri=TTM.unsecret, domain=None, range=Optional[str])

slots.bte = Slot(uri=TTM.bte, name="bte", curie=TTM.curie('bte'),
                   model_uri=TTM.bte, domain=None, range=Optional[str])

slots.improving = Slot(uri=TTM.improving, name="improving", curie=TTM.curie('improving'),
                   model_uri=TTM.improving, domain=None, range=Optional[str])

slots.pks = Slot(uri=TTM.pks, name="pks", curie=TTM.curie('pks'),
                   model_uri=TTM.pks, domain=None, range=Optional[Union[Union[str, TestResultPKSetId], List[Union[str, TestResultPKSetId]]]])

slots.results = Slot(uri=TTM.results, name="results", curie=TTM.curie('results'),
                   model_uri=TTM.results, domain=None, range=Optional[Union[Union[str, TestOutputId], List[Union[str, TestOutputId]]]])

slots.test_case_id = Slot(uri=TTM.test_case_id, name="test_case_id", curie=TTM.curie('test_case_id'),
                   model_uri=TTM.test_case_id, domain=None, range=Optional[str])

slots.parameter = Slot(uri=TTM.parameter, name="parameter", curie=TTM.curie('parameter'),
                   model_uri=TTM.parameter, domain=None, range=Optional[str])

slots.value = Slot(uri=TTM.value, name="value", curie=TTM.curie('value'),
                   model_uri=TTM.value, domain=None, range=Optional[str])

slots.test_entity_parameters = Slot(uri=TTM.test_entity_parameters, name="test_entity_parameters", curie=TTM.curie('test_entity_parameters'),
                   model_uri=TTM.test_entity_parameters, domain=None, range=Optional[Union[Union[dict, TestEntityParameter], List[Union[dict, TestEntityParameter]]]])

slots.timestamp = Slot(uri=TTM.timestamp, name="timestamp", curie=TTM.curie('timestamp'),
                   model_uri=TTM.timestamp, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=TTM.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=TTM.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=TTM.description, domain=None, range=Optional[str])

slots.tags = Slot(uri=SCHEMA.additionalType, name="tags", curie=SCHEMA.curie('additionalType'),
                   model_uri=TTM.tags, domain=None, range=Optional[Union[str, List[str]]])

slots.test_source = Slot(uri=TTM.test_source, name="test_source", curie=TTM.curie('test_source'),
                   model_uri=TTM.test_source, domain=None, range=Optional[Union[str, "TestSourceEnum"]])

slots.test_reference = Slot(uri=TTM.test_reference, name="test_reference", curie=TTM.curie('test_reference'),
                   model_uri=TTM.test_reference, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.test_objective = Slot(uri=TTM.test_objective, name="test_objective", curie=TTM.curie('test_objective'),
                   model_uri=TTM.test_objective, domain=None, range=Optional[Union[str, "TestObjectiveEnum"]])

slots.test_case_objective = Slot(uri=TTM.test_case_objective, name="test_case_objective", curie=TTM.curie('test_case_objective'),
                   model_uri=TTM.test_case_objective, domain=None, range=Optional[Union[str, "TestObjectiveEnum"]])

slots.test_case_source = Slot(uri=TTM.test_case_source, name="test_case_source", curie=TTM.curie('test_case_source'),
                   model_uri=TTM.test_case_source, domain=None, range=Optional[Union[str, "TestSourceEnum"]])

slots.test_annotations = Slot(uri=TTM.test_annotations, name="test_annotations", curie=TTM.curie('test_annotations'),
                   model_uri=TTM.test_annotations, domain=None, range=Optional[Union[Union[dict, TestEntityParameter], List[Union[dict, TestEntityParameter]]]])

slots.test_case_input_id = Slot(uri=TTM.test_case_input_id, name="test_case_input_id", curie=TTM.curie('test_case_input_id'),
                   model_uri=TTM.test_case_input_id, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.test_case_predicate_name = Slot(uri=TTM.test_case_predicate_name, name="test_case_predicate_name", curie=TTM.curie('test_case_predicate_name'),
                   model_uri=TTM.test_case_predicate_name, domain=None, range=Optional[str])

slots.test_case_predicate_id = Slot(uri=TTM.test_case_predicate_id, name="test_case_predicate_id", curie=TTM.curie('test_case_predicate_id'),
                   model_uri=TTM.test_case_predicate_id, domain=None, range=Optional[str])

slots.input_id = Slot(uri=TTM.input_id, name="input_id", curie=TTM.curie('input_id'),
                   model_uri=TTM.input_id, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.input_name = Slot(uri=TTM.input_name, name="input_name", curie=TTM.curie('input_name'),
                   model_uri=TTM.input_name, domain=None, range=Optional[str])

slots.input_category = Slot(uri=TTM.input_category, name="input_category", curie=TTM.curie('input_category'),
                   model_uri=TTM.input_category, domain=None, range=Optional[Union[str, ConceptCategory]])

slots.predicate_id = Slot(uri=TTM.predicate_id, name="predicate_id", curie=TTM.curie('predicate_id'),
                   model_uri=TTM.predicate_id, domain=None, range=Optional[Union[str, PredicateType]])

slots.predicate_name = Slot(uri=TTM.predicate_name, name="predicate_name", curie=TTM.curie('predicate_name'),
                   model_uri=TTM.predicate_name, domain=None, range=Optional[str])

slots.biolink_predicate = Slot(uri=TTM.biolink_predicate, name="biolink_predicate", curie=TTM.curie('biolink_predicate'),
                   model_uri=TTM.biolink_predicate, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.biolink_subject_aspect_qualifier = Slot(uri=TTM.biolink_subject_aspect_qualifier, name="biolink_subject_aspect_qualifier", curie=TTM.curie('biolink_subject_aspect_qualifier'),
                   model_uri=TTM.biolink_subject_aspect_qualifier, domain=None, range=Optional[str])

slots.biolink_subject_direction_qualifier = Slot(uri=TTM.biolink_subject_direction_qualifier, name="biolink_subject_direction_qualifier", curie=TTM.curie('biolink_subject_direction_qualifier'),
                   model_uri=TTM.biolink_subject_direction_qualifier, domain=None, range=Optional[str])

slots.biolink_object_aspect_qualifier = Slot(uri=TTM.biolink_object_aspect_qualifier, name="biolink_object_aspect_qualifier", curie=TTM.curie('biolink_object_aspect_qualifier'),
                   model_uri=TTM.biolink_object_aspect_qualifier, domain=None, range=Optional[str])

slots.biolink_object_direction_qualifier = Slot(uri=TTM.biolink_object_direction_qualifier, name="biolink_object_direction_qualifier", curie=TTM.curie('biolink_object_direction_qualifier'),
                   model_uri=TTM.biolink_object_direction_qualifier, domain=None, range=Optional[str])

slots.biolink_qualified_predicate = Slot(uri=TTM.biolink_qualified_predicate, name="biolink_qualified_predicate", curie=TTM.curie('biolink_qualified_predicate'),
                   model_uri=TTM.biolink_qualified_predicate, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.output_id = Slot(uri=TTM.output_id, name="output_id", curie=TTM.curie('output_id'),
                   model_uri=TTM.output_id, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.output_name = Slot(uri=TTM.output_name, name="output_name", curie=TTM.curie('output_name'),
                   model_uri=TTM.output_name, domain=None, range=Optional[str])

slots.output_category = Slot(uri=TTM.output_category, name="output_category", curie=TTM.curie('output_category'),
                   model_uri=TTM.output_category, domain=None, range=Optional[Union[str, ConceptCategory]])

slots.association = Slot(uri=TTM.association, name="association", curie=TTM.curie('association'),
                   model_uri=TTM.association, domain=None, range=Optional[Union[str, AssociationCategory]])

slots.qualifiers = Slot(uri=TTM.qualifiers, name="qualifiers", curie=TTM.curie('qualifiers'),
                   model_uri=TTM.qualifiers, domain=None, range=Optional[Union[Union[dict, Qualifier], List[Union[dict, Qualifier]]]])

slots.expected_output = Slot(uri=TTM.expected_output, name="expected_output", curie=TTM.curie('expected_output'),
                   model_uri=TTM.expected_output, domain=None, range=Optional[str])

slots.test_issue = Slot(uri=TTM.test_issue, name="test_issue", curie=TTM.curie('test_issue'),
                   model_uri=TTM.test_issue, domain=None, range=Optional[Union[str, "TestIssueEnum"]])

slots.semantic_severity = Slot(uri=TTM.semantic_severity, name="semantic_severity", curie=TTM.curie('semantic_severity'),
                   model_uri=TTM.semantic_severity, domain=None, range=Optional[Union[str, "SemanticSeverityEnum"]])

slots.in_v1 = Slot(uri=TTM.in_v1, name="in_v1", curie=TTM.curie('in_v1'),
                   model_uri=TTM.in_v1, domain=None, range=Optional[Union[bool, Bool]])

slots.well_known = Slot(uri=TTM.well_known, name="well_known", curie=TTM.curie('well_known'),
                   model_uri=TTM.well_known, domain=None, range=Optional[Union[bool, Bool]])

slots.test_runner_settings = Slot(uri=TTM.test_runner_settings, name="test_runner_settings", curie=TTM.curie('test_runner_settings'),
                   model_uri=TTM.test_runner_settings, domain=None, range=Optional[Union[str, List[str]]])

slots.must_pass_date = Slot(uri=TTM.must_pass_date, name="must_pass_date", curie=TTM.curie('must_pass_date'),
                   model_uri=TTM.must_pass_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.must_pass_environment = Slot(uri=TTM.must_pass_environment, name="must_pass_environment", curie=TTM.curie('must_pass_environment'),
                   model_uri=TTM.must_pass_environment, domain=None, range=Optional[Union[str, "TestEnvEnum"]])

slots.scientific_question = Slot(uri=TTM.scientific_question, name="scientific_question", curie=TTM.curie('scientific_question'),
                   model_uri=TTM.scientific_question, domain=None, range=Optional[str])

slots.string_entry = Slot(uri=TTM.string_entry, name="string_entry", curie=TTM.curie('string_entry'),
                   model_uri=TTM.string_entry, domain=None, range=Optional[str])

slots.direction = Slot(uri=TTM.direction, name="direction", curie=TTM.curie('direction'),
                   model_uri=TTM.direction, domain=None, range=Optional[Union[str, "DirectionEnum"]])

slots.answer_informal_concept = Slot(uri=TTM.answer_informal_concept, name="answer_informal_concept", curie=TTM.curie('answer_informal_concept'),
                   model_uri=TTM.answer_informal_concept, domain=None, range=Optional[str])

slots.expected_result = Slot(uri=TTM.expected_result, name="expected_result", curie=TTM.curie('expected_result'),
                   model_uri=TTM.expected_result, domain=None, range=Optional[Union[str, "ExpectedResultsEnum"]])

slots.top_level = Slot(uri=TTM.top_level, name="top_level", curie=TTM.curie('top_level'),
                   model_uri=TTM.top_level, domain=None, range=Optional[int])

slots.query_node = Slot(uri=TTM.query_node, name="query_node", curie=TTM.curie('query_node'),
                   model_uri=TTM.query_node, domain=None, range=Optional[Union[str, "NodeEnum"]])

slots.notes = Slot(uri=TTM.notes, name="notes", curie=TTM.curie('notes'),
                   model_uri=TTM.notes, domain=None, range=Optional[str])

slots.test_env = Slot(uri=TTM.test_env, name="test_env", curie=TTM.curie('test_env'),
                   model_uri=TTM.test_env, domain=None, range=Optional[Union[str, "TestEnvEnum"]])

slots.query_type = Slot(uri=TTM.query_type, name="query_type", curie=TTM.curie('query_type'),
                   model_uri=TTM.query_type, domain=None, range=Optional[Union[str, "QueryTypeEnum"]])

slots.test_assets = Slot(uri=TTM.test_assets, name="test_assets", curie=TTM.curie('test_assets'),
                   model_uri=TTM.test_assets, domain=None, range=Union[Dict[Union[str, TestAssetId], Union[dict, TestAsset]], List[Union[dict, TestAsset]]])

slots.preconditions = Slot(uri=TTM.preconditions, name="preconditions", curie=TTM.curie('preconditions'),
                   model_uri=TTM.preconditions, domain=None, range=Optional[Union[Union[str, PreconditionId], List[Union[str, PreconditionId]]]])

slots.trapi_template = Slot(uri=TTM.trapi_template, name="trapi_template", curie=TTM.curie('trapi_template'),
                   model_uri=TTM.trapi_template, domain=None, range=Optional[Union[str, "TrapiTemplateEnum"]])

slots.components = Slot(uri=TTM.components, name="components", curie=TTM.curie('components'),
                   model_uri=TTM.components, domain=None, range=Optional[Union[Union[str, "ComponentEnum"], List[Union[str, "ComponentEnum"]]]])

slots.trapi_version = Slot(uri=TTM.trapi_version, name="trapi_version", curie=TTM.curie('trapi_version'),
                   model_uri=TTM.trapi_version, domain=None, range=Optional[str])

slots.biolink_version = Slot(uri=TTM.biolink_version, name="biolink_version", curie=TTM.curie('biolink_version'),
                   model_uri=TTM.biolink_version, domain=None, range=Optional[str])

slots.test_data_file_locator = Slot(uri=TTM.test_data_file_locator, name="test_data_file_locator", curie=TTM.curie('test_data_file_locator'),
                   model_uri=TTM.test_data_file_locator, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.test_data_file_format = Slot(uri=TTM.test_data_file_format, name="test_data_file_format", curie=TTM.curie('test_data_file_format'),
                   model_uri=TTM.test_data_file_format, domain=None, range=Optional[Union[str, "FileFormatEnum"]])

slots.test_metadata = Slot(uri=TTM.test_metadata, name="test_metadata", curie=TTM.curie('test_metadata'),
                   model_uri=TTM.test_metadata, domain=None, range=Union[dict, TestMetadata])

slots.test_persona = Slot(uri=TTM.test_persona, name="test_persona", curie=TTM.curie('test_persona'),
                   model_uri=TTM.test_persona, domain=None, range=Optional[Union[str, "TestPersonaEnum"]])

slots.test_cases = Slot(uri=TTM.test_cases, name="test_cases", curie=TTM.curie('test_cases'),
                   model_uri=TTM.test_cases, domain=None, range=Optional[Union[Dict[Union[str, TestCaseId], Union[dict, TestCase]], List[Union[dict, TestCase]]]])

slots.test_suite_specification = Slot(uri=TTM.test_suite_specification, name="test_suite_specification", curie=TTM.curie('test_suite_specification'),
                   model_uri=TTM.test_suite_specification, domain=None, range=Optional[Union[dict, TestSuiteSpecification]])

slots.test_run_parameters = Slot(uri=TTM.test_run_parameters, name="test_run_parameters", curie=TTM.curie('test_run_parameters'),
                   model_uri=TTM.test_run_parameters, domain=None, range=Optional[Union[Union[dict, TestEntityParameter], List[Union[dict, TestEntityParameter]]]])

slots.test_suite_id = Slot(uri=TTM.test_suite_id, name="test_suite_id", curie=TTM.curie('test_suite_id'),
                   model_uri=TTM.test_suite_id, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.test_case = Slot(uri=TTM.test_case, name="test_case", curie=TTM.curie('test_case'),
                   model_uri=TTM.test_case, domain=None, range=Optional[Union[dict, TestCase]])

slots.test_case_result = Slot(uri=TTM.test_case_result, name="test_case_result", curie=TTM.curie('test_case_result'),
                   model_uri=TTM.test_case_result, domain=None, range=Optional[Union[str, "TestCaseResultEnum"]])

slots.test_runner_name = Slot(uri=TTM.test_runner_name, name="test_runner_name", curie=TTM.curie('test_runner_name'),
                   model_uri=TTM.test_runner_name, domain=None, range=Optional[str])

slots.test_entities = Slot(uri=TTM.test_entities, name="test_entities", curie=TTM.curie('test_entities'),
                   model_uri=TTM.test_entities, domain=None, range=Optional[Union[Dict[Union[str, TestEntityId], Union[dict, TestEntity]], List[Union[dict, TestEntity]]]])

slots.test_case_results = Slot(uri=TTM.test_case_results, name="test_case_results", curie=TTM.curie('test_case_results'),
                   model_uri=TTM.test_case_results, domain=None, range=Optional[Union[Dict[Union[str, TestCaseResultId], Union[dict, TestCaseResult]], List[Union[dict, TestCaseResult]]]])

slots.Qualifier_parameter = Slot(uri=TTM.parameter, name="Qualifier_parameter", curie=TTM.curie('parameter'),
                   model_uri=TTM.Qualifier_parameter, domain=Qualifier, range=Optional[str])

slots.Qualifier_value = Slot(uri=TTM.value, name="Qualifier_value", curie=TTM.curie('value'),
                   model_uri=TTM.Qualifier_value, domain=Qualifier, range=Optional[str])

slots.TestAsset_id = Slot(uri=SCHEMA.identifier, name="TestAsset_id", curie=SCHEMA.curie('identifier'),
                   model_uri=TTM.TestAsset_id, domain=TestAsset, range=Union[str, TestAssetId])

slots.TestAsset_tags = Slot(uri=SCHEMA.additionalType, name="TestAsset_tags", curie=SCHEMA.curie('additionalType'),
                   model_uri=TTM.TestAsset_tags, domain=TestAsset, range=Optional[Union[str, List[str]]])

slots.TestAsset_test_runner_settings = Slot(uri=TTM.test_runner_settings, name="TestAsset_test_runner_settings", curie=TTM.curie('test_runner_settings'),
                   model_uri=TTM.TestAsset_test_runner_settings, domain=TestAsset, range=Optional[Union[str, List[str]]])

slots.TestCase_test_assets = Slot(uri=TTM.test_assets, name="TestCase_test_assets", curie=TTM.curie('test_assets'),
                   model_uri=TTM.TestCase_test_assets, domain=TestCase, range=Union[Dict[Union[str, TestAssetId], Union[dict, TestAsset]], List[Union[dict, TestAsset]]])

slots.TestCase_tags = Slot(uri=SCHEMA.additionalType, name="TestCase_tags", curie=SCHEMA.curie('additionalType'),
                   model_uri=TTM.TestCase_tags, domain=TestCase, range=Optional[Union[str, List[str]]])

slots.AcceptanceTestCase_test_assets = Slot(uri=TTM.test_assets, name="AcceptanceTestCase_test_assets", curie=TTM.curie('test_assets'),
                   model_uri=TTM.AcceptanceTestCase_test_assets, domain=AcceptanceTestCase, range=Union[Dict[Union[str, AcceptanceTestAssetId], Union[dict, AcceptanceTestAsset]], List[Union[dict, AcceptanceTestAsset]]])

slots.TestRunSession_test_run_parameters = Slot(uri=TTM.test_run_parameters, name="TestRunSession_test_run_parameters", curie=TTM.curie('test_run_parameters'),
                   model_uri=TTM.TestRunSession_test_run_parameters, domain=TestRunSession, range=Optional[Union[Union[dict, TestEntityParameter], List[Union[dict, TestEntityParameter]]]])

slots.TestRunSession_test_entities = Slot(uri=TTM.test_entities, name="TestRunSession_test_entities", curie=TTM.curie('test_entities'),
                   model_uri=TTM.TestRunSession_test_entities, domain=TestRunSession, range=Optional[Union[Dict[Union[str, TestEntityId], Union[dict, TestEntity]], List[Union[dict, TestEntity]]]])