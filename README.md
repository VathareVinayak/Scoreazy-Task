# 🎯 YouTube Transcript Fetcher – Scoreazy Task

This Python tool automates the process of fetching **YouTube video transcripts** in **English or Hindi** from a list of **YouTube URLs** provided in an **Excel file**. It reads each video link, extracts its transcript using the `youtube-transcript-api`, and updates the same Excel file by adding a new column with the transcript for each video.

---

## 📥 Input

| Input Name  | Type   | Description                                                  |
|-------------|--------|--------------------------------------------------------------|
| Excel File  | `.xlsx`| Should contain a column named **"YouTube URL"** with links.  |
| Sheet Name  | `str`  | (Optional) Worksheet name. Default: `'Sheet1'`               |

---

## 🔄 Workflow

### ▶️ How It Is Triggered
- The script is executed directly via terminal:  

* Automatically creates a dummy test file (`youtube_videos.xlsx`) if it doesn’t exist.

### 🔢 Step-by-Step Breakdown

1. **Read Excel File**

   * Load the `.xlsx` file using `pandas`.
   * Extract all URLs from the `"YouTube URL"` column.

2. **Parse YouTube Video ID**

   * Supports both `youtu.be/` and `youtube.com/watch?v=` formats.
   * Strips out any extra parameters like `?si=...`.

3. **Fetch Transcript Using API**

   * Uses `youtube-transcript-api` to fetch transcripts in `'en'` or `'hi'`.

4. **Handle Errors Gracefully**

   * Displays and records appropriate messages for:

     * Missing transcript
     * Video unavailable
     * Transcripts disabled by uploader

5. **Update Excel File**

   * Adds a `"Transcript"` column next to the original URLs.
   * Saves the file using `openpyxl`.

---

## 🧰 Libraries Used

* [`pandas`](https://pypi.org/project/pandas/) – For reading/writing Excel files.
* [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/) – To fetch transcripts.
* [`openpyxl`](https://pypi.org/project/openpyxl/) – Excel engine used by `pandas`.

---

## 🧠 Key Code Snippets

### ✅ Extract Video ID from URL

```python
def get_video_id(url):
    if not isinstance(url, str):
        return None
    if '?' in url:
        url = url.split('?')[0]
    if "youtu.be/" in url:
        return url.split("/")[-1]
    elif "v=" in url:
        return url.split("v=")[-1].split("&")[0]
    return None
```

### ✅ Fetch & Append Transcripts

```python
fetched_transcript = ytt_api.fetch(video_id, languages=['en', 'hi'])
transcript_list = fetched_transcript.to_raw_data()
transcript_text = ' '.join([t['text'] for t in transcript_list])
df.at[index, 'Transcript'] = transcript_text
```

### ✅ Save the Excel File

```python
df.to_excel(file_path, index=False, engine='openpyxl')
```

---

## 📊 Sample Output

### 📥 Input File (youtube\_videos.xlsx)

| YouTube URL                                                                      |
| -------------------------------------------------------------------------------- |
| [https://youtu.be/dQw4w9WgXcQ](https://youtu.be/dQw4w9WgXcQ)                     |
| [https://youtu.be/VioF7v8Mikg?si=abc123](https://youtu.be/VioF7v8Mikg?si=abc123) |

### 📤 Output File (after script runs)

| YouTube URL                                                                      | Transcript                        |
| -------------------------------------------------------------------------------- | --------------------------------- |
| [https://youtu.be/dQw4w9WgXcQ](https://youtu.be/dQw4w9WgXcQ)                     | Never gonna give you up...        |
| [https://youtu.be/VioF7v8Mikg?si=abc123](https://youtu.be/VioF7v8Mikg?si=abc123) | Welcome to today’s walkthrough... |

---

## 🔗 GitHub Repository

[Scoreazy Task Repository](https://github.com/VathareVinayak/Scoreazy-Task)

---

## 📬 Assignment Submission Info

* **Name**: Vinayak Vathare
* **Email**: [vinayakvathare@gmail.com](mailto:vinayakvathare@gmail.com)
* **Role Applied**: Python Developer Intern
* **Submitted To**: [internship@scoreazy.com](mailto:internship@scoreazy.com)
