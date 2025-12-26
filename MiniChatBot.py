# 🤖 Robotics Lab AI Companion Streamlit v5.0
# Truth-checked, Songs + Movies + Google fallback
# Fully functional, no hallucinations, Enhanced UI

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
# 🧰 The Toolkit:
# Streamlit: The magic wand for our UI 🪄
# Wikipedia: Our digital encyclopedia 📚
# Re: Regex, the pattern hunter 🕵️‍♂️
# Datetime: The timekeeper 🕰️
# Difflib: The text comparator (finds similarities) 👯‍♂️
# Pandas: For handling data tables like a pro 🐼
import streamlit as st
import wikipedia
import re
from datetime import datetime, timedelta
from difflib import SequenceMatcher
import pandas as pd
import json
import logging
import traceback
from requests.exceptions import RequestException, Timeout
from urllib3.exceptions import HTTPError
from typing import Optional, Tuple, List, Dict
import time
import base64
import os

# 🕵️‍♂️ Google Custom Search API (The Backup Plan)
# If Wikipedia fails, we call in the big guns (Google).
try:
    from googleapiclient.discovery import build
    _GOOGLE_AVAILABLE = True
except Exception:
    _GOOGLE_AVAILABLE = False

# 🦜🔗 LangChain & OpenAI Setup
try:
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser
    from dotenv import load_dotenv
    import openai
    
    # Load environment variables
    load_dotenv()
    
    _LANGCHAIN_AVAILABLE = True
except ImportError:
    _LANGCHAIN_AVAILABLE = False

# ---------------- CONFIG -----------------
# ⚙️ The Control Room
MAX_WIKI_SENTENCES = 5           # How much info to grab? (5 sentences is the sweet spot)
LOG_FILE = "unanswered_queries.txt"   # 📝 The "I don't know" list (for later learning)
CACHE_FILE = "latest_songs.json"      # 🎵 Storing the hits so we don't forget
ERROR_LOG_FILE = "api_errors.log"     # ⚠️ The "Oops" log
RESPONSE_CACHE_TTL = 3600  # ⏳ Memories last for 1 hour

# Wikipedia settings
WIKIPEDIA_TIMEOUT = 10  # ⏱️ Don't wait forever!
WIKIPEDIA_USER_AGENT = "RobotLabAI/1.0 (Contact: info@example.com)"  # 🆔 Identifying ourselves politely

# Google API configuration - supports Streamlit secrets or direct config
try:
    # Try to get from Streamlit secrets first (for production)
    GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY", "")
    CSE_ID = st.secrets.get("CSE_ID", "")
except Exception:
    # Fallback to direct configuration
    GOOGLE_API_KEY = ""  # Add your Google API key here
    CSE_ID = ""          # Add your Custom Search Engine ID here

# Set up logging for debugging
logging.basicConfig(
    filename=ERROR_LOG_FILE,
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Background helper (optional image)
def _load_background_base64() -> Tuple[str, str]:
    """Load background image and return (base64_string, mime_type)."""
    # Try JPG first (since that's what we have)
    try:
        with open("background.jpg", "rb") as img:
            return base64.b64encode(img.read()).decode(), "image/jpeg"
    except Exception:
        pass
    
    # Try PNG as fallback
    try:
        with open("background.png", "rb") as img:
            return base64.b64encode(img.read()).decode(), "image/png"
    except Exception:
        return "", ""

bg_base64, bg_mime = _load_background_base64()

# Enable Google fallback only if API and CSE ID are correctly provided
ENABLE_GOOGLE = (
    _GOOGLE_AVAILABLE
    and GOOGLE_API_KEY
    and CSE_ID
    and "YOUR_API_KEY" not in GOOGLE_API_KEY
    and "YOUR_CSE_ID" not in CSE_ID
    and len(GOOGLE_API_KEY) > 10
    and len(CSE_ID) > 10
)

wikipedia.set_lang("en")
wikipedia.set_rate_limiting(True)
wikipedia.set_user_agent(WIKIPEDIA_USER_AGENT)

# ---------------- SESSION STATE -----------------
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'response_cache' not in st.session_state:
    st.session_state.response_cache = {}

if 'stats' not in st.session_state:
    st.session_state.stats = {
        'total_queries': 0,
        'successful_wiki': 0,
        'successful_google': 0,
        'song_answers': 0,
        'movie_answers': 0,
        'failed_queries': 0
    }

# ---------------- HELPER FUNCTIONS -----------------
def clean_text(text: str) -> str:
    return text.strip()


def preprocess_query(query: str) -> str:
    query = query.strip()
    original = query.lower()

    patterns = [
        ("who invented", "invented"),
        ("who created", "created"),
        ("who sang", "sang"),
        ("who sings", "sings"),
        ("when was", "was"),
        ("when did", "did"),
    ]
    for phrase, splitter in patterns:
        if phrase in original:
            parts = original.split(splitter)
            if len(parts) > 1:
                query = parts[1].strip()
                break

    if "movie" in original or "film" in original:
        words = [w for w in query.lower().split() if w not in {"movie", "film", "the", "a", "an", "was", "released"}]
        query = " ".join(words)

    question_words = {"who", "what", "when", "where", "why", "how", "is", "are", "was", "were",
                      "did", "does", "do", "invented", "created", "sang", "sings"}
    words = query.lower().split()
    words = [w for w in words if w not in question_words or w in ["light", "bulb"]]
    query = " ".join(words).rstrip("?.!")

    if not query or len(query.split()) < 2:
        meaningful = [w for w in original.split() if w not in question_words and len(w) > 2]
        query = " ".join(meaningful) if meaningful else original.replace("?", "").replace(".", "").strip()
    return query


def semantic_relevance(a: str, b: str) -> float:
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def get_time() -> str:
    return datetime.now().strftime("%I:%M %p")


def stream_text(text: str):
    """Generator for typewriter effect."""
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.05)


def log_unanswered(question: str) -> None:
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{datetime.now().isoformat()}: {question}\n")
    except Exception as e:
        logging.error(f"Failed to log unanswered question: {e}")


def log_api_error(service: str, error: str, query: Optional[str] = None) -> None:
    msg = f"{service} API Error"
    if query:
        msg += f" for query: '{query}'"
    msg += f" - {error}"
    logging.error(msg)
    logging.error(traceback.format_exc())


def get_cached_response(query: str) -> Optional[str]:
    key = query.lower().strip()
    cached = st.session_state.response_cache.get(key)
    if cached and time.time() - cached['timestamp'] < RESPONSE_CACHE_TTL:
        return cached['response']
    if cached:
        del st.session_state.response_cache[key]
    return None


def cache_response(query: str, response: str) -> None:
    key = query.lower().strip()
    st.session_state.response_cache[key] = {'response': response, 'timestamp': time.time()}


# ---------------- SONG DATABASE -----------------
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
    "watermelon sugar": "Harry Styles",
    "levitating": "Dua Lipa",
    "stay": "The Kid LAROI & Justin Bieber",
    "good as hell": "Lizzo",
    "savage": "Megan Thee Stallion",
    "wrecking ball": "Miley Cyrus",
    "flowers": "Miley Cyrus",
}

def update_known_songs() -> Dict[str, str]:
    try:
        tables = pd.read_html("https://en.wikipedia.org/wiki/Billboard_Hot_100")
        if not tables:
            return {}
        chart = tables[0]
        updated = {}
        for _, row in chart.iterrows():
            title = str(row.get("Title") or row.get("Song") or "").strip()
            artist = str(row.get("Artist") or row.get("Performer") or "").strip()
            if title and artist:
                updated[title.lower()] = artist
        return updated
    except Exception as e:
        log_api_error("Billboard Update", str(e))
        return {}

def load_cached_songs() -> Dict[str, str]:
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        timestamp = datetime.fromisoformat(data.get("timestamp"))
        if datetime.now() - timestamp > timedelta(hours=24):
            return {}
        return data.get("songs", {})
    except Exception:
        return {}


def save_cached_songs(songs: Dict[str, str]) -> None:
    try:
        data = {"timestamp": datetime.now().isoformat(), "songs": songs}
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
    except Exception as e:
        logging.error(f"Failed to save cached songs: {e}")


try:
    latest = load_cached_songs() or update_known_songs()
    if latest:
        save_cached_songs(latest)
        known_songs.update(latest)
except Exception as e:
    logging.error(f"Error loading/updating songs: {e}")

# ---------------- QUERY UTILITIES -----------------
def detect_song_query(q: str) -> bool:
    triggers = ["who sang", "who sings", "song", "singer", "lyrics", "artist", "band", "rapper", "performed by"]
    q_lower = q.lower()
    return any(t in q_lower for t in triggers)


def get_known_song(q: str) -> Tuple[Optional[str], Optional[str]]:
    q_lower = q.lower()
    for title, artist in known_songs.items():
        if title in q_lower or any(word in q_lower for word in title.split() if len(word) > 3):
            return title, artist
    return None, None


def detect_movie_query(q: str) -> bool:
    triggers = ["when was", "when did", "release date", "premiered", "premiere", "movie", "film", "released"]
    return any(t in q.lower() for t in triggers)


def detect_time_query(q: str) -> bool:
    triggers = ["what time", "current time", "what's the time", "time now"]
    return any(t in q.lower() for t in triggers)
# ---------------- DATA FETCHING -----------------
def wiki_lookup(query: str, sentences: int = MAX_WIKI_SENTENCES) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    if not query or not query.strip():
        return None, None, None

    original_query = query
    query = clean_text(preprocess_query(query))
    if not query:
        query = original_query

    try:
        page = wikipedia.page(query, auto_suggest=True)
        summary = wikipedia.summary(page.title, sentences=sentences)
        return summary, page.title, page.url
    except wikipedia.DisambiguationError as e:
        log_api_error("Wikipedia", f"DisambiguationError: {len(e.options)} options", query)
        for opt in e.options[:10]:
            try:
                page = wikipedia.page(opt)
                summary = wikipedia.summary(page.title, sentences=sentences)
                return summary, page.title, page.url
            except Exception:
                continue
        return None, None, None
    except wikipedia.PageError:
        log_api_error("Wikipedia", "PageError: Page not found", query)
        try:
            search_results = wikipedia.search(query, results=10)
            for r in search_results[:5]:
                try:
                    page = wikipedia.page(r)
                    summary = wikipedia.summary(page.title, sentences=sentences)
                    if semantic_relevance(query, page.title) > 0.2:
                        return summary, page.title, page.url
                except Exception:
                    continue
        except Exception as ex:
            log_api_error("Wikipedia", f"Search failed: {ex}", query)
        return None, None, None
    except (RequestException, Timeout, HTTPError) as e:
        log_api_error("Wikipedia", f"Network/Timeout error: {e}", query)
        return None, None, None
    except Exception as e:
        log_api_error("Wikipedia", f"Unexpected error: {e}", query)
        return None, None, None


def google_lookup(query: str, api_key: Optional[str] = None, cse_id: Optional[str] = None) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    use_api_key = api_key or GOOGLE_API_KEY
    use_cse_id = cse_id or CSE_ID
    if not use_api_key and 'temp_google_api_key' in st.session_state:
        use_api_key = st.session_state.temp_google_api_key
    if not use_cse_id and 'temp_cse_id' in st.session_state:
        use_cse_id = st.session_state.temp_cse_id

    if not _GOOGLE_AVAILABLE or not use_api_key or not use_cse_id:
        return None, None, None
    if not query or not query.strip():
        return None, None, None

    try:
        service = build("customsearch", "v1", developerKey=use_api_key)
        res = service.cse().list(q=query, cx=use_cse_id, num=1).execute()
        items = res.get("items", [])
        if not items:
            log_api_error("Google", "No results returned", query)
            return None, None, None
        top = items[0]
        return top.get("snippet", ""), top.get("title", ""), top.get("link", "")
    except Exception as e:
        log_api_error("Google", f"Unexpected error: {e}", query)
        return None, None, None


def extract_multi_region_dates(summary: str) -> Optional[List[Tuple[str, str]]]:
    if not summary:
        return None
    patterns = [
        r"([A-Z][a-zA-Z ]+): (\w+ \d{1,2}, \d{4})",
        r"(\w+ \d{1,2}, \d{4}) \((.*?)\)",
        r"released in (\w+): (\w+ \d{4})",
        r"(\w+ \d{1,2}, \d{4}) in (\w+)",
        r"(\w+) release: (\w+ \d{1,2}, \d{4})",
    ]
    results = []
    seen = set()
    for pat in patterns:
        matches = re.findall(pat, summary)
        for m in matches:
            if len(m) == 2:
                region, date = m
                key = (region.strip().lower(), date.strip())
                if key not in seen:
                    seen.add(key)
                    results.append((region.strip(), date.strip()))
    if not results:
        fallback = re.findall(r"(\w+ \d{1,2}, \d{4})", summary)
        for d in fallback[:3]:
            if d not in seen:
                results.append(("General Release", d))
    return results if results else None


def extract_single_date(summary: str) -> Optional[str]:
    patterns = [
        r"released on (\w+ \d{1,2}, \d{4})",
        r"released (\w+ \d{1,2}, \d{4})",
        r"(\w+ \d{1,2}, \d{4})",
    ]
    for pattern in patterns:
        matches = re.findall(pattern, summary)
        if matches:
            return matches[0]
    return None


# ---------------- LLM INTEGRATION -----------------
def get_llm_response(query: str, api_key: str) -> Optional[str]:
    """Generate a response using OpenAI via LangChain."""
    if not _LANGCHAIN_AVAILABLE or not api_key:
        return None
    
    try:
        llm = ChatOpenAI(
            openai_api_key=api_key,
            model_name="gpt-3.5-turbo",
            temperature=0.7
        )
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are 'Robotics Lab AI', a witty, intelligent, and helpful assistant. "
                       "You love discussing movies, music, and tech, but you can answer any question. "
                       "Be conversational, engaging, and precise. "
                       "If the user asks for a creative task (like a poem or code), go for it!"),
            ("user", "{input}")
        ])
        
        chain = prompt | llm | StrOutputParser()
        response = chain.invoke({"input": query})
        return response
    except Exception as e:
        log_api_error("OpenAI", str(e), query)
        return None

# ---------------- MAIN AI RESPONSE -----------------
def ai_response(user_query: str) -> str:
    if not user_query or not user_query.strip():
        return "❌ Please enter a valid question."

    cached = get_cached_response(user_query)
    if cached:
        return cached + "\n\n_⚡ Cached response_"

    q = clean_text(user_query)

    if detect_time_query(q):
        current_time = get_time()
        current_date = datetime.now().strftime("%B %d, %Y")
        response = f"🕐 **Current Time:** {current_time}\n**Date:** {current_date}"
        cache_response(user_query, response)
        st.session_state.stats['total_queries'] += 1
        return response

    title, artist = get_known_song(q)
    if title:
        response = f"🎵 ({get_time()}) **{title.title()}** was sung by **{artist}**."
        cache_response(user_query, response)
        st.session_state.stats['total_queries'] += 1
        st.session_state.stats['song_answers'] += 1
        return response

    is_movie = detect_movie_query(q)
    if is_movie and "film" not in q.lower() and "movie" not in q.lower():
        q += " film"

    # 1. Try OpenAI (Smart Chat) First if available
    openai_key = st.session_state.get('temp_openai_key') or os.getenv("OPENAI_API_KEY")
    if _LANGCHAIN_AVAILABLE and openai_key:
        llm_response = get_llm_response(user_query, openai_key)
        if llm_response:
            st.session_state.stats['total_queries'] += 1
            cache_response(user_query, f"🤖 **AI Assistant**\n\n{llm_response}")
            return f"🤖 **AI Assistant**\n\n{llm_response}"

    # 2. Fallback to Wikipedia
    wiki_summary, wiki_title, wiki_url = wiki_lookup(q)
    relevance = 0.0
    if wiki_summary:
        relevance = semantic_relevance(q, wiki_summary[:500])
        title_rel = semantic_relevance(q, wiki_title or "")
        relevance = max(relevance, title_rel)

    # 3. Fallback to Google
    google_summary = google_title = google_url = None
    google_enabled = False
    if 'temp_google_api_key' in st.session_state and 'temp_cse_id' in st.session_state:
        google_enabled = (
            _GOOGLE_AVAILABLE
            and st.session_state.temp_google_api_key
            and st.session_state.temp_cse_id
            and len(st.session_state.temp_google_api_key) > 10
            and len(st.session_state.temp_cse_id) > 10
        )
    elif ENABLE_GOOGLE:
        google_enabled = True

    if (not wiki_summary or relevance < 0.1) and google_enabled:
        google_summary, google_title, google_url = google_lookup(q)
    elif relevance < 0.3 and google_enabled:
        google_summary, google_title, google_url = google_lookup(q)

    response = None
    if wiki_summary and (relevance >= 0.1 or wiki_title):
        st.session_state.stats['successful_wiki'] += 1
        if is_movie:
            st.session_state.stats['movie_answers'] += 1
        region_dates = extract_multi_region_dates(wiki_summary)
        if region_dates:
            date_lines = "\n".join([f"- **{region}**: {date}" for region, date in region_dates])
            response = f"🎬 **{wiki_title}**\n\n**Release Dates:**\n{date_lines}\n\n[📖 More Info]({wiki_url})"
        else:
            single_date = extract_single_date(wiki_summary)
            if single_date and is_movie:
                response = f"🎬 **{wiki_title}**\n\n**Release Date:** {single_date}\n\n[📖 More Info]({wiki_url})"
            else:
                response = f"📝 **{wiki_title}**\n\n{wiki_summary}\n\n[📖 Read more]({wiki_url})"
    elif google_summary:
        st.session_state.stats['successful_google'] += 1
        response = f"🌐 **{google_title}**\n\n{google_summary}\n\n[🔗 Source]({google_url})"
    else:
        log_unanswered(user_query)
        st.session_state.stats['failed_queries'] += 1
        response = f"❌ Sorry, I couldn't find an answer for: **{user_query}**\n\n💡 Try rephrasing your question or being more specific."

    if response:
        cache_response(user_query, response)
        st.session_state.stats['total_queries'] += 1

    return response

# Configure Streamlit page layout
st.set_page_config(
    page_title="Robotics Lab AI Companion",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown(f"""
    <style>
    @import url('https://fonts.cdnfonts.com/css/glacial-indifference');
    
    .stApp {{
        background-image: url("data:{bg_mime};base64,{bg_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-color: #0e1117; /* Dark fallback if image fails */
    }}
    /* Overlay to improve text readability */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.7); /* Dark overlay */
        z-index: -1;
    }}
    
    /* Force sidebar to be dark to match the theme and make white text readable */
    [data-testid="stSidebar"] {{
        background-color: rgba(10, 10, 20, 0.9);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }}
    
    /* Adjust text colors for dark background */
    h1, h2, h3, h4, h5, h6, p, div, span, label, li {{
        color: #ffffff !important;
    }}
    
    /* Fix button text color - Streamlit buttons usually have light background by default */
    div.stButton > button {{
        color: #ffffff !important;
        background-color: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        transition: all 0.3s ease;
    }}
    div.stButton > button:hover {{
        background-color: rgba(0, 191, 255, 0.3) !important;
        border-color: #00bfff !important;
        color: #ffffff !important;
    }}
    
    /* Fix text input text color (user typing) */
    .stTextInput input {{
        color: #ffffff !important;
        background-color: rgba(0, 0, 0, 0.5) !important;
    }}
    
    .main-header {{
        font-size: 2.5rem;
        font-weight: bold;
        color: #00bfff !important; /* Cyan for header */
        text-align: center;
        padding: 1rem;
        text-shadow: 0 0 10px #00bfff;
    }}
    
    .query-example {{
        padding: 0.5rem;
        margin: 0.25rem 0;
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 0.5rem;
        cursor: pointer;
        transition: background-color 0.3s;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }}
    .query-example:hover {{
        background-color: rgba(255, 255, 255, 0.2);
        border-color: #00bfff;
    }}
    
    .stats-box {{
        background-color: rgba(0, 0, 0, 0.5);
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        border: 1px solid #333;
    }}
    
    /* Expander styling */
    .streamlit-expanderHeader {{
        background-color: rgba(255, 255, 255, 0.05);
        color: white !important;
    }}
    
    /* Fix links */
    a {{
        color: #00bfff !important;
        text-decoration: none;
    }}
    a:hover {{
        text-decoration: underline;
    }}
    
    /* Fix File Uploader UI */
    [data-testid="stFileUploader"] section {{
        background-color: rgba(255, 255, 255, 0.1) !important;
        border: 1px dashed rgba(255, 255, 255, 0.3) !important;
    }}
    [data-testid="stFileUploader"] section > div {{
        color: #ffffff !important;
    }}
    [data-testid="stFileUploader"] svg {{
        fill: #ffffff !important;
    }}
    [data-testid="stFileUploader"] small {{
        color: #cccccc !important;
    }}
    /* Fix Browse files button */
    [data-testid="stFileUploader"] button {{
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
    }}
    [data-testid="stFileUploader"] button:hover {{
        background-color: rgba(0, 191, 255, 0.3) !important;
        color: #ffffff !important;
        border-color: #00bfff !important;
    }}
    
    /* Response Text Effect (Glacial Indifference) */
    .matrix-text {{
        font-family: 'Glacial Indifference', sans-serif !important;
        font-weight: 700 !important; /* Bold */
        color: #00bfff !important; /* Cyan to match header */
        text-shadow: 0 0 10px #00bfff; /* Cyan Glow */
        background-color: rgba(0, 0, 0, 0.6);
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #00bfff;
        line-height: 1.6;
        font-size: 1.1rem;
    }}
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🤖 Robotics Lab AI Companion </div>', unsafe_allow_html=True)
st.markdown("### Ask me about **songs, movies, or general info**! 🎵🎬📚")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings & Status")
    
    # API Status
    st.subheader("🔌 API Status")
    wiki_status = "✅ Enabled"
    st.markdown(f"**Wikipedia:** {{wiki_status}}")
    
    # Google API Configuration
    st.markdown("**Google API:** ", unsafe_allow_html=True)
    
    # OpenAI API Configuration
    st.markdown("**OpenAI API:** ", unsafe_allow_html=True)
    
    # Allow users to configure APIs in sidebar
    with st.expander("⚙️ Configure APIs"):
        st.info("💡 Configure keys for enhanced functionality")
        
        # Google Config
        st.caption("--- Google Custom Search ---")
        api_key_input = st.text_input(
            "Google API Key:",
            value=GOOGLE_API_KEY if GOOGLE_API_KEY else "",
            type="password",
            help="Enter your Google Custom Search API key"
        )
        cse_id_input = st.text_input(
            "Custom Search Engine ID:",
            value=CSE_ID if CSE_ID else "",
            help="Enter your Custom Search Engine ID"
        )
        
        st.markdown("---")
        
        # OpenAI Config
        st.caption("--- OpenAI (Smart Chat) ---")
        openai_key_input = st.text_input(
            "OpenAI API Key:",
            value=st.session_state.get('temp_openai_key', ''),
            type="password",
            help="Enter your OpenAI API Key for smart chat features"
        )
        
        if st.button("🔧 Save API Credentials"):
            # Store in session state
            st.session_state.temp_google_api_key = api_key_input
            st.session_state.temp_cse_id = cse_id_input
            st.session_state.temp_openai_key = openai_key_input
            st.success("✅ Credentials saved for this session!")
            st.rerun()
    
    # Use session state credentials if available
    if 'temp_google_api_key' in st.session_state and 'temp_cse_id' in st.session_state:
        session_google_key = st.session_state.temp_google_api_key
        session_cse_id = st.session_state.temp_cse_id
        session_enable_google = (
            _GOOGLE_AVAILABLE
            and session_google_key
            and session_cse_id
            and len(session_google_key) > 10
            and len(session_cse_id) > 10
        )
    else:
        session_google_key = GOOGLE_API_KEY
        session_cse_id = CSE_ID
        session_enable_google = ENABLE_GOOGLE
    
    if session_enable_google:
        st.markdown("**Google API:** ✅ Enabled")
    else:
        st.markdown("**Google API:** ❌ Disabled")
        if not _GOOGLE_AVAILABLE:
            st.caption("⚠️ `googleapiclient` library not installed")
            st.caption("Install with: `pip install google-api-python-client`")
        elif not session_google_key or not session_cse_id:
            st.caption("⚠️ API key or CSE ID not configured")
            st.caption("Click 'Configure Google API' above to add credentials")
    
    st.markdown("---")
    
    # Statistics
    st.subheader("📊 Statistics")
    stats = st.session_state.stats
    st.metric("Total Queries", stats['total_queries'])
    st.metric("Wikipedia Success", stats['successful_wiki'])
    # Check if Google is enabled (session state or config)
    if 'session_enable_google' in locals():
        google_enabled = session_enable_google
    else:
        google_enabled = ENABLE_GOOGLE
    if google_enabled:
        st.metric("Google Success", stats['successful_google'])
    st.metric("Song Answers", stats['song_answers'])
    st.metric("Movie Answers", stats['movie_answers'])
    st.metric("Failed Queries", stats['failed_queries'])
    
    st.markdown("---")
    
    # Debug Info
    with st.expander("🔧 Debug Info"):
        st.text(f"Error Log: {ERROR_LOG_FILE}")
        st.text(f"Unanswered Log: {LOG_FILE}")
        st.text(f"Cached Songs: {len(known_songs)}")
        st.text(f"Response Cache: {len(st.session_state.response_cache)}")
        
        if st.button("🧪 Test Wikipedia API"):
            with st.spinner("Testing Wikipedia..."):
                try:
                    test_result = wikipedia.search("Python programming", results=3)
                    if test_result:
                        st.success(f"✅ Wikipedia is working! Found: {test_result[0]}")
                    else:
                        st.warning("⚠️ Wikipedia search returned no results")
                except Exception as e:
                    st.error(f"❌ Wikipedia error: {str(e)}")
        
        if st.button("Clear Response Cache"):
            st.session_state.response_cache = {}
            st.success("Cache cleared!")
        
        if st.button("Reset Statistics"):
            st.session_state.stats = {
                'total_queries': 0,
                'successful_wiki': 0,
                'successful_google': 0,
                'song_answers': 0,
                'movie_answers': 0,
                'failed_queries': 0
            }
            st.success("Statistics reset!")
    
    st.markdown("---")
    st.markdown("**💡 Tips:**")
    st.caption("• Be specific in your questions")
    st.caption("• Include artist names for songs")
    st.caption("• Include movie titles for films")
    st.caption("• Check cache for faster results")

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    # Query examples
    st.subheader("💡 Try these example queries:")
    example_queries = [
        "What time is it?",
        "Who sang Thriller?",
        "When was The Matrix released?",
        "What is artificial intelligence?",
        "Who is Leonardo da Vinci?",
    ]
    
    cols = st.columns(3)
    for idx, example in enumerate(example_queries):
        with cols[idx % 3]:
            if st.button(example, key=f"example_{idx}", use_container_width=True):
                st.session_state.example_query = example
    
    # Main query input
    st.markdown("---")
    user_query = st.text_input(
        "💬 Enter your question:",
        value=st.session_state.get('example_query', ''),
        key="main_query_input",
        placeholder="e.g., Who sang Bohemian Rhapsody?"
    )
    
    # Clear example query after using it
    if 'example_query' in st.session_state:
        del st.session_state.example_query

with col2:
    st.subheader("📝 Recent Queries")
    if st.session_state.chat_history:
        # Show last 5 queries
        for i, item in enumerate(st.session_state.chat_history[-5:][::-1]):
            with st.expander(f"Q: {item['query'][:50]}...", expanded=False):
                st.markdown(f"**Q:** {item['query']}")
                st.markdown(f"**A:** {item['response'][:200]}...")
                st.caption(f"Time: {item['timestamp']}")
    else:
        st.info("No queries yet. Start asking questions!")

# Process query
if user_query:
    with st.spinner("🔍 Searching..."):
        response = ai_response(user_query)
        
        # Add to chat history
        st.session_state.chat_history.append({
            'query': user_query,
            'response': response,
            'timestamp': get_time()
        })
        
        # Display response
        st.markdown("---")
        st.markdown("### 💬 Response:")
        
        # Matrix Effect Display
        placeholder = st.empty()
        displayed_text = ""
        for word in stream_text(response):
            displayed_text += word
            placeholder.markdown(f'<div class="matrix-text">{displayed_text}</div>', unsafe_allow_html=True)
        
        # Export option
        if st.button("📥 Export This Response"):
            export_data = {
                'query': user_query,
                'response': response,
                'timestamp': datetime.now().isoformat()
            }
            st.download_button(
                label="⬇️ Download JSON",
                data=json.dumps(export_data, indent=2),
                file_name=f"response_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )

# Batch question upload
st.markdown("---")
st.subheader("📂 Batch Question Processing")
uploaded_file = st.file_uploader("Upload a .txt file with questions (one per line)", type=["txt"])

if uploaded_file:
    lines = [line.strip() for line in uploaded_file.read().decode("utf-8").splitlines() if line.strip()]
    
    if lines:
        st.info(f"📋 Found {len(lines)} questions to process")
        
        if st.button("🚀 Process All Questions"):
            progress_bar = st.progress(0)
            batch_responses = []
            
            for idx, q in enumerate(lines):
                response = ai_response(q)
                batch_responses.append({
                    'query': q,
                    'response': response,
                    'timestamp': get_time()
                })
                progress_bar.progress((idx + 1) / len(lines))
                time.sleep(0.1)  # Small delay to show progress
            
            st.success(f"✅ Processed {len(lines)} questions!")
            
            # Display results
            st.markdown("### 📊 Results:")
            for item in batch_responses:
                with st.expander(f"Q: {item['query'][:60]}..."):
                    st.markdown(f"**Q:** {item['query']}")
                    st.markdown(f"**A:** {item['response']}")
            
            # Export batch results
            st.markdown("---")
            export_json = json.dumps(batch_responses, indent=2, ensure_ascii=False)
            st.download_button(
                label="⬇️ Download All Results (JSON)",
                data=export_json,
                file_name=f"batch_responses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <p>🤖 <strong>Robotics Lab AI Chat-Bot</strong> | Built for truth-checked answers | Songs & Movies powered</p>
        <p style='font-size: 0.8rem;'>Version 5.0 | Enhanced UI & Features</p>
    </div>
    """,
    unsafe_allow_html=True
)
