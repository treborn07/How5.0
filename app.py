from flask import Flask, render_template, redirect, url_for, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Crie uma instância do Flask
app = Flask(__name__)

# Dados de usuários (simulando um banco de dados simples)
users = {'john': 'secret', 'mary': 'password'}

# Configurações de e-mail
email_sender = 'seuemail@gmail.com'  # Seu e-mail de envio
email_password = 'sua_senha'  # Sua senha de e-mail
email_receiver = 'seuemail@gmail.com'  # O e-mail para o qual você deseja enviar a mensagem

# Função para enviar e-mail
def enviar_email(nome, email, mensagem):
    # Configurar servidor SMTP
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(email_sender, email_password)

        # Construir mensagem de e-mail
        msg = MIMEMultipart()
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg['Subject'] = 'Nova mensagem de contato'

        # Corpo do e-mail
        corpo_email = f"""
        Nome: {nome}
        Email: {email}
        Mensagem: {mensagem}
        """
        msg.attach(MIMEText(corpo_email, 'plain'))

        # Enviar e-mail
        server.sendmail(email_sender, email_receiver, msg.as_string())

# Rota para a página de contato
@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']
        enviar_email(nome, email, mensagem)
        return render_template('contato.html', enviado=True)  # Redireciona para a página de contato com uma mensagem de confirmação
    return render_template('contato.html', enviado=False)  # Renderiza a página de contato

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para o login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            # Autenticação bem-sucedida, redireciona para a página principal
            return redirect(url_for('dashboard'))
        else:
            # Autenticação falhou, redireciona de volta para o login
            return render_template('login.html', message='Login inválido. Tente novamente.')
    return render_template('login.html')

# Rota para a página principal após o login bem-sucedido
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Rota para fazer logout
@app.route('/logout')
def logout():
    return redirect(url_for('login'))

# Rota para o registro
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            # Registra o novo usuário
            users[username] = password
            return redirect(url_for('login'))
        else:
            return render_template('registro.html', message='Nome de usuário já está em uso. Tente outro.')
    return render_template('registro.html')

# Rota para a página de portfólio
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

# Rota para a página de depoimentos
@app.route('/depoimentos')
def depoimentos():
    return render_template('depoimentos.html')

# Rota para a página de contratos
@app.route('/contratos')
def contratos():
    return render_template('contratos.html')

# Rota para a página de serviços
@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

# Rota para a página de valores a receber
@app.route('/valores_a_receber')
def valores_a_receber():
    return render_template('valores_a_receber.html')

# Verifica se o arquivo foi executado diretamente
if __name__ == '__main__':
    app.run(debug=True)

