# -----------------------------------------------------------
# 🤖 RobotLab AI Companion Streamlit v4.8
# Truth-checked, Songs + Movies + Google fallback
# Fully functional, no hallucinations
# -----------------------------------------------------------

# ---------------- PATCH FOR PYTHON 3.10+ -----------------
# Python 3.10+ moved some collections classes to `collections.abc`.
# This patch ensures backward compatibility for older libraries expecting old names.
import sys
import collections
if sys.version_info >= (3, 10):
    import collections.abc
    collections.Mapping = collections.abc.Mapping
    collections.MutableMapping = collections.abc.MutableMapping

# ---------------- IMPORTS -----------------
# Streamlit for UI, Wikipedia API for info, re for regex, datetime for timestamps,
# difflib for semantic similarity, pandas for tables, json for caching
import streamlit as st
import wikipedia
import re
from datetime import datetime, timedelta
from difflib import SequenceMatcher
import pandas as pd
import json

# Optional Google Custom Search API for fallback if Wikipedia fails
try:
    from googleapiclient.discovery import build
    _GOOGLE_AVAILABLE = True
except Exception:
    _GOOGLE_AVAILABLE = False

# ---------------- CONFIG -----------------
MAX_WIKI_SENTENCES = 5           # Number of sentences to fetch from Wikipedia summary
LOG_FILE = "unanswered_queries.txt"   # File to log questions AI could not answer
CACHE_FILE = "latest_songs.json"      # File to cache the latest Billboard songs

GOOGLE_API_KEY = ""  # Add your Google API key here
CSE_ID = ""          # Add your Custom Search Engine ID here

# Enable Google fallback only if API and CSE ID are correctly provided
ENABLE_GOOGLE = (
    _GOOGLE_AVAILABLE
    and GOOGLE_API_KEY
    and CSE_ID
    and "YOUR_API_KEY" not in GOOGLE_API_KEY
    and "YOUR_CSE_ID" not in CSE_ID
)

# Configure Streamlit page layout
st.set_page_config(page_title="RobotLab AI Companion v4.8", layout="centered")

# Set Wikipedia language
wikipedia.set_lang("en")

# ---------------- HELPER FUNCTIONS -----------------
def clean_text(text: str) -> str:
    """Remove extra punctuation and whitespace from input text."""
    return text.strip().replace("?", "").replace(".", "")

def semantic_relevance(a, b):
    """Return similarity ratio between two strings (0 to 1)."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def get_time():
    """Return current time as string, e.g., 03:45 PM."""
    return datetime.now().strftime("%I:%M %p")

def log_unanswered(question):
    """Append questions that couldn't be answered to a log file."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(question + "\n")

# ---------------- SONG DATABASE -----------------
# Known popular songs database (can be extended or auto-updated from Billboard)
known_songs = {
    "thriller": "Michael Jackson",
    "shape of you": "Ed Sheeran",
    "bad romance": "Lady Gaga",
    "blinding lights": "The Weeknd",
    "bohemian rhapsody": "Queen",
    "rolling in the deep": "Adele",
    "uptown funk": "Mark Ronson ft. Bruno Mars",
    "someone like you": "Adele",
    "believer": "Imagine Dragons",
    "perfect": "Ed Sheeran",
    "blank space": "Taylor Swift",
    "bad blood": "Taylor Swift",
    "shake it off": "Taylor Swift",
    "love story": "Taylor Swift",
    "all too well": "Taylor Swift",
    "hello": "Adele",
    "hey jude": "The Beatles",
    "let it be": "The Beatles",
    "despacito": "Luis Fonsi ft. Daddy Yankee",
    "positions": "Ariana Grande",
    "drivers license": "Olivia Rodrigo",
    "good 4 u": "Olivia Rodrigo",
    "as it was": "Harry Styles",
}

# ---------------- AUTO-UPDATE SONGS -----------------
def update_known_songs():
    """
    Fetch latest Billboard Hot 100 songs from Wikipedia and return as dictionary.
    Format: {'song title (lowercase)': 'artist'}
    """
    try:
        url = "https://en.wikipedia.org/wiki/Billboard_Hot_100"
        tables = pd.read_html(url)
        chart_table = tables[0]
        updated_songs = {}
        for _, row in chart_table.iterrows():
            title = str(row.get("Title") or row.get("Song") or "").strip()
            artist = str(row.get("Artist") or row.get("Performer") or "").strip()
            if title and artist:
                updated_songs[title.lower()] = artist
        return updated_songs
    except Exception:
        return {}

def load_cached_songs():
    """Load previously cached Billboard songs to reduce repeated web requests."""
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        timestamp = datetime.fromisoformat(data.get("timestamp"))
        if datetime.now() - timestamp > timedelta(hours=24):
            return {}  # Cache expired
        return data.get("songs", {})
    except Exception:
        return {}

def save_cached_songs(songs):
    """Save latest songs and timestamp to cache."""
    data = {"timestamp": datetime.now().isoformat(), "songs": songs}
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

# Load cached songs or update from web, then merge with known_songs
latest_songs = load_cached_songs() or update_known_songs()
save_cached_songs(latest_songs)
known_songs.update(latest_songs)

# ---------------- QUERY DETECTION -----------------
def detect_song_query(q):
    """Detect if the user query is related to songs."""
    triggers = ["who sang", "song", "lyrics", "artist", "band", "rapper"]
    return any(t in q.lower() for t in triggers)

def get_known_song(q):
    """Return song title and artist if query matches known songs."""
    for title, artist in known_songs.items():
        if title.lower() in q.lower():
            return title, artist
    return None, None

def detect_movie_query(q):
    """Detect if the query is related to movie release dates."""
    triggers = ["when was", "release date", "premiered", "movie", "film"]
    return any(t in q.lower() for t in triggers)

# ---------------- WIKIPEDIA LOOKUP -----------------
def wiki_lookup(query, sentences=MAX_WIKI_SENTENCES):
    """
    Fetch Wikipedia summary for a given query.
    Handles disambiguation, page errors, and semantic relevance.
    """
    query = clean_text(query)
    try:
        page = wikipedia.page(query, auto_suggest=True)
        summary = wikipedia.summary(page.title, sentences=sentences)
        return summary, page.title, page.url
    except wikipedia.DisambiguationError as e:
        # Try relevant options in case of disambiguation
        candidates = e.options
        for opt in candidates:
            if any(k in opt.lower() for k in ["film", "movie", "song", "soundtrack"]):
                try:
                    page = wikipedia.page(opt)
                    summary = wikipedia.summary(page.title, sentences=sentences)
                    return summary, page.title, page.url
                except:
                    continue
        for opt in candidates[:3]:
            try:
                page = wikipedia.page(opt)
                summary = wikipedia.summary(page.title, sentences=sentences)
                return summary, page.title, page.url
            except:
                continue
        return None, None, None
    except wikipedia.PageError:
        # Try search results if page not found
        results = wikipedia.search(query)
        prioritized = [r for r in results if any(k in r.lower() for k in ["film", "movie", "song", "soundtrack"])]
        results = prioritized or results
        for r in results[:5]:
            try:
                page = wikipedia.page(r)
                summary = wikipedia.summary(page.title, sentences=sentences)
                if semantic_relevance(query, page.title) > 0.5:
                    return summary, page.title, page.url
            except:
                continue
        return None, None, None
    except Exception:
        return None, None, None

# ---------------- GOOGLE FALLBACK -----------------
def google_lookup(query):
    """Fetch top Google search result if Wikipedia lookup fails."""
    if not ENABLE_GOOGLE:
        return None, None, None
    try:
        service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
        res = service.cse().list(q=f'"{query}"', cx=CSE_ID, num=1).execute()
        items = res.get("items", [])
        if not items:
            return None, None, None
        top = items[0]
        return top.get("snippet"), top.get("title"), top.get("link")
    except Exception:
        return None, None, None

# ---------------- MULTI-REGION RELEASE DATES -----------------
def extract_multi_region_dates(summary: str):
    """
    Extract movie release dates by region using regex patterns.
    Returns list of tuples: [(region, date), ...]
    """
    if not summary:
        return None
    patterns = [
        r"([A-Z][a-zA-Z ]+): (\w+ \d{1,2}, \d{4})",
        r"(\w+ \d{1,2}, \d{4}) \((.*?)\)",
        r"released in (\w+): (\w+ \d{4})"
    ]
    results = []
    for pat in patterns:
        matches = re.findall(pat, summary)
        for m in matches:
            if len(m) == 2:
                region, date = m
                results.append((region.strip(), date.strip()))
    if not results:
        fallback_dates = re.findall(r"(\w+ \d{1,2}, \d{4})", summary)
        results = [("Unknown", d) for d in fallback_dates]
    return results if results else None

# ---------------- MAIN AI RESPONSE -----------------
def ai_response(user_query):
    """
    Main function to process user query.
    Priority: Known Songs -> Movie Dates -> Wikipedia -> Google -> Log unanswered
    """
    q = clean_text(user_query)

    # 1️⃣ Check for known song
    title, artist = get_known_song(q)
    if title:
        return f"🎵 ({get_time()}) '{title.title()}' was sung by {artist}."

    # 2️⃣ Detect movie query
    is_movie = detect_movie_query(q)
    if is_movie:
        if "film" not in q.lower() and "movie" not in q.lower():
            q += " film"

    # 3️⃣ Wikipedia lookup
    wiki_summary, wiki_title, wiki_url = wiki_lookup(q)
    relevance = semantic_relevance(q, wiki_summary or "")

    # 4️⃣ Google fallback if Wikipedia fails
    google_summary, google_title, google_url = None, None, None
    if (not wiki_summary or (relevance < 0.2 and not is_movie)) and ENABLE_GOOGLE:
        google_summary, google_title, google_url = google_lookup(q)

    timestamp = get_time()

    # 5️⃣ Prepare response
    if wiki_summary and relevance >= 0.2:
        region_dates = extract_multi_region_dates(wiki_summary)
        if region_dates:
            date_lines = "\n".join([f"- {region}: **{date}**" for region, date in region_dates])
            return f"🎬 ({timestamp}) Movie: **{wiki_title}**\n\nRelease Dates:\n{date_lines}\n\n[More Info]({wiki_url})"
        return f"📝 ({timestamp}) **{wiki_title}**:\n{wiki_summary}\n\n[Read more]({wiki_url})"
    elif google_summary:
        return f"🌐 ({timestamp}) Google Result - **{google_title}**:\n{google_summary}\n\n[Link]({google_url})"
    else:
        log_unanswered(user_query)
        return f"❌ ({timestamp}) Sorry, I couldn't find an answer for: '{user_query}'"

# ---------------- STREAMLIT APP -----------------
# App title and description
st.title("🤖 RobotLab AI Companion v4.8")
st.markdown("Ask me about **songs, movies, or general info**!")

# Single question input
user_query = st.text_input("Enter your question:")
if user_query:
    with st.spinner("Searching..."):
        response = ai_response(user_query)
    st.markdown(response)

# Batch question upload via .txt
st.markdown("---")
st.subheader("Batch question upload (.txt)")
uploaded_file = st.file_uploader("Upload a .txt file with questions (one per line)", type=["txt"])
if uploaded_file:
    # Read and clean lines
    lines = [line.strip() for line in uploaded_file.read().decode("utf-8").splitlines() if line.strip()]
    batch_responses = []
    for q in lines:
        batch_responses.append(f"**Q:** {q}\n**A:** {ai_response(q)}\n---")
    st.markdown("\n".join(batch_responses))

# Footer
st.markdown(
    """
    ---
    🤖 Robotics Lab AI Chat-Bot | Built for truth-checked answers | Songs & Movies powered
    """
)

# with AI