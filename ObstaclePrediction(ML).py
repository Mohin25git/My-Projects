# -------------------------------
# Chapter 1: Import our tools
# -------------------------------
import numpy as np        # for creating synthetic sensor data
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# -------------------------------
# Chapter 2: Create our dataset
# -------------------------------
# Features: front_distance, left_distance, right_distance, speed, angle
# Label: 0 = no obstacle, 1 = obstacle

# Let's create 100 sample points
np.random.seed(42)  # for reproducibility

n_samples = 100

# Front distance in cm (simulate close/far obstacles)
front_distance = np.random.randint(5, 100, size=n_samples)

# Left & right distances in cm
left_distance = np.random.randint(5, 100, size=n_samples)
right_distance = np.random.randint(5, 100, size=n_samples)

# Speed in arbitrary units (1-15)
speed = np.random.randint(1, 16, size=n_samples)

# Steering angle (-30 left to +30 right)
angle = np.random.randint(-30, 31, size=n_samples)

# Stack features together
X = np.column_stack((front_distance, left_distance, right_distance, speed, angle))

# -------------------------------
# Chapter 3: Create labels
# -------------------------------
# Rule: if front distance < 15 cm, obstacle = 1, else 0
y = (front_distance < 15).astype(int)

# -------------------------------
# Chapter 4: Split dataset
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -------------------------------
# Chapter 5: Train Decision Tree
# -------------------------------
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# -------------------------------
# Chapter 6: Test & evaluate
# -------------------------------
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy*100:.2f}%")

# -------------------------------
# Chapter 7: Predict new input
# -------------------------------
# Imagine the robot senses these values
new_input = np.array([[12, 30, 25, 8, 0]])  # front_distance=12cm, left=30, right=25, speed=8, angle=0
prediction = model.predict(new_input)

if prediction[0] == 1:
    print("⚠️ Obstacle detected ahead!")
else:
    print("✅ Path is clear.")
