from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class LLMWrapper:
    def __init__(self):
        self.llm = Ollama(model="mistral")

        # Schema-aware prompt
        self.prompt = PromptTemplate(
            input_variables=["question"],
            template="""
You are a SQL expert working with a SQLite database that contains a table named 'sales'.
The table has the following columns:
- date
- id_client
- product
- quantity
- price

Translate the user's natural language question into a valid SQL query using the table 'sales'.

Only return the SQL query. Do NOT include any explanation or formatting like ```sql.

Question: {question}
SQL:
"""
        )

        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def get_sql_query(self, user_input: str) -> str:
        try:
            result = self.chain.run(user_input).strip()

            # Clean formatting
            if "```sql" in result:
                result = result.split("```sql")[-1].split("```")[0].strip()
            elif "```" in result:
                result = result.split("```")[1].strip()

            # Strip "SQL:" if present
            if result.lower().startswith("sql:"):
                result = result[4:].strip()

            return result
        except Exception as e:
            return f"-- ERROR generating SQL: {e}"
