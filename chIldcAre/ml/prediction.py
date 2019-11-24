import sys 
import json
import tensorflow.keras as keras
import tensorflow 
from tensorflow.keras.models import load_model
import string 
def predict(sentences):
     
    translation = str.maketrans("","", string.punctuation)
    #text is array of sentences 
    for i,s in enumerate(sentences):
        sentences[i]=sentences[i].translate(translation);
        sentences[i]=sentences[i].lower()
        
    #loading model 
    my_model = load_model('my_model.h5')
    #loading necessary dictionaries 
    with open('label2id.json', 'r') as fp:
        label2id = json.load(fp)
    with open('word2id.json', 'r') as fp:
        word2id = json.load(fp)
    with open('id2label.json', 'r') as fp:
        id2label= json.load(fp)
    pred=[]
        
    for s in sentences:
        # Encode samples
        tokenized_sample = s.split(" ")
        encoded_samples = []
        for word in tokenized_sample:
            if word2id.get(word,-1) != -1:
                encoded_samples.append(word2id.get(word))
        encoded_samples = [encoded_samples]

        # Padding
        encoded_samples = keras.preprocessing.sequence.pad_sequences(encoded_samples, maxlen=101)

        # Make predictions
        label_probs= my_model.predict(encoded_samples)
        label_probs = {id2label[str(_id)]: prob for (label, _id), prob in zip(label2id.items(),label_probs[0])}
        pred.append(label_probs)

    return (pred)