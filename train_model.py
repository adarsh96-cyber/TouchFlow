import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# =========================
# Load Dataset
# =========================

data = pd.read_csv("gesture_data.csv", header=None)

# =========================
# Features and Labels
# =========================

X = data.iloc[:, :-1]

y = data.iloc[:, -1]

# =========================
# Split Dataset
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# Create KNN Model
# =========================

model = KNeighborsClassifier(n_neighbors=3)

# =========================
# Train Model
# =========================

model.fit(X_train, y_train)

# =========================
# Predict
# =========================

y_pred = model.predict(X_test)

# =========================
# Accuracy
# =========================

accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy * 100)

# =========================
# Save Model
# =========================

pickle.dump(model, open("gesture_model.pkl", "wb"))

print("Model Saved Successfully")