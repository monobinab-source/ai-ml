# Bank Marketing Campaign: Classifier Comparison and Insights

## Overview

This project explores and compares various machine learning classifiers to predict customer responses to term deposit marketing campaigns, using the UCI Bank Marketing dataset. The goal is to identify the most effective model for predicting whether a client will subscribe to a term deposit, using both customer and macroeconomic features.

## Dataset

- **Source:** [UCI Machine Learning Repository: Bank Marketing Data Set](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)
- **Size:** 41,188 records, 22 features (bank client data, last contact, campaign info, and macroeconomic indicators)

## Models Compared

- Logistic Regression
- K Nearest Neighbors (KNN)
- Decision Tree
- Support Vector Machine (SVM)

## Feature Engineering

- Encoded categorical variables using both one-hot and ordinal encoding.
- Checked for missing values and imputed or removed as appropriate.
- Created engineered features such as “was previously contacted.”
- Explored and addressed potential data leakage (e.g., with duration feature).

## Key Findings

### Model Results

| Model                | Test Accuracy | Test F1 (class "yes") | Precision (class "yes") | Recall (class "yes") |
|----------------------|--------------|-----------------------|-------------------------|----------------------|
| **Decision Tree**    | **0.91**     | **0.61**              | 0.62                    | **0.59**             |
| Logistic Regression  | 0.91         | 0.51                  | 0.70                    | 0.40                 |
| SVM                  | 0.91         | 0.52                  | 0.65                    | 0.43                 |
| KNN                  | 0.90         | 0.48                  | 0.56                    | 0.43                 |

- **Decision Tree** achieved the highest F1-score and recall for predicting "yes" (term deposit subscriber), making it the preferred model if recall is the business priority.
- All models demonstrated high accuracy due to the class imbalance (majority “no”), but F1-score and recall reveal true effectiveness for the minority class.

### Feature Importance

- **duration** (call duration) and several macroeconomic indicators (e.g., employment variation rate, number of employees) are the most predictive features.
- **Warning:** The `duration` feature may introduce data leakage if used for real-time prediction, as it is only known after a call completes.
- Other features, such as previous contact history and consumer confidence, also contributed to model performance.

### Error Analysis

- For the chosen Decision Tree, the model achieved perfect recall for "yes" (no false negatives) but with low precision (many false positives).
- Adjusting the probability threshold did not improve the precision-recall tradeoff, as the predicted probabilities from the shallow decision tree were not well-calibrated.

### Recommendations

- Consider removing or carefully handling the `duration` feature for real-world deployment.
- Explore class weighting, oversampling, or ensemble methods (like Random Forests) to further improve precision and recall.
- Implement a feedback loop in production to continuously learn from new customer responses and update the model.
- Monitor macroeconomic indicators closely, as they significantly affect campaign outcomes.

## How to Reproduce

1. Clone this repository.
2. Install dependencies from `requirements.txt`.
3. Run the provided Jupyter notebooks or Python scripts for feature engineering, training, evaluation, and analysis.

## License

MIT License

---


