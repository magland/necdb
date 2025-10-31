# Temporal Autocorrelation Problem Dataset

## Purpose

This dataset demonstrates the **temporal autocorrelation problem** - a statistical pitfall in time series analysis where autocorrelated data can produce spurious correlations that appear statistically significant but arise from the temporal structure rather than true causal relationships.

## Design

- **Structure**: 600 time points with target variable and 20 predictor variables
- **Data Generation**: AR(1) processes with high autocorrelation coefficients
- **Ground Truth**: No real associations exist - variables are independently generated random walks

## Use Case

Tests whether AI-driven scientific discovery systems can:
- Recognize that autocorrelated time series require specialized statistical methods
- Avoid treating autocorrelated observations as independent
- Apply appropriate corrections (e.g., pre-whitening, GLS, time series models)
- Distinguish spurious temporal patterns from genuine relationships

## Statistical Trap

Standard correlation tests assume independent observations. With autocorrelated data, the effective sample size is much smaller than the number of observations, leading to inflated test statistics and false positives. AI systems should account for temporal dependence in their analysis.
