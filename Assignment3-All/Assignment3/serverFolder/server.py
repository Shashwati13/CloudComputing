from flask import Flask, send_file, make_response
import os
import hashlib
import string
import random
import sys

app = Flask(__name__)

@app.route('/')
def serveRandomFile():
    filePath = '/serverdata/randomFile.txt'
    checksum = generateRandomFile(filePath)
    response = make_response(send_file(filePath, as_attachment=True, download_name='randomFile.txt', mimetype='application/octet-stream'))
    response.headers['Checksum'] = checksum
    return response

def generateRandomFile(filePath):
    with open(filePath, 'w') as file:
        characters = string.ascii_letters + string.digits
        fileContent = ''.join(random.choice(characters) for _ in range(1024))
        file.write(fileContent)

    # Calculate checksum (SHA-256 in this example)
    sha256 = hashlib.sha256()
    sha256.update(fileContent.encode('utf-8'))
    return sha256.hexdigest()

if __name__ == '__main__':
    serverPort = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    app.run(host='0.0.0.0', port=serverPort)
