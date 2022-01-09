import os
from flask import Flask, flash, request, redirect, render_template
import hashlib

UPLOAD_FOLDER = './uploads' #criando uma pasta para uploads
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'} #definindo as extensoes de arquivos permitidas 

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #configurando a pasta de uploads
app.config['SECRET_KEY'] = 'secret' #definindo o segredo que é nescessario para upar arquivos


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def sha256sum(filename):
    h = hashlib.sha256() #Declarando h como a função sha256 contida na biblioteca hashlib
    b = bytearray(128*1024) #criando um byte array de 128 por 1024 bytes
    mv = memoryview(b) #criando uma memory view que referencia o bite arra
    with open(filename, 'rb', buffering=0) as f:  #abrindo o arquivo
        for n in iter(lambda : f.readinto(mv), 0): #usando uma function lamba para ser mais eficiente
            h.update(mv[:n])
    return h.hexdigest() #retornado o hash em sha256

@app.route('/')
def central():
    return render_template('index.html')


@app.route('/sha-256', methods=['POST'])
def sha_256():
    print(request)
    count = 0
    for extension in ALLOWED_EXTENSIONS:
        if extension == request.files['file'].filename.split('.')[1]:
            count += 1
    
    #Aqui estamos verificando se a extensão do arquivo é permitida, devido ao fato do file não possuir um atributo .ext
    #temos que improvisar, nesse caso, rodando um for e verificando se a extensão do arquivo que é obtida através de uma quebra de string
    #é igual a uma das extensoes permitidas

    if count == 0:
            return render_template("message.html", message = "Extensão de arquivo inválida!")

    # se a contagem for zero, sabemos que a extensão do arquivo não é permitida, então redirecionamos para a página de mensagem
    # com a mensagem de erro
    print(request.files)
    if request.method == 'POST':
        if 'file' not in request.files:
            #aqui estamos verificando se o arquivo existe na request recebida pelo formulario
            flash('No file part')
            return redirect('/')
            #caso deixasemos redirect(request.url) ele redireciona para a url do sha-256 mas com erro de method not allowed
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect('/')
            #caso deixasemos redirect(request.url) ele redireciona para a url do sha-256 mas com erro de method not allowed

        if file and allowed_file(file.filename):

            filename = file.filename

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            path_arquivo_maquina = os.path.join(app.config['UPLOAD_FOLDER']+"/"+filename)
            #na linha acima estamos pegando o path do arquivo recem upado na pasta upload para enviar para o metodo sha256sum

            sha256 = sha256sum(path_arquivo_maquina)
            #chamando a funcao geradora de sha256 enviado como parametro o caminho do arquivo

            #return sha256
            return render_template("message.html", message= sha256)
            #retornando o sha256 gerado para o html


if __name__ == '__main__':
    app.run(debug=True)
