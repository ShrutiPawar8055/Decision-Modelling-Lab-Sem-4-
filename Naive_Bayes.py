import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import CategoricalNB

# -------------------- TASK 1: Student Performance --------------------

data = [
["Low","Poor","Low","Low","Fail"],
["Low","Poor","High","Low","Fail"],
["Low","Good","Low","Low","Pass"],
["Medium","Good","Low","Low","Pass"],
["Medium","Good","High","High","Pass"],
["High","Good","High","High","Distinction"],
["High","Good","Low","High","Distinction"],
["High","Poor","High","High","Pass"],
["Medium","Poor","Low","Low","Fail"],
["Medium","Good","High","Low","Pass"],
["High","Good","High","Low","Distinction"],
["Low","Good","High","High","Pass"],
["Low","Poor","Low","High","Fail"],
["Medium","Good","Low","High","Pass"],
["High","Good","High","High","Distinction"],
["Medium","Poor","High","Low","Fail"],
["Low","Good","Low","Low","Pass"],
["High","Poor","Low","High","Pass"],
["Medium","Good","High","High","Distinction"],
["Low","Poor","High","Low","Fail"],
["High","Good","Low","Low","Pass"],
["Medium","Good","Low","Low","Pass"],
["High","Good","High","High","Distinction"],
["Low","Poor","Low","Low","Fail"],
["Medium","Poor","High","High","Pass"],
["High","Good","High","Low","Distinction"],
["Low","Good","High","Low","Pass"],
["Medium","Good","Low","High","Pass"],
["High","Poor","High","Low","Pass"],
["Medium","Good","High","High","Distinction"]
]

cols = ["StudyTime","Attendance","ParentalSupport","PreviousGrade","Performance"]
df = pd.DataFrame(data, columns=cols)

enc = {}
for c in df.columns:
    le = LabelEncoder()
    df[c] = le.fit_transform(df[c])
    enc[c] = le

X = df.drop("Performance", axis=1)
y = df["Performance"]

model1 = CategoricalNB()
model1.fit(X, y)

sample1 = pd.DataFrame([{
    "StudyTime":"High",
    "Attendance":"Good",
    "ParentalSupport":"High",
    "PreviousGrade":"High"
}])

for c in sample1.columns:
    sample1[c] = enc[c].transform(sample1[c])

pred1 = model1.predict(sample1)
print("Student Prediction:", enc["Performance"].inverse_transform(pred1)[0])


# -------------------- TASK 2: Medical Diagnosis --------------------

data2 = [
["Yes","Yes","Positive","Disease"],
["Yes","No","Positive","Disease"],
["No","Yes","Positive","Disease"],
["No","No","Negative","NoDisease"],
["Yes","Yes","Negative","Disease"],
["No","Yes","Negative","NoDisease"],
["Yes","No","Negative","NoDisease"],
["No","No","Positive","NoDisease"]
]

cols2 = ["Symptom","Fever","Test","Result"]
df2 = pd.DataFrame(data2, columns=cols2)

enc2 = {}
for c in df2.columns:
    le = LabelEncoder()
    df2[c] = le.fit_transform(df2[c])
    enc2[c] = le

X2 = df2.drop("Result", axis=1)
y2 = df2["Result"]

model2 = CategoricalNB()
model2.fit(X2, y2)

sample2 = pd.DataFrame([{
    "Symptom":"Yes",
    "Fever":"Yes",
    "Test":"Positive"
}])

for c in sample2.columns:
    sample2[c] = enc2[c].transform(sample2[c])

pred2 = model2.predict(sample2)
print("Medical Diagnosis:", enc2["Result"].inverse_transform(pred2)[0])


# -------------------- TASK 3: Car Starting Problem --------------------

data3 = [
["Good","Full","Start"],
["Good","Empty","NoStart"],
["Bad","Full","NoStart"],
["Bad","Empty","NoStart"],
["Good","Full","Start"],
["Bad","Full","NoStart"],
["Good","Empty","NoStart"],
["Good","Full","Start"]
]

cols3 = ["Battery","Fuel","Start"]
df3 = pd.DataFrame(data3, columns=cols3)

enc3 = {}
for c in df3.columns:
    le = LabelEncoder()
    df3[c] = le.fit_transform(df3[c])
    enc3[c] = le

X3 = df3.drop("Start", axis=1)
y3 = df3["Start"]

model3 = CategoricalNB()
model3.fit(X3, y3)

sample3 = pd.DataFrame([{
    "Battery":"Good",
    "Fuel":"Full"
}])

for c in sample3.columns:
    sample3[c] = enc3[c].transform(sample3[c])

pred3 = model3.predict(sample3)
print("Car Start Prediction:", enc3["Start"].inverse_transform(pred3)[0])



import networkx as nx
import matplotlib.pyplot as plt


# ----------- STUDENT NETWORK -----------
G1 = nx.DiGraph()

G1.add_edges_from([
    ("StudyTime","Performance"),
    ("Attendance","Performance"),
    ("ParentalSupport","Performance"),
    ("PreviousGrade","Performance")
])

plt.figure()
nx.draw(G1, with_labels=True, node_size=3000)
plt.title("Student Performance Bayesian Network")
plt.show()


# ----------- MEDICAL NETWORK -----------
G2 = nx.DiGraph()

G2.add_edges_from([
    ("Disease","Symptom"),
    ("Disease","Fever"),
    ("Disease","Test")
])

plt.figure()
nx.draw(G2, with_labels=True, node_size=3000)
plt.title("Medical Diagnosis Bayesian Network")
plt.show()


# ----------- CAR NETWORK -----------
G3 = nx.DiGraph()

G3.add_edges_from([
    ("Battery","Start"),
    ("Fuel","Start")
])

plt.figure()
nx.draw(G3, with_labels=True, node_size=3000)
plt.title("Car Starting Bayesian Network")
plt.show()