# RAC_allocator_train-seat-allocation-
Hello,i have made a project using python,html,css,google  cloud api's for a trian seat allocation system.When a passenger with a RAC allocation approaches this website, they may get a confiramation seat as the other passengers gets down.It will be helpful in long trains in India,Still where the seat allocation are hectic to the TTRs

I have used python libraries like pandas and flask to manipulate the datas that are stored as CSV.

To make the storage of the datas easy and usefull i have used GOOGLE SHEETS 

i have used goolge cloud api's like DRIVE and GOOGLE SHEETS for the project

BE SURE THAT YOUR FILE DIRECTORY IS LIKE THIS
project_fr/
├── app.py
├── templates/
│   └── index.html
└── static/ (optional, for CSS, JS, images, etc.)

RUN YOUR APP.PY CODE AND THE HOST LINK WILL BE PRINTED,PASTE IT IN YOUR WEB BROWSER TO RUN THE APPLICATION

few things has to be done in the google cloud API to make a link between GOOGLE SHEETS AND THE USER INTERFACE those are:-
First, turn on Google Cloud APIs.

    Open the Cloud Console on Google.
    If you haven't already, choose your project or start a new one.
    From the navigation menu (APIs & Services > Library), select the API Library.
    Find and activate the following APIs:
        The Google Sheets API
        API for Google Drive

Create a service account in step two.

    In the Google Cloud Console, select IAM & Admin > Service Accounts.
    Click "Create Service Account."
    Complete the following:
        The term "Train Booking System" is an example of a service account name.
        (Optional) Description: An account description.
    Click "Create" to proceed.
    Assign the Position:
        To assign it, search for Editor or Project > Editor.
    To complete the service account creation, click Done.

Creating a JSON Key in Step Three

    Click the three dots next to the service account in the list of service accounts after it has been created.
    Choose Manage Keys.
    To create a new key, click Add Key.
    After selecting JSON, download the key file. A file with the extension ".json" will be downloaded as a result.
    Place the.json file in the project directory (D:\project_fr\, for example).

Step 4: Give the Service Account access to the Google Sheet

    Launch the desired Google Sheet (passengers, for example).
    From the Google Cloud Console (IAM & Admin > Service Accounts), copy the email address associated with your service account.
    Give that email address access to the sheet:
        In your Google Sheet, click Share.
        The service account email should be pasted.
        Click Send after assigning the role Editor.

HOPE THE README FILE HELPED YOU TO UNDERSTAND ABOUT THE PROJECT DESCRIPTION
