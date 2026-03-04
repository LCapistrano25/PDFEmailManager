from database.email_credential import EmailCredentials
from interface.connection.con_interface import ConnectionInterface

class ImapConnection(ConnectionInterface):
    def __init__(self, credentials: EmailCredentials):
        self._credentials = credentials
        self._connection = None

    def connect(self):
        """Responsável por realizar o login"""
        try:
            self._connection = MailBox(self._credentials.imap_server).login(self._credentials.email, self._credentials.password, self._credentials.initial_folder)
            return self._connection
        except Exception as e:
            print(f"Erro ao conectar: {e}")
            return None

    def disconnect(self):
        """Responsável por realizar o logout"""
        try:
            self._connection.logout()
        except Exception as e:
            print(f"Erro ao desconectar: {e}")
