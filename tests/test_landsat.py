"""Test cases related to LANDSAT satellites."""


from unittest import TestCase

from src.cdsr_pack import CDSRDecoderException, \
                          build_collection, build_item, decode_path



class TestCDSRPackLANDSAT(TestCase):
    """TestCDSRPackDecodeLANDSAT"""

    def test__landsat__valid_assets(self):
        """Tests valid LANDSAT assets."""

        test_cases = [
            {
                'asset_path': '/TIFF/LANDSAT1/1973_05/LANDSAT1_MSS_19730521.120000/237_059_0/'
                                '2_BC_UTM_WGS84/LANDSAT_1_MSS_19730521_237_059_L2_BAND4.tif',
                'expected_metadata': {
                    'satellite': 'LANDSAT1', 'sensor': 'MSS', 'path': '237', 'row': '059',
                    'date': '1973-05-21', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'LANDSAT1_MSS_L2_DN',
                'expected_item': 'LANDSAT1_MSS_237059_19730521_ND'
            },
            {
                'asset_path': '/TIFF/LANDSAT1/1973_05/LANDSAT1_MSS_19730521.120000/237_059_0/'
                                '2_BC_UTM_WGS84/LANDSAT_1_MSS_19730521_237_059_L2_BAND4.xml',
                'expected_metadata': {
                    'satellite': 'LANDSAT1', 'sensor': 'MSS', 'path': '237', 'row': '059',
                    'date': '1973-05-21', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'LANDSAT1_MSS_L2_DN',
                'expected_item': 'LANDSAT1_MSS_237059_19730521_ND'
            },
            {
                'asset_path': '/TIFF/LANDSAT2/1982_02/LANDSAT2_MSS_19820201.120000/005_055_0/'
                                '2_BC_UTM_WGS84/LANDSAT_2_MSS_19820201_005_055_L2_BAND4.tif',
                'expected_metadata': {
                    'satellite': 'LANDSAT2', 'sensor': 'MSS', 'path': '005', 'row': '055',
                    'date': '1982-02-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'LANDSAT2_MSS_L2_DN',
                'expected_item': 'LANDSAT2_MSS_005055_19820201_ND'
            },
            {
                'asset_path': '/TIFF/LANDSAT2/1982_02/LANDSAT2_MSS_19820201.120000/005_055_0/'
                                '2_BC_UTM_WGS84/LANDSAT_2_MSS_19820201_005_055_L2_BAND4.xml',
                'expected_metadata': {
                    'satellite': 'LANDSAT2', 'sensor': 'MSS', 'path': '005', 'row': '055',
                    'date': '1982-02-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'LANDSAT2_MSS_L2_DN',
                'expected_item': 'LANDSAT2_MSS_005055_19820201_ND'
            },
            {
                'asset_path': '/TIFF/LANDSAT3/1978_04/LANDSAT3_MSS_19780405.120000/235_075_0/'
                                '2_BC_UTM_WGS84/LANDSAT_3_MSS_19780405_235_075_L2_BAND4.tif',
                'expected_metadata': {
                    'satellite': 'LANDSAT3', 'sensor': 'MSS', 'path': '235', 'row': '075',
                    'date': '1978-04-05', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'LANDSAT3_MSS_L2_DN',
                'expected_item': 'LANDSAT3_MSS_235075_19780405_ND'
            },
            {
                'asset_path': '/TIFF/LANDSAT3/1978_04/LANDSAT3_MSS_19780405.120000/235_075_0/'
                                '2_BC_UTM_WGS84/LANDSAT_3_MSS_19780405_235_075_L2_BAND4.xml',
                'expected_metadata': {
                    'satellite': 'LANDSAT3', 'sensor': 'MSS', 'path': '235', 'row': '075',
                    'date': '1978-04-05', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'LANDSAT3_MSS_L2_DN',
                'expected_item': 'LANDSAT3_MSS_235075_19780405_ND'
            },
            {
                'asset_path': '/TIFF/LANDSAT5/2011_11/LANDSAT5_TM_20111101.140950/233_054_0/'
                                '2_BC_UTM_WGS84/LANDSAT_5_TM_20111101_233_054_L2_BAND1.tif',
                'expected_metadata': {
                    'satellite': 'LANDSAT5', 'sensor': 'TM', 'path': '233', 'row': '054',
                    'date': '2011-11-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'LANDSAT5_TM_L2_DN',
                'expected_item': 'LANDSAT5_TM_233054_20111101_ND'
            },
            {
                'asset_path': '/TIFF/LANDSAT5/2011_11/LANDSAT5_TM_20111101.140950/233_054_0/'
                                '2_BC_UTM_WGS84/LANDSAT_5_TM_20111101_233_054_L2_BAND1.xml',
                'expected_metadata': {
                    'satellite': 'LANDSAT5', 'sensor': 'TM', 'path': '233', 'row': '054',
                    'date': '2011-11-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'LANDSAT5_TM_L2_DN',
                'expected_item': 'LANDSAT5_TM_233054_20111101_ND'
            },
            {
                'asset_path': '/TIFF/LANDSAT7/1999_07/LANDSAT7_ETM_19990731.144148/004_072_0/'
                                '2_BC_UTM_WGS84/LANDSAT_7_ETMXS_19990731_004_072_L2_BAND1.tif',
                'expected_metadata': {
                    'satellite': 'LANDSAT7', 'sensor': 'ETM', 'path': '004', 'row': '072',
                    'date': '1999-07-31', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'LANDSAT7_ETM_L2_DN',
                'expected_item': 'LANDSAT7_ETM_004072_19990731_ND'
            },
            {
                'asset_path': '/TIFF/LANDSAT7/1999_07/LANDSAT7_ETM_19990731.144148/004_072_0/'
                                '2_BC_UTM_WGS84/LANDSAT_7_ETMXS_19990731_004_072_L2_BAND1.xml',
                'expected_metadata': {
                    'satellite': 'LANDSAT7', 'sensor': 'ETM', 'path': '004', 'row': '072',
                    'date': '1999-07-31', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'LANDSAT7_ETM_L2_DN',
                'expected_item': 'LANDSAT7_ETM_004072_19990731_ND'
            },
            {
                'asset_path': '/TIFF/LANDSAT2/1982_02/LANDSAT2_MSS_19820201.120000/005_055_0/'
                                '2_BC_UTM_WGS84/LANDSAT_2_MSS_19820201_005_055.png',
                'expected_metadata': {
                    'satellite': 'LANDSAT2', 'sensor': 'MSS', 'path': '005', 'row': '055',
                    'date': '1982-02-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'LANDSAT2_MSS_L2_DN',
                'expected_item': 'LANDSAT2_MSS_005055_19820201_ND'
            },
            {
                'asset_path': '/TIFF/LANDSAT5/2011_11/LANDSAT5_TM_20111101.140950/233_054_0/'
                                '2_BC_UTM_WGS84/LANDSAT_5_TM_20111101_233_054.png',
                'expected_metadata': {
                    'satellite': 'LANDSAT5', 'sensor': 'TM', 'path': '233', 'row': '054',
                    'date': '2011-11-01', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'LANDSAT5_TM_L2_DN',
                'expected_item': 'LANDSAT5_TM_233054_20111101_ND'
            },
            {
                'asset_path': '/TIFF/LANDSAT7/1999_07/LANDSAT7_ETM_19990731.144148/004_072_0/'
                                '2_BC_UTM_WGS84/LANDSAT_7_ETMXS_19990731_004_072.png',
                'expected_metadata': {
                    'satellite': 'LANDSAT7', 'sensor': 'ETM', 'path': '004', 'row': '072',
                    'date': '1999-07-31', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'LANDSAT7_ETM_L2_DN',
                'expected_item': 'LANDSAT7_ETM_004072_19990731_ND'
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

    # def test__landsat__valid_paths(self):
    #     TODO """Tests valid LANDSAT paths."""

    def test__landsat__invalid_assets(self):
        """Tests invalid LANDSAT assets."""

        test_cases = [
            '/TIFF/LANDSAT1/1973_05/LANDSAT1_MSS_19730521.120000/237_059_0/'
                '2_BC_UTM_WGS84/LANDSAT_1_MSS_19730521_237_059png',
            '/TIFF/LANDSAT2/1982_02/LANDSAT2_MSS_19820201.120000/005_055_0/'
                '2_BC_UTM_WGS84/LANDSAT_2_MSS_19820201_005_055_png',
            '/TIFF/LANDSAT3/1978_04/LANDSAT3_MSS_19780405.120000/235_075_0/'
                '2_BC_UTM_WGS84/LANDSAT_3_MSS_19780405_235_075',
            '/TIFF/LANDSAT5/2011_11/LANDSAT5_TM_20111101.140950/233_054_0/'
                '2_BC_UTM_WGS84/LANDSAT_5_TM_20111101_233_054,png',
            '/TIFF/LANDSAT7/1999_07/LANDSAT7_ETM_19990731.144148/004_072_0/'
                '2_BC_UTM_WGS84/LANDSAT_7_ETMXS_19990731_004_072png'
        ]

        for test_case in test_cases:
            with self.assertRaises(CDSRDecoderException) as error:
                decode_path(test_case)

            self.assertEqual('An asset must have an extension.', str(error.exception))
