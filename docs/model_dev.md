# Model Development

![Model Development](/media/img/model_development.png)

## Data Acquisition

This project uses Universitas Pelita Harapan students data of academic year 2018/2019 with the permission from Information
Technology Directorate (ITD) department. There are three main raw datasets given:

* Online Admission (OA) datasets - contains students' admission data 
* OPCS datasets - contains GPA and CGPA information
* High School (HS) datasets - contains high school scores information

You can find all the raw data [here](/data/raw).

## Data Cleansing

Data cleansing process includes renaming columns to more familiar name, merging useful tables, uniting minor categories, 
feature extraction, pivot table, etc. The main point of data cleansing is to make each row represents one student and to
make the data make more sense when joined together.
For detailed process, you can refer to each of the following notebook:

* [OA cleansing](/notebooks/0.0-OA_data_cleansing.ipynb)
* [OPCS cleansing](/notebooks/0.1-OPCS_data_cleansing.ipynb)
* [HS cleansing](/notebooks/0.2-HS_data_cleansing.ipynb)

## Exploratory Data Analysis

[Exploratory Data Analaysis](https://en.wikipedia.org/wiki/Exploratory_data_analysis) (EDA) is done to see the main
characteristic of the features. Some visualizations are plotted to
make analysis easier. Here are several examples of what EDA can tell us about the data. 

* Distribution of Last CGPA

![eda1](/media/img/eda1.png)

* Major count

![eda2](/media/img/eda2.png)

* Finding out which faculty is more likely to fail

![eda3](/media/img/eda3.png)

Go [here](/notebooks/1.0-data_integration_EDA.ipynb) to see the integration between three datasets and complete EDA.

## Feature Selection

Before selecting features, target variable called `fail` is defined using `Last_CGPA` variable. If `Last_CGPA` is less than
2.00 then `fail` will be flagged `1`, otherwise it will be flagged as `0`. After this, unecessary features will be eliminated
to optimize model performance and to prevent data leakage. Selected features can be seen in the image below.

![Selected Features](/media/img/selected_features.png)

## Feature Transformation

This process includes encoding categorical variables. Label Encoder is used to encode categorical features.

### [Label Encoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)

Most of machine learning algorithms cannot take `string` as input. Therefore, all categorical variables must be encoded 
to `int` or `float` format to proceed. There are many encoding techniques, one of the most known is Label Encoder due to its
simplicity. It uses simple ordinal encoding scheme to encode the categorical variables into integer. 

You can see [this](/notebooks/2.0-model_development_feature_engineering.ipynb) to understand more on how to implement feature 
transformation with Python. 

## Train-Test Split

Before splitting the data into train and test set, features are then eliminated again from the last selected features shown 
above due to app simplicity reason and to remove [multicollinearity](https://en.wikipedia.org/wiki/Multicollinearity) between 
features. Final predictors used for model can be seen below, while the target remains `fail` column.

![Final Predictor](/media/img/final_predictor.png)

Then, the data is splitted **2/3 for training** and **1/3 for testing**.

## Model Training

Before training the model, imbalance resampling is performed using [`SMOTE`](https://imbalanced-learn.readthedocs.io/en/stable/generated/imblearn.over_sampling.SMOTE.html). 
The objective is to raise minority class, which is the `1` class so that the ratio between classes will be 50:50.

Next, we train the model using three different classifiers:

* [Logistic Regression](https://medium.com/analytics-vidhya/logistic-regression-b35d2801a29c) - default parameters
* [Random Forest Classifier](https://towardsdatascience.com/understanding-random-forest-58381e0602d2) - `max_depth` set to 3
* [Support Vector Classifier](https://medium.com/@ankitnitjsr13/math-behind-support-vector-machine-svm-5e7376d0ee4d) - default parameters

Check [this notebook](/notebooks/2.1-model_development_train.ipynb) to see more detailed process on training the model.

## Model Evaluation

After models are trained, performance of each model is evaluated using the test set. We chose `Logistic Regression` as it 
gives the best metrics compared to the other two models. 

In the image below you can see the `Logistic Regression` model metrics score for various probability cutoffs. It gives 
`accuracy` and `recall` around **68%** when the cutoff is 0.47. Not bad!

![cutoffs](/media/img/eval1.png)

We also provide the `Confusion Matrix` and `AUC-ROC Curve` for both train and test set below. The `AUC score` for train set is **0.73** while the test set gives **0.71**. Seems like the model is not overfitted, another good sign!

![CMs](/media/img/eval2.png)

If you want to see the performance of the other two models, check [here](/notebooks/2.2-model_development_evaluation.ipynb).

