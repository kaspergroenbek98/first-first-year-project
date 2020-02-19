"""
This is already in the notebook, but it is defined there - if that is fine this may be omitted.
"""
def tweet_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in tweet_words)
    return features
