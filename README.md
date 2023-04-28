This project is aimed at getting data from clients through a Google Form, collecting it in a Google Sheet, and triggering a Python code deployed on Vercel through a Google App Script. The Python code calculates various parameters such as age, BMR, TDEE, etc., and updates the Google Sheet with the calculated parameters for the respective clients.

Technologies Used
Google Forms
Google Sheets
Google App Script
Python
Vercel

Prerequisites
To use this project, you will need:

Access to Google Forms and Google Sheets
A Google Cloud Platform project and a service account JSON file to access the Google Sheet via the Google Sheets API
A deployed Vercel project with the necessary environment variables set

Usage
To use this project, follow the steps below:

Create a Google Form to collect client data.
Connect the Google Form to a Google Sheet. You can use the Clientsdata.xlsx file provided in this repository.
Create a Google Cloud Platform project, and download a JSON file for a service account that has access to the Google Sheets API. Save this file as myserviceacc.json in the project directory.
Deploy the Python code on Vercel. Use the vercel.json file provided in this repository to configure the deployment.
Write a Google App Script to call the API that runs the Python code. Use the app.py file provided in this repository as the code that runs on Vercel.
A trigger on Google form submit is set in the Google App Script to update the Google Sheet with the calculated parameters automatically.

Credits
This project was created by Harini Balaji.
