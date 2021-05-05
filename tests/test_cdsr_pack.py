"""test_cdsr_pack.py test module."""

from unittest import TestCase

from src.cdsr_pack import CDSRBuilderException, CDSRDecoderException, \
                          build_collection, decode_path


class TestCDSRPackAMAZONIA1(TestCase):
    """TestCDSRPackAMAZONIA1"""

    def test__amazonia1__valid_assets(self):
        """Tests valid AMAZONIA1 assets."""

        test_cases = [
            '/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.12_57_40_CB11/'
                '217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015_L2_BAND4.tif',
            '/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.12_57_40_CB11/'
                '217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015_L2_BAND3.xml'
        ]

        expected_metadata = {
            'satellite': 'AMAZONIA1', 'sensor': 'WFI', 'path': '217', 'row': '015',
            'geo_processing': '2', 'radio_processing': 'DN'
        }

        for test_case in test_cases:
            self.assertEqual(expected_metadata, decode_path(test_case))

        self.assertEqual('AMAZONIA1_WFI_L2_DN', build_collection(expected_metadata))

    def test__amazonia1__invalid_assets(self):
        """Tests invalid AMAZONIA1 assets."""

        asset_path = ('/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.12_57_40_CB11/'
                      '217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015.png')

        with self.assertRaises(CDSRDecoderException) as error:
            decode_path(asset_path)

        self.assertEqual('Just TIFF and XML files can be decoded.', str(error.exception))


class TestCDSRPackCBERS2B(TestCase):
    """TestCDSRPackCBERS2B"""

    def test__cbers2b__valid_assets(self):
        """Tests valid CBERS2B assets."""

        test_cases = [
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_CCD_20100301.130915/151_098_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_CCD2XS_20100301_151_098_L2_BAND1.tif',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'CCD',
                    'path': '151', 'row': '098',
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS2B_CCD_L2_DN'
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_CCD_20100301.130915/151_098_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_CCD2XS_20100301_151_098_L2_BAND1.xml',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'CCD',
                    'path': '151', 'row': '098',
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS2B_CCD_L2_DN'
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_B_141_5_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_HRC_20100301_151_B_141_5_L2_BAND1.tif',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'HRC',
                    'path': '151', 'row': '141',
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS2B_HRC_L2_DN'
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_B_141_5_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_HRC_20100301_151_B_141_5_L2_BAND1.xml',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'HRC',
                    'path': '151', 'row': '141',
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS2B_HRC_L2_DN'
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_A_142_1_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_HRC_20100301_151_A_142_1_L2_BAND1.tif',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'HRC',
                    'path': '151', 'row': '142',
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS2B_HRC_L2_DN'
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_A_142_1_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_HRC_20100301_151_A_142_1_L2_BAND1.xml',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'HRC',
                    'path': '151', 'row': '142',
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS2B_HRC_L2_DN'
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_WFI_20100301.144734/177_092_0/'
                                '2_BC_LCC_WGS84/CBERS_2B_WFI_20100301_177_092_L2_BAND1.tif',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'WFI',
                    'path': '177', 'row': '092',
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS2B_WFI_L2_DN'
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_WFI_20100301.144734/177_092_0/'
                                '2_BC_LCC_WGS84/CBERS_2B_WFI_20100301_177_092_L2_BAND1.xml',
                'expected_metadata': {
                    'satellite': 'CBERS2B', 'sensor': 'WFI',
                    'path': '177', 'row': '092',
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS2B_WFI_L2_DN'
            }
        ]

        for test_case in test_cases:
            # check if decode_path function works
            self.assertEqual(test_case['expected_metadata'],
                             decode_path(test_case['asset_path']))
            # check if build_collection function works
            self.assertEqual(test_case['expected_collection'],
                             build_collection(test_case['expected_metadata']))

    def test__cbers2b__invalid_assets(self):
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
            with self.assertRaises(CDSRDecoderException) as error:
                decode_path(test_case)

            self.assertEqual('Just TIFF and XML files can be decoded.', str(error.exception))


class TestCDSRPackCBERS4(TestCase):
    """TestCDSRPackCBERS4"""

    def test__cbers4__valid_assets(self):
        """Tests valid CBERS4 assets."""

        test_cases = [
            {
                'asset_path': '/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_2021_02_01.13_07_00_CB11/'
                            '154_117_0/4_BC_UTM_WGS84/CBERS_4_AWFI_20210201_154_117_L4_BAND13.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'AWFI',
                    'path': '154', 'row': '117',
                    'geo_processing': '4', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS4_AWFI_L4_DN'
            },
            {
                'asset_path': '/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_2021_02_01.13_07_00_CB11/'
                            '154_117_0/4_BC_UTM_WGS84/CBERS_4_AWFI_20210201_154_117_L4_BAND13.xml',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'AWFI',
                    'path': '154', 'row': '117',
                    'geo_processing': '4', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS4_AWFI_L4_DN'
            },
            {
                'asset_path': '/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_2021_02_01.13_07_00_CB11/'
                    '154_117_0/4_BC_UTM_WGS84/CBERS_4_AWFI_20210201_154_117_L4_CMASK_GRID_SURFACE.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'AWFI',
                    'path': '154', 'row': '117',
                    'geo_processing': '4', 'radio_processing': 'SR'
                },
                'expected_collection': 'CBERS4_AWFI_L4_SR'
            },
            {
                'asset_path': '/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_2021_02_01.13_07_00_CB11/'
                    '154_117_0/4_BC_UTM_WGS84/CBERS_4_AWFI_20210201_154_117_L4_BAND13_GRID_SURFACE.xml',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'AWFI',
                    'path': '154', 'row': '117',
                    'geo_processing': '4', 'radio_processing': 'SR'
                },
                'expected_collection': 'CBERS4_AWFI_L4_SR'
            },
            {
                'asset_path': '/TIFF/CBERS4/2020_07/CBERS_4_MUX_DRD_2020_07_31.13_07_00_CB11/'
                            '155_103_0/4_BC_UTM_WGS84/CBERS_4_MUX_20200731_155_103_L4_EVI.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'MUX',
                    'path': '155', 'row': '103',
                    'geo_processing': '4', 'radio_processing': 'SR'
                },
                'expected_collection': 'CBERS4_MUX_L4_SR'
            },
            {
                'asset_path': '/TIFF/CBERS4/2020_07/CBERS_4_MUX_DRD_2020_07_31.13_07_00_CB11/'
                            '155_103_0/4_BC_UTM_WGS84/CBERS_4_MUX_20200731_155_103_L4_NDVI.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'MUX',
                    'path': '155', 'row': '103',
                    'geo_processing': '4', 'radio_processing': 'SR'
                },
                'expected_collection': 'CBERS4_MUX_L4_SR'
            },
            {
                'asset_path': '/TIFF/CBERS4/2020_07/CBERS_4_MUX_DRD_2020_07_31.13_07_00_CB11/'
                    '155_103_0/4_BC_UTM_WGS84/CBERS_4_MUX_20200731_155_103_L4_BAND5_GRID_SURFACE.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'MUX',
                    'path': '155', 'row': '103',
                    'geo_processing': '4', 'radio_processing': 'SR'
                },
                'expected_collection': 'CBERS4_MUX_L4_SR'
            },
            {
                'asset_path': '/TIFF/CBERS4/2020_07/CBERS_4_MUX_DRD_2020_07_31.13_07_00_CB11/'
                    '155_103_0/4_BC_UTM_WGS84/CBERS_4_MUX_20200731_155_103_L4_BAND5_GRID_SURFACE.xml',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'MUX',
                    'path': '155', 'row': '103',
                    'geo_processing': '4', 'radio_processing': 'SR'
                },
                'expected_collection': 'CBERS4_MUX_L4_SR'
            },
            {
                'asset_path': '/TIFF/CBERS4/2018_01/CBERS_4_MUX_DRD_2018_01_01.13_14_00_CB11/'
                        '156_103_0/4_BC_UTM_WGS84/CBERS_4_MUX_20180101_156_103_L4_BAND5.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'MUX',
                    'path': '156', 'row': '103',
                    'geo_processing': '4', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS4_MUX_L4_DN'
            },
            {
                'asset_path': '/TIFF/CBERS4/2018_01/CBERS_4_MUX_DRD_2018_01_01.13_14_00_CB11/'
                        '156_103_0/4_BC_UTM_WGS84/CBERS_4_MUX_20180101_156_103_L4_BAND6.xml',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'MUX',
                    'path': '156', 'row': '103',
                    'geo_processing': '4', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS4_MUX_L4_DN'
            },
            {
                'asset_path': '/TIFF/CBERS4/2021_02/CBERS_4_PAN10M_DRD_2021_02_02.01_32_45_CB11/'
                        '073_113_0/2_BC_UTM_WGS84/CBERS_4_PAN10M_20210201_073_113_L2_BAND2.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'PAN10M',
                    'path': '073', 'row': '113',
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS4_PAN10M_L2_DN'
            },
            {
                'asset_path': '/TIFF/CBERS4/2021_02/CBERS_4_PAN10M_DRD_2021_02_02.01_32_45_CB11/'
                        '073_113_0/2_BC_UTM_WGS84/CBERS_4_PAN10M_20210201_073_113_L2_BAND2.xml',
                'expected_metadata': {
                    'satellite': 'CBERS4', 'sensor': 'PAN10M',
                    'path': '073', 'row': '113',
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS4_PAN10M_L2_DN'
            }
        ]

        for test_case in test_cases:
            # check if decode_path function works
            self.assertEqual(test_case['expected_metadata'],
                             decode_path(test_case['asset_path']))
            # check if build_collection function works
            self.assertEqual(test_case['expected_collection'],
                             build_collection(test_case['expected_metadata']))

    def test__cbers4__invalid_assets(self):
        """Tests invalid CBERS4 assets."""

        test_cases = [
            '/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_2021_02_01.13_07_00_CB11/154_117_0/'
                '4_BC_UTM_WGS84/CBERS_4_AWFI_20210201_154_117.png',
            '/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_2021_02_01.13_07_00_CB11/154_117_0/'
                '4_BC_UTM_WGS84/CBERS_4_AWFI_20210201_154_117.png',
            '/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_2021_02_01.13_07_00_CB11/154_117_0/'
                '4_BC_UTM_WGS84/CBERS_4_AWFI_20210201_154_117_L4_CMASK_GRID_SURFACE.json',
            '/TIFF/CBERS4/2020_07/CBERS_4_MUX_DRD_2020_07_31.13_07_00_CB11/155_103_0/'
                '4_BC_UTM_WGS84/CBERS_4_MUX_20200731_155_103.png',
            '/TIFF/CBERS4/2020_07/CBERS_4_MUX_DRD_2020_07_31.13_07_00_CB11/155_103_0/'
                '4_BC_UTM_WGS84/CBERS_4_MUX_20200731_155_103_L4_CMASK_GRID_SURFACE.json',
            '/TIFF/CBERS4/2018_01/CBERS_4_MUX_DRD_2018_01_01.13_14_00_CB11/156_103_0/'
                '4_BC_UTM_WGS84/CBERS_4_MUX_20180101_156_103.png',
            '/TIFF/CBERS4/2021_02/CBERS_4_PAN10M_DRD_2021_02_02.01_32_45_CB11/073_113_0/'
                '2_BC_UTM_WGS84/CBERS_4_PAN10M_20210201_073_113.png'
        ]

        for test_case in test_cases:
            with self.assertRaises(CDSRDecoderException) as error:
                decode_path(test_case)

            self.assertEqual('Just TIFF and XML files can be decoded.', str(error.exception))


class TestCDSRPackCBERS4A(TestCase):
    """TestCDSRPackCBERS4A"""

    def test__cbers4a__valid_assets(self):
        """Tests valid CBERS4A assets."""

        test_cases = [
            {
                'asset_path': '/TIFF/CBERS4A/2021_01/CBERS_4A_MUX_RAW_2021_01_01.13_48_30_ETC2/'
                        '209_110_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20210101_209_110_L2_BAND5.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'MUX', 'path': '209', 'row': '110',
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS4A_MUX_L2_DN'
            },
            {
                'asset_path': '/TIFF/CBERS4A/2021_01/CBERS_4A_MUX_RAW_2021_01_01.13_48_30_ETC2/'
                        '209_110_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20210101_209_110_L2_BAND5.xml',
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'MUX', 'path': '209', 'row': '110',
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS4A_MUX_L2_DN'
            },
            {
                'asset_path': '/TIFF/CBERS4A/2020_12/CBERS_4A_MUX_RAW_2020_12_01.13_47_30_ETC2/'
                        '209_122_0/3_BC_UTM_WGS84/CBERS_4A_MUX_20201201_209_122_L3_BAND5.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'MUX', 'path': '209', 'row': '122',
                    'geo_processing': '3', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS4A_MUX_L3_DN'
            },
            {
                'asset_path': '/TIFF/CBERS4A/2020_12/CBERS_4A_MUX_RAW_2020_12_01.13_47_30_ETC2/'
                        '209_122_0/3_BC_UTM_WGS84/CBERS_4A_MUX_20201201_209_122_L3_BAND5.xml',
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'MUX', 'path': '209', 'row': '122',
                    'geo_processing': '3', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS4A_MUX_L3_DN'
            },
            {
                'asset_path': '/TIFF/CBERS4A/2020_12/CBERS_4A_MUX_RAW_2020_12_01.13_47_30_ETC2/'
                        '209_122_0/4_BC_UTM_WGS84/CBERS_4A_MUX_20201201_209_122_L4_BAND5.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'MUX', 'path': '209', 'row': '122',
                    'geo_processing': '4', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS4A_MUX_L4_DN'
            },
            {
                'asset_path': '/TIFF/CBERS4A/2020_12/CBERS_4A_MUX_RAW_2020_12_01.13_47_30_ETC2/'
                        '209_122_0/4_BC_UTM_WGS84/CBERS_4A_MUX_20201201_209_122_L4_BAND5.xml',
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'MUX', 'path': '209', 'row': '122',
                    'geo_processing': '4', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS4A_MUX_L4_DN'
            },
            {
                'asset_path': '/TIFF/CBERS4A/2020_12/CBERS_4A_WFI_RAW_2020_12_22.13_53_30_ETC2_CHUNK/'
                            '211_108_0/2B_BC_UTM_WGS84/CBERS_4A_WFI_20201222_211_108_L2B_BAND13.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '211', 'row': '108',
                    'geo_processing': '2B', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS4A_WFI_L2B_DN'
            },
            {
                'asset_path': '/TIFF/CBERS4A/2020_12/CBERS_4A_WFI_RAW_2020_12_22.13_53_30_ETC2_CHUNK/'
                            '211_108_0/2B_BC_UTM_WGS84/CBERS_4A_WFI_20201222_211_108_L2B_BAND14.xml',
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '211', 'row': '108',
                    'geo_processing': '2B', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS4A_WFI_L2B_DN'
            },
            {
                'asset_path': '/TIFF/CBERS4A/2020_12/CBERS_4A_WFI_RAW_2020_12_07.14_03_00_ETC2/'
                        '214_108_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20201207_214_108_L4_LEFT_EVI.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '214', 'row': '108',
                    'geo_processing': '4', 'radio_processing': 'SR'
                },
                'expected_collection': 'CBERS4A_WFI_L4_SR'
            },
            {
                'asset_path': '/TIFF/CBERS4A/2020_12/CBERS_4A_WFI_RAW_2020_12_07.14_03_00_ETC2/'
                        '214_108_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20201207_214_108_L4_LEFT_NDVI.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '214', 'row': '108',
                    'geo_processing': '4', 'radio_processing': 'SR'
                },
                'expected_collection': 'CBERS4A_WFI_L4_SR'
            },
            {
                'asset_path': '/TIFF/CBERS4A/2020_12/CBERS_4A_WFI_RAW_2020_12_07.14_03_00_ETC2/'
                    '214_108_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20201207_214_108_L4_LEFT_CMASK_GRID_SURFACE.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '214', 'row': '108',
                    'geo_processing': '4', 'radio_processing': 'SR'
                },
                'expected_collection': 'CBERS4A_WFI_L4_SR'
            },
            {
                'asset_path': '/TIFF/CBERS4A/2020_12/CBERS_4A_WFI_RAW_2020_12_07.14_03_00_ETC2/'
                    '214_108_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20201207_214_108_L4_LEFT_BAND13_GRID_SURFACE.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '214', 'row': '108',
                    'geo_processing': '4', 'radio_processing': 'SR'
                },
                'expected_collection': 'CBERS4A_WFI_L4_SR'
            },
            {
                'asset_path': '/TIFF/CBERS4A/2020_12/CBERS_4A_WFI_RAW_2020_12_07.14_03_00_ETC2/'
                    '214_108_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20201207_214_108_L4_LEFT_BAND13_GRID_SURFACE.xml',
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '214', 'row': '108',
                    'geo_processing': '4', 'radio_processing': 'SR'
                },
                'expected_collection': 'CBERS4A_WFI_L4_SR'
            },
            {
                'asset_path': '/TIFF/CBERS4A/2019_12/CBERS_4A_WFI_RAW_2019_12_27.13_53_00_ETC2/'
                            '215_132_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20191227_215_132_L4_BAND13.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '215', 'row': '132',
                    'geo_processing': '4', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS4A_WFI_L4_DN'
            },
            {
                'asset_path': '/TIFF/CBERS4A/2019_12/CBERS_4A_WFI_RAW_2019_12_27.13_53_00_ETC2/'
                        '215_132_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20191227_215_132_L4_LEFT_BAND15.xml',
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '215', 'row': '132',
                    'geo_processing': '4', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS4A_WFI_L4_DN'
            },
            {
                'asset_path': '/TIFF/CBERS4A/2020_11/CBERS_4A_WFI_RAW_2020_11_22.14_11_30_ETC2/'
                        '217_156_0/3_BC_UTM_WGS84/CBERS_4A_WFI_20201122_217_156_L3_BAND13.tif',
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '217', 'row': '156',
                    'geo_processing': '3', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS4A_WFI_L3_DN'
            },
            {
                'asset_path': '/TIFF/CBERS4A/2020_11/CBERS_4A_WFI_RAW_2020_11_22.14_11_30_ETC2/'
                        '217_156_0/3_BC_UTM_WGS84/CBERS_4A_WFI_20201122_217_156_L3_BAND14.xml',
                'expected_metadata': {
                    'satellite': 'CBERS4A', 'sensor': 'WFI', 'path': '217', 'row': '156',
                    'geo_processing': '3', 'radio_processing': 'DN'
                },
                'expected_collection': 'CBERS4A_WFI_L3_DN'
            }
        ]

        for test_case in test_cases:
            # check if decode_path function works
            self.assertEqual(test_case['expected_metadata'],
                             decode_path(test_case['asset_path']))
            # check if build_collection function works
            self.assertEqual(test_case['expected_collection'],
                             build_collection(test_case['expected_metadata']))

    def test__cbers4a__invalid_assets(self):
        """Tests invalid CBERS4A assets."""

        test_cases = [
            '/TIFF/CBERS4A/2021_01/CBERS_4A_MUX_RAW_2021_01_01.13_48_30_ETC2/209_110_0/'
                '2_BC_UTM_WGS84/CBERS_4A_MUX_20210101_209_110.png',
            '/TIFF/CBERS4A/2020_12/CBERS_4A_MUX_RAW_2020_12_01.13_47_30_ETC2/209_122_0/'
                '3_BC_UTM_WGS84/CBERS_4A_MUX_20201201_209_122.png',
            '/TIFF/CBERS4A/2020_12/CBERS_4A_MUX_RAW_2020_12_01.13_47_30_ETC2/209_122_0/'
                '4_BC_UTM_WGS84/CBERS_4A_MUX_20201201_209_122.png',
            '/TIFF/CBERS4A/2020_12/CBERS_4A_WFI_RAW_2020_12_22.13_53_30_ETC2_CHUNK/211_108_0/'
                '2B_BC_UTM_WGS84/CBERS_4A_WFI_20201222_211_108.png',
            '/TIFF/CBERS4A/2020_12/CBERS_4A_WFI_RAW_2020_12_07.14_03_00_ETC2/214_108_0/'
                '4_BC_UTM_WGS84/CBERS_4A_WFI_20201207_214_108.png',
            '/TIFF/CBERS4A/2020_12/CBERS_4A_WFI_RAW_2020_12_07.14_03_00_ETC2/214_108_0/'
                '4_BC_UTM_WGS84/CBERS_4A_WFI_20201207_214_108_L4_LEFT_CMASK_GRID_SURFACE.json',
            '/TIFF/CBERS4A/2019_12/CBERS_4A_WFI_RAW_2019_12_27.13_53_00_ETC2/215_132_0/'
                '4_BC_UTM_WGS84/CBERS_4A_WFI_20191227_215_132.png',
            '/TIFF/CBERS4A/2020_11/CBERS_4A_WFI_RAW_2020_11_22.14_11_30_ETC2/217_156_0/'
                '3_BC_UTM_WGS84/CBERS_4A_WFI_20201122_217_156.png'
        ]

        for test_case in test_cases:
            with self.assertRaises(CDSRDecoderException) as error:
                decode_path(test_case)

            self.assertEqual('Just TIFF and XML files can be decoded.', str(error.exception))


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
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'LANDSAT1_MSS_L2_DN'
            },
            {
                'asset_path': '/TIFF/LANDSAT1/1973_05/LANDSAT1_MSS_19730521.120000/237_059_0/'
                                '2_BC_UTM_WGS84/LANDSAT_1_MSS_19730521_237_059_L2_BAND4.xml',
                'expected_metadata': {
                    'satellite': 'LANDSAT1', 'sensor': 'MSS', 'path': '237', 'row': '059',
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'LANDSAT1_MSS_L2_DN'
            },
            {
                'asset_path': '/TIFF/LANDSAT2/1982_02/LANDSAT2_MSS_19820201.120000/005_055_0/'
                                '2_BC_UTM_WGS84/LANDSAT_2_MSS_19820201_005_055_L2_BAND4.tif',
                'expected_metadata': {
                    'satellite': 'LANDSAT2', 'sensor': 'MSS', 'path': '005', 'row': '055',
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'LANDSAT2_MSS_L2_DN'
            },
            {
                'asset_path': '/TIFF/LANDSAT2/1982_02/LANDSAT2_MSS_19820201.120000/005_055_0/'
                                '2_BC_UTM_WGS84/LANDSAT_2_MSS_19820201_005_055_L2_BAND4.xml',
                'expected_metadata': {
                    'satellite': 'LANDSAT2', 'sensor': 'MSS', 'path': '005', 'row': '055',
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'LANDSAT2_MSS_L2_DN'
            },
            {
                'asset_path': '/TIFF/LANDSAT3/1978_04/LANDSAT3_MSS_19780405.120000/235_075_0/'
                                '2_BC_UTM_WGS84/LANDSAT_3_MSS_19780405_235_075_L2_BAND4.tif',
                'expected_metadata': {
                    'satellite': 'LANDSAT3', 'sensor': 'MSS', 'path': '235', 'row': '075',
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'LANDSAT3_MSS_L2_DN'
            },
            {
                'asset_path': '/TIFF/LANDSAT3/1978_04/LANDSAT3_MSS_19780405.120000/235_075_0/'
                                '2_BC_UTM_WGS84/LANDSAT_3_MSS_19780405_235_075_L2_BAND4.xml',
                'expected_metadata': {
                    'satellite': 'LANDSAT3', 'sensor': 'MSS', 'path': '235', 'row': '075',
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'LANDSAT3_MSS_L2_DN'
            },
            {
                'asset_path': '/TIFF/LANDSAT5/2011_11/LANDSAT5_TM_20111101.140950/233_054_0/'
                                '2_BC_UTM_WGS84/LANDSAT_5_TM_20111101_233_054_L2_BAND1.tif',
                'expected_metadata': {
                    'satellite': 'LANDSAT5', 'sensor': 'TM', 'path': '233', 'row': '054',
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'LANDSAT5_TM_L2_DN'
            },
            {
                'asset_path': '/TIFF/LANDSAT5/2011_11/LANDSAT5_TM_20111101.140950/233_054_0/'
                                '2_BC_UTM_WGS84/LANDSAT_5_TM_20111101_233_054_L2_BAND1.xml',
                'expected_metadata': {
                    'satellite': 'LANDSAT5', 'sensor': 'TM', 'path': '233', 'row': '054',
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'LANDSAT5_TM_L2_DN'
            },
            {
                'asset_path': '/TIFF/LANDSAT7/1999_07/LANDSAT7_ETM_19990731.144148/004_072_0/'
                                '2_BC_UTM_WGS84/LANDSAT_7_ETMXS_19990731_004_072_L2_BAND1.tif',
                'expected_metadata': {
                    'satellite': 'LANDSAT7', 'sensor': 'ETM', 'path': '004', 'row': '072',
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'LANDSAT7_ETM_L2_DN'
            },
            {
                'asset_path': '/TIFF/LANDSAT7/1999_07/LANDSAT7_ETM_19990731.144148/004_072_0/'
                                '2_BC_UTM_WGS84/LANDSAT_7_ETMXS_19990731_004_072_L2_BAND1.xml',
                'expected_metadata': {
                    'satellite': 'LANDSAT7', 'sensor': 'ETM', 'path': '004', 'row': '072',
                    'geo_processing': '2', 'radio_processing': 'DN'
                },
                'expected_collection': 'LANDSAT7_ETM_L2_DN'
            }
        ]

        for test_case in test_cases:
            # check if decode_path function works
            self.assertEqual(test_case['expected_metadata'],
                             decode_path(test_case['asset_path']))
            # check if build_collection function works
            self.assertEqual(test_case['expected_collection'],
                             build_collection(test_case['expected_metadata']))

    def test__landsat__invalid_assets(self):
        """Tests invalid LANDSAT assets."""

        test_cases = [
            '/TIFF/LANDSAT1/1973_05/LANDSAT1_MSS_19730521.120000/237_059_0/'
                '2_BC_UTM_WGS84/LANDSAT_1_MSS_19730521_237_059.png',
            '/TIFF/LANDSAT2/1982_02/LANDSAT2_MSS_19820201.120000/005_055_0/'
                '2_BC_UTM_WGS84/LANDSAT_2_MSS_19820201_005_055.png',
            '/TIFF/LANDSAT3/1978_04/LANDSAT3_MSS_19780405.120000/235_075_0/'
                '2_BC_UTM_WGS84/LANDSAT_3_MSS_19780405_235_075.png',
            '/TIFF/LANDSAT5/2011_11/LANDSAT5_TM_20111101.140950/233_054_0/'
                '2_BC_UTM_WGS84/LANDSAT_5_TM_20111101_233_054.png',
            '/TIFF/LANDSAT7/1999_07/LANDSAT7_ETM_19990731.144148/004_072_0/'
                '2_BC_UTM_WGS84/LANDSAT_7_ETMXS_19990731_004_072.png'
        ]

        for test_case in test_cases:
            with self.assertRaises(CDSRDecoderException) as error:
                decode_path(test_case)

            self.assertEqual('Just TIFF and XML files can be decoded.', str(error.exception))


class TestCDSRPackErrors(TestCase):
    """TestCDSRPackDecodeErrors"""

    def test__decode_path__errors__invalid_assets(self):
        """Tests invalid assets."""

        test_cases = [
            {
                'asset_path': '/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.12_57/'
                            '217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015_L2_BAND4.tif',
                'expected': 'Invalid spplited time: `12_57`.'
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_CCD_201001.130915/151_098_0/'
                                '2_BC_UTM_WGS84/CBERS_2B_CCD2XS_20100301_151_098_L2_BAND1.tif',
                'expected': 'Size of `201001` date is not 8.'
            },
            {
                'asset_path': '/TIFF/LANDSAT1/1973_05/LANDSAT1_MSS_19730521.1200/237_059_0/'
                            '2_BC_UTM_WGS84/LANDSAT_1_MSS_19730521_237_059_L2_BAND4.tif',
                'expected': 'Size of `1200` time is not 6.'
            },
            {
                'asset_path': '/TIFF/SENTINEL/2021_01/SENTINEL_X_MUX_RAW_2021_01_01.13_48_30_ETC2/'
                        '209_110_0/2_BC_UTM_WGS84/SENTINEL_X_SL_20210101_209_110_L2_BAND5.tif',
                'expected': 'Invalid scene directory: `SENTINEL_X_MUX_RAW_2021_01_01.13_48_30_ETC2`.'
            },
            {
                'asset_path': '/TIFF/CBERS4A/2021_01/CBERS_4A_MUX_RAW_2021_01_01.13_48_30_ETC2/'
                        '209_110_0_1/2_BC_UTM_WGS84/CBERS_4A_MUX_20210101_209_110_L2_BAND5.tif',
                'expected': '`209_110_0_1` path/row directory cannot be decoded.'
            },
            {
                'asset_path': '/TIFF/CBERS2B/2010_03/CBERS2B_HRC_20100301.130915/151_A_142_1_0/'
                                '8_BC_UTM_WGS84/CBERS_2B_HRC_20100301_151_A_142_1_L2_BAND1.tif',
                'expected': '`8_BC_UTM_WGS84` geo. processing directory cannot be decoded.'
            },
            {
                'asset_path': '/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_2021_02_01.13_07_00_CB11/'
                            'CBERS_4_AWFI_20210201_154_117_L4_BAND13.tif',
                'expected': 'Invalid `5` level to path: `/TIFF/CBERS4/2021_02/CBERS_4_AWFI_DRD_'
                        '2021_02_01.13_07_00_CB11/CBERS_4_AWFI_20210201_154_117_L4_BAND13.tif`.'
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
                'expected': "Metadata must be a dict, not a `<class 'str'>`."
            },
            {
                'metadata': 0,
                'expected': "Metadata must be a dict, not a `<class 'int'>`."
            },
            {
                'metadata': [],
                'expected': "Metadata must be a dict, not a `<class 'list'>`."
            },
            {
                'metadata': {'sensor': 'WFI'},
                'expected': 'Missing keys inside metadata: `satellite, geo_processing, '
                            'radio_processing`.'
            },
            {
                'metadata': {'radio_processing': 'SR'},
                'expected': 'Missing keys inside metadata: `satellite, sensor, geo_processing`.'
            },
            {
                'metadata': {'satellite': 'AMAZONIA1', 'sensor': 'WFI'},
                'expected': 'Missing keys inside metadata: `geo_processing, radio_processing`.'
            }
        ]

        for test_case in test_cases:
            with self.assertRaises(CDSRBuilderException) as error:
                build_collection(test_case['metadata'])

            self.assertEqual(test_case['expected'], str(error.exception))
