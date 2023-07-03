from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Define the dataset
numbers = list(range(1, 10000001))
labels = [num % 2 == 0 for num in numbers]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(numbers, labels, test_size=0.2, random_state=42)

# Reshape the features to fit the model's input requirements
X_train = [[num] for num in X_train]
X_test = [[num] for num in X_test]

# Create a logistic regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
