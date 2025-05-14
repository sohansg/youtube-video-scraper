from googleapiclient.discovery import build


def get_youtube_video_data(video_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Fetch video details
    request = youtube.videos().list(
        part='snippet,statistics',
        id=video_id
    )
    response = request.execute()

    if 'items' in response and response['items']:
        video_data = response['items'][0]
        title = video_data['snippet']['title']
        views = video_data['statistics'].get('viewCount', 'Views not found')
        likes = video_data['statistics'].get('likeCount', 'Likes not found')
        comments = video_data['statistics'].get('commentCount', 'Comments not found')

        return {
            'title': title,
            'views': views,
            'likes': likes,
            'comments': comments
        }
    else:
        print("No video data found or invalid video ID.")
        return None


# Example usage
video_id = "bn8gP5N8hqM"  # Replace with your video ID
api_key = "AIzaSyCyGKa0Km2KlAM3rBjmmnD2dBowdv8Iz84"  # Replace with your actual API key
data = get_youtube_video_data(video_id, api_key)
print(data)