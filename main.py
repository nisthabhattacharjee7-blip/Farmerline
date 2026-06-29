from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from app.bot import register_handlers
from app.scheduler import start_scheduler
from dotenv import load_dotenv
import os

load_dotenv()

app = App(token=os.environ["SLACK_BOT_TOKEN"],
          signing_secret=os.environ["SLACK_SIGNING_SECRET"])

register_handlers(app)

if __name__ == "__main__":
    start_scheduler(app)
    # TEMP: trigger briefing immediately for screenshot — remove after
    from app.scheduler import send_morning_briefing
    send_morning_briefing(app)
    
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    print("⚡ FarmerLine is running!")
    handler.start()