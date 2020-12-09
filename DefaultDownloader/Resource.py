import urllib.request
import zipfile
import os
import sys
import time

def load(block_count, block_size, total_size):
	percentage = 100.0 * block_count * block_size / total_size
	total_size_kb = total_size / 1024
	if percentage > 100:
		percentage = 100
	sys.stdout.write(f'\rダウンロード >> {percentage:.2f}% ({total_size_kb:.0f}kb)')

DLname = 'Resource'
version = '1.16.200' #ダウンロードに失敗した場合はこの値を最新バージョンに変更してください
resourceUrl = f'https://meedownloads.blob.core.windows.net/worlds/Vanilla_{DLname}_Pack_{version}.zip'
os.makedirs(DLname, exist_ok=True)
urllib.request.urlretrieve(resourceUrl, f'{DLname}/{DLname}.zip', load)
sys.stdout.write('\nファイルの解凍 >> 進行中')
with zipfile.ZipFile(f'{DLname}/{DLname}.zip') as zf:
	zf.extractall(f'{DLname}/')
sys.stdout.write('\rファイルの解凍 >> 完了   ')
sys.stdout.write('\nファイルの削除 >> 進行中')
os.remove(f'{DLname}/{DLname}.zip')
sys.stdout.write('\rファイルの削除 >> 完了    ')

time.sleep(3)
sys.exit()