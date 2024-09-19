from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created using NLTK.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about You?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "Alright, keep it up!",]
    ],
    [
        r"quit",
        ["Bye, take care!",]
    ]
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Hi, I'm a chatbot! Type something to start the conversation. Type 'quit' to end.")
chatbot.converse()

