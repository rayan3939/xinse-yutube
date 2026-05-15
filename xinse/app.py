import os
import uuid
import threading
import time
from flask import Flask, render_template, request, send_file, jsonify
import yt_dlp

app = Flask(__name__)
DOWNLOAD_FOLDER = 'downloads'
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# Cleanup function to delete files after 10 minutes
def cleanup_file(filepath):
    time.sleep(600)
    if os.path.exists(filepath):
        os.remove(filepath)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_info', methods=['POST'])
def get_info():
    url = request.json.get('url')
    ydl_opts = {'quiet': True, 'no_warnings': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            return jsonify({
                'title': info.get('title', 'Video'),
                'thumbnail': info.get('thumbnail'),
                'duration': info.get('duration_string')
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 400

@app.route('/download', methods=['GET'])
def download():
    url = request.args.get('url')
    format_type = request.args.get('format') # mp3 or mp4
    
    file_id = str(uuid.uuid4())
    
    if format_type == 'mp3':
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{DOWNLOAD_FOLDER}/{file_id}.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }
    else:
        # MP4 - Supports 4K/8K by merging best video + best audio
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{DOWNLOAD_FOLDER}/{file_id}.%(ext)s',
            'merge_output_format': 'mp4',
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        # Handle extension change for mp3
        if format_type == 'mp3':
            filename = filename.rsplit('.', 1)[0] + '.mp3'

    # Start a thread to delete the file after download
    threading.Thread(target=cleanup_file, args=(filename,)).start()

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))