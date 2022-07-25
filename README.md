# Pricing_options_with_ANNs

## Table of Contents
- About
- Dataset creations
- Model investigations
- Model initialisation
- Model Analysis
- Web application for option pricing via my models

## About

This repository contains the source code for my research paper titled 'Neural Network Models for Pricing Call and Put Options Simultaneously', where I investigate the ability of ANNs to approximate call and put option prices/valuations under two classical option pricing models. The Black-Scholes model and the Heston model under the Monte Carlo solving method.

ANN-1 is an ANN which predicts call and put option prices under the Black-Scholes model.

ANN-2 is an ANN which predicts call option prices under the Black-Scholes model.

ANN-3 is an ANN which predicts put option prices under the Black-Scholes model.

ANN-4 is an ANN which predicts call and put option prices under the Heston Monte Carlo model.

## Dataset creations

All ANNs were trained and tested on synthetic data. 

The dataset used to train ANN-1, ANN-2 and ANN-3 is created in the /BS_data_generation directory. The full dataset was created by using Latin Hypercube Sampling to generate the Black-Scholes inputs, then these inputs were passed to the Black-Scholes model to get the call and put prices. The Black-Scholes pricing model is in the /option_pricing_formulas.py file and the notebook /black_scholes_data_creation.ipynb contains the code used to create and save the dataset. The complete dataset is too large to upload, however the out-of-sample dataset used for testing was uploaded in /out_of_sample_bs_data.csv.

## Model investigations


## Model Analysis

## Web application for opting pricing via my models
