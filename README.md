# Red_Eye_Correction
Eye Detection and Correction with Flask and React
Project Overview:

This project is a web-based application that performs red-eye detection and correction using image processing techniques. The backend is built using Flask and OpenCV, while the frontend is built with React.
Users can upload images via the frontend, which are then processed by the backend to detect and correct red eyes.
Technologies Used:

Frontend: React with Vite for fast development and component-based UI.
Backend: Flask for handling requests and OpenCV for processing images.
Image Processing: The application uses Haar cascades (haarcascade_eye.xml) to detect eyes in images and applies custom logic to correct red-eye effects.
File Handling: Images are uploaded via the frontend and passed to the Flask backend for processing.
Key Features:

Red-Eye Detection: Automatically detects red eyes in uploaded images.
Red-Eye Correction: Applies filters and image transformations to correct red eyes.
Seamless Frontend-Backend Communication: React frontend communicates with Flask backend through API endpoints to send and retrieve images.
How to Run:

Install required dependencies using pip install -r requirements.txt for Flask and npm install for React.
Use npm run dev to start the Vite-powered React frontend.
Use flask run to start the Flask backend.
Upload an image through the React frontend and click "Show Corrected Result" to view the processed image.
Future Enhancements:

Additional eye detection improvements and support for more image formats.
Enhanced UI/UX for easier interaction with the app.
![Screenshot (317)](https://github.com/user-attachments/assets/f7164589-b3ab-4294-929c-07c1a003943a)
![Screenshot (316)](https://github.com/user-attachments/assets/fdca05dd-757b-4fd2-ba0c-be7a4f8f13ba)

