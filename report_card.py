import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Report Card Management System", layout="wide")

st.title("REPORT CARD GENERATION PORTAL")

# ---------------- Session State ----------------

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=[
        "name",
        "age",
        "English",
        "Hindi",
        "Maths",
        "Science",
        "Social_sci"
    ])

df = st.session_state.df
n = len(df)

# ---------------- Menu ----------------

choice = st.sidebar.selectbox(
    "Choose Operation",
    (
        "Enter Details",
        "Total and Percentage",
        "Grades",
        "Subject Wise Average",
        "Subject Wise Highest Marks",
        "Generate Report Card"
    )
)

match(choice):

    # =====================================================
    # CASE 1
    # =====================================================

    case "Enter Details":

        st.header("Enter Student Details")

        records = st.number_input(
            "Enter number of records you want to store",
            min_value=1,
            step=1
        )

        for i in range(records):

            st.subheader(f"Student {i+1}")

            name = st.text_input("Enter Name", key=f"name{i}")

            roll = st.number_input(
                "Enter Roll NO",
                min_value=1,
                max_value=100,
                key=f"age{i}"
            )

            English = st.number_input(
                "English Marks",
                min_value=0,
                max_value=100,
                key=f"eng{i}"
            )

            Hindi = st.number_input(
                "Hindi Marks",
                min_value=0,
                max_value=100,
                key=f"hin{i}"
            )

            Maths = st.number_input(
                "Maths Marks",
                min_value=0,
                max_value=100,
                key=f"math{i}"
            )

            Science = st.number_input(
                "Science Marks",
                min_value=0,
                max_value=100,
                key=f"sci{i}"
            )

            Social_sci = st.number_input(
                "Social Science Marks",
                min_value=0,
                max_value=100,
                key=f"ss{i}"
            )

            if st.button("Save Student", key=f"save{i}"):

                df.loc[len(df)] = [
                    name,
                    roll,
                    English,
                    Hindi,
                    Maths,
                    Science,
                    Social_sci
                ]

                st.session_state.df = df

                st.success(f"{name} Added Successfully")

        st.subheader("Current Data")

        st.dataframe(df, use_container_width=True)
        # =====================================================
    # CASE 2
    # =====================================================

    case "Total and Percentage":

        st.header("Total and Percentage")

        name = st.text_input("Enter the name of student whose total you want to see")

        if st.button("Calculate Total and percentage"):

            found = False

            for i in range(len(df)):

                if(name.lower() == str(df.loc[i,'name']).lower()):

                    total = (df.loc[i,'English'] +
                             df.loc[i,'Hindi'] +
                             df.loc[i,'Maths'] +
                             df.loc[i,'Science'] +
                             df.loc[i,'Social_sci'])

                    percentage = total * 100 / 500

                    st.success(f"Total Marks : {total}")
                    st.success(f"Percentage : {percentage:.2f}%")

                    found = True

            if not found:
                st.error("Student Not Found")


    # =====================================================
    # CASE 3
    # =====================================================

    case "Grades":

        st.header("Grades")

        name = st.text_input("Enter name of student whose grades you want to find out")

        if st.button("Show Grades"):

            found = False

            for i in range(len(df)):

                if(str(df.loc[i,"name"]).lower() == name.lower()):

                    st.subheader("Grades")

                    subjects = [
                        "English",
                        "Hindi",
                        "Maths",
                        "Science",
                        "Social_sci"
                    ]

                    for subject in subjects:

                        marks = df.loc[i, subject]

                        if marks >= 90:
                            grade = "A"

                        elif marks >= 80:
                            grade = "B"

                        elif marks >= 70:
                            grade = "C"

                        elif marks >= 50:
                            grade = "D"

                        elif marks >= 35:
                            grade = "E"

                        else:
                            grade = "F"

                        st.write(subject, ":", grade)

                    found = True

            if not found:
                st.error("Student Not Found")
        # =====================================================
    # CASE 4
    # =====================================================

    case "Subject Wise Average":

        st.header("Subject Wise Average")

        if len(df) == 0:

            st.warning("No Records Found")

        else:

            a = df['English'].sum() / len(df)
            st.write("English Average :", a)

            b = df['Hindi'].sum() / len(df)
            st.write("Hindi Average :", b)

            c = df['Maths'].sum() / len(df)
            st.write("Maths Average :", c)

            d = df['Science'].sum() / len(df)
            st.write("Science Average :", d)

            e = df['Social_sci'].sum() / len(df)
            st.write("Social Science Average :", e)


    # =====================================================
    # CASE 5
    # =====================================================

    case "Subject Wise Highest Marks":

        st.header("Subject Wise Highest Marks")

        if len(df) == 0:

            st.warning("No Records Found")

        else:

            i = df['English'].idxmax()
            st.write("Highest Marks in English :", df.loc[i,'English'])
            st.write("Student :", df.loc[i,'name'])

            k = df['Maths'].idxmax()
            st.write("Highest Marks in Maths :", df.loc[k,'Maths'])
            st.write("Student :", df.loc[k,'name'])

            j = df['Hindi'].idxmax()
            st.write("Highest Marks in Hindi :", df.loc[j,'Hindi'])
            st.write("Student :", df.loc[j,'name'])

            l = df['Science'].idxmax()
            st.write("Highest Marks in Science :", df.loc[l,'Science'])
            st.write("Student :", df.loc[l,'name'])

            m = df['Social_sci'].idxmax()
            st.write("Highest Marks in Social Science :", df.loc[m,'Social_sci'])
            st.write("Student :", df.loc[m,'name'])


    # =====================================================
    # CASE 6
    # =====================================================

    case "Generate Report Card":

        st.header("Student Report Card")

        a = st.text_input("Enter Student Name")

        if st.button("Generate Report Card"):

            found = False

            for i in range(len(df)):

                if a.lower() == str(df.loc[i,'name']).lower():

                    st.subheader("Report Card")

                    st.write(df.loc[i])

                    total = (
                        df.loc[i,'English'] +
                        df.loc[i,'Hindi'] +
                        df.loc[i,'Maths'] +
                        df.loc[i,'Science'] +
                        df.loc[i,'Social_sci']
                    )

                    percentage = total * 100 / 500

                    st.write("Total Marks :", total)
                    st.write("Percentage :", percentage)

                    found = True

            for i in range(len(df)):

                if(str(df.loc[i,"name"]).lower() == a.lower()):

                    st.write("Grades:")
                    subjects = [
                        "English",
                        "Hindi",
                        "Maths",
                        "Science",
                        "Social_sci"
                    ]

                    for subject in subjects:

                        marks = df.loc[i, subject]

                        if marks >= 90:
                            grade = "A"

                        elif marks >= 80:
                            grade = "B"

                        elif marks >= 70:
                            grade = "C"

                        elif marks >= 50:
                            grade = "D"

                        elif marks >= 35:
                            grade = "E"

                        else:
                            grade = "F"

                        st.write(subject, ":", grade)

            if not found:

                st.error(f"Student {a} not found.")
