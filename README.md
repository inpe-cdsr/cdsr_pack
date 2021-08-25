# cdsr_pack

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/inpe-cdsr/cdsr_pack/blob/master/LICENSE)
![Github Actions](https://github.com/inpe-cdsr/cdsr_pack/actions/workflows/python-package.yml/badge.svg)
[![Software Life Cycle](https://img.shields.io/badge/lifecycle-stable-sucess.svg)](https://www.tidyverse.org/lifecycle/#stable)


CDSR pack is a package to store common functions from CDSR project.


## Installation

```
$ pip install cdsr-pack==<version>
```

Look at [here](https://pypi.org/project/cdsr-pack/#history) to see the available versions.


## Usage

```python
>>> from cdsr_pack import build_collection, build_item, decode_path

>>> image = ('/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.12_57_40_CB11/'
             '217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015_L2_BAND4.tif')

>>> decoded_image = decode_path(image)

>>> decoded_image
{
    'satellite': 'AMAZONIA1', 'sensor': 'WFI', 'path': '217', 'row': '015',
    'date': '2021-03-03', 'geo_processing': '2', 'radio_processing': 'DN',
    'antenna': 'CB11'
}

>>> build_collection(decoded_image)
'AMAZONIA1_WFI_L2_DN'

>>> build_item(decoded_image)
'AMAZONIA1_WFI_217015_20210303_CB11'
```

## Development

Install a specific Python version and create a virtualenv with it. For example:

```
$ pyenv install 3.8.5 && \
    pyenv virtualenv 3.8.5 inpe_cdsr_cdsr_pack
```

Activate the virtualenv and install the dependencies inside it:

```
$ pyenv activate inpe_cdsr_cdsr_pack && \
    pip install -r requirements.txt
```


### Testing

Activate the virtualenv and run the test cases:

```
$ pyenv activate inpe_cdsr_cdsr_pack
$ ./run_tests.sh
```
