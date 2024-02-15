#!/usr/bin/python3

import requests
import zipfile
import io

response = requests.get('https://update.wallabyjs.com/wallaby.json').json()
print(f'Latest WallabyJS versions: {response}')

latestServerVersion = response['latestServer'][0]
downloadFolder = f'WallabyJs.wallaby-vscode-{latestServerVersion}'

print(f'Fetch latest version of WallabyJS server ({latestServerVersion})')
r = requests.get(f'https://wallaby-downloads.s3.amazonaws.com/wallaby-v{latestServerVersion}.zip')
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall(f'{downloadFolder}/wallaby')

print('Fetch latest version of WallabyJS app')
r = requests.get(f'https://wallaby-downloads.s3.amazonaws.com/wallaby-app.zip')
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall(f'{downloadFolder}/wallaby-app')

print(f'Finished OK')
print(f'WallabyJS files can be found here: {downloadFolder}')