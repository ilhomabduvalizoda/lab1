import telebot
import requests

TOKEN = '8137977647:AAEQJjwlMqgPQPQVwzsTvz_BxzD5yOK3auU'


OWM_API_KEY = 'dc0250615bb80a29062d6b86871d75f0'

bot = telebot.TeleBot(TOKEN)

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OWM_API_KEY}&units=metric&lang=ru"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"].capitalize()
        wind_speed = data["wind"]["speed"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]

        weather_text = (
            f"Текущая погода в {city}:\n"
            f"Температура: {temp}°C (ощущается как {feels_like}°C)\n"
            f"Ветер: {wind_speed} м/с\n"
            f"Влажность: {humidity}%\n"
            f"Давление: {pressure} гПа\n"
            f"Погода: {description}\n"
        )

        return weather_text
    else:
        return "К сожалению, возникла ошибка при получении данных о погоде."


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(text="Узнать погоду в Самаре", callback_data="samara_weather")
    markup.add(button)

    bot.reply_to(message, "Привет! Я могу показать вам текущую погоду. Нажмите на кнопку ниже.", reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.reply_to(message,
                 "/start - Приветственное сообщение\n/get_weather - Узнать погоду в Самаре")


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == "samara_weather":
        weather_text = get_weather("Самара")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=weather_text)


if __name__ == "__main__":
    bot.polling(none_stop=True)