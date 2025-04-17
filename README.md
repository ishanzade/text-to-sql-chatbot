# 🧠 Text-to-SQL Sales Chatbot (Offline | Streamlit | SQLite | LangChain)

This is an offline AI chatbot that translates NLP into SQL queries and runs them on a local sales dataset. Built with **Streamlit**, **LangChain**, **Ollama models (Mistral)**, and **SQLite**, it allows users to interact with their data effortlessly via chat.

---

## 🚀 Features

- 🔍 **Ask questions in plain English** — get SQL + results instantly
- 🧾 **Generates accurate SQL queries** using local LLM (Mistral via Ollama)
- 📋 **Displays results in table format**
- 📊 **Visualizes query results with charts**
- 🧠 **Maintains search history** like ChatGPT (on the side panel)
- 🔥 **Top 5 popular queries** displayed on startup
- 🛠️ **Fully offline and local**, no internet or OpenAI key needed

---

## 🧰 Tech Stack

- [Streamlit](https://streamlit.io/) – UI
- [LangChain](https://www.langchain.com/) – NLP to SQL conversion
- [Ollama](https://ollama.com/) – Local language model (Mistral)
- [SQLite](https://www.sqlite.org/) – Local database
- [Pandas + Matplotlib](https://pandas.pydata.org/) – Data & charts

---

## 📦 Setup Instructions

### 1️⃣ Clone or Download the Project

```bash
git clone https://github.com/YOUR_USERNAME/text-to-sql-chatbot.git
cd text-to-sql-chatbot
