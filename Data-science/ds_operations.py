import pandas as pd  
import numpy as np 
import json
bands_df=pd.read_csv("datasets/bands-csv.csv")

#load json data
with open('datasets/users.json') as f:
    users_data =json.load(f)
users_df=pd.json_normalize(users_data)

#filling missing values with a placeholder
bands_df.fillna({
    "year": '2026',
    'industry_name_ANZSIC': "Undefined Industry",
    'value': 0
}, inplace=True)

#Convert string columns 'id', 'age' to integers
users_df['id'] = users_df['id'].astype(int)
users_df['age'] = users_df['age'].astype(int)

print("\nCleaned Bands Dataframe: ")
print(bands_df.head())

print("\nCleaned Users Dataframe: ")
print(users_df.head())
#BASIC ANALYSIS USING PANDAS
#Counting the occurances of each city in our dataset
user_age_count = users_df['city'].value_counts()
print(user_age_count)

#mean age of users
user_age_average = users_df['age'].mean().astype(int)
print(f"\n The average age of users is: {user_age_average}")

#BASIC TRANSFORMATION METHODS WITH NUMPY
# creating a numpy array from a dataframe column 'age'
ages=users_df['age'].to_numpy()
mean_age=np.mean(ages)
std_age=np.std(ages)

narmalized_age=(ages - mean_age)/std_age
print(f"\n The average age of users is: {mean_age} \n The standard Deviation of age: {std_age}")
print(narmalized_age[:10])# Displays the first 10 normalized ages

#Advanced data transformation
current_year =pd.Timestamp.now().year
bands_df['value']=current_year - (bands_df['year']).astype(int)
print(bands_df.head())

#categorize users into age groups
def age_group(age):
    if age < 20:
        return 'Teen'
    elif 20 <= age < 30:
        return 'Young Adult'
    elif 30 <= age < 50:
        return "Adult"
    else:
        return "senior"
users_df['Age Group'] = users_df['age'].apply(age_group)
print("\nUsers Dataframe with age group")
print(users_df.head())
print("{users_df}")






