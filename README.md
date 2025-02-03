# Emergency Alert System

## Project Description

--The Emergency Alert System is a full-stack web application that allows users to report emergencies, respond to alerts, and coordinate aid in real time. The system is built using a Flask backend and a React frontend, providing a seamless and user-friendly experience for users who need to report or respond to emergencies quickly.



---
### Features (MVP)

`User Authentication:` Users can sign up and log in.

`Create Emergency Alerts:` Users can submit emergency alerts with location details and descriptions.

`View Emergency Alerts:` Users can browse a list of reported emergencies with relevant details.

`Respond to Emergencies:` Users can post responses to emergency alerts to offer help or additional information.

`CRUD Operations:` users can add and delete post.

`Form Validation:` Input validation using Formik for structured and error-free submissions.

`Navigation:` Multiple client-side routes using React Router.

### Technologies Used

## Backend

`Flask (Python)`

`Flask-RESTful`

`Flask-Migrate`

`Flask-SQLAlchemy`

`SQLite3 (Database)`

`Flask-CORS`


### Frontend

`React.js`

`React Router`

`Bootstrap + MDB React UI Kit`

`Formik (for form validation)`
### Installation & Setup

## Backend (Flask API)

### Clone the repository:

`git clone https://github.com/your-repo/emergency-alert-system.git`
`cd emergency-alert-system/server`

### Create and activate a virtual environment:

`python3 -m venv .venv`
`source .venv/bin/activate  # On Windows use `

### Install dependencies:

`pip install -r requirements.txt`

### Initialize the database:

`flask db init`
`flask db migrate -m "Initial migration."`
`flask db upgrade`

### Seed the database (if needed):

`python seed.py`

### Start the Flask server:

`flask run`

### Frontend (React App)

### Navigate to the frontend directory:

`cd ../client`

Install dependencies:

npm install

Start the React development server:

npm start

Deployment

Backend: Deployed on Render

Frontend: Hosted on Netlify/GitHub Pages

Future Enhancements

Real-time Notifications: Implement WebSocket or Firebase for live emergency updates.

Map Integration: Use Google Maps API to visualize emergency locations.

User Roles: Differentiate between responders and reporters.

File Uploads: Allow users to upload images/videos of emergencies.

Author

Philip Emdokolo
