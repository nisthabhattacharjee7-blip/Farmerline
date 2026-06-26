from apscheduler.schedulers.background import BackgroundScheduler
from app.weather import format_weather
from app.mandi import format_mandi_prices
import os

def send_morning_briefing(app):
    channel = os.getenv("SUPERVISOR_CHANNEL")
    weather = format_weather()
    prices = format_mandi_prices()
    
    app.client.chat_postMessage(
        channel=channel,
        text=(
            f"🌅 *Good Morning — FarmerLine Daily Briefing*\n\n"
            f"{weather}\n\n"
            f"{prices}\n\n"
            f"📋 Field workers: log your visits today using `/log`\n"
            f"📍 Stay safe and hydrated out there!"
        )
    )

def start_scheduler(app):
    scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
    scheduler.add_job(
        send_morning_briefing,
        trigger="cron",
        hour=7,
        minute=0,
        args=[app]
    )
    scheduler.start()
    print("⏰ Morning briefing scheduler started (7:00 AM IST daily)")
    return scheduler