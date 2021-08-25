"""Module with utility functions related to test cases."""


from unittest import TestCase

from src.cdsr_pack import CDSRBuilderException, CDSRDecoderException, \
                          build_collection, build_item, decode_path


class TestCDSRPack(TestCase):
    """Base class for creating test cases related to CDSR pack."""

    def assert_valid_assets(self, test_cases):
        """Checks if assets are valid."""

        for test_case in test_cases:
            # check if decode_path function works
            self.assertEqual(test_case['expected_metadata'],
                             decode_path(test_case['asset_path']))
            # check if build_collection function works
            self.assertEqual(test_case['expected_collection'],
                             build_collection(test_case['expected_metadata']))
            # check if build_item function works
            self.assertEqual(test_case['expected_item'],
                             build_item(test_case['expected_metadata']))

    def assert_valid_paths(self, test_cases):
        """Checks if paths are valid."""

        # `radio_processing` and `date` keys are get from asset, not path

        # check decode_path function
        for test_case in test_cases:
            self.assertEqual(test_case['expected_metadata'], decode_path(test_case['path']))

            # check build_collection function
            with self.assertRaises(CDSRBuilderException) as error:
                build_collection(test_case['expected_metadata'])

            self.assertEqual('All mandatory values inside metadata dict must be strings, '
                             'but the following keys are not: `radio_processing`.',
                             str(error.exception))

            # check build_item function
            with self.assertRaises(CDSRBuilderException) as error:
                build_item(test_case['expected_metadata'])

            self.assertEqual('All mandatory values inside metadata dict must be strings, '
                             'but the following keys are not: `date`.',
                             str(error.exception))

    def assert_invalid_resources(self, test_cases):
        """Checks if resources (i.e. either assets or paths) are invalid."""

        for test_case in test_cases:
            with self.assertRaises(CDSRDecoderException) as error:
                decode_path(test_case['path'])

            self.assertEqual(test_case['expected_error_message'], str(error.exception))
