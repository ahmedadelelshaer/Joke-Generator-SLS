# Joke-Generator-SLS
A React app that fetches random jokes from an AWS API Gateway backend with Lambda. Each button press adds a new joke to the list without page reloads. The app uses Axios for HTTP requests and handles errors gracefully. The backend is serverless and deployed on AWS.
# Joke Generator App

A React application that fetches random jokes from an AWS API Gateway backend with Lambda. Each time the "Get a Joke" button is pressed, a new joke is added to the list without needing to reload the page. The backend is serverless and deployed on AWS.

## Features
- Fetches random jokes from an AWS API Gateway and Lambda backend.
- Displays jokes dynamically with each button press, without page reload.
- Handles API errors and displays a fallback message.

## Technologies
- **Frontend**: React.js, Axios
- **Backend**: AWS Lambda, API Gateway
- **Deployment**: Backend deployed on AWS, Frontend can be run locally or hosted.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
2.Install dependencies:
cd <project-directory>
npm install

3.Run the app locally:
npm start


The backend API is hosted on AWS API Gateway. Make sure the endpoint is correctly set up in the app if deploying locally.

License
This project is licensed under the MIT License - see the LICENSE file for details.

This README covers essential information, including a description, features, setup instructions, and technologies used. You can adjust the details as needed.
