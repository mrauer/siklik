# Sīklik

**Sīklik** is a small software designed to identify cyclic continuous positive variations over a large quantity of stock.

Current Version **0.1**

## Objective

The objective is to identify the subset of stocks that have had a large number of cyclic continuous positive variations over different steps, and % growth to guarantee diversification. A $1,000 target per asset can be build as portfolio. It will eventually be possible to build a model using these attributes in the future. The number of cycles and the growth rate will be a way to process the data in a higher dimension, and adding a layer of machine learning on top this summarized data should be a way to pseudo-predict the risk or at least weigh it.

## Outline

In a nutshell, the sofware will perform the following tasks:
* Call the api.iextrading.com against a static list of stocks.
* Store **date** and **close** in memory.
* For each stock, and for an increasing value **step**, compute the number of continuous positive variations **cycles**, and store the average increase as well **changeOverCycle**. (ex: for a step 30, if the number of cycles is 8, and the changeOverCycle value is 4.34%, then the stock has had a monthly continuous growth of 4.34% for 8 months)

## How to run it?
    python main.py '{"action":"update"}'

## API endpoint sample

[https://api.iextrading.com/1.0/stock/aapl/batch?types=quote,news,chart&range=1m&last=10](https://api.iextrading.com/1.0/stock/aapl/batch?types=quote,news,chart&range=1m&last=10)

## Technology

The first version V1.0 can be all built in Python 2.7.

## Timeline

* V1.0 should be deployed by 6/24.

## Versions

#### 0.1
* Virtualenv
* API key/initial call
* Module structure

#### 1.0
* Scale to 1K+ stocks
* Workable output

## Further development
* Predicting model
* Automation
* Python 3
