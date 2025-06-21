# 📚 Auto Book Publisher (Groq + LLaMA + Human-in-the-Loop)

An automated AI pipeline that rewrites public domain books with collaborative feedback from AI and humans. Scrapes content from Wikisource, rewrites it using Groq-hosted LLaMA 3, reviews via an AI editor, integrates human feedback, stores all versions using ChromaDB, and exports the final version as PDF.

---

## ✨ Features

- 🔍 **Web scraping & screenshots** from Wikisource using Playwright
- ✍️ **AI writing** via LLaMA 3 (Groq API)
- 🧠 **AI review** for coherence, tone, and grammar
- 👤 **Human-in-the-loop editing** for high-quality refinement
- 🗃️ **Version control** using ChromaDB
- 🧬 **RL-based retrieval** to select the best version (prioritizing human edits)
- 📄 **PDF export** of the finalized chapter

---

## 🧠 Human-in-the-Loop Editing (HITL)

After the AI writer and reviewer finish their steps, the system **invites human feedback** before finalizing.

### 🛠️ How it Works

1. The AI-generated text is shown to you in the terminal (or editor).
2. You can:
   - Approve as-is (press Enter)
   - Or manually edit it (paste your changes or edit in a file)
3. The human-edited version is saved separately and prioritized by the retrieval system.

### 🧪 Advanced Option

Want to edit in your favorite editor (e.g. VS Code)?

## 🚀 Quickstart
### 1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/auto-book-publisher.git
cd auto-book-publisher

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Install Playwright Browsers
playwright install
This installs the required Chromium engine used for scraping and screenshot capture.

### 4. Add Groq API Key
- Create a .env file:
- GROQ_API_KEY=your_groq_api_key_here

Get your free key from https://console.groq.com

### 5. Run the Project
- python app.py
