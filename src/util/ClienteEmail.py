import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class ClienteEmail:
    def __init__(self, emailRemetente, emailUsuarioSenha, emailDestinatario, assunto, texto, arquivo):
        self.email_user = emailRemetente
        self.email_password = emailUsuarioSenha
        self.email_send = emailDestinatario #nao sei o que isso faz
        subject = assunto

        msg = MIMEMultipart()
        msg['From'] = self.email_user
        msg['To'] = self.email_send
        msg['Subject'] = subject

        body = texto
        msg.attach(MIMEText(body,'plain'))

        filename = arquivo#'documento.pdf'
        attachment  = open(filename,'rb')

        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+filename)

        msg.attach(part)
        self.text = msg.as_string()

    def enviarEmail(self):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.email_user, self.email_password)
        self.server.sendmail(self.email_user, self.email_send, self.text)
        self.server.quit()