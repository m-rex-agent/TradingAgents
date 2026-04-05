from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(
    dotenv_path="/Users/ailab/Desktop/development/TradingAgents/.env",
    override=True
)

print("KEY:", os.getenv("OPENAI_API_KEY"))      # verify it loads
print("URL:", os.getenv("OPENAI_BASE_URL"))      # verify it loads

# Create a custom config
config = DEFAULT_CONFIG.copy()
#LOCAL SETUP
#config["llm_provider"] = "ollama"
#config["deep_think_llm"] = "qwen3.5:27b-q4_K_M"
#config["quick_think_llm"] = "qwen3.5:9b-q4_K_M" 
# CLOUD OPENAI SETUP
config["llm_provider"] = "openai"
config["deep_think_llm"] = "gpt-5.1"
config["quick_think_llm"] = "gpt-4o-mini"
config["max_debate_rounds"] = 1
#config["backend_url"] = os.getenv("OPENAI_BASE_URL", config["backend_url"])
# CLOUD QWEN SETUP
#config["llm_provider"] = "openai"
#config["deep_think_llm"] = "qwen3.6-plus"
#config["quick_think_llm"] = "qwen3.6-plus"
#config["max_debate_rounds"] = 2
#config["backend_url"] = os.getenv("OPENAI_BASE_URL", config["backend_url"])

# Configure data vendors (default uses yfinance, no extra API keys needed)
config["data_vendors"] = {
    "core_stock_apis": "yfinance",           # Options: alpha_vantage, yfinance
    "technical_indicators": "yfinance",      # Options: alpha_vantage, yfinance
    "fundamental_data": "yfinance",          # Options: alpha_vantage, yfinance
    "news_data": "yfinance",                 # Options: alpha_vantage, yfinance
}

# Initialize with custom config
ta = TradingAgentsGraph(debug=True, config=config)

# forward propagate
ta = TradingAgentsGraph(debug=True, config=config)
_, decision = ta.propagate("XRP", "2026-04-03")
print(decision)

# Memorize mistakes and reflect
# ta.reflect_and_remember(1000) # parameter is the position returns
