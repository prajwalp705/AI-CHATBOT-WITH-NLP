import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('punkt')
nltk.download('wordnet')



# Initialize NLP tools
lemmatizer = WordNetLemmatizer()

# Sample intents dictionary
intents = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "greetings"],
        "responses": ["Hello!", "Hi there!", "Greetings! How can I help you?"]
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see you", "farewell"],
        "responses": ["Goodbye!", "See you soon!", "Take care!"]
    },
    "name": {
        "keywords": ["your name", "who are you"],
        "responses": ["I'm a simple chatbot powered by NLTK.", "I’m your friendly assistant!"]
    },
    "help": {
        "keywords": ["help", "support", "assist", "need help"],
        "responses": ["Sure, I'm here to help. Ask me anything!", "I'm here to assist you."]
    },
    "unknown": {
        "responses": ["Sorry, I didn't understand that.", "Could you please rephrase your question?"]
    }
}

def preprocess(user_input):
    tokens = word_tokenize(user_input.lower())
    return [lemmatizer.lemmatize(token) for token in tokens]

def get_response(user_input):
    tokens = preprocess(user_input)

    for intent, data in intents.items():
        if intent == "unknown":
            continue
        for keyword in data["keywords"]:
            if any(keyword in " ".join(tokens) for keyword in data["keywords"]):
                return random.choice(data["responses"])
    
    return random.choice(intents["unknown"]["responses"])

def chat():
    print("Chatbot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    import random
    chat()
