# DeepGrain.AI - TTS Service Client

## Install

`pip install deep-tts`

## Usage

```python
import os

from dotenv import load_dotenv

load_dotenv(".env")

from deep_tts import DeepTTS

if __name__ == "__main__":
    access_token = os.getenv("ACCESS_TOKEN") or ""

    # text data to stream
    text_data = ["Hello, ", "this is ", "streamed ", "text ", "data."]
    text_data = ["今天天气不错，", "适合春游。"]

    # Send streamed text data to the server
    tts_client = DeepTTS(access_token)
    response = tts_client.stream_text(text_data)

    print(response.text)
    chunk_id = response.json().get("chunk_id")

    status = tts_client.stream_status(chunk_id)
    print(status.text)

    tts_client.stream_to_file(chunk_id)

```
