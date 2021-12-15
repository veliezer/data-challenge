## General Description
This job receives the datasets & brings a few things:
- The top 10 best games for each console/company.
- The worst 10 games for each console/company.
- The top 10 best games for all consoles.
- The worst 10 games for all consoles.

## Prerequisities
To run this ETL Job, you need the next prerequisites:

- Pandas library
- Python 2.7+
- Docker Engine

## How to Run
- Clone repository
```sh
git clone https://github.com/veliezer/de-challenge.git
cd de-challenge/src/main
python3 main.py
cat ../../data/report-walmart.txt
```

## Deployment
- Clone repository
```sh
git clone https://github.com/veliezer/de-challenge.git
cd de-challenge
docker image build tag etljob:0.0.1 .
docker images
docker run etljob:0.0.1
```
