import streamlit as st

st.set_page_config(page_title="Smart Notes", page_icon="📝")

st.title("📝 Smart Notes App")

st.write("Create and save your notes.")

note = st.text_area("Write your note here:")

if st.button("Save Note"):
    st.success("Note saved!")
    st.write("Your Note:")
    st.write(note)
