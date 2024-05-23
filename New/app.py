import random
from flask import Flask, request, jsonify
from nltk.chat.util import Chat, reflections  # Add this line
from flask import render_template
chatbot = None  # Define chatbot globally

app = Flask(__name__)

# Rest of your code...
@app.route('/')
def index():
    return render_template('index.html')


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

@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.json.get('user_input')
    response = chatbot.respond(user_input)
    if response is None:
        # If response is None, randomly select a response from miscellaneous_pairs
        miscellaneous_responses = miscellaneous_pairs[-1][1]  # Get the list of miscellaneous responses
        if miscellaneous_responses:
            response = random.choice(miscellaneous_responses)
        else:
            response = "I'm sorry, I couldn't understand that. Can you please rephrase your question?"
    return jsonify(response)

class Chatbot:
    def __init__(self, pairs):
        self.pairs = pairs
        self.chatbot = Chat(pairs, reflections)

    def respond(self, user_input):
        return self.chatbot.respond(user_input)

chatbot = Chatbot(all_pairs)

if __name__ == '__main__':
    app.run(debug=True)
