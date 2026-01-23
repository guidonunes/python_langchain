# 🚀 AI Financial Analyst: The "Scalper & Strategist" Pipeline

A high-performance financial news analysis agent built with **LangChain**. This project demonstrates a hybrid AI architecture that combines **Groq's LPU speed** for real-time data extraction with **Google Gemini's reasoning** for strategic reporting.

## 🏗 Architecture

The system uses a "Relay Race" pattern to optimize for both cost and latency:

1.  **The Source:** Ingests financial headlines (via `yfinance` or API).
2.  **The Scalper (Groq / Llama 3.3 70B):**
    * **Role:** High-Frequency Trading Algorithm.
    * **Task:** Instantly analyzes sentiment, extracts ticker symbols, and assigns an "Urgency Score" (1-10).
    * **Performance:** ~300 tokens/sec. Sub-second latency.
3.  **The Filter:** Logic gate that discards low-urgency news (saving compute costs).
4.  **The Strategist (Google Gemini Flash/Pro):**
    * **Role:** Senior Portfolio Manager.
    * **Task:** Takes the raw signal + original news to draft a nuanced memo for high-net-worth clients, focusing on the "Why" and portfolio impact.

## ⚡️ Tech Stack

* **Python 3.10+**
* **LangChain:** Orchestration & Chain management.
* **Groq API:** Access to Llama 3.3 on LPU hardware.
* **Google GenAI:** Access to Gemini models.
* **Pydantic:** (Optional) For strict JSON output parsing.

## 🛠 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv langchain_env
    source langchain_env/bin/activate  # Linux/Mac
    # langchain_env\Scripts\activate   # Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install langchain langchain-groq langchain-google-genai python-dotenv yfinance
    ```

4.  **Set up Environment Variables:**
    Create a `.env` file in the root directory:
    ```env
    GROQ_API_KEY=gsk_...
    GEMINI_API_KEY=AIza...
    ```

## 🚀 Usage

Run the main pipeline:

```bash
python lang_chain.py
Example Output
Input: "Tech stocks soar as new AI advancements promise to revolutionize the industry"

1. Groq (The Scalper):

JSON
{
  "sentiment": "BULLISH",
  "tickers": ["NVDA", "MSFT", "AAPL"],
  "urgency": 8
}
(Processed in 0.09s)

2. Gemini (The Strategist):

"The surge in tech stocks driven by AI advancements signals a structural shift in productivity. For your portfolio, this validates our overweight position in semiconductor and software infrastructure. We recommend holding current positions to capture long-term compounding, rather than taking immediate profits."
```

🔮 Roadmap
[x] Hybrid Chain Implementation (Groq + Gemini)

[x] JSON Output Parsing

[ ] Real-time Loop: Fully integrate yfinance websocket for continuous monitoring.

[ ] Notification System: Connect "High Urgency" alerts to Telegram/Discord.

[ ] Database: Store sentiment trends in PostgreSQL/Supabase.
