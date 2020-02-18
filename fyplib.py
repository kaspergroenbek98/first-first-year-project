def csv_reader:  # Read the data into a header and a data np.array
	with open('data.csv', encoding='latin1') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
    	data = np.array([np.array(line) for line in csv_reader])
	header, data = data[0,:], data[1:,:]
	return header, data
