import cv2 
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import os

mnist = tf.keras.datasets.mnist

if not os.path.exists('digit.keras'): # if the model does exist, make it

    # x = the image, y = the label (what number the image is)
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # Normalize the data
    x_train = tf.keras.utils.normalize(x_train, axis=1) # noralising here means that the values are between 0 and 1 
    x_test = tf.keras.utils.normalize(x_test, axis=1) # (in this case, the values of the pixel brightness are between 0 and 255)


    # Create the model
    model = tf.keras.models.Sequential() # basic model
    model.add(tf.keras.layers.Flatten(input_shape=(28, 28))) # "translates" the 28x28 image into a 1 dimensional array
    model.add(tf.keras.layers.Dense(128, activation='relu')) # 128 neurons, rectified linear unit activation function => res = max(0, x)
    model.add(tf.keras.layers.Dense(128, activation='relu'))
    model.add(tf.keras.layers.Dense(10, activation='softmax')) # 10 neurons (10 possible output numbers), softmax activation function => returns a probability distribution (sum of all neurons = 1)

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy']) # adam optimizer, sparse categorical crossentropy loss function

    model.fit(x_train, y_train, epochs=5) # train the model, runnnig through the data 3 times

    model.save('digit.keras') # save the model

    loss, accuracy = model.evaluate(x_test, y_test) # test the model
    print(f"Accuracy: {accuracy}") # print the accuracy
    print(f"Loss: {loss}") # print the loss


model = tf.keras.models.load_model('digit.keras') # load the model



image_num = input("Enter the number to be checked: ") # get the path to the image

while not os.path.isfile(f"Digits/{image_num}.png"): # check if the image exists
    print("The image does not exist.")
    image_num = input("Enter the number to be checked: ")

try:
    image = cv2.imread(f"Digits/{image_num}.png")[:,:,0] # read the image
    image = np.invert(np.array([image])) # invert the image (black = 0, white = 255)
    prediction = model.predict(image) # predict the image
    print(f"The number is: {np.argmax(prediction)}") # print the prediction
    plt.imshow(image[0], cmap=plt.cm.binary) # show the image
    plt.show()

except:
    print("The image could not be read.")