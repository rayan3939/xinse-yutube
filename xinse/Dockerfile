FROM python:3.9-slim

# Install FFmpeg for video processing
RUN apt-get update && apt-get install -y ffmpeg

WORKDIR /app
COPY . .

RUN python3 -m pip install -r requirements.txt

CMD ["python", "app.py"]
