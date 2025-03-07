

# EVALUATION OF VARIOUS ML ALGORITHMS FOR SPAM EMAIL DETECTION

import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.naive_bayes  import  MultinomialNB
from sklearn.linear_model import LogisticRegression 
from sklearn.svm import  SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier  
from sklearn.ensemble import GradientBoostingClassifier 
from xgboost  import  XGBClassifier
from sklearn.neural_network import MLPClassifier 
from sklearn.metrics  import  accuracy_score
 # Load the dataset
file_path = input("Enter the file path of the dataset containing email data: ") 
df =  pd.read_csv(file_path,  encoding='latin1')
 # Preprocess the dataset
df['spam'] = df['v1'].apply(lambda x: 1  if x ==  'spam' else 0) 
df['message']  =  df['v2']
df = df.drop(columns=['v1', 'v2', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'])
 # Balance the dataset  by sampling equal number of spam and ham emails 
df_spam =  df[df['spam']  ==  1]
df_ham = df[df['spam'] == 0].sample(df_spam.shape[0]) 
df =  pd.concat([df_ham,  df_spam])
 # Split  the dataset into training and testing  sets
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['spam'], test_size=0.2, 
random_state=42)
 #  Vectorize the text  data  
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train) 
X_test_vec = vectorizer.transform(X_test)
# List of models to evaluate 
models =  {
 'Naive Bayes': MultinomialNB(),
 'Logistic Regression': LogisticRegression(max_iter=1000), 
 'SVM':  SVC(kernel='linear'),
 'Decision Tree': DecisionTreeClassifier(),  
 'Random Forest': RandomForestClassifier(),  
 'Gradient Boosting': GradientBoostingClassifier(), 
 'XGBoost':  XGBClassifier(),
 'Neural Network': MLPClassifier(hidden_layer_sizes=(100,), max_iter=500)
 }
 # Dictionary to store accuracy results 
accuracy_results =  {}
 # Train and evaluate each model
for model_name, model in models.items(): 
    model.fit(X_train_vec,  y_train)
    y_pred =  model.predict(X_test_vec)  
    accuracy = accuracy_score(y_test, y_pred) 
    accuracy_results[model_name] = accuracy
    print(f"{model_name}: Accuracy = {accuracy:.4f}")
 # Identify the most  efficient  algorithm
most_efficient_algorithm = max(accuracy_results, key=accuracy_results.get)  
print(f"The most  efficient  algorithm is {most_efficient_algorithm} with an accuracy of {accuracy_results[most_efficient_algorithm]:.4f}.")


# EMAIL SPAM DETECTION USING NAIVE BAYES WITH TF-IDF


import numpy as np 
import pandas as pd
from sklearn.feature_extraction.text  import  TfidfVectorizer 
from sklearn.naive_bayes  import  MultinomialNB
from sklearn.pipeline import  Pipeline
 # Load the dataset
file_path =  input("Enter the  file path of the dataset containing email data: ") 
df =  pd.read_csv(file_path,  encoding='latin1')
 # Preprocess the dataset
df['spam'] = df['v1'].apply(lambda x: 1 if x == 'spam' else 0) 
df['message']  =  df['v2']
df = df.drop(columns=['v1', 'v2', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'])
 # Balance the dataset  by sampling equal number of spam and ham emails 
df_spam =  df[df['spam']  ==  1]
df_ham = df[df['spam'] == 0].sample(df_spam.shape[0]) 
df =  pd.concat([df_ham,  df_spam])
 # Split  the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['spam'], test_size=0.2, 
random_state=42)
 # Create a pipeline with TF-IDF vectorizer and Naive Bayes classifier 
model =  Pipeline([
 ('tfidf',  TfidfVectorizer()),  
('naive_bayes', MultinomialNB())
 ])
 #  Train the  model  
model.fit(X_train, y_train)
 # Predict whether a user input message is spam or not 
while True:
    user_input  = input("Enter a message to  check  if it's spam or not (or type  'exit' to quit): ") 
    if user_input.lower()  ==  'exit':
        break 
    else:
        prediction = model.predict([user_input]) 
        if prediction[0]  ==  1:
            print("The message is predicted as spam.") 
        else:
            print("The message is predicted as not spam.")


# In[ ]:




