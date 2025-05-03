from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import yaml

def create_chatbot():
    bot = ChatBot(
        "DiscordBot",
        logic_adapters=["chatterbot.logic.BestMatch"],
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        database_uri="sqlite:///database.sqlite3"
    )
    return bot

def train_bot(bot):
    # Train with built-in English corpus
    corpus_trainer = ChatterBotCorpusTrainer(bot)
    corpus_trainer.train("chatterbot.corpus.english")

    # Train with custom corpus
    with open("data/custom_corpus.yml", "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
        conversations = data.get("conversations", [])
    
    if conversations:
        list_trainer = ListTrainer(bot)
        for convo in conversations:
            list_trainer.train(convo)
