import sys
from typing import Dict
import importlib.metadata
import json
import os
import platform
import qupiato.cli.config as c
import requests
import tempfile
import uuid
import websockets
import zipfile
import base64

async def ws_api_call(req: Dict):
    async with websockets.connect(c.DEPLOYER_WS_URL) as ws:
        await ws.send(json.dumps(req))

        while True:
            try:
                resp = await ws.recv()
                data = json.loads(resp)
                yield data
            except websockets.exceptions.ConnectionClosedOK:
                break

            except websockets.exceptions.ConnectionClosedError:
                break

def encode_secret():
    for root, _, files in os.walk('.'):
        for file in files:
            file_path = os.path.join(root, file)
            norm_path = os.path.normpath(file_path)

            if os.path.basename(norm_path) == '.env':
                with open(norm_path, 'r') as file:
                    env = file.read()
                    env_bytes = base64.b64encode(env.encode('utf-8'))
                    env_string = env_bytes.decode('utf-8')
                    return env_string

# 현재 디렉토리와 하위 디렉토리에 있는 모든 파일 압축
def create_zip_archive(zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk('.'):
            for file in files:
                file_path = os.path.join(root, file)
                norm_path = os.path.normpath(file_path)
                d_name = os.path.dirname(norm_path)

                if os.path.basename(norm_path).startswith('.env'):
                    continue
                if os.path.basename(norm_path) == 'db.json':
                    continue
                if os.path.basename(norm_path).startswith('.bash'):
                    continue
                if d_name and d_name.startswith('.'):
                    continue
                if d_name and os.path.basename(d_name) == '__pycache__':
                    continue
                if d_name and os.path.basename(d_name).startswith('.'):
                    continue
                if d_name and os.path.basename(d_name) == 'logs':
                    continue
                if os.path.basename(norm_path).endswith('.ipynb'):
                    continue
                if os.path.basename(norm_path).endswith('.zip'):
                    continue
                if os.path.basename(norm_path).endswith('.tar.gz'):
                    continue
                if os.path.basename(norm_path).endswith('.log'):
                    continue
                if os.path.basename(norm_path) == 'code':
                    continue

                zipf.write(file_path, os.path.relpath(file_path))


def upload_using_api(zip_filename):
    url = f"{c.API_SERVER_URL}/deployments/upload"
    headers = {
        'Authorization': f'Bearer {get_token()}'
    }
    files = { 'file': (zip_filename, open(zip_filename, 'rb')) }
    response = requests.post(url, headers=headers, files=files)

    if response.status_code != 200 and response.status_code != 201:
        raise Exception("Failed to upload zip file")

    return os.path.basename(zip_filename)


def create_and_upload_to_gcs_bucket():
    with tempfile.TemporaryDirectory() as temp_dir:
        zipfile_name = os.path.join(temp_dir, f'{str(uuid.uuid4()).replace("-", "")}.zip')

        create_zip_archive(zipfile_name)
        object_key = upload_using_api(zipfile_name)
        print(f"done. {object_key}")
        return object_key

def get_version():
    version = importlib.metadata.version('pyqqq-cli')
    return version

# websocket 메시지에 추가될 agent 정보
def get_agent():
    operating_system = {
        'Linux': 'linux',
        'Darwin': 'mac',
        'Windows': 'win',
    }
    os = operating_system.get(platform.system(), 'unknown')
    version = get_version()

    return {
        'name': 'command_line',
        'os': os,
        'version': version
    }

def get_token():
    if c.PYQQQ_API_KEY:
        return c.PYQQQ_API_KEY

    elif os.path.exists(c.CREDENTIAL_FILE_PATH):
            with open(c.CREDENTIAL_FILE_PATH, 'r') as f:
                return f.read().strip()

    else:
        print("ERROR: Key not found.")
        print("")
        print("Please set PYQQQ_API_KEY environment variable or create a file at ~/.qred with the API key.")
        sys.exit(1)