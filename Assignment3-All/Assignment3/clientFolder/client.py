import requests
import hashlib
import time
import os

SERVER_URL = "http://server:8080/"
FILE_PATH = '/clientdata/receivedFile.txt'

def downloadFile(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open(FILE_PATH, 'wb') as file:
            file.write(response.content)
        return FILE_PATH, response.headers.get('Checksum')
    else:
        return None, None

def calculateChecksum(filePath):
    sha256 = hashlib.sha256()
    with open(filePath, 'rb') as file:
        for chunk in iter(lambda: file.read(8192), b''):
            sha256.update(chunk)
    return sha256.hexdigest()

def verification(filePath, recievedChecksum):
    actual_checksum = calculateChecksum(filePath)
    return actual_checksum == recievedChecksum

def main():
    downloadedFile, recievedChecksum = downloadFile(SERVER_URL)
    if downloadedFile and recievedChecksum:
        if verification(downloadedFile, recievedChecksum):
            print("-------- File received and Checksum verified. --------")
        else:
            print("Checksum verification failed.")
    else:
        print("Error downloading file")
    
    while True:
        time.sleep(10)

if __name__ == '__main__':
    main()
