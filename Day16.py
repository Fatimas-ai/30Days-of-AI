import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Dataset
data = {
"Area":[1000,1200,1500,1800,2200],"Price":[50,60,75,90,110]

}
df = pd.DataFrame(data)
print(df)

# Features
X = df[["Area"]]
# Label
y = df["Price"]
# Split
X_train,X_test,y_train,y_test=train_test_split(
X,
y,
test_size=0.2,
random_state=42
)

# Create Model
model=LinearRegression()

# Train
model.fit(X_train,y_train)

# Prediction
prediction=model.predict(X_test)
print("Actual Price")
print(y_test.values)
print("Predicted Price")
print(prediction)

# New House
new_house=[[1700]]
price=model.predict(new_house)
print("Predicted Price of 1700 sq ft house")
print(price)



import pandas as pd
from sklearn.linear_model import LinearRegression
data={
    "hours":[1,2,3,4,5],
    "marks":[20,35,50,65,80]
}
df=pd.DataFrame(data)
x=df[["hours"]]
y=df[["marks"]]
model=LinearRegression()
model.fit(x,y)
prediction=model.predict([[6]])
print(prediction)
