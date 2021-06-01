import nltk
# run the following in terminal to remove the error
# nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow as tf
import pickle
import json
import collections

with open("datasets/intents.json") as file:
    data = json.load(file)

try:
    with open("builds/data.pickle", "rb") as f:
        # Read all date items from the dataset
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    # Analize the tags, patterns and responses
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    # Map the closest patterns so that
    # future data retrieval is optimised
    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    with open("builds/data.pickle", "wb") as f:
        # Create portable serialized representations of required objects
        pickle.dump((words, labels, training, output), f)

# Build and train the model from the datasets

tf.compat.v1.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

# Initializing a model
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')

# If model already trained and existing, load the model
try:
    model.load("builds/model.tflearn")

# Else train the model accordingly
except:
    # tensorflow.reset_default_graph()
    tf.compat.v1.reset_default_graph()

    net = tflearn.input_data(shape=[None, len(training[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
    net = tflearn.regression(net)

    model = tflearn.DNN(net, tensorboard_dir='tflearn_logs', tensorboard_verbose=0)

    model.fit(training, output, n_epoch=400, batch_size=8, show_metric=True, snapshot_step=1, snapshot_epoch=True, run_id= 'Voice_Model_Run-1')
    model.save("builds/model.tflearn")

# Tokenizing words from data items
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)

def map_input(inp):
    results = model.predict([bag_of_words(inp, words)])[0]
    results_index = numpy.argmax(results)
    tag = labels[results_index]
    result = collections.namedtuple('result', ['res', 'res_ind', 't'])
    return result(res=results, res_ind=results_index, t=tag)