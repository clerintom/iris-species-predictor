
import pandas as pd
import pickle

from sklearn.linear_model import LogisticRegression


df=pd.read_excel(r"iris.xls")
print(df.head())

from sklearn.model_selection import train_test_split
x=df.drop(['Classification'],axis=1) #Splitting the data set into target and features
y=pd.DataFrame(df['Classification'])
#print(y)

# Spliting the dataset for training and testing
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.3)
#print(x_train)

classifier = LogisticRegression()
classifier.fit(x_train, y_train)

#saving model to disk

pickle.dump(classifier,open('model.pkl','wb'))


