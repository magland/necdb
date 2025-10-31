# NecDB - Negative Control Database for Benchmarking the AI Scientist

A collection of datasets designed to evaluate the performance of AI-driven scientific discovery systems in their ability to not find false positive associations.

Each dataset is a directory of the form `datasets/<dataset_name>` and contains a single `generate.py` script that produces a `dataset.zip` file that gets hosted on the GitHub pages site for this repository. The ZIP file contains the generated data files and a README.md file describing the dataset.

An example of how to run a test:

Upload one of the negative control datasets to ChatGPT with the prompt:

> I have attached a dataset. Please analyze this dataset and produce a pdf report with your findings. Report any significant findings, but be careful not to make unsupported claims.
