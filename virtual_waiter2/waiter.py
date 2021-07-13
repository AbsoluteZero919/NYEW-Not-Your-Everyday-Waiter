from utilities.model_handler import data, map_input
import random
from utilities.audio_functions import get_audio, speak
from utilities.ordering_functions import place_order, show_menu, show_order, remove_order, append_recommend_menu, order

'''
    Nyew: Not Your Everyday Waiter
    
    A virtual waiter aims to take on the responsibilities and functionality of a waiter in
    a restaurant, through the use of machine learning models.
    
    Developed By: Batch-23
    
    PRANAV G V
    SKANDA N KASHYAP
    SUBHAYAN MUKHOPADHYAY
    SWATHI K S
'''









# Main function
def chat():
    # Initiate the conversation with the assistant
    # print("Start talking with the bot (type quit to stop)!")
    speak("Hi! I am your waiter, start talking with me (say checkout to stop)!")

    while True:
        inp = get_audio()

        # Quitting the assistant
        if inp.lower() == "checkout" or inp.lower() == "check out":
            append_recommend_menu('datasets/Recommendations_menu.csv', order)
            speak("See you later then !")
            exit()

        # Map input voice recognition to previous data items
        r = map_input(inp)

        if r.res[r.res_ind] > 0.5:
            for tg in data["intents"]:
                # execute function after mapping
                if r.t == 'order':
                    responses = tg['responses']
                    res = random.choice(responses)
                    speak(res)
                    place_order()
                    speak("let me know if i can do anything else ?")
                    break
                elif r.t == 'menu':
                    show_menu(inp)
                    speak("ready to order ? Tell me whenever you are ready !")
                    break
                elif r.t == 'showorder':
                    show_order()
                    speak("wanna add more to your order ? Tell me whenever you are ready to order !")
                    break
                elif r.t == 'remove':
                    remove_order(inp)
                    speak("let me know if i can do anything else ?")
                    break
                # Choose appropriate responses from dataset after mapping
                elif r.t == tg['tag']:
                    responses = tg['responses']
                    res = random.choice(responses)
                    if res =="":
                        speak("didn't get that can you rephrase that for me ?")
                    else:
                        speak(res)
        else:
            speak("I don't understand, Please ask another question.")


chat()


