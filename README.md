# 🤵 NYEW-Not-Your-Everyday-Waiter

This is a virtual waiter which aims to take on the responsibilities and functionality of a waiter in a restaurant, through the use of Machine Learning algorithms and models. The backend is developed using Python, Machine Learning and NLP libraries. As for the frontend, we have developed a UI using Tkinter, while also building a web application using Django (which is still ongoing). The application is quite easy to understand, setup and use. This project was developed as an attempt to address the problems of crowded restaurants without waiters, and botched orders because of the same, by providing a low-cost and easy management solution.

We have also published a paper based on this project, called '*A Novel Approach to Virtual Waiter for Restaurants*', in the proceedings of the *International Conference on "Global Convergence in Technology, Entrepreneurship, Computing and Value Engineering: Principles and Practices"* (ICGCP-2021), ISBN: 979-85-27243-61-1.

## Requirements

This project was built on a system with Windows 10 OS, with intel core i5 8th gen, at least 4GB RAM to run smoothly, and it needs an internet connection.
- Python version 3.7+ and a code Editor (such as Visual Studio Code)
- Tkinter and Django libraries for the UI
- TensorFlow, NLTK, and other ML and NLP libraries (which are easily found inside the source codes)
- Audio handling libraries such as Google Text-to-Speech, SpeechRecognition, sounddevice, etc. (also found in the source codes)

## Installations and Setup

First you need to create a folder named `builds` under the `virtual_waiter2` directory. As for the required packages and libraried, almost all the libraries can simply be installed using `pip install` commands.

To run the application from user POV, we can train the model before running the UI. To do this run this command in the CLI:

```bash
# Get into the utilities sub-directory in the virtual_waiter2 directory
cd virtial_waiter2/utilities

# Run the model training program file
python model_handler.py
```

After running these commands, we'll know the model has trained when the CLI shows that it's ready for the next command.

For some of the possible setup issues and errors, there are instructions provided in the comments of the respective program files.<br>
More updates on the setup instructions will be provided after the completion of the project

## Usage

To make the best of this project, make sure to go through the source codes in all the directories. Do not forget to go through the comments in the code as well, as they will help in getting a good idea of the flow of the project, along with some cool implementation instructions.

For the Tkinter UI application, the backend is completely in the `virtual_waiter2` directory itself, whereas for the Django web application, the backend is distributed.

To run and test the working of the backend,...

### To be continued 😉
