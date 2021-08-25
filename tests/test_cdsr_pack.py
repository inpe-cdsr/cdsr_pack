"""Test cases related to other behaviors."""


from unittest import TestCase

from src.cdsr_pack import CDSRBuilderException, CDSRDecoderException, \
                          build_collection, build_item, decode_path


class TestCDSRPackOtherBehaviors(TestCase):
    """TestCDSRPackOtherBehaviors"""

    def test__other_behaviors(self):
        """Tests other expected behaviors."""

        test_cases = [
            {
                'metadata': {
                    'satellite': 'AMAZONIA1', 'sensor': 'WFI', 'path': '217', 'row': '015',
                    'date': None, 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'ND'
                },
                'expected_collection': 'AMAZONIA1_WFI_L2_DN',
                'expected_build_item_error': 'All mandatory values inside metadata dict must be '
                                             'strings, but the following keys are not: `date`.'
            },
            {
                'metadata': {
                    'satellite': 'AMAZONIA1', 'sensor': 'WFI', 'path': '217', 'row': None,
                    'date': '2021-03-03', 'geo_processing': '2', 'radio_processing': None,
                    'antenna': 'ND'
                },
                'expected_build_collection_error': 'All mandatory values inside metadata dict must '
                                'be strings, but the following keys are not: `radio_processing`.',
                'expected_build_item_error': 'All mandatory values inside metadata dict must be '
                                'strings, but the following keys are not: `row`.'
            }
        ]

        for test_case in test_cases:
            if 'expected_collection' in test_case:
                self.assertEqual(test_case['expected_collection'],
                                 build_collection(test_case['metadata']))

            if 'expected_build_collection_error' in test_case:
                with self.assertRaises(CDSRBuilderException) as error:
                    build_collection(test_case['metadata'])

                self.assertEqual(test_case['expected_build_collection_error'], str(error.exception))

            with self.assertRaises(CDSRBuilderException) as error:
                build_item(test_case['metadata'])

            self.assertEqual(test_case['expected_build_item_error'], str(error.exception))


class TestCDSRPackErrors(TestCase):
    """TestCDSRPackDecodeErrors"""

    def test__decode_path__errors__invalid_assets(self):
        """Tests invalid assets."""

        test_cases = [
            {
                'asset_path': '',
                'expected': 'Invalid `1` level to path: ``.'
            },
            {
                'asset_path': '/',
                'expected': 'Invalid `1` level to path: ``.'
            },
            {
                'asset_path': None,
                'expected': "Path must be a str, not a `<class 'NoneType'>`."
            },
            {
                'asset_path': 0,
                'expected': "Path must be a str, not a `<class 'int'>`."
            },
            {
                'asset_path': [],
                'expected': "Path must be a str, not a `<class 'list'>`."
            },
            {
                'asset_path': ('/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.12_57/'
                    '217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015_L2_BAND4.tif'),
                'expected': ('Invalid reception time in scene_dir: '
                             '`AMAZONIA_1_WFI_DRD_2021_03_03.12_57`.')
            },
            {
                'asset_path': ('/TIFF/CBERS2B/2010_03/CBERS2B_CCD_201001.130915/151_098_0/'
                              '2_BC_UTM_WGS84/CBERS_2B_CCD2XS_20100301_151_098_L2_BAND1.tif'),
                'expected': 'Invalid reception date in scene_dir: `CBERS2B_CCD_201001.130915`.'
            },
            {
                'asset_path': ('/TIFF/LANDSAT1/1973_05/LANDSAT1_MSS_19730521.1200/237_059_0/'
                              '2_BC_UTM_WGS84/LANDSAT_1_MSS_19730521_237_059_L2_BAND4.tif'),
                'expected': 'Invalid reception time in scene_dir: `LANDSAT1_MSS_19730521.1200`.'
            },
            {
                'asset_path': ('/TIFF/SENTINEL/2021_01/SENTINEL_X_MUX_RAW_2021_01_01.13_48_30_ETC2/'
                        '209_110_0/2_BC_UTM_WGS84/SENTINEL_X_SL_20210101_209_110_L2_BAND5.tif'),
                'expected': ('Invalid scene directory: '
                            '`SENTINEL_X_MUX_RAW_2021_01_01.13_48_30_ETC2`.')
            },
            {
                'asset_path': ('/TIFF/CBERS4A/2021_01/CBERS_4A_MUX_RAW_2021_01_01.13_48_30_ETC2/'
                        '209_110_0_1/2_BC_UTM_WGS84/CBERS_4A_MUX_20210101_209_110_L2_BAND5.tif'),
                'expected': 'Path/row directory cannot be decoded: `209_110_0_1`.'
            },
            {
                'asset_path': ('/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_A_142_1_0/'
                              '8_BC_UTM_WGS84/CBERS_2B_HRC_20100301_151_A_142_1_L2_BAND1.tif'),
                'expected': 'Geo. processing directory cannot be decoded: `8_BC_UTM_WGS84`.'
            },
            {
                'asset_path': ('/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_2021_02_01.13_07_00_CB11/'
                              'CBERS_4_AWFI_20210201_154_117_L4_BAND13.tif'),
                'expected': 'Invalid `5` level to path: `/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_'
                        '2021_02_01.13_07_00_CB11/CBERS_4_AWFI_20210201_154_117_L4_BAND13.tif`.'
            },
            {
                'asset_path': ('/TIFF/LANDSAT1/1973_05/LANDSAT1_MSS_19730521.120000/237_059_0/'
                              '2_BC_UTM_WGS84/LANDSAT_1_MSS_1973521_237_059_L2_BAND4.tif'),
                'expected': 'Invalid date inside asset: `1973521`.'
            }
        ]

        for test_case in test_cases:
            with self.assertRaises(CDSRDecoderException) as error:
                decode_path(test_case['asset_path'])

            self.assertEqual(test_case['expected'], str(error.exception))

    def test__build_collection__errors__invalid_metadata(self):
        """Tests invalid metadata."""

        test_cases = [
            {
                'metadata': '',
                'expected_build_collection_error': ("Metadata must be a dict, "
                                                    "not a `<class 'str'>`."),
                'expected_build_item_error': ("Metadata must be a dict, not a "
                                              "`<class 'str'>`.")
            },
            {
                'metadata': 0,
                'expected_build_collection_error': ("Metadata must be a dict, "
                                                    "not a `<class 'int'>`."),
                'expected_build_item_error': ("Metadata must be a dict, not a "
                                              "`<class 'int'>`.")
            },
            {
                'metadata': [],
                'expected_build_collection_error': ("Metadata must be a dict, "
                                                    "not a `<class 'list'>`."),
                'expected_build_item_error': ("Metadata must be a dict, not a "
                                              "`<class 'list'>`.")
            },
            {
                'metadata': {'sensor': 'WFI'},
                'expected_build_collection_error': ('Missing keys inside metadata: '
                                        '`satellite, geo_processing, radio_processing`.'),
                'expected_build_item_error': ('Missing keys inside metadata: `satellite, '
                                              'path, row, date, antenna`.')
            },
            {
                'metadata': {'radio_processing': 'SR'},
                'expected_build_collection_error': ('Missing keys inside metadata: '
                                                    '`satellite, sensor, geo_processing`.'),
                'expected_build_item_error': ('Missing keys inside metadata: `satellite, sensor, '
                                             'path, row, date, antenna`.'),
            },
            {
                'metadata': {'satellite': 'AMAZONIA1', 'sensor': 'WFI'},
                'expected_build_collection_error': ('Missing keys inside metadata: '
                                                    '`geo_processing, radio_processing`.'),
                'expected_build_item_error': ('Missing keys inside metadata: `path, '
                                              'row, date, antenna`.')
            },
            {
                'metadata': {'antenna': 'CP11', 'sensor': 'WFI'},
                'expected_build_collection_error': ('Missing keys inside metadata: '
                                                    '`satellite, geo_processing, '
                                                    'radio_processing`.'),
                'expected_build_item_error': ('Missing keys inside metadata: `satellite, '
                                              'path, row, date`.')
            }
        ]

        for test_case in test_cases:
            with self.assertRaises(CDSRBuilderException) as error:
                build_collection(test_case['metadata'])

            self.assertEqual(test_case['expected_build_collection_error'], str(error.exception))

            with self.assertRaises(CDSRBuilderException) as error:
                build_item(test_case['metadata'])

            self.assertEqual(test_case['expected_build_item_error'], str(error.exception))
