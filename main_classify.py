from tflite_runtime.interpreter import Interpreter 
from PIL import Image
import numpy as np
import time


def load_labels(path): # Read the labels from the text file as a Python list.
    with open(path, 'r') as f:
        return [line.strip() for i, line in enumerate(f.readlines())]

def set_input_tensor(interpreter, image):
    tensor_index = interpreter.get_input_details()[0]['index']
    input_tensor = interpreter.tensor(tensor_index)()[0]
    input_tensor[:, :] = image

def classify_image(interpreter, image, top_k=1):
    set_input_tensor(interpreter, image)

    interpreter.invoke()
    output = np.squeeze(interpreter.get_tensor(output_details[0]['index']))

    ordered = np.argpartition(-output, 1)
    return [(i, output[i]) for i in ordered[:top_k]][0]

def classify(image_path):
    image = Image.open(image_path).convert('RGB').resize((224, 224))
    time1 = time.time()
    label_id, prob = classify_image(interpreter, image)
    time2 = time.time()
    classification_time = np.round(time2-time1, 3)
    print("Classificaiton Time =", classification_time, "seconds.")

    # Read class labels.
    labels = load_labels(label_path)

    # Return the classification label of the image.
    classification_label = labels[label_id]
    print("Image Label is :", classification_label, ", with Accuracy :", np.round(prob*100, 2), "%.")

    return (classification_label, np.round(prob*100, 2))

data_folder = "/home/admin/PyCamGUI/"
model_path = '/home/admin/Model_1_EfficientNetB0_with_fine-tuning.tflite'
label_path = data_folder + "classes.txt"

interpreter = Interpreter(model_path)
print("Model Loaded Successfully.")

interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

interpreter.allocate_tensors()
_, height, width, _ = interpreter.get_input_details()[0]['shape']

