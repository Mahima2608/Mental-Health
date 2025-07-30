# import random
# from flask import Flask, render_template, request, jsonify

# app = Flask(__name__)

# # Define pairs of patterns and responses
# pairs = [

#     {
#         "pattern": ["hi", "hello", "hey", "hii"],
#         "responses": [
#             "Hello, how are you "
#         ]
#     },
#     {
#         "pattern": ["depressed", "sad", "unhappy", "down"],
#         "responses": [
#             "I'm sorry to hear that you're feeling {0}. It's important to talk to someone about it. Do you have someone you can talk to?",
#             "Feeling {0} can be really tough. I'm here to listen. What's been going on?"
#         ]
#     },
#     {
#         "pattern": ["happy", "good", "great", "well"],
#         "responses": [
#             "That's wonderful to hear! What's been making you feel {0}?",
#             "It's great that you're feeling {0}. Can you tell me more about what's been going well?"
#         ]
#     },
#     {
#         "pattern": ["stress", "anxiety", "anxious", "nervous"],
#         "responses": [
#             "It sounds like you're dealing with a lot of stress. What do you think is causing it?",
#             "Anxiety can be really challenging. Would you like to talk more about what's making you feel {0}?"
#         ]
#     },
#     {
#         "pattern": ["help"],
#         "responses": [
#             "I'm here to help. Can you tell me more about what you're going through?",
#             "I'm here to support you. What's been on your mind?"
#         ]
#     },
#     {
#         "pattern": ["quit", "exit", "bye", "goodbye"],
#         "responses": [
#             "Goodbye. Remember, talking to a mental health professional can be really helpful.",
#             "Take care! Don't hesitate to reach out if you need support."
#         ]
#     }
# ]

# # Function to generate responses
# def generate_response(user_input):
#     user_input = user_input.lower()
#     for pair in pairs:
#         for pattern in pair["pattern"]:
#             if pattern in user_input:
#                 response = random.choice(pair["responses"]).format(pattern)
#                 return response
#     return "I'm not sure how to respond to that. Can you tell me more about what you're feeling?"

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/get_response', methods=['POST'])
# def get_response():
#     user_input = request.json.get('message')
#     response = generate_response(user_input)
#     return jsonify(response=response)

# if __name__ == "__main__":
#     app.run(debug=True)
