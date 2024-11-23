import pandas
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib
import datetime

df = pandas.read_csv("Output.csv")
#print(df.head)

X = df.drop(columns=["image_path", "label"])
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


k = 3
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"accuracy: {accuracy * 100: .2f}%")


counts = y.value_counts()
idle_count = counts[0]
bad_count = counts[1]
good_count = counts[2]

print(idle_count, bad_count, good_count)

now = datetime.datetime.now()
formatted_date = now.strftime("%Y-%m-%d_%H_%M_%S")
filename = f"KNN_model_{formatted_date}_{idle_count}_idle_{bad_count}_bad_{good_count}_good_{y.shape[0]}_images.joblib"

print(filename)

#joblib.dump(model, filename)