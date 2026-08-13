print("Welcome to my Rule-Based AI Chatbot!")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi" or user_input == "hey":
        print("Bot: Hello! How can I help you?")

    elif user_input == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user_input == "what is your name":
        print("Bot: My name is DecodeBot.")

    elif user_input == "what can you do":
        print("Bot: I can answer simple predefined questions.")

    elif user_input == "bye" or user_input == "exit":
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
