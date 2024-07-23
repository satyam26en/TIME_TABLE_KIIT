### README.md

# Class Timetable Visualization

## Objective
The objective of this project is to create a comprehensive and visually appealing class timetable for students based on their roll numbers. The project involves reading timetable data from various sources, combining this data into a single timetable, and then visualizing the timetable using a tabular format.

## Features
- **Roll Number-Based Timetable Generation**: Generate personalized timetables for students based on their roll numbers.
- **Data Integration**: Combine core and elective class data into a single, unified timetable.
- **Error Handling**: Ensure accurate data processing and handling of missing or incorrect data entries.
- **Visual Representation**: Present the timetable in a clean and easy-to-read tabular format using Plotly.
- **Export as Image**: Save the generated timetable as a JPG image for further use or sharing.
- **Streamlit Integration**: Share and visualize the timetable through a web application using Streamlit.
- **Streamlit Cloud Hosting**: Host the web application on Streamlit Cloud for easy access and sharing.

## Technologies Used
- **Pandas**: For data manipulation and analysis.
- **Plotly**: For visualizing the timetable in a tabular format.
- **NumPy**: For numerical operations and managing data arrays.
- **Streamlit**: For building and hosting the web application.

## Project Structure
- **data**: Contains the CSV files with section, core, and elective timetable data.
- **scripts**: Contains the main Python script for generating and visualizing the timetable.
- **output**: Directory where the generated timetable images and CSV files are saved.

## Data Sources
- **SECTION.csv**: Contains the mapping of roll numbers to core and elective sections.
- **Elective_TIME_TABLE.csv**: Contains the timetable data for elective subjects.
- **CORE_TIME_TABLE_2-Sheet1.csv**: Contains the timetable data for core subjects.

## How It Works
1. **Load Data**: The data is read from the provided CSV files using Pandas.
2. **Normalize Data**: The roll numbers are normalized to ensure consistency and to remove any leading/trailing spaces.
3. **Generate Timetable**:
   - Extract the relevant sections for the given roll number.
   - Retrieve the timetable data for core and elective subjects.
   - Combine the data into a single timetable.
4. **Visualize Timetable**: The timetable is displayed in a tabular format using Plotly for clear and easy interpretation.
5. **Export Timetable**: The generated timetable is saved as a JPG image for easy sharing and future reference.
6. **Streamlit Integration**: The timetable is shared through a Streamlit web application for easy access.
7. **Streamlit Cloud Hosting**: The web application is hosted on Streamlit Cloud for seamless sharing and accessibility.

## Usage
1. **Run the Script**: Execute the main Python script `generate_timetable.py`.
2. **Enter Roll Number**: When prompted, enter the student's roll number.
3. **View Timetable**: The timetable will be displayed in the console and visualized using Plotly.
4. **Save Timetable**: The timetable will be saved as a JPG image in the `output` directory.
5. **Access the Web Application**: The timetable can be viewed and interacted with through the Streamlit web application.
6. **Streamlit Cloud Hosting**: The web application is hosted on Streamlit Cloud, making it easily accessible through a web browser.

## Hosting on Streamlit Cloud
1. **Create a Streamlit Account**: Sign up for a free account on Streamlit Cloud at [streamlit.io](https://streamlit.io/).
2. **Deploy the App**: Deploy the Streamlit app by linking your GitHub repository containing the project files.
3. **Share the App**: Once deployed, share the app URL with users to allow them to access and interact with the timetable.

This project provides an efficient and user-friendly way to generate, visualize, and share personalized class timetables for students, ensuring they have easy access to their schedule in a clear and organized format through both local and web-based platforms.
