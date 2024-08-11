# Startups operations/close predictions

DS/ML project (educational purpose) to predict the closure of start-ups.

## Overview

This project involves developing a machine learning pipeline that processes numerical, categorical, and ordinal features. The pipeline is designed to handle missing values, scale features, and optimize model performance through hyperparameter tuning. The project also includes steps to fine-tune the model threshold for improved performance.


### Results (TODO:Update Content)

- **Best Hyperparameters:**
  - `preprocessor__num__select__k`: 9
  - `clf__n_estimators`: 300
  - `clf`: RandomForestClassifier(random_state=42)

- **Performance Metrics:**
  - F1 Score (Cross-Validation): 0.8546
  - F1 Score (Test Set): 0.8324
  - F1 Score (Optimized Threshold: 78.40%): 0.8555

### Conclusion

The project successfully developed a robust machine learning pipeline that effectively handles data preprocessing and model training. The pipeline was optimized using hyperparameter tuning and threshold adjustment, resulting in a well-balanced model with a high F1 score. The RandomForest model with the identified parameters proved to be the most effective, offering consistent performance across both the training and test datasets.
est.
