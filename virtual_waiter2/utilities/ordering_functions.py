from utilities.model_handler import map_input
from utilities.keyword_extraction import keyword_extract, match_menu
from utilities.association_rule import apriori_algorithm
from utilities.audio_functions import get_audio, speak
import pandas as pd
from csv import writer

order = []
dataset = pd.read_csv('datasets/nyew_menu.csv')
df = dataset.iloc[:, :]
menu_items = df['menu_items']

# Converting list items to string for suggestion
def listToString(lst):
    return ', '.join(lst)

def place_order():
    speak("Say I want to order, followed by the item, say quit when done!")
    while True:
        inp = get_audio()
        re = map_input(inp)
        # Quitting the assistant
        if re.res[re.res_ind] > 0.5:
            if re.t == 'quit':
                show_order()
                break
        # get keyword from the input sentence
        keyword = keyword_extract(inp)

        if keyword == '':
            speak("I don't copy that! Please repeat")
        else:
            # match the keyword with the existing menu list
            item = match_menu(keyword, menu_items)
            speak("Do you want me to add " + item[0] + " to your order ?")
            inp_qu = get_audio()
            r = map_input(inp_qu)
            if r.res[r.res_ind] > 0.5:
                if r.t == 'affirmative':
                    # There is a limit of 8 items because that's the maximum number of columns in recommendations_menu.csv
                    # the dataframe used in the apriori algorithm takes only 8 columns as input.
                    if len(order) < 8:
                        order.append(item[0])
                        speak("Added " + item[0])
                        recommend_item(item[0])
                    else:
                        speak("Sorry! Can't order more than eight items")
                        show_order()
                        break
            # if inp_qu.lower() == "yes":
            #     order.append(item[0])
            #     speak("Added " + item[0])
            #     recommend_item(item[0])

                elif r.t == 'quit':
                    show_order()
                    break

                elif r.t == 'negative':
                    speak("Sorry! Did you mean " + listToString(item[0:3]))
                else:
                    speak("ha ? didn't get that, please repeat your order !")
            else:
                speak("I could not catch that, please repeat your order !")


    return


def show_order():
    if not order:
        # speak("Wow ! such empty !")
        speak("Your order list is empty !")
    else:
        total = 0
        for o in order:
            total += float(df.loc[df['menu_items'] == o, 'prices'])
        speak("Your order is " + listToString(order) + " and the total amount would be " + str(round(total, 2)) + " Rupees")
        total_time()

def total_time():
    totaltm = 0
    for t in order:
        totaltm += float(df.loc[df['menu_items'] == t, 'time'])
    hr = int(totaltm/60)
    mi = int(totaltm%60)
    if hr == 0:
        speak("Your order will be ready in " + str(mi) + " minutes")
    elif mi == 0:
        speak("Your order will be ready in " + str(hr) + " hours")
    else:
        speak("Your order will be ready in " + str(hr) + " hours " + str(mi) + " minutes")

def remove_order(str_inp):
    # get keyword from the input sentence
    keyword = keyword_extract(str_inp)
    # match the keyword with the existing menu list
    item = match_menu(keyword, menu_items)
    if item[0] in order:
        order.remove(item[0])
        speak(item[0] + " removed from your order !")
    else:
        speak("You have not ordered that !")


def show_menu(str_inp):
    keyword = keyword_extract(str_inp)
    # match the keyword with the existing column names
    df2 = df['sub_menu'].unique()
    item = match_menu(keyword, df2)
    # get menu items from a specified sub menu
    a = df.loc[(df['sub_menu'] == item[0])]
    speak(str(item[0]), exit=True)
    for ind in a.index:
        speak(str(df['menu_items'][ind]) + " costs " + str(df['prices'][ind]), exit=True)


def recommend_item(order_item):
    recommend_list = apriori_algorithm(order_item)
    # check if the item already exists in the order list
    a = set(recommend_list).intersection(order)
    # print(a, recommend_list)
    # if already ordered, remove from recommendation list
    for x in a:
        recommend_list.drop(recommend_list.index[recommend_list == x], inplace=True)

    if len(recommend_list) == 0:
        speak("what more do you want ?")
        return
    else:
        # speak("People who ordered " + order_item + " also ordered " + listToString(recommend_list))
        speak(listToString(recommend_list) + " is popular choice with " + order_item, exit=True)
        speak("Please, Consider ordering it")


# appends each order to the recommendation_menu
def append_recommend_menu(file_name, list_of_elem):
    # Open file in append mode
    if list_of_elem:
        with open(file_name, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(list_of_elem)