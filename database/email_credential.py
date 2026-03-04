from dataclasses import dataclass

@dataclass(frozen=True)
class EmailCredentials:
    imap_server: str
    email: str
    password: str
    initial_folder: str = "INBOX"