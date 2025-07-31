# Scoreazy-Task

````markdown
# 🎥 YouTube Transcript Fetcher from Excel

This Python script reads a list of YouTube video URLs from an Excel file, fetches their transcripts (in English or Hindi), and updates the Excel file by adding a new column with the transcript text.

## 📂 How It Works

1. **Reads** video URLs from an Excel file (default: `youtube_videos.xlsx`).
2. **Extracts** the video ID from each YouTube URL.
3. **Fetches** the transcript using the `youtube-transcript-api` library.
4. **Handles errors** like unavailable videos, disabled transcripts, or missing transcripts.
5. **Saves** the updated Excel file with an added `Transcript` column.

---

## 🛠 Requirements

Install dependencies using pip:

```bash
pip install pandas openpyxl youtube-transcript-api
````

---

## 📁 Excel Format

Your Excel file should contain a column named:

```
YouTube URL
```

Example:

| YouTube URL                                                  |
| ------------------------------------------------------------ |
| [https://youtu.be/dQw4w9WgXcQ](https://youtu.be/dQw4w9WgXcQ) |

---

## 🚀 How to Run

```bash
python your_script_name.py
```

The script will:

* Create a dummy Excel file (`youtube_videos.xlsx`) for testing.
* Process each URL and fetch transcripts.
* Save the updated file with a new `Transcript` column.

---

## 📌 Important Notes

* Only **public videos** with **available transcripts** (in English or Hindi) can be fetched.
* URLs must be valid and follow the correct YouTube format.
* Invalid or unavailable videos will be skipped or marked with appropriate error messages.

---

## 📄 Sample Output

| YouTube URL                                              | Transcript              |
| -------------------------------------------------------- | ----------------------- |
| [https://youtu.be/abc123xyz](https://youtu.be/abc123xyz) | Full transcript text... |
| [https://youtu.be/qwe456qwe](https://youtu.be/qwe456qwe) | Transcripts disabled... |

---

## 📧 Author

Developed by Vinayak Vathare.
Feel free to contribute or report issues!

