from imap_tools import MailBox, AND, MailMessageFlags
from interface.client.email_client import EmailClient

class ImapToolsEmailClient(EmailClient):

    def __init__(self, mailbox: MailBox):
        self._mailbox = mailbox

    def box(self, criteria: str = None):
        return self._mailbox.fetch(criteria)
    
    def get_unread_emails(self):
        return self._mailbox.fetch(AND(seen=False))

    def mark_as_read(self, uid: str):
        self._mailbox.flag(uid, MailMessageFlags.SEEN, True)

    def move_to_folder(self, uid: str, folder: str):
        self._mailbox.move(uid, folder)

    def delete(self, uid: str):
        self._mailbox.delete(uid)

    def create_folder(self, folder_name: str) -> None:
        current = self._mailbox.folder.get()
        
        if not self.exist_folder(folder_name):
            self._mailbox.folder.create(folder_name)
        
        self._mailbox.folder.set(current)

    def folder_exists(self, folder: str):
        return self._mailbox.folder.exists(folder)
