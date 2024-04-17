from .base import GeneratorBase


class NanoID(GeneratorBase):
    def __init__(self, config=None):
        super().__init__()
        if config is None:
            config = {
                "alphabet": "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz-",
                "length": 21
            }
        self.config = config

    def generate(self):
        import secrets
        id_str = ''.join(secrets.choice(self.config['alphabet']) for _ in range(self.config['length']))
        return id_str