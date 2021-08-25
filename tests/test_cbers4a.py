"""Test cases related to CBERS4A satellite."""


from unittest import TestCase

from src.cdsr_pack import CDSRDecoderException, \
                          build_collection, build_item, decode_path


class TestCDSRPackCBERS4A(TestCase):
    """TestCDSRPackCBERS4A"""

    def test__cbers4a__valid_assets(self):
        """Tests valid CBERS4A assets."""

        test_cases = [
            {
                'asset_path': ('/TIFF/CBERS4A/2021_01/CBERS_4A_MUX_RAW_2021_01_01.13_48_30_ETC2/'
                        '209_110_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20210101_209_110_L2_BAND5.tif'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'MUX', 'path': '209', 'row': '110',
                    'date': '2021-01-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ETC2'
                },
                'expected_collection': 'CBERS4A_MUX_L2_DN',
                'expected_item': 'CBERS4A_MUX_209110_20210101_ETC2'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2021_01/CBERS_4A_MUX_RAW_2021_01_01.13_48_30_ETC2/'
                        '209_110_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20210101_209_110_L2_BAND5.xml'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'MUX', 'path': '209', 'row': '110',
                    'date': '2021-01-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ETC2'
                },
                'expected_collection': 'CBERS4A_MUX_L2_DN',
                'expected_item': 'CBERS4A_MUX_209110_20210101_ETC2'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_12/CBERS_4A_MUX_RAW_2020_12_01.13_47_30_ETC2/'
                        '209_122_0/3_BC_UTM_WGS84/CBERS_4A_MUX_20201201_209_122_L3_BAND5.tif'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'MUX', 'path': '209', 'row': '122',
                    'date': '2020-12-01', 'geo_processing': '3', 'radio_processing': 'DN',
                    'antenna': 'ETC2'
                },
                'expected_collection': 'CBERS4A_MUX_L3_DN',
                'expected_item': 'CBERS4A_MUX_209122_20201201_ETC2'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_12/CBERS_4A_MUX_RAW_2020_12_01.13_47_30_ETC2/'
                        '209_122_0/3_BC_UTM_WGS84/CBERS_4A_MUX_20201201_209_122_L3_BAND5.xml'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'MUX', 'path': '209', 'row': '122',
                    'date': '2020-12-01', 'geo_processing': '3', 'radio_processing': 'DN',
                    'antenna': 'ETC2'
                },
                'expected_collection': 'CBERS4A_MUX_L3_DN',
                'expected_item': 'CBERS4A_MUX_209122_20201201_ETC2'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_12/CBERS_4A_MUX_RAW_2020_12_01.13_47_30_ETC2/'
                        '209_122_0/4_BC_UTM_WGS84/CBERS_4A_MUX_20201201_209_122_L4_BAND5.tif'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'MUX', 'path': '209', 'row': '122',
                    'date': '2020-12-01', 'geo_processing': '4', 'radio_processing': 'DN',
                    'antenna': 'ETC2'
                },
                'expected_collection': 'CBERS4A_MUX_L4_DN',
                'expected_item': 'CBERS4A_MUX_209122_20201201_ETC2'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_12/CBERS_4A_MUX_RAW_2020_12_01.13_47_30_ETC2/'
                        '209_122_0/4_BC_UTM_WGS84/CBERS_4A_MUX_20201201_209_122_L4_BAND5.xml'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'MUX', 'path': '209', 'row': '122',
                    'date': '2020-12-01', 'geo_processing': '4', 'radio_processing': 'DN',
                    'antenna': 'ETC2'
                },
                'expected_collection': 'CBERS4A_MUX_L4_DN',
                'expected_item': 'CBERS4A_MUX_209122_20201201_ETC2'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_12/CBERS_4A_WFI_RAW_2020_12_22.13_53_30_ETC2_'
                    'CHUNK/211_108_0/2B_BC_UTM_WGS84/CBERS_4A_WFI_20201222_211_108_L2B_BAND13.tif'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '211', 'row': '108',
                    'date': '2020-12-22', 'geo_processing': '2B', 'radio_processing': 'DN',
                    'antenna': 'ETC2'
                },
                'expected_collection': 'CBERS4A_WFI_L2B_DN',
                'expected_item': 'CBERS4A_WFI_211108_20201222_ETC2'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_12/CBERS_4A_WFI_RAW_2020_12_22.13_53_30_ETC2_'
                    'CHUNK/211_108_0/2B_BC_UTM_WGS84/CBERS_4A_WFI_20201222_211_108_L2B_BAND14.xml'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '211', 'row': '108',
                    'date': '2020-12-22', 'geo_processing': '2B', 'radio_processing': 'DN',
                    'antenna': 'ETC2'
                },
                'expected_collection': 'CBERS4A_WFI_L2B_DN',
                'expected_item': 'CBERS4A_WFI_211108_20201222_ETC2'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_12/CBERS_4A_WFI_RAW_2020_12_07.14_03_00_ETC2/'
                    '214_108_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20201207_214_108_L4_LEFT_EVI.tif'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '214', 'row': '108',
                    'date': '2020-12-07', 'geo_processing': '4', 'radio_processing': 'SR',
                    'antenna': 'ETC2'
                },
                'expected_collection': 'CBERS4A_WFI_L4_SR',
                'expected_item': 'CBERS4A_WFI_214108_20201207_ETC2'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_12/CBERS_4A_WFI_RAW_2020_12_07.14_03_00_ETC2/'
                        '214_108_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20201207_214_108_L4_LEFT_NDVI.tif'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '214', 'row': '108',
                    'date': '2020-12-07', 'geo_processing': '4', 'radio_processing': 'SR',
                    'antenna': 'ETC2'
                },
                'expected_collection': 'CBERS4A_WFI_L4_SR',
                'expected_item': 'CBERS4A_WFI_214108_20201207_ETC2'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_12/CBERS_4A_WFI_RAW_2020_12_07.14_03_00_ETC2/'
                                '214_108_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20201207_214_108_L4_LEFT_'
                                'CMASK_GRID_SURFACE.tif'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '214', 'row': '108',
                    'date': '2020-12-07', 'geo_processing': '4', 'radio_processing': 'SR',
                    'antenna': 'ETC2'
                },
                'expected_collection': 'CBERS4A_WFI_L4_SR',
                'expected_item': 'CBERS4A_WFI_214108_20201207_ETC2'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_12/CBERS_4A_WFI_RAW_2020_12_07.14_03_00_ETC2/'
                                '214_108_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20201207_214_108_L4_LEFT_'
                                'BAND13_GRID_SURFACE.tif'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '214', 'row': '108',
                    'date': '2020-12-07', 'geo_processing': '4', 'radio_processing': 'SR',
                    'antenna': 'ETC2'
                },
                'expected_collection': 'CBERS4A_WFI_L4_SR',
                'expected_item': 'CBERS4A_WFI_214108_20201207_ETC2'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_12/CBERS_4A_WFI_RAW_2020_12_07.14_03_00_ETC2/'
                                '214_108_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20201207_214_108_L4_LEFT_'
                                'BAND13_GRID_SURFACE.xml'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '214', 'row': '108',
                    'date': '2020-12-07', 'geo_processing': '4', 'radio_processing': 'SR',
                    'antenna': 'ETC2'
                },
                'expected_collection': 'CBERS4A_WFI_L4_SR',
                'expected_item': 'CBERS4A_WFI_214108_20201207_ETC2'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2019_12/CBERS_4A_WFI_RAW_2019_12_27.13_53_00_ETC2/'
                            '215_132_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20191227_215_132_L4_BAND13.tif'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '215', 'row': '132',
                    'date': '2019-12-27', 'geo_processing': '4', 'radio_processing': 'DN',
                    'antenna': 'ETC2'
                },
                'expected_collection': 'CBERS4A_WFI_L4_DN',
                'expected_item': 'CBERS4A_WFI_215132_20191227_ETC2'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2019_12/CBERS_4A_WFI_RAW_2019_12_27.13_53_00_ETC2/'
                    '215_132_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20191227_215_132_L4_LEFT_BAND15.xml'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '215', 'row': '132',
                    'date': '2019-12-27', 'geo_processing': '4', 'radio_processing': 'DN',
                    'antenna': 'ETC2'
                },
                'expected_collection': 'CBERS4A_WFI_L4_DN',
                'expected_item': 'CBERS4A_WFI_215132_20191227_ETC2'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_11/CBERS_4A_WFI_RAW_2020_11_22.14_11_30_ETC2/'
                    '217_156_0/3_BC_UTM_WGS84/CBERS_4A_WFI_20201122_217_156_L3_BAND13.tif'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '217', 'row': '156',
                    'date': '2020-11-22', 'geo_processing': '3', 'radio_processing': 'DN',
                    'antenna': 'ETC2'
                },
                'expected_collection': 'CBERS4A_WFI_L3_DN',
                'expected_item': 'CBERS4A_WFI_217156_20201122_ETC2'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_11/CBERS_4A_WFI_RAW_2020_11_22.14_11_30_ETC2/'
                        '217_156_0/3_BC_UTM_WGS84/CBERS_4A_WFI_20201122_217_156_L3_BAND14.xml'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '217', 'row': '156',
                    'date': '2020-11-22', 'geo_processing': '3', 'radio_processing': 'DN',
                    'antenna': 'ETC2'
                },
                'expected_collection': 'CBERS4A_WFI_L3_DN',
                'expected_item': 'CBERS4A_WFI_217156_20201122_ETC2'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2021_01/CBERS_4A_MUX_RAW_2021_01_01.13_48_30_ETC2/'
                                '209_110_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20210101_209_110.png'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'MUX', 'path': '209', 'row': '110',
                    'date': '2021-01-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ETC2'
                },
                'expected_collection': 'CBERS4A_MUX_L2_DN',
                'expected_item': 'CBERS4A_MUX_209110_20210101_ETC2'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_12/CBERS_4A_MUX_RAW_2020_12_01.13_47_30_ETC2/'
                                '209_122_0/3_BC_UTM_WGS84/CBERS_4A_MUX_20201201_209_122.png'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'MUX', 'path': '209', 'row': '122',
                    'date': '2020-12-01', 'geo_processing': '3', 'radio_processing': 'DN',
                    'antenna': 'ETC2'
                },
                'expected_collection': 'CBERS4A_MUX_L3_DN',
                'expected_item': 'CBERS4A_MUX_209122_20201201_ETC2'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2019_12/CBERS_4A_WFI_RAW_2019_12_27.13_53_00_ETC2/'
                                '215_132_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20191227_215_132.png'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '215', 'row': '132',
                    'date': '2019-12-27', 'geo_processing': '4', 'radio_processing': 'DN',
                    'antenna': 'ETC2'
                },
                'expected_collection': 'CBERS4A_WFI_L4_DN',
                'expected_item': 'CBERS4A_WFI_215132_20191227_ETC2'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_12/CBERS_4A_WFI_RAW_2020_12_22.13_53_30_ETC2_'
                               'CHUNK/211_108_0/2B_BC_UTM_WGS84/CBERS_4A_WFI_20201222_211_108.png'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '211', 'row': '108',
                    'date': '2020-12-22', 'geo_processing': '2B', 'radio_processing': 'DN',
                    'antenna': 'ETC2'
                },
                'expected_collection': 'CBERS4A_WFI_L2B_DN',
                'expected_item': 'CBERS4A_WFI_211108_20201222_ETC2'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_04/CBERS_4A_MUX_RAW_2020_04_23.01_24_22_CP5'
                        '/266_023_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200422_266_023_L2_BAND7.tif'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'MUX', 'path': '266', 'row': '023',
                    'date': '2020-04-22', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'CP5'
                },
                'expected_collection': 'CBERS4A_MUX_L2_DN',
                'expected_item': 'CBERS4A_MUX_266023_20200422_CP5'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_04/CBERS_4A_MUX_RAW_2020_04_06.00_56_20_CP5'
                        '/164_025_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200405_164_025_L2_BAND6.xml'),
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'MUX', 'path': '164', 'row': '025',
                    'date': '2020-04-05', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'CP5'
                },
                'expected_collection': 'CBERS4A_MUX_L2_DN',
                'expected_item': 'CBERS4A_MUX_164025_20200405_CP5'
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

    # def test__cbers4a__valid_paths(self):
    #     TODO """Tests valid CBERS4A paths."""

    def test__cbers4a__invalid_assets(self):
        """Tests invalid CBERS4A assets."""

        test_cases = [
            {
                'asset_path': ('/TIFF/CBERS4A/2021_01/CBERS_4A_MUX_RAW_2021_01_01.13_48_30_ETC2/'
                               '209_110_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20210101_209_110png'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_12/CBERS_4A_MUX_RAW_2020_12_01.13_47_30_ETC2/'
                               '209_122_0/3_BC_UTM_WGS84/CBERS_4A_MUX_20201201_209_122_png'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_12/CBERS_4A_MUX_RAW_2020_12_01.13_47_30_ETC2/'
                               '209_122_0/4_BC_UTM_WGS84/CBERS_4A_MUX_20201201_209_122'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_12/CBERS_4A_WFI_RAW_2020_12_22.13_53_30_ETC2_'
                               'CHUNK/211_108_0/2B_BC_UTM_WGS84/CBERS_4A_WFI_20201222_211_108,png'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_12/CBERS_4A_WFI_RAW_2020_12_07.14_03_00_ETC2/'
                               '214_108_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20201207_214_108png'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_12/CBERS_4A_WFI_RAW_2020_12_07.14_03_00_ETC2/'
                               '214_108_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20201207_214_108_L4_LEFT_'
                               'CMASK_GRID_SURFACE_json'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2019_12/CBERS_4A_WFI_RAW_2019_12_27.13_53_00_ETC2/'
                               '215_132_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20191227_215_132'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2020_11/CBERS_4A_WFI_RAW_2020_11_22.14_11_30_ETC2/'
                               '217_156_0/3_BC_UTM_WGS84/CBERS_4A_WFI_20201122_217_156,png'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'asset_path': ('/TIFF/CBERS4A_01/2019_12/CBERS_4A_MUX_RAW_2019_12_28.14_15_00/'
                               '221_108_0/4_BC_UTM_WGS84/CBERS_4A_MUX_20191228_221_108.h5_0.json'),
                'expected_error_message': ('Invalid antenna in scene_dir: '
                                           '`CBERS_4A_MUX_RAW_2019_12_28.14_15_00`.')
            }
        ]

        for test_case in test_cases:
            with self.assertRaises(CDSRDecoderException) as error:
                decode_path(test_case['asset_path'])

            self.assertEqual(test_case['expected_error_message'], str(error.exception))
