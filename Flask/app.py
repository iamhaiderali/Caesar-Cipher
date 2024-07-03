from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                char_code = ord(char) + shift_amount
                if char_code > ord('z'):
                    char_code -= 26
                encrypted_text += chr(char_code)
            elif char.isupper():
                char_code = ord(char) + shift_amount
                if char_code > ord('Z'):
                    char_code -= 26
                encrypted_text += chr(char_code)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                char_code = ord(char) - shift_amount
                if char_code < ord('a'):
                    char_code += 26
                decrypted_text += chr(char_code)
            elif char.isupper():
                char_code = ord(char) - shift_amount
                if char_code < ord('A'):
                    char_code += 26
                decrypted_text += chr(char_code)
        else:
            decrypted_text += char
    return decrypted_text

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    message = data['message']
    shift = int(data['shift'])
    encrypted_message = caesar_cipher_encrypt(message, shift)
    return jsonify({'encrypted_message': encrypted_message})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    message = data['message']
    shift = int(data['shift'])
    decrypted_message = caesar_cipher_decrypt(message, shift)
    return jsonify({'decrypted_message': decrypted_message})

if __name__ == '__main__':
    app.run(debug=True)
