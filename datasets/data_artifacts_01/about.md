# Data Artifacts Problem Dataset

## Purpose

This dataset demonstrates the **data artifacts problem** - where technical issues during data collection create spurious correlations between independent variables.

## Design

- **Structure**: 21,600 time points with neural firing rates from two brain regions
- **Data Generation**: Two independent signals (10-20 Hz) with synchronized zero chunks
- **Ground Truth**: No real associations exist - signals are independently generated

## Use Case

Tests whether AI-driven scientific discovery systems can:
- Identify data quality issues and corrupted recording periods
- Recognize that correlations may result from technical artifacts
- Properly exclude problematic data segments before analysis
- Distinguish spurious correlations from genuine relationships

## Statistical Trap

When both signals drop to zero during the same periods (due to shared technical failures), they appear highly correlated despite being independent. AI systems should detect these anomalous patterns and recognize that findings may be artifacts rather than real phenomena.
