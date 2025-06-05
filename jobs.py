import profile

def register(bot):
    @bot.message_handler(commands=['job'])
    def choose_job(message):
        user_id = str(message.from_user.id)
        data = profile.load_data()
        if user_id not in data:
            bot.send_message(message.chat.id, "❌ اول /start رو بزن.")
            return
        jobs = ["برنامه‌نویس", "موزیسین", "ورزشکار"]
        msg = "🔧 شغل مورد نظر را انتخاب کن:\n" + "\n".join([f"- {j}" for j in jobs])
        bot.send_message(message.chat.id, msg)

    @bot.message_handler(func=lambda m: m.text in ["برنامه‌نویس", "موزیسین", "ورزشکار"])
    def set_job(message):
        user_id = str(message.from_user.id)
        data = profile.load_data()
        if user_id not in data:
            return
        job = message.text
        data[user_id]["job"] = job
        profile.save_data(data)
        bot.send_message(message.chat.id, f"✅ شغل شما: {job}")