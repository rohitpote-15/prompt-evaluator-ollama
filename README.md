# 🧠 Prompt Evaluator App (Local LLM with Ollama + Streamlit)

A lightweight Streamlit app to evaluate and compare AI prompts using a locally hosted LLM via [Ollama](https://ollama.com/). No OpenAI key or cloud dependency required.

---

## 🚀 Features

- 🧪 Evaluate custom prompts against a local LLM
- 🔒 Runs fully offline using Ollama
- 🖥️ Streamlit-powered clean UI
- ⚡ Supports small models like `tinyllama` for low-memory systems

---

## 🛠️ Requirements

- Python 3.10+
- Git
- [Ollama](https://ollama.com/download) installed and running
- A supported Ollama model installed (e.g., `tinyllama`, `llama3`, etc.)

---

## 📦 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/rohitpote-15/prompt-evaluator-ollama.git
   cd prompt-evaluator-ollama
````

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Start Ollama** (make sure it's running in background):

   ```bash
   ollama run tinyllama
   ```

   Or preload a model:

   ```bash
   ollama pull tinyllama
   ```

---

## ▶️ Run the App

```bash
streamlit run src/app.py
```

Once running, open your browser at: [http://localhost:8501](http://localhost:8501)

---

## 📁 Project Structure

```
prompt-evaluator-ollama/
│
├── .env.template           # Template for environment variables (no secrets)
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── src/
│   ├── app.py              # Streamlit app logic
│   └── prompts.json        # Pre-defined or saved prompts
└── .gitignore
```

---

## 🧩 Customization

* Edit `prompts.json` to include your own prompt templates.
* Switch models in `app.py` by replacing:

  ```python
  Ollama(model="tinyllama")
  ```

  with any other supported local model (e.g., `llama3`, `mistral`, etc.)

---

## 🛑 Notes

* This app will not run on **Streamlit Cloud** https://prompt-evaluator-ollama.streamlit.app/, but due to its dependency on `localhost:xxxx`.
* Your system must have enough RAM to load the selected LLM model via Ollama.

---

## ✨ Author

Rohit Pote

💼 AI/ML Engineer | LLM Architect | Prompt Engineer
🌐 LinkedIn
📬 rohitrajupote97@gmail.com
🚀 [Streamlit App] https://legal-docs-rag-chatbot.streamlit.app/

---
