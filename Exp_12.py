
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Robots.txt"
# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find and extract the text content
    text_content = soup.get_text()
    
    # Display the extracted text
    print(text_content)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")





