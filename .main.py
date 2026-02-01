import time
import requests
import random
from flask import Flask
from threading import Thread

# --- إعدادات السيرفر ---
app = Flask('')
@app.route('/')
def home(): return "Mini X-Mood Legendary AI is Online"
def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()

# --- البيانات الأساسية ---
TOKEN = "7979949298:AAFHH5cp3tI2Za8jqQr0rJHQ0jYEoDEIO1Y"
FREE_CH = "@xmoodbank"
VIP_CH = "-1003842599169"
SIGNATURE = "𝑻𝑯𝑬 𝑳𝑬𝑮𝑬𝑵𝑫 𝑿.𝑴𝑶𝑶𝑫"
BOT_NAME = "ميني اكسمود (Mini X-Mood)"

# --- قائمة العملات والتحفيز ---
WATCHLIST = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT']
MOTIVATION = [
    "صباح الثروة! تذكر أن الصبر هو مفتاح الأرباح في هذا السوق. 🧠",
    "لا تدع العواطف تقود تداولاتك، ميني اكسمود هنا ليرشدك. ✨",
    "الثراء ليس ضربة حظ، بل التزام بالخطة. استمر! 🚀"
]

REASONS_UP = ["تزايد في سيولة الحيتان", "أخبار إيجابية عن اعتماد مؤسسي", "ارتداد فني من منطقة دعم قوية"]
REASONS_DOWN = ["ضغوط بيع لجني الأرباح", "توترات سياسية عالمية", "تصحيح فني طبيعي بعد صعود"]

# --- الوظائف الذكية ---
def send_msg(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={'chat_id': chat_id, 'text': text, 'parse_mode': 'Markdown'})

def get_market_analysis(symbol, change):
    reason = random.choice(REASONS_UP) if change > 0 else random.choice(REASONS_DOWN)
    return reason

# --- نظام اللعبة (الربح اليومي) ---
def daily_game_msg():
    return (
        f"🎮 *لعبة ربح نقاط اكسمود (Daily Spin)*\n"
        f"━━━━━━━━━━━━━━━\n"
        f"مبروك! لقد ربحت اليوم 50 نقطة XP.\n"
        f"جمع النقاط واستبدلها باشتراك VIP مجاني!\n"
        f"تفاعل مع الرسائل لتزيد نقاطك. 💰"
    )

# --- محرك الثورة ---
def start_revolution():
    last_daily_time = 0
    print(f"🚀 {BOT_NAME} انطلق للسيطرة..")
    
    while True:
        try:
            current_time = time.time()
            
            # 1. الرسالة التحفيزية واللعبة (مرة كل 24 ساعة)
            if current_time - last_daily_time > 86400:
                msg = f"🌅 *رسالة التحفيز اليومية*\n{random.choice(MOTIVATION)}\n\n{daily_game_msg()}\n\n✍️ {SIGNATURE}"
                send_msg(FREE_CH, msg)
                last_daily_time = current_time

            # 2. مراقبة السوق الذكية
            for symbol in WATCHLIST:
                url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"
                data = requests.get(url).json()
                change = float(data['priceChangePercent'])
                price = float(data['lastPrice'])
                
                # إرسال تقرير مفصل عند الحركة (أكثر من 3%)
                if abs(change) >= 3.0:
                    reason = get_market_analysis(symbol, change)
                    
                    # نسخة القناة المجانية
                    free_report = (
                        f"🤖 *ميني اكسمود يحلل السوق
