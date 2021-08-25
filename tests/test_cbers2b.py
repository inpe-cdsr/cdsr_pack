"""Test cases related to CBERS2B satellite."""


from unittest import TestCase

from src.cdsr_pack import CDSRBuilderException, CDSRDecoderException, \
                          build_collection, build_item, decode_path


class TestCDSRPackCBERS2B(TestCase):
    """TestCDSRPackCBERS2B"""

    def test__cbers2b__valid_assets(self):
        """Tests valid CBERS2B assets."""

        test_cases = [
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_CCD_20100301.130915/151_098_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_CCD2XS_20100301_151_098_L2_BAND1.tif',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'CCD', 'path': '151', 'row': '098',
                    'date': '2010-03-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'CBERS2B_CCD_L2_DN',
                'expected_item': 'CBERS2B_CCD_151098_20100301_ND'
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_CCD_20100301.130915/151_098_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_CCD2XS_20100301_151_098_L2_BAND1.xml',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'CCD', 'path': '151', 'row': '098',
                    'date': '2010-03-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'CBERS2B_CCD_L2_DN',
                'expected_item': 'CBERS2B_CCD_151098_20100301_ND'
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_B_141_5_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_HRC_20100301_151_B_141_5_L2_BAND1.tif',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'HRC', 'path': '151', 'row': '141',
                    'date': '2010-03-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'CBERS2B_HRC_L2_DN',
                'expected_item': 'CBERS2B_HRC_151141_20100301_ND'
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_B_141_5_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_HRC_20100301_151_B_141_5_L2_BAND1.xml',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'HRC', 'path': '151', 'row': '141',
                    'date': '2010-03-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'CBERS2B_HRC_L2_DN',
                'expected_item': 'CBERS2B_HRC_151141_20100301_ND'
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_A_142_1_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_HRC_20100301_151_A_142_1_L2_BAND1.tif',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'HRC', 'path': '151', 'row': '142',
                    'date': '2010-03-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'CBERS2B_HRC_L2_DN',
                'expected_item': 'CBERS2B_HRC_151142_20100301_ND'
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_A_142_1_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_HRC_20100301_151_A_142_1_L2_BAND1.xml',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'HRC', 'path': '151', 'row': '142',
                    'date': '2010-03-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'CBERS2B_HRC_L2_DN',
                'expected_item': 'CBERS2B_HRC_151142_20100301_ND'
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_WFI_20100301.144734/177_092_0/'
                                '2_BC_LCC_WGS84/CBERS_2B_WFI_20100301_177_092_L2_BAND1.tif',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'WFI', 'path': '177', 'row': '092',
                    'date': '2010-03-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'CBERS2B_WFI_L2_DN',
                'expected_item': 'CBERS2B_WFI_177092_20100301_ND'
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_WFI_20100301.144734/177_092_0/'
                                '2_BC_LCC_WGS84/CBERS_2B_WFI_20100301_177_092_L2_BAND1.xml',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'WFI', 'path': '177', 'row': '092',
                    'date': '2010-03-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'CBERS2B_WFI_L2_DN',
                'expected_item': 'CBERS2B_WFI_177092_20100301_ND'
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_CCD_20100301.130915/151_098_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_CCD1XS_20100301_151_098.png',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'CCD', 'path': '151', 'row': '098',
                    'date': '2010-03-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'CBERS2B_CCD_L2_DN',
                'expected_item': 'CBERS2B_CCD_151098_20100301_ND'
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_B_141_5_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_HRC_20100301_151_B_5_L2.png',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'HRC', 'path': '151', 'row': '141',
                    'date': '2010-03-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'CBERS2B_HRC_L2_DN',
                'expected_item': 'CBERS2B_HRC_151141_20100301_ND'
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_A_142_1_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_HRC_20100301_151_A_1_L2.png',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'HRC', 'path': '151', 'row': '142',
                    'date': '2010-03-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'CBERS2B_HRC_L2_DN',
                'expected_item': 'CBERS2B_HRC_151142_20100301_ND'
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_WFI_20100301.144734/177_092_0/'
                                '2_BC_LCC_WGS84/CBERS_2B_WFI_20100301_177_092.png',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'WFI', 'path': '177', 'row': '092',
                    'date': '2010-03-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'CBERS2B_WFI_L2_DN',
                'expected_item': 'CBERS2B_WFI_177092_20100301_ND'
            }

        ]

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

    def test__cbers2b__valid_paths(self):
        """Tests valid CBERS2B paths."""

        test_cases = [
            {
                'path': '/TIFF/CBERS2B/2010_03/CBERS2B_CCD_20100301.130915/151_098_0/'
                        '2_BC_UTM_WGS84',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'CCD', 'path': '151', 'row': '098',
                    'date': None, 'geo_processing': '2', 'radio_processing': None,
                    'antenna': 'ND'
                }
            },
            {
                'path': '/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_B_141_5_0/'
                        '2_BC_UTM_WGS84/',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'HRC', 'path': '151', 'row': '141',
                    'date': None, 'geo_processing': '2', 'radio_processing': None,
                    'antenna': 'ND'
                }
            },
            {
                'path': '/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_A_142_1_0/'
                        '2_BC_UTM_WGS84',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'HRC', 'path': '151', 'row': '142',
                    'date': None, 'geo_processing': '2', 'radio_processing': None,
                    'antenna': 'ND'
                }
            },
            {
                'path': '/TIFF/CBERS2B/2010_03/CBERS2B_WFI_20100301.144734/177_092_0/'
                        '2_BC_LCC_WGS84/',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'WFI', 'path': '177', 'row': '092',
                    'date': None, 'geo_processing': '2', 'radio_processing': None,
                    'antenna': 'ND'
                }
            }
        ]

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

    def test__cbers2b__invalid_assets(self):
        """Tests invalid CBERS2B assets."""

        test_cases = [
            '/TIFF/CBERS2B/2010_03/CBERS2B_CCD_20100301.130915/151_098_0/2_BC_UTM_WGS84/'
                'CBERS_2B_CCD1XS_20100301_151_098png',
            '/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_B_141_5_0/2_BC_UTM_WGS84/'
                'CBERS_2B_HRC_20100301_151_B_5_L2_png',
            '/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_A_142_1_0/2_BC_UTM_WGS84/'
                'CBERS_2B_HRC_20100301_151_A_1_L2,png',
            '/TIFF/CBERS2B/2010_03/CBERS2B_WFI_20100301.144734/177_092_0/2_BC_LCC_WGS84/'
                'CBERS_2B_WFI_20100301_177_092'
        ]

        for test_case in test_cases:
            with self.assertRaises(CDSRDecoderException) as error:
                decode_path(test_case)

            self.assertEqual('An asset must have an extension.', str(error.exception))
