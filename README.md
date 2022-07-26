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

The dataset used to train ANN-4 is created in the /Heston_data_generation directory. The full dataset was created by using Latin Hypercube Sampling to generate the Heston model inputs, then these inputs were passed to the Black-Scholes model to get the call and put prices. The Heston pricing model is in the /monte_carlo_class.py fileand the notebook /monte_carlo_data_creation.ipynb contains the code used to create and save the dataset. Similarly to the Black-Scholes dataset, the Heston dataset could not be uploaded because it is too large.

## Model investigations

Each ANN had a hyperparameter tuning stage to find the optimal model infrastructure. To find the steps carried out for hyperparameter tuning, navigate to the directory of the ANN of interest and inspect the /ANN_*_investigation file. Once the optimal model infrastucture is found, the models are trained and saved in the /ANN_*_initialisation file.

## Model Analysis

The accuracy and speed comparison for ANN-1 against ANN-2 & ANN-3 and the Black-Scholes model is in the '/ANN-1 vs ANN-2 & ANN-3 Analysis' directory.

The accuracy and speed comparison for ANN-4 against the Heston Monte Carlo model is in the '/ANN-4 Analysis' directory.

## Web application for opting pricing via my models

To interact and compare the pricings of the models made in my paper, please go to: https://ann-option-pricing-kn5a2j4j5a-nw.a.run.app

