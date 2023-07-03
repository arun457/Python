import tensorflow as tf
import numpy as np

# Check if the model file exists
import os.path
if not os.path.isfile('model.h5'):
    # Generate the training data
    train_numbers = np.arange(0, 100001).reshape(-1, 1)
    train_labels = np.mod(train_numbers, 2)

    # Define the model architecture
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(8, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(train_numbers, train_labels, epochs=100, verbose=0)

    # Save the model
    model.save('model.h5')
else:
    # Load the model from disk
    model = tf.keras.models.load_model('model.h5')

# Test the model
test_number = np.array([[2]], dtype=np.float32)
prediction = model.predict(test_number)

print(prediction)

# if prediction < 0.5:
#     print("The number is even")
# else:
#     print("The number is odd")
