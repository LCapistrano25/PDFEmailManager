from imap_tools import MailBox
from interface.connection.con_interface import ConnectionInterface

class Connection(ConnectionInterface):
    """Responsável por realizar a conexão com o email"""
    def __init__(self, imap_server, email, password, initial_folder="INBOX"):
        super().__init__(imap_server, email, password, initial_folder)

    def perform_connection(self):
        """Responsável por realizar o login"""
        try:
            return MailBox(self._imap_server).login(self._email, self._password, self._initial_folder)
        except Exception as e:
            print(f"Erro ao conectar: {e}")
            return None