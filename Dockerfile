# -----------------------------------------------------
# Project    : CherryMusic 2.0
# Powered by : TeamAlfaBots
# -----------------------------------------------------
FROM nikolaik/python-nodejs:python3.10-nodejs20

# Install FFmpeg and certificates from the OS package repository.
# The base image is Debian/Ubuntu compatible.
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg ca-certificates && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# Keep the project's existing startup command.
CMD ["bash", "start"]
