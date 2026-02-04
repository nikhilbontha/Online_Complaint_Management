
import streamlit as st
import sqlite3

conn = sqlite3.connect("complaints.db", check_same_thread=False)
cursor = conn.cursor()

st.sidebar.title("Admin Panel")
option = st.sidebar.selectbox("Menu", ["View Complaints", "Search by ID"])

if option == "View Complaints":
    cursor.execute("SELECT * FROM complaints")
    rows = cursor.fetchall()
    for row in rows:
        with st.expander(f"Complaint ID: {row[0]}"):
            st.write(f"Name: {row[1]}")
            st.write(f"Email: {row[2]}")
            st.write(f"Category: {row[3]}")
            st.write(f"Description: {row[4]}")
            status = st.selectbox("Status", ["Open", "In Progress", "Closed"], index=["Open","In Progress","Closed"].index(row[5]), key=row[0])
            if st.button("Update Status", key=f"btn{row[0]}"):
                cursor.execute("UPDATE complaints SET status=? WHERE id=?", (status, row[0]))
                conn.commit()
                st.success("Status Updated")

if option == "Search by ID":
    cid = st.number_input("Enter Complaint ID", min_value=1)
    if st.button("Search"):
        cursor.execute("SELECT * FROM complaints WHERE id=?", (cid,))
        row = cursor.fetchone()
        if row:
            st.write(row)
        else:
            st.error("Complaint not found")
