from flask import Flask, request, render_template
import yt_dlp
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form["url"]
        download_video(video_url)
        return "Download started! Check the 'downloads' folder."
    
    return '''
        <form method="post">
            <input type="text" name="url" placeholder="Enter YouTube URL" required>
            <button type="submit">Download</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
