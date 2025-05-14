from bs4 import BeautifulSoup
import requests


def scrape_youtube_video_data(video_url):
    # Send a GET request to the video URL
    response = requests.get(video_url)

    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return None

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract video title (note: YouTube's class names frequently change)
    title_element = soup.find("h1", class_="title")
    title = title_element.text.strip() if title_element else "Title not found"

    # Extract views (note: this selector likely won't work with current YouTube)
    views_element = soup.find("span", class_="view-count")
    views = views_element.text.strip() if views_element else "Views not found"

    # Extract likes (note: this selector likely won't work with current YouTube)
    likes_element = soup.find("span", class_="like-button-renderer")
    likes = likes_element.span.button.text.strip() if likes_element and likes_element.span else "Likes not found"

    # Store the data in a dictionary
    video_data = {
        'title': title,
        'views': views,
        'likes': likes
    }

    return video_data


# Example usage (note: this likely won't work with current YouTube)
video_url = "https://www.youtube.com/watch?v=Nlg4NfvPs6w"
data = scrape_youtube_video_data(video_url)
print(data)