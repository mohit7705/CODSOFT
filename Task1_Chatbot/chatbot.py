import re

def get_response(user_input):
    user_input = user_input.lower()

    # -------------------------------
    # RULE SET (TRAINING)
    # -------------------------------

    greetings = ["hello", "hi", "hey", "good morning", "good evening"]
    feelings = ["how are you", "how r u", "how are you doing"]
    help_words = ["help", "support", "assist", "guide"]
    about_bot = ["who are you", "your name", "who created you"]
    problems = ["not working", "issue", "error", "problem"]
    thanks_words = ["thank you", "thanks", "thx"]

    # -------------------------------
    # PATTERN MATCHING
    # -------------------------------

    # Greeting
    if any(word in user_input for word in greetings):
        return "Hello! I am your CodSoft rule-based chatbot. How can I help you?"

    # How are you
    if any(word in user_input for word in feelings):
        return "I'm doing great! Thanks for asking. What about you?"

    # Help intent
    if any(word in user_input for word in help_words):
        return "Sure! Tell me what problem you are facing, I will help you."

    # About bot
    if any(word in user_input for word in about_bot):
        return "I am a rule-based chatbot created for your CodSoft internship task."

    # Problems
    if any(word in user_input for word in problems):
        return "I understand you're facing an issue. Can you explain the problem clearly?"

    # Thanks
    if any(word in user_input for word in thanks_words):
        return "You’re welcome! Happy to help 😊"

    # Direct keyword pattern like "what is *"
    match = re.match(r"what is (.*)", user_input)
    if match:
        thing = match.group(1)
        return f"{thing} is something you can search on Google. I can help guide you!"

    # Exit
    if "bye" in user_input:
        return "Goodbye! Have a great day 😊"

    # Default fallback
    return "Sorry, I didn’t understand. Can you ask differently?"


# -------------------------------
# Chatbot Loop
# -------------------------------
print("Chatbot is running... Type 'bye' to exit.")

while True:
    user = input("You: ")
    reply = get_response(user)
    print("Bot:", reply)

    if "bye" in user.lower():
        break
