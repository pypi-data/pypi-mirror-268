# DeepGrain.AI - TTS Service Client

## Install

`pip install deep-tts`

## Server

```python
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from deep_tts import DeepTTS
from deep_tts.data_models import UserInput

load_dotenv(".env")

app = FastAPI()


@app.post("/raw_text")
def text_to_speech(user_text: UserInput = UserInput(text="你好吗？")):
    # get user text, send to openai to get stream
    text = user_text.model_dump().get("text")
    tts_client = DeepTTS(os.getenv("ACCESS_TOKEN"), "openai-tts1")

    # get text stream
    text_stream = tts_client.openai_text_stream(text)

    # init tts server connection
    conn_response = tts_client.init_conn()
    task_id = conn_response.headers["task_id"]

    # send text stream to tts server
    response = tts_client.send_text_stream(text_stream, task_id)
    print("\n\n", response.headers)

    return StreamingResponse(
        conn_response.iter_content(chunk_size=64),
        media_type="audio/wav",
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8182)

```

## Client
```python
import json
import threading
from datetime import datetime

import requests

from deep_tts.common import save_audio_stream_to_file


def single_request():
    "get openai text stream and send it to server to get audio chunks, and save the audio files to cache folder."
    url = "http://127.0.0.1:8182/raw_text"

    payload = json.dumps({"text": "你好吗？"})
    headers = {"accept": "application/json", "Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)

    save_audio_stream_to_file(response, "cache_folder")


single_request()

```
