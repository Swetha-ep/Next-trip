# Travel Companion: Weather & Recommendations

# Overview
Travel Dashboard is a web application designed to enhance travel planning by providing:

- **Real-Time Weather Information**: Accurate weather details for any city.
- **Packing Suggestions**: AI-driven recommendations for clothing based on the weather.
- **Tourist Destinations**: A curated list of famous attractions in the city with short descriptions.

This project utilizes Django as the web framework, LangChain (powered by ChatGroq) for generating travel insights, and OpenWeatherMap for weather data.

---

## Features

- **Real-Time Weather**: Fetches accurate and updated weather data using the OpenWeatherMap API.
- **AI-Generated Recommendations**: Leverages ChatGroq LLM for packing tips and travel recommendations.
- **Interactive UI**: A user-friendly interface for inputting city names and displaying results.

---

## Project Structure

travel_dashboard/  
├── dashboard/  
│   ├── templates/   
|   |   ├── base.html             # HTML templates for the app  
│   │   ├── index.html  
│   │   ├── about.html  
│   │   ├── contact.html  
│   ├── views.py                  # Contains view functions for handling requests  
│   ├── helper.py                 # Handles weather and travel recommendation logic  
│   ├── __init__.py  
│   └── ...  
├── travel_dashboard/             # Main Django project folder  
│   ├── settings.py  
│   ├── urls.py  
│   ├── ...  
├── .env                          # Environment variables file (API keys)  
├── requirements.txt              # Dependencies  
└── README.md                     # Documentation  
    


## Prerequisites

- Python 3.9 or highere on a Windows Machine 
- Django 4.2+ installed.
- **API Keys**:
  - OpenWeatherMap API key for fetching weather data.
  - ChatGroq API key for AI recommendations.

---

## Installation

### Step 1:  Clone the Repository
```bash
git clone <repository_url>  
cd travel_dashboard  
```

### Step 2: Set Up Virtual Environment
```bash
python -m venv travel_env  
travel_env\Scripts\activate  # Windows  
# or  
source travel_env/bin/activate  # macOS/Linux  
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Create a .env file in the project root with your API keys:
- weather_api=<your_openweathermap_api_key>  
- groq_api=<your_chatgroq_api_key>  


### Step 5:Start the Development Server
```bash
python manage.py runserver  
```


## Usage:

- **Homepage**:
- Enter the name of a city.
- Submit the form to view:
- Current weather conditions.
- Packing suggestions for the weather.
- Famous places to visit.
- **About Page**:
- Provides information about the application.
- **Contact Page**:
- Displays contact details for further inquiries.




