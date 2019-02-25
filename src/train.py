
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPool2D

def main():
	data =np.load("data/raw/dataset.npz")
	train_x,train_y,test_x,test_y = data['arr_0'], data['arr_1'],data['arr_2'],data['arr_3']
	X_train =np.concatenate([train_x,test_x])
	y_train=np.concatenate([train_y,test_y])

	print("Data loaded")

	X_train = X_train / 255
	X_train = np.expand_dims(X_train,axis=-1)
	y_train = y_train-1

	model = Sequential()
	model.add(Conv2D(100, kernel_size=(3, 3),activation='relu',input_shape=(32,32,1)))
	model.add(MaxPool2D(pool_size=(2, 2)))
	model.add(Conv2D(50, (3, 3), activation='relu'))
	model.add(MaxPool2D(pool_size=(2, 2)))
	model.add(Flatten())
	model.add(Dense(46, activation='relu'))
	model.compile(loss='sparse_categorical_crossentropy', optimizer='adam',metrics=['accuracy'])

	model.fit(X_train, y_train, epochs=10, batch_size=128)

	model.save('out/model.h5')

if __name__=='__main__':
	main()