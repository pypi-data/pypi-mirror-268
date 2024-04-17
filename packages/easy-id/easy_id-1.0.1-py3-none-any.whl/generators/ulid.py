import secrets
import time

from .base import GeneratorBase


class ULID(GeneratorBase):
    def __init__(self, config=None):
        super().__init__()
        if config is None:
            config = {
                "epoch": 0
            }
        self.config = config

    def generate(self):
        # Getting time now, converting it to milliseconds, ensuring it fits in 48 bits
        timestamp = int((time.time() - self.config["epoch"]) * 1000)
        timestamp = timestamp & ((1 << 48) - 1)  # 48-bit timestamp

        # Generating 80-bit random using secrets
        random_data = secrets.token_bytes(10)  # Generating 80 random bits

        # Converting random bytes to integer number
        random_data_int = int.from_bytes(random_data, byteorder='big')

        return (timestamp << 80) | random_data_int

