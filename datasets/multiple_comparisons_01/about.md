# Multiple Comparisons Problem Dataset

## Purpose

This dataset demonstrates the **multiple comparisons problem** (also known as the multiple testing problem) - a fundamental statistical pitfall where testing many hypotheses simultaneously increases the likelihood of finding false positive associations purely by chance.

## Design

- **Structure**: 500 participants, 100 random health variables tested against tomato consumption
- **Expected Result**: ~5% of variables will show "significant" correlations (p < 0.05) by chance alone
- **Ground Truth**: No real associations exist - all data is randomly generated

## Use Case

Tests whether AI-driven scientific discovery systems can:
- Recognize spurious correlations from multiple testing
- Apply appropriate statistical corrections (e.g., Bonferroni, FDR)
- Avoid reporting false positive findings as discoveries
- Distinguish between exploratory and confirmatory analysis

## Statistical Trap

With a significance threshold of p < 0.05 and 100 independent tests, we expect ~5 false positives even when no true associations exist. AI systems should either correct for multiple comparisons or acknowledge the exploratory nature of the findings.
