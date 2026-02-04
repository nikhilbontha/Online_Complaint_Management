
import streamlit as st
import sqlite3
from datetime import datetime

conn = sqlite3.connect("complaints.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS complaints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    category TEXT,
    description TEXT,
    status TEXT DEFAULT 'Open',
    created_at TEXT
)
''')
conn.commit()

st.title("Online Complaint Management System")

name = st.text_input("Name")
email = st.text_input("Email")
category = st.selectbox("Category", ["Technical", "Academic", "Hostel", "Other"])
description = st.text_area("Complaint Description")

if st.button("Submit Complaint"):
    if name and email and description:
        cursor.execute(
            "INSERT INTO complaints (name, email, category, description, created_at) VALUES (?, ?, ?, ?, ?)",
            (name, email, category, description, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )
        conn.commit()
        st.success("Complaint submitted successfully!")
    else:
        st.error("Please fill all fields")
