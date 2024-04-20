from talk import TableTalk
from dotenv import load_dotenv
import os

load_dotenv()

table = TableTalk(
    openai_api_key=os.getenv('OPENAI_API_KEY'),
    csv_path='./abstracts.csv'
)

answer = table.query_table(query='how many awards has intelligent fusion won?')
print(answer)