from sqlalchemy import create_engine
import pandas as pd
from openai import OpenAI

class TableTalk():
    def __init__(
            self,
            openai_api_key: str,
            csv_path: str,
            ) -> None:
        self.openai_api_key = openai_api_key
        self.csv_path = csv_path

    def query_table(
            self,
            query: str,
            table_name: str = 'data_table'
            ) -> str:
        print('Scanning your data...')
        query = str(query).strip()
        table_name = str(table_name).strip()
        engine = create_engine("sqlite:///:memory:")
        df = pd.read_csv(self.csv_path)
        columns = df.columns
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        client = OpenAI(api_key=self.openai_api_key)
        print('Generating response...')
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            # model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Using only these columns: {columns}, return the SQL query that will answer this question: {query}. This is a SQLite Database, so it's important to consider what it's limitations are. The table is called {table_name}. Err on the side of returning more information by using lowercase comparisons that are similar but not exact. The response should look like this: SELECT * FROM table_name WHERE column_name LIKE '%company name%'. Don't return the exact answer, but rather the SQL query that will return the answer. Don't return anything but the SQL query. Don't include '```sql' or '```' in the response."},
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        sql_parse = response.choices[0].message.content.replace("'''sql",'').replace("'''",'').strip()
        new_df = pd.read_sql(sql_parse, engine)
        result = []
        for _, row in new_df.iterrows():
            row_str = ','.join([f'{col}:{row[col]}' for col in new_df.columns])
            result.append(row_str)

        response2 = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            # model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Using only this list of strings: {result}, return the answer to this question: {query}. Don't reference yourself."},
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        print(f'ANSWER:\n{'-'*20}\n{response2.choices[0].message.content}\n{'-'*20}')
        return response2.choices[0].message.content

