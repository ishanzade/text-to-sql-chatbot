import streamlit as st
from utils.db_handler import DBHandler
from utils.llm_wrapper import LLMWrapper
from utils.visualizer import visualize_query_result
from utils.chat_manager import ChatManager
from utils.query_logger import QueryLogger

import os

# Setup paths
os.makedirs("data", exist_ok=True)

# Initialize modules
db = DBHandler("data/sales.db")
chat = ChatManager("data/chat_history.json")
logger = QueryLogger("data/query_logs.json")
llm = LLMWrapper()


st.set_page_config(page_title="Text-to-SQL Chatbot", layout="wide")
st.title("🧠 Text-to-SQL Sales Chatbot")

# Show top 5 most frequent queries
st.sidebar.markdown("### 🔥 Top 5 Popular Queries")
for i, q in enumerate(logger.get_top_queries(5), 1):
    st.sidebar.write(f"{i}. {q}")

# Display previous history
st.sidebar.markdown("### 💬 Chat History")
for past_query in chat.get_history():
    st.sidebar.write(past_query)

# User input
user_input = st.text_input("Ask a question about the sales data:")

if user_input:
    with st.spinner("Generating SQL and fetching results..."):
        sql_query = llm.get_sql_query(user_input)       
        result_df = db.run_query(sql_query)

        # Log and save
        logger.log_query(user_input)
        chat.add_to_history(user_input)

        st.markdown("#### 🧾 Generated SQL Query")
        st.code(sql_query, language="sql")

        tab1, tab2 = st.tabs(["📊 Visualization", "📋 Table"])

        with tab1:
            fig = visualize_query_result(result_df)
            if fig:
                st.pyplot(fig)
            else:
                st.info("Not enough data to visualize.")

        with tab2:
            st.dataframe(result_df, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Made with Streamlit, LangChain, and SQLite")   