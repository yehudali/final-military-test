import os
from dotenv import load_dotenv

load_dotenv()


class ServiseAConfig:
    def __init__(self) -> None:
        self.BOOTSTRAP_SERVERS:str = str(os.getenv("BOOTSTRAP_SERVERS"))
        self.validator()

    def validator(self):
        if not self.BOOTSTRAP_SERVERS:
            print("i not hav a BOOTSTRAP_SERVERS env!")
            raise
        