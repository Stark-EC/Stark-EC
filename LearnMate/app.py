from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.form.get('user_input')
    # Process the user input and generate a response
    response = "This is a dummy response"
    return jsonify(response)
