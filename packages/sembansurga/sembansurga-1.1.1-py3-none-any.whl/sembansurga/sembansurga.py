from google.colab import drive
import libtorrent as lt
import time
import sys
import warnings
from usellm import Message, Options, UseLLM


def authenticate_google():
    drive.mount('/content/drive')
    print("Google Drive has been connected!")

def download_from_magnet(link, save_path=None):
    if not save_path:
        save_path = '/content/downloads/'  # Default save path if not specified

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")  # Ignore deprecation warnings

        ses = lt.session()
        params = {
            'save_path': save_path,
            'storage_mode': lt.storage_mode_t(2),
        }

        handle = lt.add_magnet_uri(ses, link, params)
        ses.start_dht()

        while not handle.has_metadata():
            time.sleep(1)

        while handle.status().state != lt.torrent_status.seeding:
            s = handle.status()
            sys.stdout.write(f'\rProgress: {s.progress * 100:.2f}% - Download Speed: {s.download_rate / 1000:.2f} KB/s')
            sys.stdout.flush()
            time.sleep(1)

        info = handle.get_torrent_info()
        files = info.files()
        downloaded_file = save_path + files[0].path  # Assuming the first file in the torrent is downloaded

        print('\nDownload complete!')
        print(f"Downloaded file: {downloaded_file}")

def torrent_downloader_new(magnet_link, save_path=None):
    if save_path == 'google':
        authenticate_google()
        save_path = '/content/drive/My Drive/'  # Set default Google Drive directory
    else:
        save_path = save_path if save_path else '/content/downloads/'  # Default save path if not provided

    download_from_magnet(magnet_link, save_path)
def torrent_downloader(arg1, arg2):
    print("""
        തിയേറ്ററിൽ പോയി കാണെടോ
        എഹ് എഹ്
        New function; torrent_downloader_new('link','path')
    """)

def code():
    code = """
!pip install -Uq keras-nlp
!pip install -Uq keras

import keras
import keras_nlp
import numpy as np

def login_to_kaggle():
    print('"username": "trilokvishwam", "key": "5829ba02d16cbacbda14d0b3d0570e98"')
    import kagglehub
    kagglehub.login()

login_to_kaggle()

gemma_lm = keras_nlp.models.GemmaCausalLM.from_preset("gemma_instruct_2b_en")

import keras
import keras_nlp
import numpy as np

def generate_response(question):
    prompt = '''
You are an AI assistant designed to answer simple questions.
Please restrict your answer to the exact question asked.
Think step by step, use careful reasoning. Your name is Semban Surga
Question: {question}
Answer:
'''
    response = gemma_lm.generate(prompt.format(question=question), max_length=500)
    start_idx = response.find("Answer:") + len("Answer:")
    return response[start_idx:].strip()

def ask(question):
    response = generate_response(question)
    print(response)
"""

    print(code)



def np(message):

    # Initialize the service
    service = UseLLM(service_url="https://usellm.org/api/llm")

    # Prepare the conversation
    messages = [
        Message(role="system", content="You are a helpful assistant."),
        Message(role="user", content=message),
    ]
    options = Options(messages=messages)

    # Interact with the service
    response = service.chat(options)

    # Print the assistant's response
    print(response.content)

def re(message):

    # Initialize the service
    service = UseLLM(service_url="https://usellm.org/api/llm")

    # Prepare the conversation
    messages = [
        Message(role="system", content="You are a helpful assistant. Your name is Semban surga, when people ask hello then gree then with Namaskaram"),
        Message(role="user", content=message),
    ]
    options = Options(messages=messages)

    # Interact with the service
    response = service.chat(options)

    # Print the assistant's response
    print(response.content)




