class GenerateID:
    @classmethod
    def generate_id(cls, length=5):
        import random
        import string
        # generate id dengan 5 angka random
        id = ''.join(random.choice(string.digits) for _ in range(length))
        return id
        