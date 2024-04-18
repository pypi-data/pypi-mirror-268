
from quart import Quart, request, Response, stream_with_context
from telethon import TelegramClient, events
import re
import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Telegram Video Downloader')
    parser.add_argument('--api_id', help='Your Telegram API ID', default=os.getenv('API_ID'))
    parser.add_argument('--api_hash', help='Your Telegram API Hash', default=os.getenv('API_HASH'))
    parser.add_argument('--session_file', help='Session file name', default=os.getenv('SESSION_FILE', 'session_name'))

    args = parser.parse_args()
    return args

# Initialization of the Telegram client
args = parse_args()
client = TelegramClient(args.session_file, args.api_id, args.api_hash)
app = Quart(__name__)
CHUNK_SIZE = 64 * 1024  # 64 KB

async def download_generator(client, document, start, end):
    pos = start
    remaining = end - start + 1
    async for chunk in client.iter_download(document, offset=pos, limit=remaining):
        yield chunk
        remaining -= len(chunk)
        if remaining <= 0:
            break

@app.route("/telegram/direct/<telegram_id>")
async def telegram_direct(telegram_id):
    channel = telegram_id.split('-')[0]
    video_id = int(telegram_id.split('-')[1])
    if not video_id:
        return "Video ID is required", 400

    await client.start()
    message = await client.get_messages(channel, ids=[video_id])
    if not message or not hasattr(message[0], 'media'):
        return "Message not found or it doesn't contain any media", 404

    document = message[0].media.document
    file_size = document.size

    range_header = request.headers.get("Range")
    start, end = 0, file_size - 1 # Suposiciones iniciales
    headers = {
        "Accept-Ranges": "bytes", 
    }

    if range_header:
        match = re.match(r"bytes=(\d+)-(\d*)", range_header)
        if match:
            start, end = match.groups()
            start = int(start)
            end = int(end) if end else file_size - 1

            headers["Content-Range"] = f"bytes {start}-{end}/{file_size}"
            headers["Content-Length"] = str(end - start + 1)
            status_code = 206  # Partial Content
        else:
            return "Invalid Range header", 416  # Range Not Satisfiable
    else:
        status_code = 200  # OK
        headers["Content-Length"] = str(file_size)

    return Response(download_generator(client, document, start, end), status=status_code, headers=headers, content_type="video/mp4")
if __name__ == '__main__':
    app.run(port=5151)