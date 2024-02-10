
Incident Handling Log

This Python code provides a simple incident handling log application using the Tkinter library for the graphical user interface (GUI). It allows users to log incidents, categorize them, and store relevant information. Below is an overview of the functionalities provided by this application.

Features:
Logging Incidents:
Users can log incidents by providing details such as incident date, name, class, category, event description, systems/users affected, resolution, date completed, risk level, SOC (Security Operations Center) requirement, and additional notes.
Categories are divided into three classes: High, Medium, and Low, with several predefined categories for each class. Users can also select the "Other" category and specify a custom category if needed.

Viewing and Searching Incidents:
The application displays logged incidents in a text box, showing incident details.
Users can search for specific incidents using keywords. The search function matches the entered keyword against incident details and displays matching results.

Data Persistence:
Incidents are stored in a CSV file named "incidents.csv" upon logging.
When the application starts, it loads previously logged incidents from the CSV file.

User Interface:
The GUI is designed using Tkinter, providing a user-friendly interface for logging and viewing incidents.
Dropdown menus and entry fields enable users to input incident details efficiently.

Usage:
Launch the application by executing the Python script.
Fill in the incident details in the provided fields.
Click the "Log Incident" button to record the incident.
To search for specific incidents, enter keywords in the search box and click the "Search" button.
Click the "About" button to view information about the application and its license.

Requirements:
Python 3.x
Tkinter library (usually included with Python)
License:
This application is released under the GNU Public License. For more information, visit https://www.gnu.org/licenses/gpl-3.0.html.

Note: Make sure to customize and adapt this application according to your specific requirements before deployment.