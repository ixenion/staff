


#first feature
weather = ['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overacst','Sunny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy']

#second feature
temp = ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']

#label or target variable
play = ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

#import LabelEncoder
from sklearn import preprocessing
#creating labelEncoder
le = preprocessing.LabelEncoder()
#converting string labels into numbers:
weather_encoded = le.fit_transform(weather)
temp_encoded = le.fit_transform(temp)
label = le.fit_transform(play)
print(f"weather: {weather}")
print(f"weather encoded: {weather_encoded}")
print(f"temp; {temp}")
print(f"temp encoded: {temp_encoded}")
print(f"play? {label}")

#combining weather and temp into single listof tuples
features = list(zip(weather_encoded, temp_encoded))

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)

#training the model using the training sets
model.fit(features, label)

#predict output
predicted = model.predict([[0,2]])#0:Overcast, 2:Mild
print(f"predicted: {predicted}")#1:play

