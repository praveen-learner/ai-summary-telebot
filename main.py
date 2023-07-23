import requests
import telebot

API_TOKEN = "tele-token"

def summarize_article(article_url, length=5):
    """Summarizes an article and returns the summary."""
    url = "https://article-extractor-and-summarizer.p.rapidapi.com/summarize"
    headers = {
        "X-RapidAPI-Key": "rapidapi-token",
        "X-RapidAPI-Host": "article-extractor-and-summarizer.p.rapidapi.com"
    }
    params = {
        "url": article_url,
        "length": length,
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()["summary"]
    else:
        return None

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=["summarize"])
def summarize_article_handler(message):
    """Handles the /summarize command."""
    article_url = message.text.split(" ")[1]
    if "length" in message.text:
        length = message.text.split(" ")[2]
    else:
        length = 5
    summary = summarize_article(article_url, length)
    if summary:
        bot.send_message(message.chat.id, summary)
    else:
        bot.send_message(message.chat.id, "An error occurred.")

bot.polling()
