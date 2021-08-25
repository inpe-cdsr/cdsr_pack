"""Test cases related to CBERS4 satellite."""


from util import TestCDSRPack


class TestCDSRPackCBERS4(TestCDSRPack):
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

        self.assert_valid_assets(test_cases)

    def test__cbers4__valid_paths(self):
        """Tests valid CBERS4 paths."""

        # `radio_processing` and `date` keys are get from asset, not path
        test_cases = [
            {
                'path': '/TIFF/CBERS4/2016_01/CBERS_4_MUX_DRD_2016_01_01.13_28_32_CB11'
                        '/157_101_0/2_BC_UTM_WGS84',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'MUX', 'path': '157', 'row': '101',
                    'date': None, 'geo_processing': '2', 'radio_processing': None,
                    'antenna': 'CB11'
                }
            },
            {
                'path': '/TIFF/CBERS4/2020_12/CBERS_4_AWFI_DRD_2020_12_28.13_17_30_CB11/'
                        '157_135_0/4_BC_UTM_WGS84',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'AWFI', 'path': '157', 'row': '135',
                    'date': None, 'geo_processing': '4', 'radio_processing': None,
                    'antenna': 'CB11'
                }
            },
            {
                'path': '/TIFF/CBERS4/2021_02/CBERS_4_PAN10M_DRD_2021_02_02.01_32_45_CB11/'
                        '073_113_0/2_BC_UTM_WGS84',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'PAN10M', 'path': '073', 'row': '113',
                    'date': None, 'geo_processing': '2', 'radio_processing': None,
                    'antenna': 'CB11'
                }
            }
        ]

        self.assert_valid_paths(test_cases)

    def test__cbers4__invalid_assets(self):
        """Tests invalid CBERS4 assets."""

        test_cases = [
            {
                'path': ('/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_2021_02_01.13_07_00_CB11'
                               '/154_117_0/4_BC_UTM_WGS84/CBERS_4_AWFI_20210201_154_117png'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'path': ('/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_2021_02_01.13_07_00_CB11'
                               '/154_117_0/4_BC_UTM_WGS84/'
                               'CBERS_4_AWFI_20210201_154_117_L4_CMASK_GRID_SURFACE'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'path': ('/TIFF/CBERS4/2020_07/CBERS_4_MUX_DRD_2020_07_31.13_07_00_CB11'
                               '/155_103_0/4_BC_UTM_WGS84/CBERS_4_MUX_20200731_155_103'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'path': ('/TIFF/CBERS4/2020_07/CBERS_4_MUX_DRD_2020_07_31.13_07_00_CB11/'
                               '155_103_0/4_BC_UTM_WGS84/'
                               'CBERS_4_MUX_20200731_155_103_L4_CMASK_GRID_SURFACE_json'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'path': ('/TIFF/CBERS4/2018_01/CBERS_4_MUX_DRD_2018_01_01.13_14_00_CB11/'
                               '156_103_0/4_BC_UTM_WGS84/CBERS_4_MUX_20180101_156_103_png'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'path': ('/TIFF/CBERS4/2021_02/CBERS_4_PAN10M_DRD_2021_02_02.01_32_45_CB11/'
                           '073_113_0/2_BC_UTM_WGS84/CBERS_4_PAN10M_20210201_073_113,png'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'path': ('/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_2021_02_01.13_07_00/'
                        '154_117_0/4_BC_UTM_WGS84/CBERS_4_AWFI_20210201_154_117_L4_BAND13.tif'),
                'expected_error_message': ('Invalid antenna in scene_dir: '
                                           '`CBERS_4_AWFI_DRD_2021_02_01.13_07_00`.')
            }
        ]

        self.assert_invalid_resources(test_cases)
