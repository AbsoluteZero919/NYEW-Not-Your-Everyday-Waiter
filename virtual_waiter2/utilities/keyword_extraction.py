import spacy
from fuzzywuzzy import process
import pandas as pd

def keyword_extract(text):
    # load english language model
    # Before running this, make sure you have the required packages installed
    nlp = spacy.load('en_core_web_sm', disable=['ner', 'textcat'])
    # If error: Can't find model 'en_core_web_sm', type the below command in terminal:
    # python -m spacy download en_core_web_sm

    # text = "can i order veg sandwich?"

    # create spacy
    doc = nlp(text.lower())

    # for token in doc:
    #     print(token.text,'->',token.pos_)

    noun_obj = ""
    for token in doc:
        # check token pos
        if token.pos_ == 'NOUN':
            # print token
            # print(token.text)
            noun_obj += token.text + " "
    noun_obj = noun_obj.rstrip()

    # print(noun_obj)
    return noun_obj


def match_menu(noun_obj, df):
    # dataset = pd.read_csv('nyew_menu.csv')
    # df = dataset.iloc[:, 0].values
    menu_list = df.tolist()
    # str2Match = "vegetarian burger"

    # Match ratio
    Ratios = process.extract(noun_obj, menu_list)
    # print(Ratios)
    ratio_list = [i[0] for i in Ratios]
    # string with the highest matching percentage
    # highest = process.extractOne(noun_obj, menu_list)
    # print(highest[0])
    return ratio_list
