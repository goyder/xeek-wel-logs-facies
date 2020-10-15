# XEEK challenges

This repo covers attempts to meet the [Force Well Logs challenge](https://xeek.ai/challenges/force-well-logs/data) on xeek.ai.

## Getting started

### Data 

#### Input data tables

The data used in this challenge is available for download at the website. Download `train.csv` and `test.csv` and put them under `data/external` in this repo.

Alternatively, you can:

* Download `train.csv` and `test.csv`
* Upload them to a personally controlled S3 bucket under the keys `facies/train.csv` and `facies/test.csv`
* Define the S3 bucket as an environment variable (via `.env` in the project root, for instance)
* Run `d1-pull-dataset.ipynb` from the `scripts` dir

#### Penalty matrix

The penalty matrix file is provided in the repo.
