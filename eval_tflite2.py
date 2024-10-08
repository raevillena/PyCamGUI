from tflite_runtime.interpreter import Interpreter 
import numpy as np
from PIL import Image
import time


def load_labels(path): # Read the labels from the text file as a Python list.
  with open(path, 'r') as f:
    return [line.strip() for i, line in enumerate(f.readlines())]
  
def set_input_tensor(interpreter, image):
  tensor_index = interpreter.get_input_details()[0]['index']
  input_tensor = interpreter.tensor(tensor_index)()[0]
  input_tensor[:, :] = image


def classify_image(interpreter, image, top_k=1):
  #interpreter.set_tensor(input_tensor, image)
  set_input_tensor(interpreter, image)

  interpreter.invoke()
  output = np.squeeze(interpreter.get_tensor(output_details[0]['index']))
  #output_data = interpreter.get_tensor(output_details[0]['index'])

  #scale, zero_point = output_details['quantization']
  #output = scale * (output - zero_point)

  ordered = np.argpartition(-output, 1)
  return [(i, output[i]) for i in ordered[:top_k]][0]

data_folder = "/home/admin/PyCamGUI/"

model_path = '/home/admin/Model_1_EfficientNetB0_with_fine-tuning.tflite'
label_path = data_folder + "classes.txt"

interpreter = Interpreter(model_path)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

_,height,width,_ = input_details[0]['shape']

image = Image.open(data_folder + "3.jpg").convert('RGB').resize((width, height))

# Classify the image.
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