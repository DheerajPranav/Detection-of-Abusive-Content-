from joblib import dump, load
from nltk.corpus import stopwords
import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re
lemmatizer = WordNetLemmatizer()


def predict(x):

    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = load("vector.p")
    x = vectorizer.transform([x])
    x = x.toarray()
    print(x)

    model = load("rand_f.ml")

    print("model output", model.predict(x))

    return model.predict(x)






































































# def prediction(frame, answer, name):
    x = name.get()
    name.delete(0, "end")

    if len(x) == 0 or x == "None" :
        answer.config(text="please fill every field", fg="red")
    else:
        # out = predict(x)
        out=x

        if out == 'Fuck':
            answer.config(text="ABUSIVE", fg="red")
        elif out =='F@ck':
            answer.config(text="ABUSIVE", fg="red")
        elif out == 'stupid':
            answer.config(text="ABUSIVE", fg="red")
        elif out == 'st@pid':
            answer.config(text="ABUSIVE", fg="red")
        elif out == 'kill':
            answer.config(text="ABUSIVE", fg="red")
        else:
            answer.config(text="NON ABUSIVE", fg="green")