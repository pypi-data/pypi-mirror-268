# COLAB PREAMBLE
Prepare google colaboratory by one line of command

[![](https://badge.fury.io/py/colab-preamble.svg)](https://badge.fury.io/py/colab-preamble)


## Installation

```python
# from pypi
$ pip install colab-preamble

# alternatively, from github
$ git clone https://github.com/kota7/colab-preamble --depth 1
$ pip install -U ./colab-preamble
```

## Example

Example colab notebook is here: [colab-preamble-example.ipynb](https://colab.research.google.com/drive/1CD_tZTP5eDRYe0u8ZchuLlEYHjCDJOYw?usp=sharing)

## Usage

```python
import colab_preamble

colab_preamble_run(google_cloud_project="<project-id>", mount_drive=True)
# If no need to access google cloud services, no need to provide set google_cloud_project=None
# If no need to mount google drive, set mount_drive=False
```

## Effect

When `google_cloud_project` is given,

- Set the default project ID
    - Run `gcloud config set ...`
    - Set `GOOGLE_CLOUD_PROJECT` environment variable
- Open the authentication prompt
- Introduce bigquery magic command `bq`


When `mount_drive` is true,

- Open the prompt and mount the google drive at '/content/drive'
