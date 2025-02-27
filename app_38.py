# -*- coding: utf-8 -*-
"""APP_38.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1b-Xff7AS9-MVb6bopatx5bw_rMqjqzrx
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

# Ensure kaleido is installed
try:
    import kaleido
except ImportError:
    st.error("kaleido is not installed. Please install it using 'pip install -U kaleido'")
    st.stop()

# Load the section, professional elective, and core section files from GitHub
section_url = 'https://raw.githubusercontent.com/satyam26en/TIME_TABLE_KIIT/main/SECTION.csv'
elective_url = 'https://raw.githubusercontent.com/satyam26en/TIME_TABLE_KIIT/main/Professional_Elective%20-%20Sheet1.csv'
core_url = 'https://raw.githubusercontent.com/satyam26en/TIME_TABLE_KIIT/main/NEW_CORE.csv'

section_df = pd.read_csv(section_url)
elective_df = pd.read_csv(elective_url)
core_df = pd.read_csv(core_url)

# Normalize the 'Roll No.' column to ensure there are no leading/trailing spaces and consistent data type
section_df['Roll No.'] = section_df['Roll No.'].astype(str).str.strip()

# Define the order of days and times
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
times = ['8 TO 9', '9 TO 10', '10 TO 11', '11 TO 12', '12 TO 1', '1 TO 2', '2 TO 3', '3 TO 4', '4 TO 5']

# Define a mapping from abbreviated to full day names
day_mapping = {
    'MON': 'Monday',
    'TUE': 'Tuesday',
    'WED': 'Wednesday',
    'THU': 'Thursday',
    'FRI': 'Friday',
    'SAT': 'Saturday'
}

# Function to standardize time slot names
def standardize_time_slot(time_slot):
    time_slot_mapping = {
        '8 TO 9': '8 TO 9',
        '9 TO 10': '9 TO 10',
        '10 TO 11': '10 TO 11',
        '11 TO 12': '11 TO 12',
        '12 TO 1': '12 TO 1',
        '1 TO 2': '1 TO 2',
        '2 TO 3': '2 TO 3',
        '3 TO 4': '3 TO 4',
        '4 TO 5': '4 TO 5'
    }
    # Remove extra spaces in the time slot string to match the mapping
    standardized_slot = ' '.join(time_slot.upper().split())
    return time_slot_mapping.get(standardized_slot, time_slot)

# Function to generate and display the timetable
def generate_timetable(roll_number):
    # Find the section details for the given roll number
    student_section = section_df[section_df['Roll No.'] == roll_number]

    if student_section.empty:
        st.error("Roll number not found.")
        return None

    # Extract the core section and elective sections
    core_section = student_section['Core Section'].values[0]
    elective_1_section = student_section['Professional Elective 1'].values[0]
    elective_2_section = student_section['Professional Elective 2'].values[0]

    # Retrieve the weekly timetable for Professional Electives 1 and 2
    elective_1_timetable = elective_df[elective_df['Section(DE)'] == elective_1_section]
    elective_2_timetable = elective_df[elective_df['Section(DE)'] == elective_2_section]
    core_timetable = core_df[core_df['Section'] == core_section]

    # Initialize the timetable matrix
    timetable_matrix = pd.DataFrame(index=times, columns=days, data='')

    # Function to fill the timetable matrix with subject names and room numbers
    def fill_timetable(timetable_df):
        room_columns = [col for col in timetable_df.columns if 'ROOM' in col]
        for index, row in timetable_df.iterrows():
            day = day_mapping.get(row['DAY'], 'Unknown')
            if day == 'Unknown':
                continue  # Skip if day is not in the mapping
            for col in room_columns:
                if row[col] != '---':
                    time_col = timetable_df.columns[timetable_df.columns.get_loc(col) + 1]
                    time_slot = standardize_time_slot(time_col)
                    subject = row.get(time_col, 'N/A')
                    room_number = row[col]
                    if subject.lower() != 'x':  # Only include if it's not 'x'
                        timetable_matrix.at[time_slot, day] = f"{subject} ({room_number})"

    # Fill the timetable matrix for core and elective timetables
    fill_timetable(core_timetable)
    fill_timetable(elective_1_timetable)
    fill_timetable(elective_2_timetable)

    # Replace NaN values with blank spaces
    timetable_matrix = timetable_matrix.fillna('')

    # Sort the table based on time slots
    timetable_matrix = timetable_matrix.reindex(times)

    # Visualize the timetable using Plotly
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=['Time'] + days,
            fill_color='#2c3e50',
            align='center',  # Center align for uniformity
            font=dict(color='white', size=14),
            line_color='darkslategray',
            line_width=2  # Increase border size
        ),
        cells=dict(
            values=[timetable_matrix.index] + [timetable_matrix[day].tolist() for day in days],
            fill=dict(
                color=[['#2c3e50'] * len(times)] + [['#ecf0f1'] * len(times) for _ in days]
            ),
            align='center',  # Center align for uniformity
            font=dict(color=[['white'] * len(times)] + [['black'] * len(times) for _ in days], size=12),
            line_color='darkslategray',
            line_width=2,  # Increase border size
            height=30  # Set cell height to ensure equal length cells
        )
    )])

    fig.update_layout(
        title='Timetable',
        title_x=0.5,
        title_font=dict(size=32, family='Arial Black, sans-serif', color='darkblue'),
        margin=dict(l=10, r=10, t=50, b=10),
        height=600
    )
    return fig

# Streamlit App

# Apply custom CSS for background color and fonts
st.markdown(
    """
    <style>
    .reportview-container {
        background: #ecf0f1;
        color: #2c3e50;
    }
    .sidebar .sidebar-content {
        background: #2c3e50;
        color: white;
    }
    h1 {
        font-family: 'Arial Black', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display image
st.image('https://raw.githubusercontent.com/satyam26en/TIME_TABLE_KIIT/main/KIIT-Full-Logo-Center.png', use_column_width=True)

st.title('Student Timetable Viewer')

roll_number = st.text_input("Enter Roll Number", max_chars=10)
download = st.checkbox("Download timetable as JPG image")

st.markdown("<br>", unsafe_allow_html=True)  # Add a line break for spacing

if st.button("Generate Timetable"):
    if roll_number:
        fig = generate_timetable(roll_number)
        if fig:
            st.plotly_chart(fig, use_container_width=True)
            if download:
                img_bytes = fig.to_image(format='jpg')
                with open('timetable.jpg', 'wb') as f:
                    f.write(img_bytes)
                st.success("Timetable has been saved as 'timetable.jpg'")
                with open("timetable.jpg", "rb") as img_file:
                    btn = st.download_button(
                        label="Download timetable as JPG",
                        data=img_file,
                        file_name="timetable.jpg",
                        mime="image/jpg"
                    )
    else:
        st.error("Please enter a roll number.")
