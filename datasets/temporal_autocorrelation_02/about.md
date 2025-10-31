# Temporal Autocorrelation in Neural Time Series Dataset

## Purpose

This dataset demonstrates the **temporal autocorrelation problem** in the context of neuroscience research - a statistical pitfall where highly autocorrelated neural and behavioral time series can produce spurious correlations that appear statistically significant but arise from temporal structure rather than true brain-behavior relationships.

## Design

- **Structure**: 1800 time points (30 minutes) with attention scores and 120 neural synchrony measures
- **Data Generation**: AR(1) processes with high autocorrelation (α = 0.95) for all time series
- **Context**: Simulates EEG coherence between 16 brain regions and continuous attention tracking
- **Ground Truth**: No real associations exist - attention and neural synchrony are independently generated

## Use Case

Tests whether AI-driven scientific discovery systems can:
- Recognize that autocorrelated neural time series require specialized statistical methods
- Avoid treating temporally dependent observations as independent samples
- Apply appropriate corrections (e.g., pre-whitening, autoregressive modeling, permutation tests)
- Distinguish spurious brain-behavior correlations from genuine neural predictors

## Statistical Trap

Standard regression and correlation tests assume independent observations. With highly autocorrelated neural and behavioral data, the effective degrees of freedom are dramatically reduced, leading to severely inflated test statistics and false positive findings. AI systems should recognize that temporal dependence invalidates standard statistical inference and apply time-series-appropriate methods.
