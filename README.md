# Xinse - YouTube to MP4/MP3 Downloader

A fast, secure web application to download YouTube videos in MP4 (up to 8K) or MP3 format.

## Features

- ✅ Download videos in MP4 (best quality/8K support)
- ✅ Extract audio as MP3 (320kbps)
- ✅ No registration required
- ✅ Fast processing with yt-dlp backend
- ✅ Beautiful, responsive UI with Tailwind CSS
- ✅ Automatic cleanup (files deleted after 10 minutes)
- ✅ Proper port binding for cloud deployments (Railway, Heroku, etc.)

## Installation

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/rayan3939/xinse-yutube.git
cd xinse-yutube
```

2. **Install dependencies**
```bash
pip install -r xinse/requirements.txt
```

3. **Install FFmpeg**
- **macOS**: `brew install ffmpeg`
- **Ubuntu/Debian**: `sudo apt-get install ffmpeg`
- **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html)

4. **Run the app**
```bash
cd xinse
python app.py
```

Visit `http://localhost:5000` in your browser.

### Docker Deployment

```bash
docker build -t xinse .
docker run -p 5000:5000 xinse
```

### Cloud Deployment (Railway, Heroku, etc.)

The app automatically reads the `PORT` environment variable, so it works out of the box on Railway, Heroku, and other cloud platforms.

## Project Structure

```
xinse-yutube/
├── xinse/
│   ├── app.py                 # Flask backend
│   ├── requirements.txt        # Python dependencies
│   ├── Dockerfile            # Docker configuration
│   └── templates/
│       └── index.html        # Web UI
└── README.md
```

## API Endpoints

### GET `/`
Returns the web interface.

### POST `/get_info`
Fetches video information.

**Request:**
```json
{
  "url": "https://www.youtube.com/watch?v=..."
}
```

**Response:**
```json
{
  "title": "Video Title",
  "thumbnail": "https://...",
  "duration": "10:30"
}
```

### GET `/download`
Downloads the video.

**Query Parameters:**
- `url` (required): YouTube URL
- `format` (required): `mp4` or `mp3`

**Response:** File download

## Fixed Issues

- ✅ Fixed Dockerfile pip syntax error (`python3 -m pip`)
- ✅ Fixed PORT environment variable handling
- ✅ Added proper error handling
- ✅ Implemented real backend integration in frontend
- ✅ Pinned dependency versions for stability
- ✅ Added cleanup thread daemon mode
- ✅ Improved container efficiency (removed apt cache)

## License

For educational purposes only.

## Disclaimer

This tool is provided for educational purposes. Users are responsible for respecting copyright and YouTube's Terms of Service when downloading content.
