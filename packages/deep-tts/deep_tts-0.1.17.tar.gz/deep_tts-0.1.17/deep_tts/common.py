import os
import queue
import threading
from typing import Literal

import requests
from openai import OpenAI


class QueueGenerator:
    def __init__(self):
        self.queue = queue.Queue()

    def __iter__(self):
        return self

    def __next__(self):
        item = self.queue.get()
        if item is StopIteration:
            raise item
        return item

    def send(self, data):
        self.queue.put(data)

    def close(self):
        self.queue.put(StopIteration)


class DeepTTS:
    """
    DeepGrain Text-to-Speech (DeepTTS) service.

    Args:
        access_token (str): The access token for the DeepTTS system.
        provider (Literal["EU", "CN"], optional): The provider of the DeepTTS system. Defaults to "EU".

    Attributes:
        access_token (str): The access token for the DeepTTS system.
        provider (Literal["openai-tts1", "alibaba-langtext"]): The provider of the DeepTTS system.

    Methods:
        create(text: str, params: dict) -> str:
            Generates audio for the given text using the specified provider.

    """

    def __init__(self, access_token: str, provider: Literal["openai-tts1", "alibaba-langtext"]):
        self.access_token = access_token
        self.provider = provider
        self.g = QueueGenerator()

    def openai_text_stream(self, text: str):
        """get text stream from OpenAI."""
        client = OpenAI(api_key=os.getenv("OPENAI_KEY"))
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": text,
                }
            ],
            stream=True,
        )

        return stream

    async def init_conn(self):
        """initialize connection to server."""
        url = "http://127.0.0.1:8181/init_conn"

        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}",
        }

        s = requests.Session()
        s.headers.update(headers)
        response = s.get(url, headers=headers, data={}, stream=True)

        return response

    def send_text_stream(
        self,
        text_stream,
        task_id: str,
        stream_mode: bool = True,
        # provider: str = "openai-tts1",
        speed: str = "1",
        volume: str = "50",
        format: str = "wav",
        voice_id: str = "test_1",
    ):
        """send user text stream to server, server returns audio stream back to user."""

        def generator(text_stream):
            print("\n\n****** OpenAI Text Stream **********\n")
            for chunk in text_stream:
                if chunk.choices[0].delta.content is not None:
                    print(chunk.choices[0].delta.content, end="")
                    self.g.send(chunk.choices[0].delta.content)
                else:
                    self.g.close()
                    break

        # receive text stream chunks
        threading.Thread(target=generator, args=(text_stream,)).start()

        if stream_mode:
            mode = "true"
        else:
            mode = "false"

        # send chunks to server
        endpoint = "http://127.0.0.1:8181/text_stream"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}",
            "Content-Type": "plain/text",
            "stream": "true",
            "provider": "openai-tts1",  # "alibaba-langtext",
            "speed": "1",
            "volume": "50",
            "format": "wav",
            "voice_id": "test_1",  # "test_2",
            "task_id": task_id,
        }

        response = requests.post(url=endpoint, headers=headers, data=self.g, stream=True)

        return response


class ThreadedGenerator:
    def __init__(self):
        self.queue = queue.Queue()

    def __iter__(self):
        return self

    def __next__(self):
        item = self.queue.get()
        if item is StopIteration:
            raise item
        return item

    def send(self, data):
        self.queue.put(data)

    def close(self):
        self.queue.put(StopIteration)


def request_tts_server(endpoint: str, g):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}",
        "Content-Type": "plain/text",
        "stream": "true",
        "provider": "alibaba-langtext",
        "speed": "1",
        "volume": "50",
        "format": "wav",
        "voice_id": "test_2",
    }

    response = requests.post(url=endpoint, headers=headers, data=g, stream=True)

    return response


# def save_audio_stream_to_file(stream, cache_folder):
#     chunk_buffer = b""
#     file_count = 0
#     for chunk in stream.iter_content():
#         if chunk:
#             chunk_buffer += chunk
#             while len(chunk_buffer) >= 4:
#                 chunk_length = struct.unpack("I", chunk_buffer[:4])[0]

#                 if len(chunk_buffer) >= chunk_length + 4:
#                     chunk_data = chunk_buffer[4 : chunk_length + 4]
#                     chunk_buffer = chunk_buffer[chunk_length + 4 :]

#                     file_path = f"cache/{cache_folder}/audio_{file_count}.wav"
#                     print(file_path)
#                     os.makedirs(os.path.dirname(file_path), exist_ok=True)

#                     with open(file_path, "wb") as f:
#                         f.write(chunk_data)

#                     file_count += 1
#                 else:
#                     break
#         else:
#             print("chunk breaking...")

#     if chunk_buffer:
#         with open(f"audio_{file_count}.wav", "wb") as f:
#             f.write(chunk_buffer)

#     print("Audio stream saved to file.")
