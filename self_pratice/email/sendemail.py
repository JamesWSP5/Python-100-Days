from email.mime.text import MIMEText


def sendmsg():
    msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
    # 输入Email地址和口令:
    from_addr = input('18039111398@163.com ')
    password = input('13526494615wu')
    # 输入收件人地址:
    to_addr = input('511891957@qq.com ')
    # 输入SMTP服务器地址:
    smtp_server = input('smtp.163.com')

    import smtplib

    server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


if __name__ == '__main__':
    sendmsg()
