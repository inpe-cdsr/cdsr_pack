"""Test cases related to CBERS2B satellite."""


from util import TestCDSRPack


class TestCDSRPackCBERS2B(TestCDSRPack):
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

        self.assert_valid_assets(test_cases)

    def test__cbers2b__valid_paths(self):
        """Tests valid CBERS2B paths."""

        # `radio_processing` and `date` keys are get from asset, not path
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

        self.assert_valid_paths(test_cases)

    def test__cbers2b__invalid_assets(self):
        """Tests invalid CBERS2B assets."""

        test_cases = [
            {
                'path': ('/TIFF/CBERS2B/2010_03/CBERS2B_CCD_20100301.130915/151_098_0/'
                         '2_BC_UTM_WGS84/CBERS_2B_CCD1XS_20100301_151_098png'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'path': ('/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_B_141_5_0/'
                         '2_BC_UTM_WGS84/CBERS_2B_HRC_20100301_151_B_5_L2_png'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'path': ('/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_A_142_1_0/'
                         '2_BC_UTM_WGS84/CBERS_2B_HRC_20100301_151_A_1_L2,png'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'path': ('/TIFF/CBERS2B/2010_03/CBERS2B_WFI_20100301.144734/177_092_0/'
                         '2_BC_LCC_WGS84/CBERS_2B_WFI_20100301_177_092'),
                'expected_error_message': 'An asset must have an extension.'
            }
        ]

        self.assert_invalid_resources(test_cases)
