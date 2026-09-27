import sqlite3
from werkzeug.security import generate_password_hash
import os

DATABASE = 'cyberportal.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                is_admin INTEGER DEFAULT 0
            )
        ''')
        
        # Create threats table (CO1)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                description TEXT NOT NULL,
                symptoms TEXT NOT NULL,
                prevention TEXT NOT NULL
            )
        ''')
        
        # Create questions table for quizzes
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question_text TEXT NOT NULL,
                option_a TEXT NOT NULL,
                option_b TEXT NOT NULL,
                option_c TEXT NOT NULL,
                option_d TEXT NOT NULL,
                correct_option TEXT NOT NULL,
                explanation TEXT NOT NULL,
                co_code TEXT NOT NULL,
                category TEXT
            )
        ''')
        
        # Create scores table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                co1_score INTEGER DEFAULT 0,
                co2_score INTEGER DEFAULT 0,
                co3_score INTEGER DEFAULT 0,
                co4_score INTEGER DEFAULT 0,
                co5_score INTEGER DEFAULT 0,
                co6_score INTEGER DEFAULT 0,
                total_score INTEGER DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')
        
        # Add default admin
        cursor.execute('SELECT * FROM users WHERE username = "admin"')
        if not cursor.fetchone():
            cursor.execute('INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)',
                           ('admin', generate_password_hash('admin123'), 1))
            
        conn.commit()

if __name__ == '__main__':
    init_db()
    print("Database initialized.")
