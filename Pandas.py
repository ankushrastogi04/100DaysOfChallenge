# Import pandas package
import pandas as pd

Define a dictionary containing employee data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
print(df[['Name']])

data=pd.read_csv("/Users/arastogi/Downloads/nba.csv", index_col ="Name")
#print(data)

first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]
print(first)
print(second)

# dictionary of lists
dict = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score': [90, 40, 80, 98]}

# creating a dataframe from a dictionary
df = pd.DataFrame(dict)

iterating over rows using iterrows() function
for i, j in df.iterrows():
    print(i, j)


lst=list(df)
print(lst)

for i in lst:
    print(df[i])
    print(df[i][2])