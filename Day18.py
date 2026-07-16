def chatbot():
    print("welcome to AI assistant")
    while True:
        user=input("you:").lower()
        if user=="exit":
            print("Bot:goodbye have a nice day")
            break
        elif user=="hi":
            print("Bot:hello")
        elif user=="bye":
            print("Bot:see you again")
        elif user=="who are you":
            print("i am ai assistant")
        elif user=="python":
            print("python is popoluar language")
        elif user=="machine learning":
            print("machine learning teaches computers to learn from data")
        else:
            print("sorry")
chatbot()