import streamlit as st
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",   # change if required
        database="complaint_db"
    )

st.title("📋 Admin Complaint Management")

menu = st.sidebar.selectbox(
    "Admin Menu",
    ["View All Complaints", "Search by Roll Number"]
)

conn = get_connection()
cursor = conn.cursor()

# 🔹 VIEW ALL COMPLAINTS
if menu == "View All Complaints":
    cursor.execute("SELECT * FROM complaints")
    complaints = cursor.fetchall()

    for c in complaints:
        with st.expander(f"Roll Number: {c[0]}"):
            st.write("Name:", c[1])
            st.write("Email:", c[2])
            st.write("Category:", c[3])
            st.write("Description:", c[4])
            st.write("Created At:", c[6])

            status = st.selectbox(
                "Update Status",
                ["Open", "In Progress", "Closed"],
                index=["Open", "In Progress", "Closed"].index(c[5]),
                key=c[0]
            )

            if st.button("Update Status", key=f"btn{c[0]}"):
                cursor.execute(
                    "UPDATE complaints SET status=%s WHERE roll_no=%s",
                    (status, c[0])
                )
                conn.commit()
                st.success("✅ Status Updated")

# 🔹 SEARCH BY ROLL NUMBER
if menu == "Search by Roll Number":
    roll_no = st.text_input("Enter Roll Number")

    if st.button("Search"):
        cursor.execute(
            "SELECT * FROM complaints WHERE roll_no=%s",
            (roll_no,)
        )
        result = cursor.fetchone()

        if result:
            st.write("Roll Number:", result[0])
            st.write("Name:", result[1])
            st.write("Email:", result[2])
            st.write("Category:", result[3])
            st.write("Description:", result[4])
            st.write("Status:", result[5])
            st.write("Created At:", result[6])
        else:
            st.error("❌ Complaint not found")

conn.close()
