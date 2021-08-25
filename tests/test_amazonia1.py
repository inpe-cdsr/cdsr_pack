"""Test cases related to AMAZONIA1 satellite."""


from unittest import TestCase

from src.cdsr_pack import CDSRBuilderException, CDSRDecoderException, \
                          build_collection, build_item, decode_path


class TestCDSRPackAMAZONIA1(TestCase):
    """TestCDSRPackAMAZONIA1"""

    def test__amazonia1__valid_assets(self):
        """Tests valid AMAZONIA1 assets."""

        test_cases = [
            {
                'asset_path': ('/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.12_57_40_CB11'
                    '/217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015_L2_BAND4.tif'),
                'expected_metadata': {
                    'satellite': 'AMAZONIA1', 'sensor': 'WFI', 'path': '217', 'row': '015',
                    'date': '2021-03-03', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'CB11'
                },
                'expected_collection': 'AMAZONIA1_WFI_L2_DN',
                'expected_item': 'AMAZONIA1_WFI_217015_20210303_CB11'
            },
            {
                'asset_path': ('/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.12_57_40_CB11'
                    '/217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015_L2_BAND3.xml'),
                'expected_metadata': {
                    'satellite': 'AMAZONIA1', 'sensor': 'WFI', 'path': '217', 'row': '015',
                    'date': '2021-03-03', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'CB11'
                },
                'expected_collection': 'AMAZONIA1_WFI_L2_DN',
                'expected_item': 'AMAZONIA1_WFI_217015_20210303_CB11'
            },
            {
                'asset_path': ('/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.12_57_40_CB11'
                    '/217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015_L2_BAND3.json'),
                'expected_metadata': {
                    'satellite': 'AMAZONIA1', 'sensor': 'WFI', 'path': '217', 'row': '015',
                    'date': '2021-03-03', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'CB11'
                },
                'expected_collection': 'AMAZONIA1_WFI_L2_DN',
                'expected_item': 'AMAZONIA1_WFI_217015_20210303_CB11'
            },
            {
                'asset_path': ('/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.12_57_40_CB11'
                    '/217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015.png'),
                'expected_metadata': {
                    'satellite': 'AMAZONIA1', 'sensor': 'WFI', 'path': '217', 'row': '015',
                    'date': '2021-03-03', 'geo_processing': '2', 'radio_processing': 'DN',
                    'antenna': 'CB11'
                },
                'expected_collection': 'AMAZONIA1_WFI_L2_DN',
                'expected_item': 'AMAZONIA1_WFI_217015_20210303_CB11'
            },
            {
                'asset_path': ('/TIFF/AMAZONIA1/2021_04/AMAZONIA_1_WFI_DRD_2021_04_01.13_22_45_CP5_'
                    'COROT/035_016_0/4_BC_LCC_WGS84/AMAZONIA_1_WFI_20210401_035_016_L4_BAND1.tif'),
                'expected_metadata': {
                    'satellite': 'AMAZONIA1', 'sensor': 'WFI', 'path': '035', 'row': '016',
                    'date': '2021-04-01', 'geo_processing': '4', 'radio_processing': 'DN',
                    'antenna': 'CP5'
                },
                'expected_collection': 'AMAZONIA1_WFI_L4_DN',
                'expected_item': 'AMAZONIA1_WFI_035016_20210401_CP5'
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

    def test__amazonia1__valid_paths(self):
        """Tests valid AMAZONIA1 paths."""

        # `radio_processing` and `date` keys are get from asset, not path
        test_cases = [
            {
                'path': '/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.'
                        '12_57_40_CB11/217_015_0/2_BC_LCC_WGS84',
                'expected_metadata': {
                    'satellite': 'AMAZONIA1', 'sensor': 'WFI', 'path': '217', 'row': '015',
                    'date': None, 'geo_processing': '2', 'radio_processing': None,
                    'antenna': 'CB11'
                }
            },
            {
                'path': '/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.'
                        '14_35_23_CB11_SIR18/233_017_0/4_BC_LCC_WGS84',
                'expected_metadata': {
                    'satellite': 'AMAZONIA1', 'sensor': 'WFI', 'path': '233', 'row': '017',
                    'date': None, 'geo_processing': '4', 'radio_processing': None,
                    'antenna': 'CB11'
                }
            },
            {
                'path': '/TIFF/AMAZONIA1/2021_04/AMAZONIA_1_WFI_DRD_2021_04_01.'
                        '13_22_45_CP5_COROT/035_016_0/4_BC_LCC_WGS84',
                'expected_metadata': {
                    'satellite': 'AMAZONIA1', 'sensor': 'WFI', 'path': '035', 'row': '016',
                    'date': None, 'geo_processing': '4', 'radio_processing': None,
                    'antenna': 'CP5'
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

    def test__amazonia1__invalid_assets(self):
        """Tests invalid AMAZONIA1 assets."""

        test_cases = [
            {
                'asset_path': ('/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.12_57_40_CB11'
                        '/217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015'),
                'expected_error_message': 'An asset must have an extension.'
            },
            {
                'asset_path': ('/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.12_57_40'
                        '/217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015_L2_BAND4.tif'),
                'expected_error_message': ('Invalid antenna in scene_dir: '
                                           '`AMAZONIA_1_WFI_DRD_2021_03_03.12_57_40`.')
            },
            {
                'asset_path': ('/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.12_57_40_XYZ'
                        '/217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015_L2_BAND4.tif'),
                'expected_error_message': ('Invalid antenna in scene_dir: '
                                           '`AMAZONIA_1_WFI_DRD_2021_03_03.12_57_40_XYZ`.')
            },
            {
                'asset_path': ('/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03.12_57_40_CB11'
                    '/217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015_L2_BAND4.tif'),
                'expected_error_message': ('Invalid reception date in scene_dir: '
                                           '`AMAZONIA_1_WFI_DRD_2021_03.12_57_40_CB11`.')
            },
            {
                'asset_path': ('/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.12_40_CB11'
                    '/217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015_L2_BAND4.tif'),
                'expected_error_message': ('Invalid reception time in scene_dir: '
                                           '`AMAZONIA_1_WFI_DRD_2021_03_03.12_40_CB11`.')
            }
        ]

        for test_case in test_cases:
            with self.assertRaises(CDSRDecoderException) as error:
                decode_path(test_case['asset_path'])

            self.assertEqual(test_case['expected_error_message'], str(error.exception))
