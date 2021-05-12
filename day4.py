data=pd.read_csv("//Users/arastogi/Downloads/Ex_Files_Pandas_EssT/ExerciseFiles/data/olympics.csv",skiprows=4)
df=pd.DataFrame(data)
#1:
jo=df[df.Athlete == 'OWENS, Jesse']
print(jo.Event.value_counts())
#2:
sb=df[(df.Gender=='Men') & (df.Sport=='Badminton' ) & (df.Event=='singles' )]
print(sb.sort_values(by='Athlete').to_string())
#3:
lg=df[df.Edition >=1984 ]
print(lg.NOC.value_counts().head(3))
#4:
sb=df[(df.Gender=='Men') & (df.Medal=='Gold' ) & (df.Event=='100m' )]
print(sb.sort_values(by='Edition',ascending=False)[['City', 'Edition','Athlete', 'NOC']].to_string())

# creating charts using matplotlib library
import matplotlib.pyplot as plt
#%matplotlib inline

data=pd.read_csv("//Users/arastogi/Downloads/Ex_Files_Pandas_EssT/ExerciseFiles/data/olympics.csv",skiprows=4)
df=pd.DataFrame(data)
s=df[df.Edition == 1896]
s.Sport.value_counts().plot(kind='bar',figsize=(12,4),colormap='Pastel1')
plt.show()


#seaborn plotting

