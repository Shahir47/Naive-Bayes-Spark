# Naive-Bayes-Spark

In this program I built a Naive Bayes classifier from scratch using Map Reduce in Spark. Map Reduce allows faster training with parallel processing of the data.

The dataset is called Cyberbullying tweets. This dataset classifies cyberbullying into six categories based on texts from twitter. The categories are:

1. not_cyberbullying
2. gender (target bullying)
3. religion
4. other_cyberbullying
5. age
6. ethnicity

The model will predict where a tweet falls among the above six categories. The accuracy of the model is 70% which is close to the accuracy obtained from Scikit-learn's built-in Naive Byes model (74%).

In order to preprocess the dataset the `dataset.py` is used.

To run the program in a Apache Spark environment (Databricks) simply import the Import the `main.ipnyb` along with the dataset. Adjust the dataset directory. And you are good to go.