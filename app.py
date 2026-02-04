import streamlit as st
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",   # change if your MySQL password is different
        database="complaint_db"
    )

st.title("📝 Online Complaint Management System")

roll_no = st.text_input("Roll Number")
name = st.text_input("Name")
email = st.text_input("Email")

category = st.selectbox(
    "Complaint Category",
    ["Technical", "Academic", "Hostel", "Transport", "Other"]
)

description = st.text_area("Complaint Description")

if st.button("Submit Complaint"):
    if roll_no and name and email and description:
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO complaints
                (roll_no, name, email, category, description)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (roll_no, name, email, category, description)
            )

            conn.commit()
            conn.close()
            st.success("✅ Complaint submitted successfully")

        except mysql.connector.errors.IntegrityError:
            st.error("❌ Roll Number already exists. Use a different roll number.")

    else:
        st.error("❌ Please fill all fields")
