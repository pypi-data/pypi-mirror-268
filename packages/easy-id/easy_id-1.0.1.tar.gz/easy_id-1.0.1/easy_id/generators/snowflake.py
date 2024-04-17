import hashlib
import threading
import time
import uuid

from .base import GeneratorBase


def _generate_machine_thread_id():
    machine_id = uuid.getnode()
    thread_id = threading.current_thread().ident

    hashed = hashlib.sha1(str(machine_id).encode() + str(thread_id).encode())

    id_10bit = int(hashed.hexdigest(), 16) % 1024
    return id_10bit


MAX_TIMESTAMP = 0b11111111111111111111111111111111111111111
MAX_INSTANCE_ID = 0b1111111111
MAX_SEQUENCE_NUMBER = 0b111111111111


class SnowflakeID(GeneratorBase):
    def __init__(self, config):
        super().__init__()
        if config is None:
            config = {
                "machine_id": 0,
                "epoch": 0
            }
        self.config = config
        if self.config["machine_id"] == 0 or self.config["machine_id"] is None:
            self.config["machine_id"] = _generate_machine_thread_id()

        if not (1 <= self.config["machine_id"] <= MAX_INSTANCE_ID):
            raise ValueError(f'machine_id must be between 1 and {MAX_INSTANCE_ID}')

        if self.config["epoch"] is None:
            self.config["epoch"] = 0

        self.time_n = self.config["epoch"]
        self.seq_n = 0

    def generate(self):
        with self.lock:
            timestamp = int(time.time() * 1000)
            if timestamp == self.time_n:
                self.seq_n = (self.seq_n + 1) & MAX_SEQUENCE_NUMBER
                if self.seq_n == 0:
                    timestamp = self.wait_next_ms(timestamp)
            else:
                self.seq_n = 0

            self.time_n = timestamp
            diff_time = timestamp - self.config["epoch"]
            return ((diff_time & MAX_TIMESTAMP) << 22) | (self.config["machine_id"] << 12) | self.seq_n

    @staticmethod
    def wait_next_ms(last):
        timestamp = int(time.time() * 1000)
        while timestamp <= last:
            timestamp = int(time.time() * 1000)
        return timestamp

    def parse_id(self, id):
        timestamp = (id >> 22) + self.config.epoch
        machine_id = (id >> 12) & MAX_INSTANCE_ID
        sequence_number = id & MAX_SEQUENCE_NUMBER
        return timestamp, machine_id, sequence_number

    def __str__(self):
        mid = self.config["machine_id"]

        return f"[ID: {mid}], [Time: {self.time_n}], [Seq: {self.seq_n}]"
