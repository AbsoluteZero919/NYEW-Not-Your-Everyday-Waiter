# 🤵 NYEW-Not-Your-Everyday-Waiter

This is a virtual waiter which aims to take on the responsibilities and functionality of a waiter in a restaurant, through the use of Machine Learning algorithms and models. The backend is developed using Python, Machine Learning and NLP libraries. As for the frontend, we have developed a UI using Tkinter, while also building a web application using Django (which is still ongoing). The application is quite easy to understand, setup and use. This project was developed as an attempt to address the problems of crowded restaurants without waiters, and botched orders because of the same, by providing a low-cost and easy management solution.

We have also published a paper based on this project, titled '*A Novel Approach to Virtual Waiter for Restaurants*', in the proceedings of the *International Conference on "Global Convergence in Technology, Entrepreneurship, Computing and Value Engineering: Principles and Practices"* (ICGCP-2021), ISBN: 979-85-27243-61-1. A complete, detailed explained about the project, its working, and future ideas can be found in our paper.

## Requirements

This project was built on a system with Windows 10 OS, with intel core i5 8th gen, at least 4GB RAM to run smoothly, and it needs an internet connection.
- Python version 3.7+ and a code Editor (such as Visual Studio Code)
- Tkinter and Django libraries for the UI
- TensorFlow, NLTK, and other ML and NLP libraries (which are easily found inside the source codes)
- Audio handling libraries such as Google Text-to-Speech, SpeechRecognition, sounddevice, etc. (also found in the source codes)

## Installations and Setup

First you need to create a folder named `builds` under the `virtual_waiter2` directory. As for the required packages and libraried, almost all the libraries can simply be installed using `pip install` commands.

To run the application from user POV, we can train the model before running the UI. To do this run this command in the CLI:

```sh
# Get into the utilities sub-directory in the virtual_waiter2 directory
$ cd virtual_waiter2/utilities

# Run the model training program file
$ python model_handler.py
```

After running these commands, we'll know the model has trained when the CLI shows that it's ready for the next command.

For some of the possible setup issues and errors, there are instructions provided in the comments of the respective program files.<br>
More updates on the setup instructions will be provided after the completion of the project

## Usage

To make the best of this project, make sure to go through the source codes in all the directories. Do not forget to go through the comments in the code as well, as they will help in getting a good idea of the flow of the project, along with some cool implementation instructions.

For the Tkinter UI application, the backend is completely in the `virtual_waiter2` directory itself, whereas for the Django web application, the backend is distributed.

### Building and Testing Units

To build and re-train new models, delete the previous model's contents in the `builds` file, change the `run_id` parameter in the `model_handler.py` file, and re-run that file in CLI.

```python
# run_id parameter to be changed for each model training to get the learining graphs individually
model.fit(training, output, n_epoch=400, batch_size=8, show_metric=True, snapshot_step=1, snapshot_epoch=True, run_id='Voice_Model_Run-2')
model.save("builds/model.tflearn")
```

To run and test the working of the backend, we can run just the `waiter.py` in the `virtual_waiter2` directory, in the CLI:

```sh
$ python waiter.py
```

To look into the learning graphs and differences between the trained model with previously trained models, you need to be on the directory containing the `tflearn_logs`. You can use the following TensorBoard command:

```sh
# Get into the required directory
$ cd virtual_waiter2

# Start the TensorBoard for the model
$ tensorboard --logdir='./tflearn_logs'
```

This will give a link: `http://localhost:6006/` which can be hit to get to the TensorBoard interface.

### Django Web Application

> The usage documentation regarding the Django web application will be updated once it is completed.

### Tkinter UI and System Application

To simply run the application GUI, you can run the `GUIBOI.py` in the `virtual_waiter2` directory, in the CLI:

```sh
$ python GUIBOI.py
```

There are chances of getting some common errors here. If you're using a Windows PC and you get an error when you run this program asking you to remove app execution aliases, do the following:

`Click Start ➡️ Type 'Manage app execution aliases' ➡️ Switch off the Python App Installer(s) ➡️ Now try executing the program again`

In any case requiring the run of the waiter, the introduction is standard, i.e we'll know the waiter is up and running properly when there are no unwanted entries in the CLI or GUI, and the waiter starts with a generic greet followed by a text to let the user know that the waiter is listening for their query.

### Say 'Hi !' to Your Waiter

Initially the waiter is in the generic conversation mode, where it answers to any casual or FAQ-like queries. The user can enter the ordering mode by saying `"I wanna order"`, `"I am ready to order"`, or such. The instructions on how to converse with the waiter is generic (almost human like), and are explained by the waiter itself as the conversation goes on.<br>
If the waiter isn't able to understand something said to it, then it'll let us know about that and may ask to repeat or suggest something as required.

There are two main scenarios requiring exit mechanisms. First is the typical exit to close the waiter after all the required jobs are done. To do this, we need to first make sure the waiter is in the generic conversation mode, and then just say `"Check out"`. This is a trigger phrase, similar to a wake word, asking the waiter to leave after the required jobs are done.<br>
The second is the inner exit, from the ordering mode back to the generic conversation mode. To do this, when the waiter is in the ordering mode, we can say `"Quit"`, `"I am done ordering"`, or such.

### Run as System Application

We can create an executable application file of the waiter, to run it like normal, system applications. To create this, first make sure to be in the `virtual_waiter2` directory. After this, make sure if the `PyInstaller` library is installed in the system. Then we can run a PyInstaller command to bundle the Python applications and all their dependencies into a single package, and creates executable file:

```sh
# Get into the required directory
$ cd virtual_waiter2

# Install PyInstaller library
$ pip install pyinstaller

# Command for creating the executable file and providing the file icon
$ pyinstaller --onefile --icon=.\Images\waiter_icon_tkinter_png.ico GUIBOI.py
```

After the process is complete, we will see several new folders and files. <b>While making any future changes in the model, be careful not to confuse the `build` and `builds` folders with each other.</b> The `build` folder is created during the process by PyInstaller, and the `builds` folder is that of the model.<br>
Finally, go to the `dist` sub-directory and move the `GUIBOI.exe` file out of the sub-directory, into the `virtual_waiter2` parent directory. This is the required executable file.

That's it ! Now we can run the file like any normal application, and enjoy.😃

Feel free to let us know about any new improvements or future ideas !

Thank you! ❤️


### To be continued 😉
