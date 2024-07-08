#BASIC CHATBOT

import nltk
from nltk.chat.util import Chat, reflections  # Import necessary NLTK modules

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]  # Responds to "my name is <name>"
    ],
    [
        r"what is your name?",
        ["My name is ChatBot and I'm here to assist you.",]  # Responds to "what is your name?"
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about you ?",]  # Responds to "how are you?"
    ],
    [
        r"sorry (.*)",
        ["It's alright, no problem.",]  # Responds to apologies like "sorry <something>"
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]  # Responds to greetings like "hi", "hey", "hello"
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, I don't have an age!",]  # Responds to questions about age
    ],
    [
        r"(.*) (location|city) ?",
        ['I am from a virtual world.',]  # Responds to questions about location or city
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse!",]  # Responds to "what <something> want ?"
    ],
    [
        r"(.*) created you ?",
        ["I was created by a software developer.",]  # Responds to questions about who created the chatbot
    ],
    [
        r"bye",
        ["Bye! Take care.", "Have a great day!"]  # Responds to "bye"
    ],
]

# Create a chatbot
def chatbot():
    print("Hi, I'm ChatBot! How can I assist you today?")  # Introduction message
    chat = Chat(pairs, reflections)  # Create a Chat instance with defined pairs and reflections
    chat.converse()  # Start the conversation

if __name__ == "__main__":
    nltk.download('punkt')  # Download the necessary NLTK data for tokenization
    chatbot()  # Start the chatbot application

