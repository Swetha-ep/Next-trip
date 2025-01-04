import requests
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Set API keys
os.environ["GROQ_API_KEY"] = os.getenv("groq_api")
WEATHER_API_KEY = os.getenv("weather_api")

# Initialize the ChatGroq model
model = ChatGroq(model="llama3-8b-8192")

# Define the prompt template
system_template = """The weather in {city_name} is {temperature}°C with {conditions}. Based on this:
1. Suggest appropriate clothes for someone traveling to this city.
2. List TEN famous places to visit in {city_name} with a short description of each.
just return the answers not questions and answer format ...."""
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{city_name}")]
)

# Chain the prompt and model
chain = prompt_template | model

def get_weather(city_name):
    """
    Fetches the current weather for the given city using OpenWeatherMap API.

    Args:
        city_name (str): The name of the city.

    Returns:
        dict: A dictionary containing temperature and weather conditions.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching weather data: {response.status_code}")
    data = response.json()
    return {
        "temperature": data["main"]["temp"],
        "conditions": data["weather"][0]["description"],
    }
def get_travel_recommendations(city_name, temperature, conditions):
    """
    Invokes the LangChain-based ChatGroq model to get travel recommendations.

    Args:
        city_name (str): Name of the city.
        temperature (float): Current temperature in the city.
        conditions (str): Weather conditions in the city.

    Returns:
        dict: A structured dictionary containing the recommendations.
    """
    inputs = {
        "city_name": city_name,
        "temperature": temperature,
        "conditions": conditions,
    }
    response = chain.invoke(inputs)
    response_text = response.content.strip()

    # Example: Parse the response into a structured dictionary
    recommendations = {
        "clothes_description": "Appropriate clothes for the weather:",
        "clothes_list": [],  # Populate this based on the model's response
        "famous_places": []  # Populate this based on the model's response
    }
    
    # Parse the response (you can customize this based on the format of the returned string)
    lines = response_text.split("\n")
    
    # For example, parsing the clothes list (this will depend on how the model responds)
    clothes_start = False
    famous_places_start = False
    for line in lines:
        if "clothes" in line.lower():  # Assuming the model mentions clothes first
            clothes_start = True
            continue
        if clothes_start and "places" in line.lower():  # Assuming the clothes section ends here
            clothes_start = False
            famous_places_start = True
            continue
        if clothes_start:
            recommendations["clothes_list"].append(line.strip())
        if famous_places_start:
            recommendations["famous_places"].append(line.strip())
    
    return recommendations
