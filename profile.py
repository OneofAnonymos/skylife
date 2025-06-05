import json, os

DATA_FILE = "users.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE) as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def create_user(user_id):
    data = load_data()
    if user_id not in data:
        data[user_id] = {
            "money": 1000,
            "level": 1,
            "xp": 0,
            "energy": 100,
            "happy": 50,
            "hunger": 50,
            "sleep": 50,
            "job": None,
            "skills": [],
            "pets": [],
            "location": "تهران",
            "house": None,
            "married_to": None
        }
        save_data(data)

def get_profile(user_id):
    data = load_data()
    if user_id not in data:
        return "❌ هنوز ثبت‌نام نکردی!"
    u = data[user_id]
    return (f"👤 پروفایل:\n💰 پول: {u['money']} | ⭐ XP: {u['xp']}\n📈 سطح: {u['level']} | ⚡ انرژی: {u['energy']}\n"
            f"😄 شادی: {u['happy']} | 🍗 گرسنگی: {u['hunger']} | 💤 خواب: {u['sleep']}\n"
            f"🧭 شهر: {u['location']} | 🏠 خانه: {u['house'] or 'نداری'}\n"
            f"👔 شغل: {u['job'] or 'نداری'} | 💍 ازدواج: {'با ' + u['married_to'] if u['married_to'] else 'مجرد'}")