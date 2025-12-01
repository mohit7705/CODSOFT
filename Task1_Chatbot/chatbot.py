import re

def get_response(user_input):
    user_input = user_input.lower().strip()

    greetings = ["hello", "hi", "hey", "good morning", "good evening"]
    feelings = ["how are you", "how r u", "how are you doing"]
    help_words = ["help", "support", "assist", "guide"]
    about_bot = ["who are you", "your name", "who created you"]
    problems = ["not working", "issue", "error", "problem"]
    thanks_words = ["thank you", "thanks", "thx"]

    if any(word in user_input for word in greetings):
        return "Hello! I am your CodSoft rule-based chatbot. How can I help you?"

    if any(word in user_input for word in feelings):
        return "I'm doing great! Thanks for asking. What about you?"

    if any(word in user_input for word in help_words):
        return "Sure! Tell me what problem you are facing, I will help you."

    if any(word in user_input for word in about_bot):
        return "I am a rule-based chatbot created for your CodSoft internship task."

    if any(word in user_input for word in problems):
        return "I understand you're facing an issue. Can you explain the problem clearly?"

    if any(word in user_input for word in thanks_words):
        return "You're welcome! Happy to help 😊"

    match = re.match(r"what is (.*)", user_input)
    if match:
        thing = match.group(1)
        return f"'{thing}' is something you can search on Google. I can help guide you!"

    if "bye" in user_input:
        return "Goodbye! Have a great day 😊"

    return "Sorry, I didn’t understand that. Could you rephrase it?"
while True:
    user = input("You: ")
    print("Bot:", get_response(user))
