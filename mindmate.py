import random

class MentalHealthChatbot:
    def __init__(self):
        self.greetings = [
            "hi", "hello", "hey", "salam", "assalam o alaikum",
            "good morning", "good afternoon", "good evening",
            "yo", "greetings"
        ]

        self.sad_words = [
            "sad", "hurt", "hurts", "hurting", "angry", "tired",
            "cry", "bad", "down", "unhappy", "upset", "miserable",
            "empty", "lost", "gloomy", "exhausted", "crying",
            "lonely", "broken", "helpless", "pain", "drained"
        ]

        self.happy_words = [
            "happy", "good", "great", "joyful", "fine", "blessed",
            "pleased", "awesome", "enjoying", "nice", "wonderful",
            "content", "relaxed", "chill", "cool"
        ]

        self.thank_words = [
            "thanks", "thank you", "shukriya", "thnx", "ty",
            "appreciate it", "thanks a lot", "so kind of you",
            "thankful", "thank u"
        ]

        self.exit_words = [
            "bye", "exit", "quit", "goodbye", "see ya", "farewell",
            "allah hafiz", "take care", "gtg", "ttyl",
            "talk to you later", "see you"
        ]

        self.critical_words = [
            "suicide", "kill myself", "end my life", "give up",
            "can't take it anymore", "want to die", "dying",
            "die", "unalive", "worthless", "hopeless", "no point",
            "overwhelmed", "kill", "self harm", "cut myself"
        ]

        self.stress_words = [
            "stress", "stressed", "under pressure", "anxious",
            "panic", "nervous", "overthinking"
        ]

        self.tips = [
            "Drink a glass of water 💧",
            "Try a 2-minute breathing exercise 🧘",
            "Write your feelings in a small journal 🖊️",
            "Step outside for some fresh air 🌤️",
            "Listen to soft, calm music 🎧",
            "Try taking a short nap or rest 😴"
        ]

        self.helplines = [
            "You can also explore 'Umang – A Mental Health Helpline' → https://www.umang.com.pk",
            "For emotional support, visit 'LifeLine International' → https://lifeline-international.com",
            "In Pakistan, you can call Rozan Helpline at 0304-111-1744"
        ]

        self.greeting_responses = [
            "Hi there! 😊 How are you feeling today?",
            "Hello! I'm MindMate 👋 Always here if you need someone to talk to.",
            "Hey! 🌟 You can share anything with me. No pressure, no judgment.",
            "Assalam o Alaikum! 🌸 I'm here to support you, whatever you're going through.",
            "Greetings! 🌈 Let's make today a little lighter, together."
        ]

        self.thank_responses = [
            "You're very welcome! 😊 I'm here for you anytime.",
            "No problem at all 🌻 It means a lot to me that you're here.",
            "Always happy to help 🧡 You're never alone.",
            "Thank you for trusting me to talk to 💬",
            "I'm here whenever you need a little support or kindness 💖"
        ]

        self.exit_responses = [
            "Goodbye! 🌼 Take care of yourself.",
            "Allah Hafiz! Take care. 💙",
            "See you soon! Don't hesitate to come back if you need support.",
            "Farewell for now! 🌈",
            "Take care! Your mental health matters. 💙"
        ]

    def respond(self, user_input):
        message = user_input.lower()

        # Check critical messages first
        for word in self.critical_words:
            if word in message:
                return (
                    "💔 It sounds like you're going through something very difficult.\n"
                    "Please know you're not alone. Help is available:\n"
                    + "\n".join(self.helplines)
                    + "\n\nWould you like a calming tip? Just type 'tip'. 🌿"
                )

        # Exit
        for word in self.exit_words:
            if word in message:
                return random.choice(self.exit_responses)

        # Thanks
        for word in self.thank_words:
            if word in message:
                return random.choice(self.thank_responses)

        # Greetings
        for word in self.greetings:
            if word in message:
                return random.choice(self.greeting_responses)

        # Sad emotions
        for word in self.sad_words:
            if word in message:
                return (
                    "I'm really sorry you're feeling this way 😔\n"
                    "Would you like a small tip to lift your mood? "
                    "Just type 'tip'."
                )

        # Stress
        for word in self.stress_words:
            if word in message:
                return (
                    "Life can be overwhelming sometimes 💭\n"
                    "Try to pause, breathe, and ground yourself. "
                    "Want a self-care tip? Just type 'tip'."
                )

        # Happy emotions
        for word in self.happy_words:
            if word in message:
                return (
                    "That's lovely to hear! 😊 Stay joyful and keep shining.\n"
                    "If there's anything you want to talk about, I'm here."
                )

        # Tips
        if "tip" in message or "advice" in message or "help" in message:
            return (
                "Here's a little self-care idea for you: "
                + self.random_tip()
            )

        # Journal
        if "journal" in message:
            return (
                "Journaling can help make thoughts clearer. 📔\n"
                "Would you like a prompt to get started?"
            )

        # Anxiety
        if "anxiety" in message:
            return (
                "Anxiety can be tough, but you're not alone. 🧠\n"
                "Take a few deep breaths, and let's talk it out together."
            )

        # Depression
        if "depression" in message:
            return (
                "Thank you for opening up. 💙\n"
                "You don't have to go through this alone. "
                "I'm here to listen.\n"
                + random.choice(self.helplines)
            )

        # Professional help
        if (
            "therapist" in message
            or "doctor" in message
            or "counselor" in message
        ):
            return (
                "Talking to a professional can be a helpful step. 🧑‍⚕️\n"
                + random.choice(self.helplines)
            )

        # About chatbot
        if "who are you" in message or "what are you" in message:
            return (
                "I'm MindMate 🌼 — a friendly chatbot created "
                "to listen and provide supportive responses."
            )

        # Default response
        return (
            "I'm listening... you can share what's on your mind. 🧠💬\n"
            "Or type 'tip' if you'd like a self-care suggestion."
        )

    def random_tip(self):
        # Select a random self-care tip
        return random.choice(self.tips)


def start_chat():
    print("🌟 Welcome to MindMate - Your Friendly Mental Health Chatbot 🌟")
    print("You can talk to me about anything. Type 'bye' to exit.\n")

    bot = MentalHealthChatbot()

    while True:
        user_input = input("You: ")
        reply = bot.respond(user_input)
        print("Bot:", reply)

        if any(word in user_input.lower() for word in bot.exit_words):
            break


# Start the chatbot
start_chat()
