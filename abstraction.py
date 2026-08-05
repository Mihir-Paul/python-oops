#Abstraction 
class EmailService():
    def _connect(self):
        print("Connecting to email server")

    def _authentication(self):
        print("Authenticating...")

    def send_email(self):
        self._connect()
        self._authentication()
        print("Sending email..")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting...")

email = EmailService()
email.send_email()