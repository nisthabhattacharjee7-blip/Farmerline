import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

MANDI_API_KEY = os.getenv("MANDI_API_KEY")
CACHE_FILE = "app/mandi_cache.json"

def get_mandi_prices(state="West Bengal", district="Malda"):
    try:
        url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
        params = {
            "api-key": MANDI_API_KEY,
            "format": "json",
            "limit": 10,
            "filters[state.keyword]": state,
            "filters[district.keyword]": district
        }
        response = requests.get(url, params=params, timeout=5)
        data = response.json()
        records = data.get("records", [])
        if records:
            # Save to cache for next time
            with open(CACHE_FILE, "w") as f:
                json.dump(records, f)
            return records
        else:
            return load_cache()

    except Exception:
        return load_cache()

def load_cache():
    try:
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return []

def format_mandi_prices(state="West Bengal", district="Malda"):
    records = get_mandi_prices(state, district)
    if not records:
        return "⚠️ Could not fetch mandi prices right now."

    lines = [f"📊 *Mandi Prices — {district}, {state}*\n"]
    for r in records[:5]:
        lines.append(
            f"🌾 *{r.get('commodity')}* at {r.get('market')}\n"
            f"   Min: ₹{r.get('min_price')} | Max: ₹{r.get('max_price')} | Modal: ₹{r.get('modal_price')}\n"
        )
    return "\n".join(lines)
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

MANDI_API_KEY = os.getenv("MANDI_API_KEY")
CACHE_FILE = "app/mandi_cache.json"

def get_mandi_prices(state="West Bengal", district="Malda"):
    try:
        url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
        params = {
            "api-key": MANDI_API_KEY,
            "format": "json",
            "limit": 10,
            "filters[state.keyword]": state,
            "filters[district.keyword]": district
        }
        response = requests.get(url, params=params, timeout=5)
        data = response.json()
        records = data.get("records", [])
        if records:
            # Save to cache for next time
            with open(CACHE_FILE, "w") as f:
                json.dump(records, f)
            return records
        else:
            return load_cache()

    except Exception:
        return load_cache()

def load_cache():
    try:
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return []

def format_mandi_prices(state="West Bengal", district="Malda"):
    records = get_mandi_prices(state, district)
    if not records:
        return "⚠️ Could not fetch mandi prices right now."

    lines = [f"📊 *Mandi Prices — {district}, {state}*\n"]
    for r in records[:5]:
        lines.append(
            f"🌾 *{r.get('commodity')}* at {r.get('market')}\n"
            f"   Min: ₹{r.get('min_price')} | Max: ₹{r.get('max_price')} | Modal: ₹{r.get('modal_price')}\n"
        )
    return "\n".join(lines)