"""
This module provides a 'facade' layer to access (Pydantic 1) TestSuites
and their corresponding TestCase entries, in a source-agnostic manner.
"""
from typing import Optional, List, Generator
from linkml_runtime.loaders import tsv_loader, json_loader, yaml_loader
from src.translator_testing_model.datamodel.pydanticmodel import (
    TestMetadata,
    TestAsset,
    AcceptanceTestAsset,
    TestCase,
    TestSuite,
    FileFormatEnum,
    AcceptanceTestSuite,
    BenchmarkTestSuite,
    StandardsComplianceTestSuite,
    OneHopTestSuite,
    TestSuiteSpecification
)


class TestSuiteInputException(RuntimeError):
    pass


class TestCaseGenerator:

    def __init__(
            self,
            test_suite: TestSuite,
            test_metadata: Optional[TestMetadata] = None
    ):
        self.test_suite = test_suite
        self.metadata = test_metadata
        # self.bind_test_suite()

    def test_asset_class(self):
        """
        Identify the (TestSuite (sub)class-specific) TestAsset class
        """
        if isinstance(self.test_suite, AcceptanceTestSuite):
            return AcceptanceTestAsset
        # elif isinstance(self.test_suite, TestSuite):
        #     pass
        # elif isinstance(self.test_suite, BenchmarkTestSuite):
        #     pass
        # elif isinstance(self.test_suite, StandardsComplianceTestSuite):
        #     pass
        # elif isinstance(self.test_suite, OneHopTestSuite):
        #     pass
        else:
            return TestAsset

    def test_assets(self) -> Generator:
        """
        Sequentially generate a list of the input TestAssets.

        Warning: this method uses the LinkML 'load_any' method for various input format types
        but assumes that the test assets data input file will most specify a **List** of
        YAMLRoot objects. It may not properly work for an input file loading a single data object.
        """
        if self.test_suite.test_suite_specification.test_data_file_format == FileFormatEnum.TSV:
            loader = tsv_loader
        elif self.test_suite.test_suite_specification.test_data_file_format == FileFormatEnum.JSON:
            loader = json_loader
        elif self.test_suite.test_suite_specification.test_data_file_format == FileFormatEnum.YAML:
            loader = yaml_loader
        else:
            raise RuntimeError(
                f"Unknown TestAsset file format: {self.test_suite.test_suite_specification.test_data_file_format}"
            )

        if loader:

            for asset in loader.load_any(
                                         source=self.test_suite.test_suite_specification.test_data_file_locator,
                                         # the target class here is for the TestAssets you are loading,
                                         # not the TestSuite!
                                         target_class=self.test_asset_class()
                                         ):
                yield asset

    def load(self) -> Generator:
        # Generate the list of TestCases from the specified input test assets.
        n = 0
        for asset in self.test_assets():
            print(asset)
            n += 1
            tc_id = f"TestCase:{n}"
            test_case = TestCase(id=tc_id, test_assets=[asset])
            yield test_case
