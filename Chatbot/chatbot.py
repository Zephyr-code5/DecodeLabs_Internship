
print("Chatpal: Hello, I'm chatpal, your friendly chatbot!")
print("Enter 'exit' to end the conversation.")

while True:
    user_input = input("you: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("chatpal: Hello there! How can i help you")

    elif user_input == "how are you":
        print("chatpal: I'm doing great! Thank you")

    elif user_input == "what is your name":
        print("chatpal: I am Chatpal, a simple ruled-based chatbot")

    elif user_input == "":
        print("chatpal: please type something")
        
    elif user_input in ["bye", "exit", "quit", "goodbye"]:
        print("chatpal: Goodbye! Have a great day!")
        break
    else:
        print("chatpal: Sorry I don't understand")
        
