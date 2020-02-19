def filtering(data)  # Filters data by removing stopwords, non-alph, stems
   porter = nltk.PorterStemmer(data)

    # Remove all stopwords, non-alphabet words (except spaces), and stem the words
    for i, row in enumerate(data[:,6]):
        row = row.lower()
        row = ''.join(char for char in row if char.isalpha() or char == ' ')
        row = ' '.join(porter.stem(word) for word in row.split() if word not in stopwords)
        data[i,6] = row

    # Create a long string of ALL words, then token them, and create a frequency distribution
    actualWords = ' '.join(token for sentence in data[:,6] for token in sentence.split())
    #tokens = nltk.word_tokenize(actualWords)
    tokens = actualWords.split()
    fd = nltk.FreqDist(tokens)
    # Returns all words and frequency distribution
    return fd, tokens
