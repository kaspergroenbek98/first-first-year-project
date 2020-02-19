def tweet_features2(tweet):  # for bigrams
    tweet_words = set(tweet)
    features = {}
    for word in word_features:
        features[f'contains({word})'] = (word in tweet_words)
    return features
