def identify_hashtags(data):	
	col = np.zeros((data.shape[0],1), 'str')
	data = np.append(data, col, axis=1)
	print(data.shape) # Note that shape starts at 1 and ends at 16, so the interval is [0:15]

	for i, text in enumerate(data[:,6]):
    		results = re.findall(r"#\w+", text) # Finds matches and returns them as an iterable
    		if results:
        		data[i,15] = ' '.join(results)
    		else:
        		data[i,15] = ''
	hashtags = set(hashtag for row in data[:,15] for hashtag in row.split())
