# import nltk
# from nltk.chat.util import Chat, reflections
# import time
# import random

# # Additional patterns and responses
# pairs = [
#     ("(.*)math(.*)", ["Mathematics is fascinating! Let's solve some equations together."]),
#     ("(.*)science(.*)", ["Science is the pursuit of knowledge! What scientific concepts intrigue you?"]),
#     ("(.*)study tips(.*)", ["Sure! Here are some study tips: set a schedule, stay organized, and practice regularly."]),
#     ("(.*)tutorial videos(.*)", ["You can find tutorial videos on various topics on our educational platform. What topic interests you?"]),
#     ("(.*)translate(.*)", ["I can help with that! What language would you like to translate to?"]),
#     ("(.*)", ["Tell me more. I'm here to assist you on your learning journey!"]),  # Default response
# ]

# def learnmate_bot():
#     print("Hi, I'm LearnMate, your friendly educational AI bot. Ask me anything!")
#     chatbot = Chat(pairs, reflections)
#     while True:
#         user_input = input("You: ")
#         response = chatbot.respond(user_input)
#         type_response(response)

# def type_response(response):
#     for char in response:
#         # Print each character with a random delay
#         print(char, end='', flush=True)
#         time.sleep(random.uniform(0.03, 0.1))  # Adjust delay for moderate typing speed
#     print()  # Print a new line after completing the response

# learnmate_bot()


# #======================boundary here================
# import nltk
# from nltk.chat.util import Chat, reflections
# import time
# import random

# # Additional patterns and responses
# pairs = [
#     (r".*math.*", ["Mathematics is fascinating! Let's solve some equations together."]),
#     (r".*science.*", ["Science is the pursuit of knowledge! What scientific concepts intrigue you?"]),
#     (r".*study.*tips.*", ["Sure! Here are some study tips: set a schedule, stay organized, and practice regularly."]),
#     (r".*tutorial.*videos.*", ["You can find tutorial videos on various topics on our educational platform. What topic interests you?"]),
#     (r".*translate.*", ["I can help with that! What language would you like to translate to?"]),
#     (r".*", ["Tell me more. I'm here to assist you on your learning journey!"]),  # Default response
# ]

# def learnmate_bot():
#     print("Hi, I'm LearnMate, your friendly educational AI bot. Ask me anything!")
#     chatbot = Chat(pairs, reflections)
#     while True:
#         user_input = input("You: ")
#         response = chatbot.respond(user_input)
#         type_response(response)

# def type_response(response):
#     for char in response:
#         # Print each character with a random delay
#         print(char, end='', flush=True)
#         time.sleep(random.uniform(0.03, 0.1))  # Adjust delay for moderate typing speed
#     print()  # Print a new line after completing the response

# learnmate_bot()


#====================another boundary for more working code=================


# import nltk
# from nltk.chat.util import Chat, reflections
# import time
# import random

# # Categorized question-answer pairs
# greetings_pairs = [
#     (r".*hello.*", ["Hello there! How can I assist you today?"]),
#     (r".*hi.*", ["Hi there! What can I do for you?"]),
#     (r".*hey.*", ["Hey! How can I help you today?"]),
# ]

# vehicles_pairs = [
#     (r".*car.*", ["Cars are fascinating vehicles! What do you want to know about them?"]),
#     (r".*bike.*", ["Bikes are a popular mode of transportation. What bike-related information do you need?"]),
#     (r".*vehicle.*", ["Vehicles come in various shapes and sizes. What specific vehicle are you interested in?"]),
# ]

# school_pairs = [
#     (r".*math.*", ["Mathematics is fascinating! Let's solve some equations together."]),
#     (r".*science.*", ["Science is the pursuit of knowledge! What scientific concepts intrigue you?"]),
#     (r".*study.*tips.*", ["Sure! Here are some study tips: set a schedule, stay organized, and practice regularly."]),
# ]

# miscellaneous_pairs = [
#     (r".*thanks.*", ["You're welcome! Learning is a collaborative journey. How else can I assist you?"]),
#     (r".*", ["Tell me more. I'm here to help you on your learning quest!"]),  # Default response
# ]

# all_pairs = greetings_pairs + vehicles_pairs + school_pairs + miscellaneous_pairs

# def learnmate_bot():
#     print("Hi, I'm LearnMate, your friendly educational AI bot. Ask me anything!")
#     chatbot = Chat(all_pairs, reflections)
#     while True:
#         user_input = input("You: ")
#         response = chatbot.respond(user_input)
#         type_response(response)

# def type_response(response):
#     for char in response:
#         # Print each character with a random delay
#         print(char, end='', flush=True)
#         time.sleep(random.uniform(0.03, 0.1))  # Adjust delay for moderate typing speed
#     print()  # Print a new line after completing the response

# learnmate_bot()


# #================new boundary working currently

# import nltk
# from nltk.chat.util import Chat, reflections
# import time
# import random

# # Categorized question-answer pairs
# greetings_pairs = [
#     (r".*hello.*", ["Hello there! How can I assist you today?"]),
#     (r".*hi.*", ["Hi there! What can I do for you?"]),
#     (r".*hey.*", ["Hey! How can I help you today?"]),
# ]

# vehicles_pairs = [
#     (r".*car.*", ["Cars are fascinating vehicles! What do you want to know about them?"]),
#     (r".*bike.*", ["Bikes are a popular mode of transportation. What bike-related information do you need?"]),
#     (r".*vehicle.*", ["Vehicles come in various shapes and sizes. What specific vehicle are you interested in?"]),
# ]

# school_pairs = [
#     (r".*math.*", ["Mathematics is fascinating! Let's solve some equations together."]),
#     (r".*science.*", ["Science is the pursuit of knowledge! What scientific concepts intrigue you?"]),
#     (r".*study.*", ["Sure! Here are some study tips: set a schedule, stay organized, and practice regularly."]),
# ]

# miscellaneous_pairs = [
#     (r".*thanks.*", ["You're welcome! Learning is a collaborative journey. How else can I assist you?"]),
#     (r"Tell me more. I'm here to help you on your learning quest!", [
#         "I'm glad you're eager to learn! What specific topic are you interested in?",
#         "Learning is exciting! Let's explore new horizons together.",
#         "Absolutely! Learning is the key to growth and success. What can I help you with today?",
#         "we will meet tomorrow"
#     ]),
# ]

# all_pairs = greetings_pairs + vehicles_pairs + school_pairs + miscellaneous_pairs

# def type_response(response):
#     if response is None:
#         # If response is None, randomly select a response from miscellaneous_pairs
#         miscellaneous_responses = miscellaneous_pairs[-1][1]  # Get the list of miscellaneous responses
#         if miscellaneous_responses:
#             response = random.choice(miscellaneous_responses)
#         else:
#             response = "I'm sorry, I couldn't understand that. Can you please rephrase your question?"
    
#     for char in response:
#         # Print each character with a random delay
#         print(char, end='', flush=True)
#         time.sleep(random.uniform(0.03, 0.1))  # Adjust delay for moderate typing speed
#     print()  # Print a new line after completing the response

# def learnmate_bot():
#     print("Hi, I'm LearnMate, your friendly educational AI bot. Ask me anything!")
#     chatbot = Chat(all_pairs, reflections)
#     while True:
#         user_input = input("You: ")
#         response = chatbot.respond(user_input)
#         type_response(response)

# learnmate_bot()


#=======================With user interface==============

# import tkinter as tk
# from tkinter import scrolledtext
# import nltk
# from nltk.chat.util import Chat, reflections
# import time
# import random

# # Categorized question-answer pairs
# greetings_pairs = [
#     (r".*hello.*", ["Hello there! How can I assist you today?"]),
#     (r".*hi.*", ["Hi there! What can I do for you?"]),
#     (r".*hey.*", ["Hey! How can I help you today?"]),
# ]

# vehicles_pairs = [
#     (r".*car.*", ["Cars are fascinating vehicles! What do you want to know about them?"]),
#     (r".*bike.*", ["Bikes are a popular mode of transportation. What bike-related information do you need?"]),
#     (r".*vehicle.*", ["Vehicles come in various shapes and sizes. What specific vehicle are you interested in?"]),
# ]

# school_pairs = [
#     (r".*math.*", ["Mathematics is fascinating! Let's solve some equations together."]),
#     (r".*science.*", ["Science is the pursuit of knowledge! What scientific concepts intrigue you?"]),
#     (r".*study.*tips.*", ["Sure! Here are some study tips: set a schedule, stay organized, and practice regularly."]),
# ]

# miscellaneous_pairs = [
#     (r".*thanks.*", ["You're welcome! Learning is a collaborative journey. How else can I assist you?"]),
#     (r"Tell me more. I'm here to help you on your learning quest!", [
#         "I'm glad you're eager to learn! What specific topic are you interested in?",
#         "Learning is exciting! Let's explore new horizons together.",
#         "Absolutely! Learning is the key to growth and success. What can I help you with today?"
#     ]),
# ]

# all_pairs = greetings_pairs + vehicles_pairs + school_pairs + miscellaneous_pairs

# def type_response(response):
#     if response is None:
#         # If response is None, randomly select a response from miscellaneous_pairs
#         miscellaneous_responses = miscellaneous_pairs[-1][1]  # Get the list of miscellaneous responses
#         if miscellaneous_responses:
#             response = random.choice(miscellaneous_responses)
#         else:
#             response = "I'm sorry, I couldn't understand that. Can you please rephrase your question?"
    
#     for char in response:
#         # Print each character with a random delay
#         text_box.insert(tk.END, char)
#         time.sleep(random.uniform(0.03, 0.1))  # Adjust delay for moderate typing speed
#         text_box.see(tk.END)  # Scroll to the end of the text box
#         text_box.update()  # Update the text box display
#     text_box.insert(tk.END, '\n')  # Print a new line after completing the response

# def handle_user_input(event=None):
#     user_input = entry.get()
#     text_box.insert(tk.END, f"You: {user_input}\n")
#     response = chatbot.respond(user_input)
#     type_response(response)
#     entry.delete(0, tk.END)  # Clear the entry widget after submitting the input

# # Create the main window
# window = tk.Tk()
# window.title("LearnMate Chatbot")

# # Create a scrolled text widget to display the conversation
# text_box = scrolledtext.ScrolledText(window, width=60, height=20)
# text_box.pack(padx=10, pady=10)

# # Create an entry widget for user input
# entry = tk.Entry(window, width=50)
# entry.pack(padx=10, pady=5)

# # Bind the entry widget to the handle_user_input function
# entry.bind('<Return>', handle_user_input)

# # Create the chatbot instance
# chatbot = Chat(all_pairs, reflections)

# # Start the event loop
# window.mainloop()


#=======modified--========

# import tkinter as tk
# from tkinter import scrolledtext
# from tkinter import ttk
# import nltk
# from nltk.chat.util import Chat, reflections
# import time
# import random

# # Categorized question-answer pairs
# greetings_pairs = [
#     (r".*hello.*", ["Hello there! How can I assist you today?"]),
#     (r".*hi.*", ["Hi there! What can I do for you?"]),
#     (r".*hey.*", ["Hey! How can I help you today?"]),
# ]

# vehicles_pairs = [
#     (r".*car.*", ["Cars are fascinating vehicles! What do you want to know about them?"]),
#     (r".*bike.*", ["Bikes are a popular mode of transportation. What bike-related information do you need?"]),
#     (r".*vehicle.*", ["Vehicles come in various shapes and sizes. What specific vehicle are you interested in?"]),
# ]

# school_pairs = [
#     (r".*math.*", ["Mathematics is fascinating! Let's solve some equations together."]),
#     (r".*science.*", ["Science is the pursuit of knowledge! What scientific concepts intrigue you?"]),
#     (r".*study.*tips.*", ["Sure! Here are some study tips: set a schedule, stay organized, and practice regularly."]),
# ]

# miscellaneous_pairs = [
#     (r".*thanks.*", ["You're welcome! Learning is a collaborative journey. How else can I assist you?"]),
#     (r"Tell me more. I'm here to help you on your learning quest!", [
#         "I'm glad you're eager to learn! What specific topic are you interested in?",
#         "Learning is exciting! Let's explore new horizons together.",
#         "Absolutely! Learning is the key to growth and success. What can I help you with today?"
#     ]),
# ]

# all_pairs = greetings_pairs + vehicles_pairs + school_pairs + miscellaneous_pairs

# def type_response(response):
#     if response is None:
#         # If response is None, randomly select a response from miscellaneous_pairs
#         miscellaneous_responses = miscellaneous_pairs[-1][1]  # Get the list of miscellaneous responses
#         if miscellaneous_responses:
#             response = random.choice(miscellaneous_responses)
#         else:
#             response = "I'm sorry, I couldn't understand that. Can you please rephrase your question?"
    
#     for char in response:
#         # Print each character with a random delay
#         text_box.insert(tk.END, char)
#         time.sleep(random.uniform(0.03, 0.1))  # Adjust delay for moderate typing speed
#         text_box.see(tk.END)  # Scroll to the end of the text box
#         text_box.update()  # Update the text box display
#     text_box.insert(tk.END, '\n')  # Print a new line after completing the response

# def handle_user_input(event=None):
#     user_input = entry.get()
#     chat_history.insert(tk.END, f"You: {user_input}\n")
#     response = chatbot.respond(user_input)
#     type_response(response)
#     entry.delete(0, tk.END)  # Clear the entry widget after submitting the input

# # Create the main window
# window = tk.Tk()
# window.title("LearnMate Chatbot")

# # Create a sidebar (listbox) to display chat history
# chat_history = tk.Listbox(window, width=40, height=20)
# chat_history.pack(side=tk.LEFT, padx=10, pady=10)

# # Create a scrolled text widget to display the conversation
# text_box = scrolledtext.ScrolledText(window, width=60, height=20)
# text_box.pack(side=tk.LEFT, padx=10, pady=10)

# # Create an entry widget for user input
# entry = tk.Entry(window, width=50)
# entry.pack(side=tk.BOTTOM, padx=10, pady=5)
# entry.insert(0, "Ask me anything...")  # Set placeholder text in the entry widget
# entry.bind('<Return>', handle_user_input)

# # Create the chatbot instance
# chatbot = Chat(all_pairs, reflections)

# # Start the event loop
# window.mainloop()


#===================UPDATED AGAIN================

# import tkinter as tk
# from tkinter import scrolledtext
# from tkinter import ttk
# import nltk
# from nltk.chat.util import Chat, reflections
# import time
# import random

# # Categorized question-answer pairs
# greetings_pairs = [
#     (r".*hello.*", ["Hello there! How can I assist you today?"]),
#     (r".*hi.*", ["Hi there! What can I do for you?"]),
#     (r".*hey.*", ["Hey! How can I help you today?"]),
# ]

# vehicles_pairs = [
#     (r".*car.*", ["Cars are fascinating vehicles! What do you want to know about them?"]),
#     (r".*bike.*", ["Bikes are a popular mode of transportation. What bike-related information do you need?"]),
#     (r".*vehicle.*", ["Vehicles come in various shapes and sizes. What specific vehicle are you interested in?"]),
# ]

# school_pairs = [
#     (r".*math.*", ["Mathematics is fascinating! Let's solve some equations together."]),
#     (r".*science.*", ["Science is the pursuit of knowledge! What scientific concepts intrigue you?"]),
#     (r".*study.*tips.*", ["Sure! Here are some study tips: set a schedule, stay organized, and practice regularly."]),
# ]

# miscellaneous_pairs = [
#     (r".*thanks.*", ["You're welcome! Learning is a collaborative journey. How else can I assist you?"]),
#     (r"Tell me more. I'm here to help you on your learning quest!", [
#         "I'm glad you're eager to learn! What specific topic are you interested in?",
#         "Learning is exciting! Let's explore new horizons together.",
#         "Absolutely! Learning is the key to growth and success. What can I help you with today?"
#     ]),
# ]

# all_pairs = greetings_pairs + vehicles_pairs + school_pairs + miscellaneous_pairs

# def type_response(response):
#     if response is None:
#         # If response is None, randomly select a response from miscellaneous_pairs
#         miscellaneous_responses = miscellaneous_pairs[-1][1]  # Get the list of miscellaneous responses
#         if miscellaneous_responses:
#             response = random.choice(miscellaneous_responses)
#         else:
#             response = "I'm sorry, I couldn't understand that. Can you please rephrase your question?"
    
#     for char in response:
#         # Print each character with a random delay
#         text_box.insert(tk.END, char)
#         time.sleep(random.uniform(0.03, 0.1))  # Adjust delay for moderate typing speed
#         text_box.see(tk.END)  # Scroll to the end of the text box
#         text_box.update()  # Update the text box display
#     text_box.insert(tk.END, '\n')  # Print a new line after completing the response

# def handle_user_input(event=None):
#     user_input = entry.get()
#     chat_history.insert(tk.END, f"You: {user_input}\n")
#     response = chatbot.respond(user_input)
#     type_response(response)
#     entry.delete(0, tk.END)  # Clear the entry widget after submitting the input

# def add_chat():
#     chat_history.insert(tk.END, "New chat added!\n")

# def delete_chat():
#     selected_index = chat_history.curselection()
#     if selected_index:
#         chat_history.delete(selected_index)

# # Create the main window
# window = tk.Tk()
# window.title("LearnMate Chatbot")

# # Create a sidebar (listbox) to display chat history
# chat_history = tk.Listbox(window, width=40, height=20)
# chat_history.pack(side=tk.LEFT, padx=10, pady=10)

# # Create a scrolled text widget to display the conversation
# text_box = scrolledtext.ScrolledText(window, width=60, height=20)
# text_box.pack(side=tk.LEFT, padx=10, pady=10)

# # Create an entry widget for user input
# entry = tk.Entry(window, width=50)
# entry.pack(side=tk.BOTTOM, padx=10, pady=5)
# entry.insert(0, "Ask me anything...")  # Set placeholder text in the entry widget
# entry.bind('<Return>', handle_user_input)

# # Create buttons for adding and deleting chats
# add_button = tk.Button(window, text="Add Chat", command=add_chat)
# add_button.pack(side=tk.TOP, padx=10, pady=5)

# delete_button = tk.Button(window, text="Delete Chat", command=delete_chat)
# delete_button.pack(side=tk.TOP, padx=10, pady=5)

# # Create the chatbot instance
# chatbot = Chat(all_pairs, reflections)

# # Start the event loop
# window.mainloop()


#=========using Flask for UI/UX=============
from flask import Flask, render_template, request
import nltk
from nltk.chat.util import Chat, reflections
import time
import random

app = Flask(__name__)

# Categorized question-answer pairs
greetings_pairs = [
    (r".*hello.*", ["Hello there! How can I assist you today?"]),
    (r".*hi.*", ["Hi there! What can I do for you?"]),
    (r".*hey.*", ["Hey! How can I help you today?"]),
]

vehicles_pairs = [
    (r".*car.*", ["Cars are fascinating vehicles! What do you want to know about them?"]),
    (r".*bike.*", ["Bikes are a popular mode of transportation. What bike-related information do you need?"]),
    (r".*vehicle.*", ["Vehicles come in various shapes and sizes. What specific vehicle are you interested in?"]),
]

school_pairs = [
    (r".*math.*", ["Mathematics is fascinating! Let's solve some equations together."]),
    (r".*science.*", ["Science is the pursuit of knowledge! What scientific concepts intrigue you?"]),
    (r".*study.*tips.*", ["Sure! Here are some study tips: set a schedule, stay organized, and practice regularly."]),
]

miscellaneous_pairs = [
    (r".*thanks.*", ["You're welcome! Learning is a collaborative journey. How else can I assist you?"]),
    (r"Tell me more. I'm here to help you on your learning quest!", [
        "I'm glad you're eager to learn! What specific topic are you interested in?",
        "Learning is exciting! Let's explore new horizons together.",
        "Absolutely! Learning is the key to growth and success. What can I help you with today?"
    ]),
]

all_pairs = greetings_pairs + vehicles_pairs + school_pairs + miscellaneous_pairs

def type_response(response):
    if response is None:
        # If response is None, randomly select a response from miscellaneous_pairs
        miscellaneous_responses = miscellaneous_pairs[-1][1]  # Get the list of miscellaneous responses
        if miscellaneous_responses:
            response = random.choice(miscellaneous_responses)
        else:
            response = "I'm sorry, I couldn't understand that. Can you please rephrase your question?"
    
    return response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.form['user_input']
    response = chatbot.respond(user_input)
    typed_response = type_response(response)
    return typed_response

if __name__ == '__main__':
    nltk.download('punkt')
    chatbot = Chat(all_pairs, reflections)
    app.run(debug=True)
