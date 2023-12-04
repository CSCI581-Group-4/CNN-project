import tensorflow as tf

# Load dataset directly from tensorflow
data = tf.keras.datasets.mnist

# Separate into training data and test data
(training_pixels, training_labels), (test_pixels, test_labels) = data.load_data()
training_pixels = tf.keras.utils.normalize(training_pixels, axis=1)

# Create the CNN
cnn = tf.keras.models.Sequential()

# Add the input layer
cnn.add(tf.keras.layers.Conv2D(1, (14, 14), activation="sigmoid", input_shape=(28, 28, 1)))
cnn.add(tf.keras.layers.Conv2D(12, (7, 7), activation="sigmoid"))
cnn.add(tf.keras.layers.AveragePooling2D((3, 3)))
cnn.add(tf.keras.layers.Flatten())
cnn.add(tf.keras.layers.Dense(10, activation="softmax"))

# Generate an image of the CNN
tf.keras.utils.plot_model(cnn, to_file='cnn_model.png', show_shapes=True, show_layer_names=True)

# Compile the CNN
cnn.compile(
    optimizer="sgd", 
    loss="sparse_categorical_crossentropy", 
    metrics=["accuracy"]
)

# Train and save the CNN model
cnn.fit(training_pixels, training_labels, epochs=5)
cnn.save("kendal.model")
