import profile

def register(bot):
    @bot.message_handler(commands=['learn'])
    def learn_skill(message):
        user_id = str(message.from_user.id)
        skills = ["برنامه‌نویسی", "موسیقی", "ورزش"]
        msg = "🎓 مهارتی را یاد بگیر:\n" + "\n".join(skills)
        bot.send_message(message.chat.id, msg)

    @bot.message_handler(func=lambda m: m.text in ["برنامه‌نویسی", "موسیقی", "ورزش"])
    def add_skill(message):
        user_id = str(message.from_user.id)
        data = profile.load_data()
        if message.text not in data[user_id]["skills"]:
            data[user_id]["skills"].append(message.text)
            profile.save_data(data)
            bot.send_message(message.chat.id, f"✅ مهارت {message.text} به لیست شما اضافه شد.")