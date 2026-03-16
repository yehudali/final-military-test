import os
from dotenv import load_dotenv

load_dotenv()


class ServiseAConfig:
    def __init__(self) -> None:
        self.BOOTSTRAP_SERVERS:str = str(os.getenv("BOOTSTRAP_SERVERS"))
        self.MONGO_URL:str = str(os.getenv('MONGO_URL'))
        self.validator()

    def validator(self):
        if not self.BOOTSTRAP_SERVERS:
            print("i not hav a BOOTSTRAP_SERVERS env!")
            raise
        if not self.MONGO_URL:
            print("i not hav a MONGO_URL env!")
            raise

        