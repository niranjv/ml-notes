## Data Preprocessing
When features have different units and scales, create features that have similar ranges so we don't overweight a feature only because of its scale. Need to normalize/standardize all feature, not just a subset. Standardization may be more important than normalization for most algorithms.
* Standardize - subtract mean & scale to unit variance from each feature independently. Does not bound data (like normalization).
* Normalization - scale all numeric features to [0,1]. Loses info about outliers in data.
