import nltk
from nltk.stem import WordNetLemmatizer
import random


nltk.download('wordnet')


lemmatizer = WordNetLemmatizer()


intents = {
    "greeting": {
        "keywords": ["hello", "hi", "hey"],
        "responses": ["Hi there!", "Hello!", "Hey!"]
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see you"],
        "responses": ["Goodbye!", "See you later!", "Take care!"]
    },
    "thanks": {
        "keywords": ["thanks", "thank you"],
        "responses": ["You're welcome!", "No problem!", "Glad to help!"]
    },
    "unknown": {
        "responses": ["Sorry, I didn't get that.", "Can you rephrase?"]
    }
}


def preprocess(text):
    words = text.lower().split()
    return [lemmatizer.lemmatize(word) for word in words]


def get_intent(text):
    words = preprocess(text)
    for intent, data in intents.items():
        if intent == "unknown":
            continue
        for word in words:
            if word in data["keywords"]:
                return intent
    return "unknown"


def get_response(intent):
    return random.choice(intents[intent]["responses"])


print("🤖 ChatBot: Hello! (type 'quit' to exit)")
while True:
    msg = input("You: ")
    if msg.lower() == "quit":
        print("🤖 ChatBot: Goodbye!")
        break
    intent = get_intent(msg)
    print("🤖 ChatBot:", get_response(intent))

