import streamlit as st
st.title("My First Streamlit App")
st.write("Hello Streamlit")

# # # # # # # # # # # # # # # # # # # # # # # # # # # 

name = st.text_input("Enter your name")
age = st.number_input("Enter your age")
if st.button("Submit"):
    st.write("Name:", name)
    st.write("Age:", age)

# # # # # # # # # # # # # # # # # # # # # # # # # # # 

students = [
    {"name": "Arun", "age": 19},
    {"name": "Vinu", "age": 20}
]

st.table(students)

# # # # # # # # # # # # # # # # # # # # # # # # # # # 

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1)
if "students" not in st.session_state:
    st.session_state.students = []
if st.button("Submit"):
    if name:
        st.session_state.students.append({"name": name, "age": int(age)})
        st.success("Student added")
    else:
        st.warning("Please enter a name")
st.table(st.session_state.students)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

students = []
name = st.text_input("Student Name")
age = st.number_input("Student Age", min_value=1)
if st.button("Add Student"):
    students.append({"name": name, "age": age})
    st.success("Student Added")
st.write(students)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import pandas as pd
data = {
    "Subject": ["Maths", "Physics", "Chemistry"],
    "Marks": [85, 90, 95]
}
df = pd.DataFrame(data)
st.bar_chart(df.set_index("Subject"))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 