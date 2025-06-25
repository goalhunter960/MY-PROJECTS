from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a ChatBot instance
bot = ChatBot('MyBot')

# Create a new trainer for the ChatBot
trainer = ChatterBotCorpusTrainer(bot)

# Train the ChatBot using the English corpus
trainer.train('chatterbot.corpus.english')

# Bot interaction loop
print("Hi, I'm your conversation bot. How can I assist you?")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break

    # Get the bot's response
    bot_response = bot.get_response(user_input)

    print("Bot:", bot_response)
