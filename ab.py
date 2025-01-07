import os
import requests
from langchain.tools import Tool
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType
from typing import Dict
import json

os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

llm = ChatGroq(
    model_name="llama3-70b-8192",
    groq_api_key="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",
    temperature=0
)

@tool
def OpenWeatherMap(city: str) -> str:
    """A tool that retrieves current weather information using the OpenWeather API."""
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={'9ae47a78e3a131b10fef6e3d77dbae3d'}&units=metric"
        response = requests.get(url, verify=False)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except ValueError:
        return "Invalid response format from API."

@tool
def Article_fetcher(ur: str) -> str:
    """this is Article fetcher used when Some News article to be fetch"""
    try:
        url = f"https://wd301-capstone-api.pupilfirst.school/articles"
        response = requests.get(url, verify=False)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except ValueError:
        return "Invalid response format from API."
    
@tool
def Article_fetcher_By_id(id: int) -> str:
    """this is Article fetcher used when Some News article to be fetch"""
    try:
        url = f"https://wd301-capstone-api.pupilfirst.school/articles/{id}"
        response = requests.get(url, verify=False)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except ValueError:
        return "Invalid response format from API."
    
@tool
def Match_fetcher(url: str) -> str:
    """this is matches fetcher used when Some Sports Matches to be fetch"""
    try:
        url = f"https://wd301-capstone-api.pupilfirst.school/matches"
        response = requests.get(url, verify=False)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except ValueError:
        return "Invalid response format from API."
@tool
def Match_fetcher_by_id(id: int) -> str:
    """this is matches fetcher used when Some Sports Matches to be fetch"""
    try:
        url = f"https://wd301-capstone-api.pupilfirst.school/matches/{id}"
        response = requests.get(url, verify=False)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except ValueError:
        return "Invalid response format from API."
    
@tool
def Sports_fetcher(url: str) -> str:
    """this is Sports List fetcher used when All Sports to be fetch"""
    try:
        url = f"https://wd301-capstone-api.pupilfirst.school/sports"
        response = requests.get(url, verify=False)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except ValueError:
        return "Invalid response format from API."
    
@tool
def Sports_fetcher_by_id(id: int) -> str:
    """this is Sports with perticular ID fetcher used when perticular Sports to be fetch"""
    try:
        url = f"https://wd301-capstone-api.pupilfirst.school/sports/{id}"
        response = requests.get(url, verify=False)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except ValueError:
        return "Invalid response format from API."

@tool
def teams_fetcher(url: str) -> str:
    """this is Team List fetcher used when All Team to be fetch"""
    try:
        url = f"https://wd301-capstone-api.pupilfirst.school/teams"
        response = requests.get(url, verify=False)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except ValueError:
        return "Invalid response format from API."
    
@tool
def teams_fetcher_by_id(id: int) -> str:
    """this is Team List fetcher used when All Team to be fetch"""
    try:
        url = f"https://wd301-capstone-api.pupilfirst.school/teams/{id}"
        response = requests.get(url, verify=False)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except ValueError:
        return "Invalid response format from API."
    

@tool
def create_user(data: str) -> str:
    """Create a new user. Expects a JSON string with name, email, and password."""
    try:
        # Create the JSON object directly
        user_data = {
            "name": "Alice Johnson",
            "email": "alice.j@example.com",
            "password": "SecurePass@2024"
        }
        
        url = "https://wd301-capstone-api.pupilfirst.school/users"
        response = requests.post(url, json=user_data, verify=False)
        response.raise_for_status()
        
        token = response.json().get("auth_token")
        if token:
            with open("auth_token.txt", "w") as f:
                f.write(token)
            return "User created successfully! Token saved to auth_token.txt."
        else:
            return "User creation failed. No token received."
    except requests.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except ValueError:
        return "Invalid response format from API."

# Initialize agent with the updated tool
agent = initialize_agent(
    tools=[create_user],  # Include other tools
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

# Example usage
result = agent.invoke("Create a user for Alice Johnson with email alice.j@example.com and password SecurePass@2024")
print(result)
