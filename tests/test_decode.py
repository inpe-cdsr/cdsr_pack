"""test_decode.py test module."""

from unittest import TestCase

from cdsr_pack.decode import CDSRDecodeException, decode_asset_path


class TestCDSRPackDecodeAMAZONIA1(TestCase):
    """TestCDSRPackDecodeAMAZONIA1"""

    def test__decode_asset_path__amazonia1__valid_assets(self):
        """Tests valid AMAZONIA1 assets."""

        test_cases = [
            '/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.12_57_40_CB11/'
                '217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015_L2_BAND4.tif',
            '/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.12_57_40_CB11/'
                '217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015_L2_BAND3.xml'
        ]

        expected = {
            'satellite': 'AMAZONIA1', 'sensor': 'WFI',
            'path': '217', 'row': '015',
            'geo_processing': '2', 'radio_processing': 'DN'
        }

        for test_case in test_cases:
            self.assertEqual(expected, decode_asset_path(test_case))

    def test__decode_asset_path__amazonia1__invalid_assets(self):
        """Tests invalid AMAZONIA1 assets."""

        asset_path = ('/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.12_57_40_CB11/'
                      '217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015.png')

        with self.assertRaises(CDSRDecodeException) as error:
            decode_asset_path(asset_path)

        self.assertEqual('Just TIFF and XML files can be decoded.', str(error.exception))


class TestCDSRPackDecodeCBERS2B(TestCase):
    """TestCDSRPackDecodeCBERS2B"""

    def test__decode_asset_path__cbers2b__valid_assets(self):
        """Tests valid CBERS2B assets."""

        test_cases = [
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_CCD_20100301.130915/151_098_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_CCD2XS_20100301_151_098_L2_BAND1.tif',
                'expected': {
                    'satellite': 'CBERS2B', 'sensor': 'CCD',
                    'path': '151', 'row': '098',
                    'geo_processing': '2', 'radio_processing': 'DN'
                }
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_CCD_20100301.130915/151_098_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_CCD2XS_20100301_151_098_L2_BAND1.xml',
                'expected': {
                    'satellite': 'CBERS2B', 'sensor': 'CCD',
                    'path': '151', 'row': '098',
                    'geo_processing': '2', 'radio_processing': 'DN'
                }
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_B_141_5_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_HRC_20100301_151_B_141_5_L2_BAND1.tif',
                'expected': {
                    'satellite': 'CBERS2B', 'sensor': 'HRC',
                    'path': '151', 'row': '141',
                    'geo_processing': '2', 'radio_processing': 'DN'
                }
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_B_141_5_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_HRC_20100301_151_B_141_5_L2_BAND1.xml',
                'expected': {
                    'satellite': 'CBERS2B', 'sensor': 'HRC',
                    'path': '151', 'row': '141',
                    'geo_processing': '2', 'radio_processing': 'DN'
                }
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_A_142_1_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_HRC_20100301_151_A_142_1_L2_BAND1.tif',
                'expected': {
                    'satellite': 'CBERS2B', 'sensor': 'HRC',
                    'path': '151', 'row': '142',
                    'geo_processing': '2', 'radio_processing': 'DN'
                }
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_A_142_1_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_HRC_20100301_151_A_142_1_L2_BAND1.xml',
                'expected': {
                    'satellite': 'CBERS2B', 'sensor': 'HRC',
                    'path': '151', 'row': '142',
                    'geo_processing': '2', 'radio_processing': 'DN'
                }
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_WFI_20100301.144734/177_092_0/'
                                '2_BC_LCC_WGS84/CBERS_2B_WFI_20100301_177_092_L2_BAND1.tif',
                'expected': {
                    'satellite': 'CBERS2B', 'sensor': 'WFI',
                    'path': '177', 'row': '092',
                    'geo_processing': '2', 'radio_processing': 'DN'
                }
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_WFI_20100301.144734/177_092_0/'
                                '2_BC_LCC_WGS84/CBERS_2B_WFI_20100301_177_092_L2_BAND1.xml',
                'expected': {
                    'satellite': 'CBERS2B', 'sensor': 'WFI',
                    'path': '177', 'row': '092',
                    'geo_processing': '2', 'radio_processing': 'DN'
                }
            }
        ]

        for test_case in test_cases:
            self.assertEqual(test_case['expected'], decode_asset_path(test_case['asset_path']))

    def test__decode_asset_path__cbers2b__invalid_assets(self):
        """Tests invalid CBERS2B assets."""

        test_cases = [
            '/TIFF/CBERS2B/2010_03/CBERS2B_CCD_20100301.130915/151_098_0/2_BC_UTM_WGS84/'
                'CBERS_2B_CCD1XS_20100301_151_098.png',
            '/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_B_141_5_0/2_BC_UTM_WGS84/'
                'CBERS_2B_HRC_20100301_151_B_5_L2.png',
            '/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_A_142_1_0/2_BC_UTM_WGS84/'
                'CBERS_2B_HRC_20100301_151_A_1_L2.png',
            '/TIFF/CBERS2B/2010_03/CBERS2B_WFI_20100301.144734/177_092_0/2_BC_LCC_WGS84/'
                'CBERS_2B_WFI_20100301_177_092.png'
        ]

        for test_case in test_cases:
            with self.assertRaises(CDSRDecodeException) as error:
                decode_asset_path(test_case)

            self.assertEqual('Just TIFF and XML files can be decoded.', str(error.exception))
