import random
import datetime

chat_history = []

def chatbot_response(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return random.choice([
            "Hello! How can I help you today?",
            "Hi there! How are you doing?",
            "Hey! Nice to chat with you."
        ])

    elif "how are you" in message:
        return random.choice([
            "I'm doing great, thanks for asking!",
            "Everything is running smoothly.",
            "I'm good. What about you?"
        ])

    elif "name" in message:
        return "My name is PyBot. I am a simple Python chatbot."

    elif "time" in message:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return "The current time is " + current_time

    elif "date" in message:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        return "Today's date is " + current_date

    elif "python" in message:
        return random.choice([
            "Python is one of the most popular programming languages.",
            "Python is beginner-friendly and powerful.",
            "Python is used in web development, AI, automation, and more."
        ])

    elif "college" in message:
        return random.choice([
            "College is a great place to learn new skills.",
            "Balancing studies and hobbies is important in college.",
            "Consistency is often more effective than last-minute studying."
        ])

    elif "exam" in message:
        return random.choice([
            "Good luck with your exams!",
            "Practice and revision are the keys to success.",
            "Stay calm and do your best."
        ])

    elif "study" in message:
        return random.choice([
            "Studying a little every day is usually more effective than cramming.",
            "Understanding concepts is often better than memorizing them.",
            "Try solving practice problems to strengthen your understanding."
        ])

    elif "joke" in message:
        return random.choice([
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "Debugging is like being a detective in a movie where you are also the culprit.",
            "Why did the programmer quit his job? Because he didn't get arrays."
        ])

    elif "thank" in message:
        return "You're welcome!"

    else:
        return random.choice([
            "That's interesting. Tell me more.",
            "I'm not sure I understand. Could you explain differently?",
            "I don't know much about that yet.",
            "Can you ask that another way?"
        ])

def view_history():
    if len(chat_history) == 0:
        print("\nNo chat history available.")
    else:
        print("\n===== CHAT HISTORY =====")
        for message in chat_history:
            print(message)

def start_chat():
    print("\nChat started!")
    print("Type 'bye' to end the conversation.\n")

    while True:
        user_message = input("You: ")

        if user_message.lower() == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        response = chatbot_response(user_message)

        print("Bot:", response)

        chat_history.append("You: " + user_message)
        chat_history.append("Bot: " + response)

def main():
    while True:
        print("\n===== SMART CHATBOT =====")
        print("1. Start Chat")
        print("2. View Chat History")
        print("3. Clear Chat History")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            start_chat()

        elif choice == "2":
            view_history()

        elif choice == "3":
            chat_history.clear()
            print("Chat history cleared.")

        elif choice == "4":
            print("Thank you for using PyBot!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()