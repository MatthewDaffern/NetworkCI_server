import smtplib
import sys
import json


# done
def create_server_object(server_name):
    server_object = smtplib.SMTP.connect(server_name)
    server_object.ehlo()
    server_object.starttls()
    server_object.ehlo()
    return server_object


# done
def login_to_server(server_connection_object, username, password):
    return server_connection_object.login(username, password)


# done
def send_mail(server_connection_object, from_address, to_address, mail_text):
    return server_connection_object.sendmail(from_address, to_address, mail_text)


# done
def load_config(file_name):
    with open(file_name, 'r+') as file:
        return json.load(file)


# done
def main(config_name, mail_text):
    config_object = load_config(config_name)
    server_object = create_server_object(config_object['server_name'])
    with_login = login_to_server(server_object, config_object['username'], config_object['password'])
    return send_mail(with_login, config_object['from_address'], config_object['to_address'], mail_text)


# done
if __name__ == '__main__':
    main('mail.json', sys.argv[1])


