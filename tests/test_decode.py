"""test_decode.py test module."""

from unittest import TestCase

from cdsr_pack.decode import CDSRDecodeException, decode_asset_path


class TestCDSRPackDecodeAmazonia1(TestCase):
    """TestCDSRPackDecodeAmazonia1"""

    def test__decode_asset_path__amazonia1__valid_assets(self):
        """Tests valid AMAZONIA1 assets."""

        test_cases= [
            {
                'asset_path': '/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.12_57_40_CB11/'
                            '217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015_L2_BAND4.tif',
            },
            {
                'asset_path': '/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.12_57_40_CB11/'
                            '217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015_L2_BAND3.xml'
            }
        ]

        expected = {
            'satellite': 'AMAZONIA1', 'sensor': 'WFI',
            'path': '217', 'row': '015',
            'geo_processing': '2', 'radio_processing': 'DN'
        }

        for test_case in test_cases:
            self.assertEqual(expected, decode_asset_path(test_case['asset_path']))

    def test__decode_asset_path__amazonia1__invalid_assets(self):
        """Tests invalid AMAZONIA1 assets."""

        asset_path = ('/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.12_57_40_CB11/'
                      '217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015.png')

        self.assertRaises(CDSRDecodeException, decode_asset_path, asset_path)
