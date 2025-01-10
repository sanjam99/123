from phi.agent import Agent, RunResponse
from phi.model.groq import Groq
import json
import httpx

def OpenWeatherMap(City: str) -> str:
    """Use this function to get Weather Report From OpenWeatherMap.

    Args:
        City (str): Name of City 

    Returns:
        str: details of weather of that city
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={City}&appid={'9ae47a78e3a131b10fef6e3d77dbae3d'}&units=metric"
    response = httpx.get(url=url, verify=False)
    response.raise_for_status()
    data = response.json()
    
    return json.dumps(data)

def Article_fetcher(Ques: str) -> str:
    """Use this function to get Articles From URL.

    Args:
        Ques (str): Question 

    Returns:
        str: whatever article would be fetched it will give answer according to Question
    """
    try:
        url = f"https://wd301-capstone-api.pupilfirst.school/articles"
        response = httpx.get(url, verify=False)
        response.raise_for_status()
        data = response.json()
        return json.dumps(data)
    except httpx.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except ValueError:
        return "Invalid response format from API."
    
def Article_fetcher_by_id(id: int) -> str:
    """Use this function to get Perticular Article from URl.

    Args:
        id (int): ID of that Article 

    Returns:
        str: whatever article would be fetched it will give answer according to Question
    """
    try:
        url = f"https://wd301-capstone-api.pupilfirst.school/articles/{id}"
        response = httpx.get(url, verify=False)
        response.raise_for_status()
        data = response.json()
        return json.dumps(data)
    except httpx.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except ValueError:
        return "Invalid response format from API."

def Match_fetcher(url: str) -> str:
    """Use this function to get all Match from URl.

    Args:
        url (str): it's an question in which you need to take and answer the ques

    Returns:
        str: whatever Match data would be fetched it will give answer according to Question
    """
    try:
        url = f"https://wd301-capstone-api.pupilfirst.school/matches"
        response = httpx.get(url, verify=False)
        response.raise_for_status()
        data = response.json()
        return json.dumps(data)
    except httpx.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except ValueError:
        return "Invalid response format from API."

def Match_fetcher_by_matchid(matchid: int) -> str:
    """Use this function to get Matchs Details by ID from URl.

    Args:
        matchid (int): this is the match id of the perticular match

    Returns:
        str: whatever Match data would be fetched it will give answer according to Question
    """
    try:
        url = f"https://wd301-capstone-api.pupilfirst.school/matches/{matchid}"
        response = httpx.get(url, verify=False)
        response.raise_for_status()
        data = response.json()
        return json.dumps(data)
    except httpx.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except ValueError:
        return "Invalid response format from API."
    
def Sports_fetcher(Question: str) -> str:
    """Use this function to get Sports List from URl.

    Args:
        Question (str): it's an question in which you need to take and answer the ques

    Returns:
        str: whatever Match data would be fetched it will give answer according to Question
    """
    try:
        url = f"https://wd301-capstone-api.pupilfirst.school/sports"
        response = httpx.get(url, verify=False)
        response.raise_for_status()
        data = response.json()
        return json.dumps(data)
    except httpx.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except ValueError:
        return "Invalid response format from API."
    
def Sports_fetcher_by_sportid(sportid: int) -> str:
    """Use this function to get Sports List from URl.

    Args:
        sportid (int): It is an Sport Id which is perticularly assigned to Sports only.

    Returns:
        str: whatever Match data would be fetched it will give answer according to Question
    """
    try:
        url = f"https://wd301-capstone-api.pupilfirst.school/sports/{sportid}"
        response = httpx.get(url, verify=False)
        response.raise_for_status()
        data = response.json()
        return json.dumps(data)
    except httpx.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except ValueError:
        return "Invalid response format from API."

def teams_fetcher(Question: str) -> str:
    """Use this function to get Teams List from URl.

    Args:
        Question (str): it's an question in which you need to take and answer the ques

    Returns:
        str: whatever Teams data would be fetched it will give answer according to Question
    """
    try:
        url = f"https://wd301-capstone-api.pupilfirst.school/teams"
        response = httpx.get(url, verify=False)
        response.raise_for_status()
        data = response.json()
        return json.dumps(data)
    except httpx.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except ValueError:
        return "Invalid response format from API."
    
def teams_fetcher_by_teamid(teamid: int) -> str:
    """Use this function to get Teams List from URl.

    Args:
        teamid (int): it's an question in which you need to take and answer the ques

    Returns:
        str: whatever Teams data would be fetched it will give answer according to Question
    """
    try:
        url = f"https://wd301-capstone-api.pupilfirst.school/teams/{teamid}"
        response = httpx.get(url, verify=False)
        response.raise_for_status()
        data = response.json()
        return json.dumps(data)
    except httpx.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except ValueError:
        return "Invalid response format from API."
    
def create_user(data: str) -> str:
    """Create a new user. Expects a JSON string with name, email, and password.

    Args:
        data (str): this is an must be processed in json

    Returns:
        str: json 
    """
    try:
        # Convert input string to a dictionary
        user_data = json.loads(data)

        url = "https://wd301-capstone-api.pupilfirst.school/users"
        response = httpx.post(url, json=user_data, verify=False)
        response.raise_for_status()
        
        token = response.json().get("auth_token")
        if token:
            with open("auth_token.txt", "w") as f:
                f.write(token)
            return "User created successfully! Token saved to auth_token.txt."
        else:
            return "User creation failed. No token received."
    except json.JSONDecodeError:
        return "Invalid input format. Please provide a valid JSON string."
    except httpx.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except ValueError:
        return "Invalid response format from API."

def login_user(data: str) -> str:
    """Login an existing user. Expects a JSON string with email and password.

    Args:
        data (str): this must be a JSON string with email and password.

    Returns:
        str: JSON response or error message.
    """
    try:
        # Convert input string to a dictionary
        login_data = json.loads(data)

        url = "https://wd301-capstone-api.pupilfirst.school/users/sign_in"
        response = httpx.post(url, json=login_data, verify=False)
        response.raise_for_status()

        # Parse the response
        token = response.json().get("auth_token")
        if token:
            with open("login_auth_token.txt", "w") as f:
                f.write(token)
            return "Login successful! Token saved to auth_token.txt."
        else:
            return "Login failed. No token received."

    except json.JSONDecodeError:
        return "Invalid input format. Please provide a valid JSON string."
    except httpx.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except ValueError:
        return "Invalid response format from API."
    
def set_preferences(preferences: dict) -> str:
    """
    Set user preferences.
    Args:
        preferences (dict): Dictionary with user preferences.

    Returns:
        str: Success or error message.
    """
    try:
        # Read the auth token from file
        with open("login_auth_token.txt", "r") as f:
            token = f.read().strip()

        url = "https://wd301-capstone-api.pupilfirst.school/user/preferences"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        response = httpx.patch(url, json={"preferences": preferences}, headers=headers, verify=False)
        response.raise_for_status()

        return "Preferences updated successfully!"
    
    except FileNotFoundError:
        return "Auth token not found. Please login first."
    except httpx.HTTPStatusError as e:
        return f"HTTP error occurred: {str(e)}"
    except httpx.RequestError as e:
        return f"Request error occurred: {str(e)}"
    except ValueError:
        return "Invalid response format from API."

def get_preferences() -> str:
    try:
        # Read the auth token from file
        with open("login_auth_token.txt", "r") as f:
            token = f.read().strip()

        url = "https://wd301-capstone-api.pupilfirst.school/user/preferences"
        headers = {"Authorization": f"Bearer {token}"}
        response = httpx.get(url, headers=headers, verify=False)
        response.raise_for_status()

        preferences = response.json()
        return json.dumps(preferences)
    
    except FileNotFoundError:
        return "Auth token not found. Please login first."
    except httpx.HTTPStatusError as e:
        return f"HTTP error occurred: {str(e)}"
    except httpx.RequestError as e:
        return f"Request error occurred: {str(e)}"
    except ValueError:
        return "Invalid response format from API."



    


model = Groq(id="llama3-70b-8192", api_key= "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")
agent = Agent(
    model=model,
    tools=[OpenWeatherMap, Article_fetcher_by_id, Match_fetcher, Match_fetcher_by_matchid, Sports_fetcher, teams_fetcher, teams_fetcher_by_teamid, create_user, login_user, set_preferences, get_preferences],
    show_tool_calls=True,
    markdown=True,
)
Query = input(">>>")
agent.print_response(Query)

#can you fetch the location of that match which has id 4? and also fetch weather of that match location
#can you fetch the currently running matches?
#can you tell me the name of matches which was held on Royal Stadium, Crownville
#is there any sport name like football
#can you name all team who play american football
#Create a user for Alice Johnson with email alice.jamb@example.com and password SecurePass@2024
