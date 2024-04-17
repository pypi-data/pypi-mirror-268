# Flexible Classifier Pipeline

This repository contains a flexible classifier pipeline that can be used to train and evaluate classification models on various datasets. The pipeline is designed to be versatile and easily adaptable to different datasets and classification tasks.

## Overview

1. **Data Preprocessing**: The pipeline preprocesses the input data, handling missing values, scaling numerical features and encoding categorical features as necessary.
2. **Classification Model**: The function employs a neural network featuring multiple hidden layers, batch normalization, and dropout regularization as components within the pipeline.
3. **Validation**: The pipeline utilizes validation data to assess the model's performance on the provided dataset. This process aids in evaluating the model's generalization capabilities and mitigating overfitting.

## Usage

1. **Prepare Your Data**: Ensure that your data is in a suitable format for classification tasks. 
2. **Import the Pipeline**: Import function `process_data` which contains  preprocessing steps and the classification model.
3. **Train and Evaluate the Model**: Pass your data to the pipeline's function along with the target variable (i.e., the label to be predicted).
4. **Interpret the Results**: The pipeline will determine the validation accuracy of the model. Use this metric to assess the performance of the model on your dataset.
5. **Use generated pipeline for predictions**: Function will return generated pipeline.

## Example Usage

You can pass path to dataset with column name to classify.

```python=
from flexible_classifier import classifier

pipeline = classifier.process_data('data.csv', 'class')
```

Or pandas DataFrame.

```python=
import pandas as pd
from flexible_classifier import classifier

df1 = pd.read_csv('train.csv')
df2 = pd.read_csv('test.csv')
df = pd.concat([df1, df2])

classifier.process_data(df, 'class')
```