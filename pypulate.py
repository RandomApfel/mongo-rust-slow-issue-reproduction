#!/usr/bin/env python3

from os import environ
from pymongo import MongoClient
import random

# Document count = SAMPLE_BLOCKS * BLOCK_SIZE
SAMPLE_BLOCKS = 500
BLOCK_SIZE = 1000

def get_example_document(timestamp: int) -> dict:
    return {
        'type': random.choice(['A', 'B']),
        'timestamp': timestamp,
        'foo': random.randrange(0, 100),
        'bar': random.randrange(0, 100),
    }


def main():
    c = MongoClient(environ.get('MONGODB_URI'))

    collection = c[environ.get('MONGODB_DB')]['sample_data']
    collection.drop()

    print('Inserting {} sample documents'.format(BLOCK_SIZE * SAMPLE_BLOCKS))

    for i in range(SAMPLE_BLOCKS):
        sample_block = []
        for j in range(BLOCK_SIZE):
            timestamp = i * BLOCK_SIZE + j
            sample_block.append(get_example_document(timestamp))

        collection.insert_many(sample_block)

    print('Done')

main()
