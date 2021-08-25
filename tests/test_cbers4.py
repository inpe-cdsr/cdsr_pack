"""Test cases related to CBERS4 satellite."""


from unittest import TestCase

from src.cdsr_pack import CDSRDecoderException, \
                          build_collection, build_item, decode_path


class TestCDSRPackCBERS4(TestCase):
    """TestCDSRPackCBERS4"""

    def test__cbers4__valid_assets(self):
        """Tests valid CBERS4 assets."""

        test_cases = [
            {
                'asset_path': '/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_2021_02_01.13_07_00_CB11/'
                            '154_117_0/4_BC_UTM_WGS84/CBERS_4_AWFI_20210201_154_117_L4_BAND13.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'AWFI', 'path': '154', 'row': '117',
                    'date': '2021-02-01', 'geo_processing': '4', 'radio_processing': 'DN',
                    'antenna': 'CB11'
                },
                'expected_collection': 'CBERS4_AWFI_L4_DN',
                'expected_item': 'CBERS4_AWFI_154117_20210201_CB11'
            },
            {
                'asset_path': '/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_2021_02_01.13_07_00_CB11/'
                            '154_117_0/4_BC_UTM_WGS84/CBERS_4_AWFI_20210201_154_117_L4_BAND13.xml',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'AWFI', 'path': '154', 'row': '117',
                    'date': '2021-02-01', 'geo_processing': '4', 'radio_processing': 'DN',
                    'antenna': 'CB11'
                },
                'expected_collection': 'CBERS4_AWFI_L4_DN',
                'expected_item': 'CBERS4_AWFI_154117_20210201_CB11'
            },
            {
                'asset_path': '/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_2021_02_01.13_07_00_CB11/154_'
                    '117_0/4_BC_UTM_WGS84/CBERS_4_AWFI_20210201_154_117_L4_CMASK_GRID_SURFACE.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'AWFI', 'path': '154', 'row': '117',
                    'date': '2021-02-01', 'geo_processing': '4', 'radio_processing': 'SR',
                    'antenna': 'CB11'
                },
                'expected_collection': 'CBERS4_AWFI_L4_SR',
                'expected_item': 'CBERS4_AWFI_154117_20210201_CB11'
            },
            {
                'asset_path': '/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_2021_02_01.13_07_00_CB11/154_'
                    '117_0/4_BC_UTM_WGS84/CBERS_4_AWFI_20210201_154_117_L4_BAND13_GRID_SURFACE.xml',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'AWFI', 'path': '154', 'row': '117',
                    'date': '2021-02-01', 'geo_processing': '4', 'radio_processing': 'SR',
                    'antenna': 'CB11'
                },
                'expected_collection': 'CBERS4_AWFI_L4_SR',
                'expected_item': 'CBERS4_AWFI_154117_20210201_CB11'
            },
            {
                'asset_path': '/TIFF/CBERS4/2020_07/CBERS_4_MUX_DRD_2020_07_31.13_07_00_CB11/'
                            '155_103_0/4_BC_UTM_WGS84/CBERS_4_MUX_20200731_155_103_L4_EVI.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'MUX', 'path': '155', 'row': '103',
                    'date': '2020-07-31', 'geo_processing': '4', 'radio_processing': 'SR',
                    'antenna': 'CB11'
                },
                'expected_collection': 'CBERS4_MUX_L4_SR',
                'expected_item': 'CBERS4_MUX_155103_20200731_CB11'
            },
            {
                'asset_path': '/TIFF/CBERS4/2020_07/CBERS_4_MUX_DRD_2020_07_31.13_07_00_CB11/'
                            '155_103_0/4_BC_UTM_WGS84/CBERS_4_MUX_20200731_155_103_L4_NDVI.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'MUX', 'path': '155', 'row': '103',
                    'date': '2020-07-31', 'geo_processing': '4', 'radio_processing': 'SR',
                    'antenna': 'CB11'
                },
                'expected_collection': 'CBERS4_MUX_L4_SR',
                'expected_item': 'CBERS4_MUX_155103_20200731_CB11'
            },
            {
                'asset_path': '/TIFF/CBERS4/2020_07/CBERS_4_MUX_DRD_2020_07_31.13_07_00_CB11/155_'
                    '103_0/4_BC_UTM_WGS84/CBERS_4_MUX_20200731_155_103_L4_BAND5_GRID_SURFACE.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'MUX', 'path': '155', 'row': '103',
                    'date': '2020-07-31', 'geo_processing': '4', 'radio_processing': 'SR',
                    'antenna': 'CB11'
                },
                'expected_collection': 'CBERS4_MUX_L4_SR',
                'expected_item': 'CBERS4_MUX_155103_20200731_CB11'
            },
            {
                'asset_path': '/TIFF/CBERS4/2020_07/CBERS_4_MUX_DRD_2020_07_31.13_07_00_CB11/155_'
                    '103_0/4_BC_UTM_WGS84/CBERS_4_MUX_20200731_155_103_L4_BAND5_GRID_SURFACE.xml',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'MUX', 'path': '155', 'row': '103',
                    'date': '2020-07-31', 'geo_processing': '4', 'radio_processing': 'SR',
                    'antenna': 'CB11'
                },
                'expected_collection': 'CBERS4_MUX_L4_SR',
                'expected_item': 'CBERS4_MUX_155103_20200731_CB11'
            },
            {
                'asset_path': '/TIFF/CBERS4/2018_01/CBERS_4_MUX_DRD_2018_01_01.13_14_00_CB11/'
                        '156_103_0/4_BC_UTM_WGS84/CBERS_4_MUX_20180101_156_103_L4_BAND5.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'MUX', 'path': '156', 'row': '103',
                    'date': '2018-01-01', 'geo_processing': '4', 'radio_processing': 'DN',
                    'antenna': 'CB11'
                },
                'expected_collection': 'CBERS4_MUX_L4_DN',
                'expected_item': 'CBERS4_MUX_156103_20180101_CB11'
            },
            {
                'asset_path': '/TIFF/CBERS4/2018_01/CBERS_4_MUX_DRD_2018_01_01.13_14_00_CB11/'
                        '156_103_0/4_BC_UTM_WGS84/CBERS_4_MUX_20180101_156_103_L4_BAND6.xml',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'MUX', 'path': '156', 'row': '103',
                    'date': '2018-01-01', 'geo_processing': '4', 'radio_processing': 'DN',
                    'antenna': 'CB11'
                },
                'expected_collection': 'CBERS4_MUX_L4_DN',
                'expected_item': 'CBERS4_MUX_156103_20180101_CB11'
            },
            {
                'asset_path': '/TIFF/CBERS4/2021_02/CBERS_4_PAN10M_DRD_2021_02_02.01_32_45_CB11/'
                        '073_113_0/2_BC_UTM_WGS84/CBERS_4_PAN10M_20210201_073_113_L2_BAND2.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'PAN10M', 'path': '073', 'row': '113',
                    'date': '2021-02-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'CB11'
                },
                'expected_collection': 'CBERS4_PAN10M_L2_DN',
                'expected_item': 'CBERS4_PAN10M_073113_20210201_CB11'
            },
            {
                'asset_path': '/TIFF/CBERS4/2021_02/CBERS_4_PAN10M_DRD_2021_02_02.01_32_45_CB11/'
                        '073_113_0/2_BC_UTM_WGS84/CBERS_4_PAN10M_20210201_073_113_L2_BAND2.xml',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'PAN10M', 'path': '073', 'row': '113',
                    'date': '2021-02-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'CB11'
                },
                'expected_collection': 'CBERS4_PAN10M_L2_DN',
                'expected_item': 'CBERS4_PAN10M_073113_20210201_CB11'
            },
            {
                'asset_path': '/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_2021_02_01.13_07_00_CB11/'
                                '154_117_0/4_BC_UTM_WGS84/CBERS_4_AWFI_20210201_154_117.png',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'AWFI', 'path': '154', 'row': '117',
                    'date': '2021-02-01', 'geo_processing': '4', 'radio_processing': 'DN',
                    'antenna': 'CB11'
                },
                'expected_collection': 'CBERS4_AWFI_L4_DN',
                'expected_item': 'CBERS4_AWFI_154117_20210201_CB11'
            },
            {
                'asset_path': '/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_2021_02_01.13_07_00_CB11/154_'
                    '117_0/4_BC_UTM_WGS84/CBERS_4_AWFI_20210201_154_117_L4_CMASK_GRID_SURFACE.json',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'AWFI', 'path': '154', 'row': '117',
                    'date': '2021-02-01', 'geo_processing': '4', 'radio_processing': 'SR',
                    'antenna': 'CB11'
                },
                'expected_collection': 'CBERS4_AWFI_L4_SR',
                'expected_item': 'CBERS4_AWFI_154117_20210201_CB11'
            },
            {
                'asset_path': '/TIFF/CBERS4/2021_02/CBERS_4_PAN10M_DRD_2021_02_02.01_32_45_CB11/'
                                '073_113_0/2_BC_UTM_WGS84/CBERS_4_PAN10M_20210201_073_113.png',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'PAN10M', 'path': '073', 'row': '113',
                    'date': '2021-02-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'CB11'
                },
                'expected_collection': 'CBERS4_PAN10M_L2_DN',
                'expected_item': 'CBERS4_PAN10M_073113_20210201_CB11'
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

    # def test__cbers4__valid_paths(self):
    #     TODO: """Tests valid CBERS4 paths."""

    def test__cbers4__invalid_assets(self):
        """Tests invalid CBERS4 assets."""

        test_cases = [
            {
                'asset_path': ('/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_2021_02_01.13_07_00_CB11'
                               '/154_117_0/4_BC_UTM_WGS84/CBERS_4_AWFI_20210201_154_117png'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'asset_path': ('/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_2021_02_01.13_07_00_CB11'
                               '/154_117_0/4_BC_UTM_WGS84/'
                               'CBERS_4_AWFI_20210201_154_117_L4_CMASK_GRID_SURFACE'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'asset_path': ('/TIFF/CBERS4/2020_07/CBERS_4_MUX_DRD_2020_07_31.13_07_00_CB11'
                               '/155_103_0/4_BC_UTM_WGS84/CBERS_4_MUX_20200731_155_103'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'asset_path': ('/TIFF/CBERS4/2020_07/CBERS_4_MUX_DRD_2020_07_31.13_07_00_CB11/'
                               '155_103_0/4_BC_UTM_WGS84/'
                               'CBERS_4_MUX_20200731_155_103_L4_CMASK_GRID_SURFACE_json'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'asset_path': ('/TIFF/CBERS4/2018_01/CBERS_4_MUX_DRD_2018_01_01.13_14_00_CB11/'
                               '156_103_0/4_BC_UTM_WGS84/CBERS_4_MUX_20180101_156_103_png'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'asset_path': ('/TIFF/CBERS4/2021_02/CBERS_4_PAN10M_DRD_2021_02_02.01_32_45_CB11/'
                           '073_113_0/2_BC_UTM_WGS84/CBERS_4_PAN10M_20210201_073_113,png'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'asset_path': ('/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_2021_02_01.13_07_00/'
                        '154_117_0/4_BC_UTM_WGS84/CBERS_4_AWFI_20210201_154_117_L4_BAND13.tif'),
                'expected_error_message': ('Invalid antenna in scene_dir: '
                                           '`CBERS_4_AWFI_DRD_2021_02_01.13_07_00`.')
            }
        ]

        for test_case in test_cases:
            with self.assertRaises(CDSRDecoderException) as error:
                decode_path(test_case['asset_path'])

            self.assertEqual(test_case['expected_error_message'], str(error.exception))
