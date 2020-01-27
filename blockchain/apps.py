import datetime
import hashlib

class Block:
    next = None
    hash = None
    nonce = 0
    block_idx = 0
    previous_hash = 0x0
    
    def __init__(self, data=None):
        self.data = data
        self.timestamp = datetime.datetime.now()

    def hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.block_idx).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return 'Block Hash: {}\nBlock No: {}\nBlock Data: {}\nCalculated Hashes: {}\n\n'.format(self.hash(), self.block_idx, self.data, self.nonce)

class Blockchain:
    def __init__(self, difficulty=4, noonce_exponent=32):
        self.difficulty = difficulty
        self.maxNonce = 2 ** noonce_exponent
        self.target = 2 ** (256 - self.difficulty)
        # initialize genesis block & set the head pointer
        self.block = Block("Genesis")
        dummy = self.head = self.block

    def add(self, block):
        block.previous_hash = self.block.hash()
        block.block_idx = self.block.block_idx + 1
        self.block.next = block
        self.block = self.block.next
        # mongo_uri = CONFIG['database']['default']['uri']
        # with DatabaseConnection(mongo_uri):
        #     chain_info = BlockChain()
        #     chain_info.previous_hash = payload['title']
        #     chain_info.description = payload['description']
        #     chain_info.tags = payload['tags']
        #     chain_info.modified_on = datetime.now()
        #     chain_info.save()

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

blockchain = Blockchain(difficulty=16, noonce_exponent=256)

import json
from faker import Faker
faker_obj = Faker()

for n in range(1000):
    payload = json.dumps({
        "name": faker_obj.name(),
        "email": faker_obj.email(),
    })
    blockchain.mine(Block(payload))

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next