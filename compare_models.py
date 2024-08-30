from tflite_runtime.interpreter import Interpreter 
from PIL import Image
import numpy as np
import time
import os
import pandas as pd



def load_model(model_path):
    
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
        classification_time = np.round(time2-time1, 10)
        print("Classificaiton Time =", classification_time, "seconds.")

        # Read class labels.
        labels = load_labels(label_path)

        # Return the classification label of the image.
        classification_label = labels[label_id]
        print("Image Label is :", classification_label, ", with Accuracy :", np.round(prob*100, 2), "%.")

        return (classification_label, prob, 2, classification_time)

    interpreter = Interpreter(model_path)
    print("Model Loaded Successfully.")
    interpreter.allocate_tensors()
    output_details = interpreter.get_output_details()

    collected_time = []
    collected_pred = []
    collected_probability = []
    collected_class = []

    for klass in load_labels(label_path):
        image_folder = data_folder + klass
        image_list = os.listdir(image_folder)
        for image in image_list:
            pred_label,probability,used_time=classify(image_folder + "/" +image)
            #put time in a buffer and average later
            collected_time.append(used_time)
            collected_pred.append(pred_label)
            collected_probability.append(probability)
            collected_class.append(klass)

    return (collected_time,collected_pred,collected_probability,klass)

data_folder = "/home/admin/test_data/"
model_dir = "/home/admin/models/"
label_path = "/home/admin/PyCamGUI/classes2.txt"

dir_list = os.listdir(model_dir)

res_model = []
res_time = []

for model in dir_list:
    model_path = model_dir+model
    res_model.append(model)
    used_time,predictions,probability,klass = load_model(model_path)
    mean = 0
    for a in used_time:
        mean = mean + a
    res_time.append(mean/len(used_time))
    each_res = {"Model":model, "class":klass,"predictions": predictions, "probability":probability, "time":used_time}
    df = pd.DataFrame(each_res)
    df.to_csv(model+".csv")

result = {"Model":res_model, "Mean time": res_time}
df = pd.DataFrame(result)
df.to_csv("res.csv")