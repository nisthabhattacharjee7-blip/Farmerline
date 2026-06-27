# 🌾 FarmerLine

> **Intelligence for the field, inside Slack.**

A Slack-native coordination and intelligence agent for NGO agricultural field workers and supervisors across rural India. FarmerLine brings live weather, crop market prices, automated briefings, and structured visit logging directly into Slack — the tool field teams already use.

Built for the **Slack Agent Builder Challenge 2026** · Agent for Good track.

---

## The Problem

Across rural India, NGO field workers visit smallholder farmers every week — but they do it blind. No morning briefing, no live crop prices, no structured way to log what they saw or who they helped. Supervisors have zero visibility until someone calls or sends a WhatsApp message.

FarmerLine fixes the coordination gap — not by building another dashboard nobody opens, but by embedding intelligence directly into Slack.

---

## Features

| Command | What it does |
|---|---|
| `/briefing` | Automated morning briefing — weather, active farmers, today's priorities |
| `/weather` | Live hyperlocal weather for the field area (OpenWeatherMap) |
| `/prices` | Real-time mandi (crop market) prices via data.gov.in |
| `/log` | Log a completed farm visit — farmer name, crop status, notes |
| Auto-briefing | Daily 7AM IST post to `#supervisor-dashboard` via APScheduler |

---

## Architecture

```
Slack Workspace
      │
      ▼
Slack Bolt SDK  ──►  FastAPI + Uvicorn  ──►  Slash Command Handlers
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
     OpenWeatherMap     data.gov.in      SQLite DB
       (weather)      Mandi API +      (visit logs)
                      JSON fallback
                              │
                              ▼
                       APScheduler
                    (7AM IST briefing)
                              │
                              ▼
                  #supervisor-dashboard
```

---

## Tech Stack

- **Bot framework** — Slack Bolt SDK + Slack SDK
- **API layer** — FastAPI + Uvicorn
- **Scheduling** — APScheduler (tzlocal for IST)
- **Database** — SQLite via SQLAlchemy
- **External APIs** — OpenWeatherMap, data.gov.in Mandi API
- **Resilience** — JSON cache fallback for mandi prices
- **Deployment** — Railway via Procfile
- **Config** — python-dotenv

---

## Getting Started

### Prerequisites

- Python 3.10+
- A Slack app with slash commands enabled ([create one here](https://api.slack.com/apps))
- OpenWeatherMap API key (free tier works)
- data.gov.in API key (free)

### Installation

```bash
git clone https://github.com/nisthabhattacharjee7-blip/Farmerline.git
cd Farmerline
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the root:

```env
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_SIGNING_SECRET=your-signing-secret
OPENWEATHER_API_KEY=your-openweather-key
MANDI_API_KEY=your-data-gov-in-key
CHANNEL_ID=your-supervisor-dashboard-channel-id
```

### Run locally

```bash
python main.py
```

---

## Deployment

Deployed on **Railway** using a `Procfile`:

```
worker: python main.py
```

The worker process keeps APScheduler alive for the daily 7AM IST briefing.

---

## Why Slack?

Field teams already use Slack for team communication. FarmerLine doesn't ask anyone to download a new app, learn a new interface, or change their workflow. The coordination layer comes to them — so adoption is zero-effort and every farm visit gets logged.

---

## What's Next

- Hindi language support for field workers across Hindi-speaking states
- Multi-region rollout across India's major agricultural zones
- Supervisor dashboard with aggregated visit analytics
- Farmer profile database linked to visit history
- Voice input for low-literacy field contexts

---

## License

MIT

---

_Submitted to the Slack Agent Builder Challenge 2026 · Agent for Good track_
