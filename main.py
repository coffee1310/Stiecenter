from fastapi import FastAPI
import jinja2
import psycopg2

app = FastAPI(
    title="Центральная научная лаборатиория"
)

def create_tables():
    try:
        conn = psycopg2.connect(
            user="postgres",
            password="nata155630",
            database="STIECENTER"
        )
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Accounts (
                id INT PRIMARY KEY, 
                username VARCHAR(64) NOT NULL, 
                email VARCHAR(512) NOT NULL, 
                created_at DATE, 
                user_level VARCHAR(32) NOT NULL, 
                post_count INT
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Publications (
                id INT PRIMARY KEY, 
                title VARCHAR(256) NOT NULL, 
                description TEXT,
                user_id INT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES Accounts (id)
            )
        ''')

        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
create_tables()
@app.get("/users/{user_id}")
def index_page(user_id: int):
    return user_id

@app.get("/post/{post_slug}")
def post(post_slug:str):
    return post_slug