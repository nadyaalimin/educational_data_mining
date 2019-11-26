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
make analysis easier. Here are several examples of EDA results. 

* Distribution of Last CGPA

![eda1](/media/img/eda1.png)

* Major count

![eda2](/media/img/eda2.png)

* Finding out which faculty is more likely to fail

![eda3](/media/img/eda3.png)

Go [here](/notebooks/1.0-data_integration_EDA.ipynb) to see the integration between three datasets and complete EDA.

## Feature Selection



## Feature Transformation

This process includes scaling numerical variables and encoding categorical variables. Label Encoder is used to encode
categorical features and Standard Scaler is used to scale numerical variables.

### [Label Encoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)

Most of machine learning algorithm cannot take `string` as input. Therefore, all categorical variables must be encoded to 
`int` or `float` format to proceed. There are many encoding techniques, one of the most simple is Label Encoder. It uses 
simple ordinal encoding scheme to encode the categorical variables into integer. 

### [Standard Scaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)

Standardization is a common requirement for many machine learning algorithm. The model might perform badly if the scale of 
numerical features are so much different from one another. Standard Scaler is one of the most popular and powerful scaler.
It uses the following equation to scale a feature:

![SS](/media/img/ss.png)

## Train-Test Split



## Model Training



## Model Evaluation



