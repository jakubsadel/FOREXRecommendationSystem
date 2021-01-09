test_data = scaler.transform(dataset[train_len - 60: , : ])
x_test = []
for i in range(60,len(test_data)):
    x_test.append(test_data[i-60:i,0])
    
x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0],x_test.shape[1],1))
x_test.shape

predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)# importance of transforme only
predictions.shape