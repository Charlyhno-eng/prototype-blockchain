import time
import hashlib

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        to_hash = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(to_hash.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.counter = 1
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block(0, "Genesis Block", "0")
        self.chain.append(genesis)

    def add_block(self):
        prev_block = self.chain[-1]
        block = Block(self.counter, str(self.counter), prev_block.hash)
        self.chain.append(block)
        self.counter += 1
        return block