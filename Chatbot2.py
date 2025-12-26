import streamlit as st
import json
import time
import requests # Used for the HTTP requests simulating the API call

# --- Configuration and Constants ---

# IMPORTANT: These variables are provided by the canvas environment.
API_KEY = "" # Leave as-is for the environment to provide the key.
API_URL_BASE = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent"

# Simulate a simple Pre-built Database (Custom Knowledge Base)
# The AI is instructed to check these specific facts first.
PREBUILT_DATABASE = {
    "CEO of Tesla company": "The CEO is Elon Musk, who founded the company in July 1, 2003.",
    "company mission": "Our mission is to build collaborative AI tools for developers.",
    "support email": "For support, please email support@mychatbot.com.",
    "where are you located": "We are located virtually, but our main team is based in Dublin, Ireland.",
    "latest product": "Our latest product is the 'Gemini Code Helper' released last month.",
}

# --- Utility Functions ---

def get_prebuilt_answer(query):
    """
    Checks the query against the simulated custom database.
    """
    query_lower = query.lower()
    for key, answer in PREBUILT_DATABASE.items():
        if key in query_lower:
            return answer
    return None

def call_gemini_api(prompt, use_grounding=True):
    """
    Calls the Gemini API with optional Google Search grounding.
    Implements exponential backoff for retries.
    """
    headers = {'Content-Type': 'application/json'}
    
    # 1. System Instruction: Define the chatbot's persona and rules.
    system_instruction = (
        "You are a helpful and friendly AI assistant. "
        "Your priority is to answer questions concisely and accurately. "
        "If the user asks a question that seems related to the custom knowledge base (e.g., 'CEO', 'mission', 'support'), prioritize that information. "
        "Otherwise, use Google Search grounding for up-to-date, external information. "
        "If using external knowledge, you MUST cite your sources."
    )

    # 2. Payload Construction
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "systemInstruction": {"parts": [{"text": system_instruction}]},
    }
    
    # 3. Add Google Search tool if grounding is enabled
    if use_grounding:
        payload["tools"] = [{"google_search": {}}]

    max_retries = 5
    for attempt in range(max_retries):
        try:
            # Note: In a production Streamlit environment, you would use a dedicated
            # backend or a robust client library. We are simulating the 'fetch'
            # behavior with the requests library here.
            response = requests.post(
                f"{API_URL_BASE}?key={API_KEY}",
                headers=headers,
                data=json.dumps(payload),
                timeout=30 # Set a reasonable timeout
            )
            response.raise_for_status() # Raises an HTTPError for bad responses (4xx or 5xx)
            
            result = response.json()
            candidate = result.get('candidates', [{}])[0]
            
            # Extract Text
            generated_text = candidate.get('content', {}).get('parts', [{}])[0].get('text', 'Error: Could not retrieve response text.')

            # Extract Sources (if grounding was used)
            sources = []
            grounding_metadata = candidate.get('groundingMetadata')
            if grounding_metadata and grounding_metadata.get('groundingAttributions'):
                sources = grounding_metadata['groundingAttributions']
            
            return generated_text, sources

        except requests.exceptions.RequestException as e:
            # Handle API/Network errors
            st.error(f"Network error during API call (Attempt {attempt+1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                sleep_time = 2 ** attempt
                # Do not log retries in the console per instruction
                time.sleep(sleep_time)
            else:
                return "I'm sorry, I'm experiencing technical difficulties and cannot connect to the service right now. Please try again later.", []
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
            return "An unexpected error occurred while processing the response.", []
            
    return "I'm sorry, I failed to get a response after multiple retries.", []


# --- Streamlit Application Layout ---

st.set_page_config(page_title="Gemini Knowledge Chatbot", layout="wide")

st.markdown(
    """
    <style>
    /* Styling to make the chat UI cleaner */
    .stApp {
        background-color: #f0f2f6;
    }
    .chat-container {
        max-width: 800px;
        margin: 0 auto;
    }
    .stChatMessage {
        border-radius: 1rem;
        padding: 0.5rem 1rem;
        margin-bottom: 0.75rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }
    .user-message {
        background-color: #e6f7ff;
        align-self: flex-end;
    }
    .ai-message {
        background-color: #ffffff;
        align-self: flex-start;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💡 Gemini Multi-Source Chatbot")
st.caption("I can answer questions using a custom knowledge base (like 'CEO of this company') or search the web for real-time information.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Main Chat Logic ---

if prompt := st.chat_input("Ask me a question..."):
    # 1. Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🙋‍♂️"):
        st.markdown(prompt)

    # 2. Check Custom Database First
    custom_answer = get_prebuilt_answer(prompt)
    
    if custom_answer:
        # Response from custom database
        full_response = custom_answer + "\n\n*(Source: Internal Knowledge Base)*"
        
        # Display AI response
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(full_response)
        
        # Update session state with AI response
        st.session_state.messages.append({"role": "assistant", "content": full_response})

    else:
        # 3. Fallback to Gemini with Google Search Grounding
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("Searching the web and generating response..."):
                response_text, sources_list = call_gemini_api(prompt)
                
                final_output = response_text
                
                # Append sources if available
                if sources_list:
                    final_output += "\n\n---\n**Sources:**\n"
                    # Limit to top 3 unique sources
                    unique_sources = {}
                    for source in sources_list:
                        uri = source.get('web', {}).get('uri')
                        title = source.get('web', {}).get('title', uri)
                        if uri:
                            unique_sources[uri] = title
                    
                    for uri, title in list(unique_sources.items())[:3]:
                        # Streamlit markdown auto-formats [Title](URI) as a link
                        final_output += f"- [{title}]({uri})\n"

                st.markdown(final_output)

            # Update session state with AI response
            st.session_state.messages.append({"role": "assistant", "content": final_output})

# Display the custom DB instructions in the sidebar for context
st.sidebar.header("Custom Knowledge Base Test")
st.sidebar.info(
    "Try asking about these specific topics to see the custom database in action:"
    "\n\n- 'What is the company mission?'"
    "\n- 'What is the CEO of this company?'"
    "\n- 'What is the latest product?'"
    "\n\nFor anything else (e.g., 'What is the capital of France?'), the AI will use Google Search."
)
