import pandas as pd 

#simple dataframe
data={
    'Name':["Joel","Eliton",None,"Afod"],
    'Age':[18, None, 23, 24],
    'Salary':[1800, 2400, None, 200004],
    'City':["Kla",'Mkn','Jja',None]
}
df_missing=pd.DataFrame(data)
ds=pd.Series(data)
print(ds['Salary'][1])
#display the missing values in the dataframe

# print(df_missing)

#drop rows with missing values
df_dropped = df_missing.dropna()
print(df_dropped)

#filling missing values
df_filled = df_missing.fillna({
    'Name': "Unknown",
    'Age': int(df_missing['Age'].mean()),
    'Salary': 0,
    'City':'Kampala'
})
# print(df_filled)

#Filtering
filtered_df=df_filled[df_filled['Age'] > 22.5]
# city_df=filtered_df[filtered_df["City"] == "Uknown"]
# print(city_df)

#Data Grouping

#Group by 'City' and calculate the mean age of each city
# group_df=df_filled.groupby('City')['Salary'].mean()
# print(group_df)