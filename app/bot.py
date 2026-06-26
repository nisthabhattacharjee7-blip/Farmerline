from slack_bolt import App
from app.weather import format_weather
from app.mandi import format_mandi_prices
from app.database import get_session, FarmerVisit, FieldWorker
from dotenv import load_dotenv
import os

load_dotenv()

def register_handlers(app: App):

    # ── Mention handler ──────────────────────────────────────
    @app.event("app_mention")
    def handle_mention(body, say):
        say("👋 Hi! I'm FarmerLine. Use `/briefing`, `/log`, or `/prices` to get started.")

    # ── /prices command ──────────────────────────────────────
    @app.command("/prices")
    def handle_prices(ack, say):
        ack()
        say(format_mandi_prices())

    # ── /weather command ─────────────────────────────────────
    @app.command("/weather")
    def handle_weather(ack, say):
        ack()
        say(format_weather())

    # ── /log command ─────────────────────────────────────────
    @app.command("/log")
    def handle_log(ack, say, body):
        ack()
        text = body.get("text", "").strip()
        user_id = body["user_id"]
        user_name = body["user_name"]

        # Expected format: farmer_name, village, crop, issue, action_taken
        parts = [p.strip() for p in text.split(",")]
        if len(parts) < 5:
            say(
                "⚠️ Please use this format:\n"
                "`/log farmer_name, village, crop, issue, action_taken`\n\n"
                "Example:\n"
                "`/log Ramesh Kumar, Kaliachak, Rice, Yellowing leaves, Applied urea`"
            )
            return

        session = get_session()
        visit = FarmerVisit(
            worker_name=user_name,
            farmer_name=parts[0],
            village=parts[1],
            crop=parts[2],
            issue=parts[3],
            action_taken=parts[4]
        )
        session.add(visit)
        session.commit()
        session.close()

        say(
            f"✅ *Visit logged successfully!*\n"
            f"👨‍🌾 Farmer: {parts[0]} | 📍 Village: {parts[1]}\n"
            f"🌾 Crop: {parts[2]}\n"
            f"🔍 Issue: {parts[3]}\n"
            f"✔️ Action: {parts[4]}"
        )

    # ── /briefing command ─────────────────────────────────────
    @app.command("/briefing")
    def handle_briefing(ack, say):
        ack()
        weather = format_weather()
        prices = format_mandi_prices()
        say(
            f"🌅 *Good Morning — FarmerLine Daily Briefing*\n\n"
            f"{weather}\n\n"
            f"{prices}\n\n"
            f"📋 Log your visits today using `/log`"
        )