import pandas as pd
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled, VideoUnavailable

# Act as a Helper Function: To Extract YouTube Video ID's
def get_video_id(url):
    """
    Extracts the unique video ID from a YouTube URL.
    
    Args:
        url (str): The full YouTube URL.
    
    Returns:
        str: The extracted video ID, or None if invalid.
    """
    if not isinstance(url, str):
        return None

    # Remove any URL parameters
    if '?' in url:
        url = url.split('?')[0]

    # Handle different YouTube URL formats
    if "youtu.be/" in url:
        return url.split("/")[-1]
    elif "v=" in url:
        return url.split("v=")[-1].split("&")[0]

    return None  # If not matched

# Main Function: Fetch & Update Transcripts
def fetch_and_update_transcripts(file_path, sheet_name='Sheet1'):
    """
    It will Reads video URLs from an Excel file, fetches their transcripts,
    and updates the Excel file with the transcript text.
    
    Args:
        file_path (str): Path to the Excel file.
        sheet_name (str): Name of the worksheet (default is 'Sheet1').
    """
    print(f"Reading data from '{file_path}'...")
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return
    except Exception as e:
        print(f"Failed to read Excel file: {e}")
        return

    # Added a new column to store transcripts
    df['Transcript'] = ''

    ytt_api = YouTubeTranscriptApi()  # Created the API instance once

    # Process each row
    for index, row in df.iterrows():
        url = row.get('YouTube URL')

        # Skip invalid or empty URLs
        if not url or not isinstance(url, str):
            print(f"Skipping row {index + 2}: Invalid or missing URL.")
            continue

        # Extract video ID
        video_id = get_video_id(url)
        if not video_id:
            print(f"Skipping row {index + 2}: Could not extract video ID from '{url}'.")
            continue

        print(f"Fetching transcript for video ID: {video_id} (URL: {url})...")

        try:
            # Try to fetch transcript in English or Hindi
            fetched_transcript = ytt_api.fetch(video_id, languages=['en', 'hi'])
            transcript_list = fetched_transcript.to_raw_data()

            # Combine all transcript text
            transcript_text = ' '.join([t['text'] for t in transcript_list])

            # Update the DataFrame
            df.at[index, 'Transcript'] = transcript_text
            print(f"Success! Transcript fetched for row {index + 2}.")

        # Handle different failure cases
        except NoTranscriptFound:
            print(f"No transcript found for video ID: {video_id}.")
            df.at[index, 'Transcript'] = "No transcript found."

        except TranscriptsDisabled:
            print(f"Transcripts are disabled for video ID: {video_id}.")
            df.at[index, 'Transcript'] = "Transcripts disabled by uploader."

        except VideoUnavailable:
            print(f"Video unavailable for video ID: {video_id}.")
            df.at[index, 'Transcript'] = "Video unavailable."

        except Exception as e:
            print(f"Error fetching transcript for video ID {video_id}: {e}")
            df.at[index, 'Transcript'] = f"Error: {e}"

    # Save the updated data to the Excel file
    print(f"Saving updated data to '{file_path}'...")
    try:
        df.to_excel(file_path, index=False, engine='openpyxl')
        print("Process complete. Excel file updated successfully.")
    except Exception as e:
        print(f"Failed to save Excel file: {e}")

# Settingup the Entry Point of Script
if __name__ == "__main__":
    excel_file = 'youtube_videos.xlsx'

    # Creating a dummy Excel file with YouTube URLs
    # To Test Every Type of Video's To Get Transcripts and Defines the problems whatever they are
    dummy_data = {
        'YouTube URL': [
            'https://youtu.be/dQw4w9WgXcQ',   # have En transcript
            'https://youtu.be/VioF7v8Mikg?si=63mivZji4BTP0Goj',   # have En transcript
            'https://youtu.be/e3MX7HoGXug?si=BK2SOrsETSr0AWLU',   # have En transcript
            'https://youtu.be/5WQgLboa_I8?si=9aa5yYadmRvEzxVn',   # have En transcript 
            'https://youtu.be/CF52N-w4anI?si=6f8tnZm1ydqOpOkt',   # Hindi transcript
        ]
    }

    dummy_df = pd.DataFrame(dummy_data)
    dummy_df.to_excel(excel_file, index=False)
    print(f"Dummy Excel file '{excel_file}' created for testing.")

    # Call the main function
    fetch_and_update_transcripts(excel_file)