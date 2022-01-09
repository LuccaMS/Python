import os
from flask import Flask, flash, request, render_template
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate2048', methods=['GET'])
def generate():
    public_return = ''
    if request.method == 'GET':
        try:
            key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
            )
            print(key)	
            public_key = key.public_key()
            pem = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
            public_return = pem.decode('utf-8')
            key_file = open('key.pem', 'wb')
            key_file.write(pem)
            key_file.close()
            flash('Key gerada com sucesso!')
        except Exception as e:
            flash('Erro ao gerar a key: ' + str(e))
            
    return render_template('message.html', message = public_return)

@app.route('/generate1024', methods=['GET'])
def generate1024():
    public_return = ''
    if request.method == 'GET':
        try:
            key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=1024,
            )
            public_key = key.public_key()
            pem = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
            public_return = pem.decode('utf-8')
            key_file = open('key.pem', 'wb')
            key_file.write(pem)
            key_file.close()
            flash('Key gerada com sucesso!')
        except Exception as e:
            flash('Erro ao gerar a key: ' + str(e))
    return render_template('message.html', message = public_return)

@app.route('/decript', methods=['GET'])
def decript():
    with open('key.pem', 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None
        )
    
    return render_template('message.html', message = private_key)


if __name__ == '__main__':
    app.run(debug=True)

