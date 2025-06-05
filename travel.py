import profile

def register(bot):
    @bot.message_handler(commands=['travel'])
    def travel(message):
        cities = ["تهران", "اصفهان", "شیراز", "مشهد", "تبریز"]
        msg = "🌍 به کدام شهر سفر می‌کنی؟\n" + "\n".join(cities)
        bot.send_message(message.chat.id, msg)

    @bot.message_handler(func=lambda m: m.text in ["تهران", "اصفهان", "شیراز", "مشهد", "تبریز"])
    def set_city(message):
        user_id = str(message.from_user.id)
        data = profile.load_data()
        data[user_id]["location"] = message.text
        profile.save_data(data)
        bot.send_message(message.chat.id, f"🧳 سفر کردی به {message.text}!")