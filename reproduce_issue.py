
import wikipedia
import re
from difflib import SequenceMatcher
import logging

# Mock logging
logging.basicConfig(level=logging.INFO)

def log_api_error(service, error, query=None):
    print(f"[{service} ERROR] {error} (Query: {query})")

def clean_text(text: str) -> str:
    return text.strip()

def preprocess_query(query: str) -> str:
    """Preprocess query for better Wikipedia search results."""
    query = query.strip()
    original = query.lower()
    
    # Handle specific question patterns
    if "who invented" in original or "who created" in original:
        parts = original.split("invented")
        if len(parts) > 1:
            query = parts[1].strip()
        else:
            parts = original.split("created")
            if len(parts) > 1:
                query = parts[1].strip()
    
    elif "who sang" in original or "who sings" in original:
        parts = original.split("sang")
        if len(parts) > 1:
            query = parts[1].strip()
        else:
            parts = original.split("sings")
            if len(parts) > 1:
                query = parts[1].strip()
    
    elif "when was" in original or "when did" in original:
        parts = original.split("was")
        if len(parts) > 1:
            query = parts[1].strip()
        else:
            parts = original.split("did")
            if len(parts) > 1:
                query = parts[1].strip()
    
    # For movie queries, extract the title better
    if "movie" in original or "film" in original:
        # Remove "movie" or "film" but keep the title
        words = query.lower().split()
        words = [w for w in words if w not in ["movie", "film", "the", "a", "an", "was", "released"]]
        query = " ".join(words)
    
    # Remove common question words ONLY if they are at the start or auxiliary
    question_words = ["who", "what", "when", "where", "why", "how", "is", "are", "was", "were", "did", "does", "do", "tell", "me", "about"]
    words = query.split()
    
    # Filter out leading question words
    while words and words[0].lower() in question_words:
        words.pop(0)
        
    # Reconstruct query
    query = " ".join(words)
    
    # Remove trailing question marks and periods
    query = query.rstrip("?.!")
    
    # If query is too short or empty, use original (cleaned)
    if not query or len(query) < 2:
        query = original.replace("?", "").replace(".", "").strip()
    
    return query

def semantic_relevance(a: str, b: str) -> float:
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def wiki_lookup(query: str, sentences: int = 5):
    print(f"\n--- Lookup: '{query}' ---")
    if not query or not query.strip():
        return None, None, None
    
    original_query = query
    query = preprocess_query(query)
    query = clean_text(query)
    print(f"Preprocessed: '{query}'")
    
    if not query:
        query = original_query
    
    try:
        # Try direct page lookup first - Trust Wikipedia's redirect handling
        try:
            page = wikipedia.page(query, auto_suggest=True)
            print(f"Direct Page Found: {page.title}")
            # Check if the page title is somewhat relevant to the original query
            # Relaxed check: if query words are in title OR title words in query
            if semantic_relevance(query, page.title) > 0.1 or \
               any(w.lower() in page.title.lower() for w in query.split() if len(w) > 3) or \
               any(w.lower() in query.lower() for w in page.title.split() if len(w) > 3):
                summary = wikipedia.summary(page.title, sentences=sentences)
                return summary, page.title, page.url
            else:
                print(f"Direct page '{page.title}' rejected due to low relevance.")
        except (wikipedia.DisambiguationError, wikipedia.PageError) as e:
            print(f"Direct lookup failed: {type(e).__name__}")

        # Search fallback
        search_queries = [query, original_query]
        if query != original_query:
             if len(query.split()) == 1:
                search_queries.append(f"History of {query}")
        
        for search_query in search_queries:
            print(f"Searching for: '{search_query}'")
            search_results = wikipedia.search(search_query, results=5)
            if not search_results:
                continue
            
            for r in search_results:
                try:
                    # Check relevance BEFORE fetching page to save time, but be generous
                    # If the result title contains our query words, it's a good candidate
                    if any(w.lower() in r.lower() for w in query.split() if len(w) > 3):
                         print(f"Match by keyword: {r}")
                         page = wikipedia.page(r)
                         summary = wikipedia.summary(page.title, sentences=sentences)
                         return summary, page.title, page.url

                    # Otherwise check semantic relevance
                    relevance = semantic_relevance(query, r)
                    print(f"Checking '{r}': Rel={relevance:.2f}")
                    if relevance > 0.2:
                        print(f"Match by relevance: {r}")
                        page = wikipedia.page(r)
                        summary = wikipedia.summary(page.title, sentences=sentences)
                        return summary, page.title, page.url
                except Exception as e:
                    print(f"Error checking '{r}': {e}")
                    continue
                    
        return None, None, None

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None, None, None

# Test Cases
queries = [
    "What is a bond?",
    "Who is the CEO of Google?",
    "Tell me about the movie Matrix",
    "Python programming",
    "Who sang Thriller?",
    "capital of france"
]

for q in queries:
    summary, title, url = wiki_lookup(q)
    if title:
        print(f"RESULT: Found '{title}'")
    else:
        print("RESULT: Not Found")
