FROM python:3.10-slim

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt update && apt install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Create app folder
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy userbot script
COPY userbot.py .

# Run bot
CMD ["python", "userbot.py"]
