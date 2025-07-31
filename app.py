# transcript_fetcher.py

import pandas as pd
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled, VideoUnavailable

# --- Script entry point ---
if __name__ == "__main__":
    print("Transcript fetcher started.")
