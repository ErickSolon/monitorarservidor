import subprocess
import smtplib
import time

from logconf.log import logrun

try:
    datahora = time.ctime()
    datahora = datahora.split()

    comando = subprocess.run(
        ["ping 8.8.8.8"]
    )

    nome = subprocess.run(
        ["whoami"]
    )

    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.ehlo()
    smtp.starttls()
    email_servidor = ""
    senha_email_servidor = ""
    email_cliente = ""
    smtp.login(email_servidor, senha_email_servidor)
    mensagem = "O comando no seu computador rodou com sucesso, segue o output: " + comando.stdout
    smtp.sendmail(email_servidor, email_cliente, f"Report simples do sistema: {nome.stdout}.".format(mensagem))
    print("Report enviado!")

    l = logrun(datahora, email_servidor, email_cliente)
    l.gravar()
except Exception as e:
    print(e)
finally:
    smtp.quit()