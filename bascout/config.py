import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Configuration class for bascout.
    """

    SECRET_KEY = os.getenv("BASCOUT_SECRET_KEY")
