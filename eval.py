import tensorflow as tf
import keras
import numpy as np

# Load the model
model = keras.models.load_model('/home/admin/Model_1_EfficientNetB0_with_fine-tuning.keras')

# Define the class names in the order they were in during training
class_names = ['excellent', 'overaged', 'underaged']

# File path of the image to test
image_path = '/home/admin/PyCamGUI/3.jpg'

image = keras.utils.load_img(image_path, target_size=(224, 224))
input_arr = keras.utils.img_to_array(image)
input_arr = np.array([input_arr])  # Convert single image to a batch.
predictions = model.predict(input_arr)

# Output the prediction probabilities
print(f"Prediction probabilities: {predictions[0]}")

# Determine the predicted class index
predicted_class_index = np.argmax(predictions[0])
predicted_class_name = class_names[predicted_class_index]

# Output the file name and the predicted class
print(f"Processing file: {image_path.split('/')[-1]}")  # Extracts and prints the file name
print(f"Predicted class index: {predicted_class_index}")
print(f"Predicted class name: {predicted_class_name}")



# Load an image file to test, resizing it to the required input size
#img = load_img(image_path, target_size=(224, 224))

# Convert the image to an array and add a batch dimension
#img_array = img_to_array(img)
#img_array = np.expand_dims(img_array, axis=0)  # model expects a batch of images

# Make a prediction
#predictions = model.predict(img_array)