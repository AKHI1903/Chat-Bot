print("🤖 Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello"]:
        print("🤖 Chatbot: Hi there! How can I help you?")
    elif "name" in user_input:
        print("🤖 Chatbot: I'm a simple rule-based chatbot written in Python.")
    elif "how are you" in user_input:
        print("🤖 Chatbot: I'm doing great, thanks for asking! How about you?")
    elif "help" in user_input:
        print("🤖 Chatbot: I can respond to greetings, tell you my name, and chat casually!")
    elif user_input in ["bye", "exit", "quit"]:
        print("🤖 Chatbot: Goodbye! Have a nice day! 👋")
        break
    else:
        print("🤖 Chatbot: Sorry, I don't understand that yet. Try something else!")