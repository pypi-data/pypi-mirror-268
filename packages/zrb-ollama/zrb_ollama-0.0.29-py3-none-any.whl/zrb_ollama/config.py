import os

_current_dir = os.path.dirname(__file__)
with open(os.path.join(_current_dir, "system-prompt.txt")) as f:
    _default_system_prompt = f.read()
SYSTEM_PROMPT = os.getenv("ZRB_SYSTEM_PROMPT", _default_system_prompt)


LLM_PROVIDER = os.getenv("ZRB_LLM_PROVIDER", "ollama")
CHAT_HISTORY_RETENTION = int(os.getenv("ZRB_CHAT_HISTORY_RETENTION", "5"))

EMBEDDING_DB_DIR = os.getenv(
    "ZRB_EMBEDDING_DB_DIR",
    os.path.expanduser(os.path.join("~", ".zrb-embedding"))
)

CHAT_HISTORY_FILE_NAME = os.getenv(
    "ZRB_CHAT_HISTORY_FILE",
    os.path.expanduser(os.path.join("~", ".zrb-ollama-history.txt"))
)

DOCUMENT_DIRS = os.getenv("ZRB_DOCUMENT_DIRS", "")

OLLAMA_BASE_URL = os.getenv("ZRB_OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("ZRB_OLLAMA_MODEL", "mistral:latest")
OLLAMA_EMBEDDING_MODEL = os.getenv("ZRB_OLLAMA_EMBEDDING_MODEL", "nomic-embed-text")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY", "")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "")
AWS_REGION_NAME = os.getenv("AWS_REGION_NAME", "us-east-1")

BEDROCK_MODEL = os.getenv("ZRB_BEDROCK_MODEL", "anthropic.claude-v2")
