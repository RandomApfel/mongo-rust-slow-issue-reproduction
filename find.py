#!/usr/bin/env python3

from os import environ
from pymongo import MongoClient
from time import time

def main():
    c = MongoClient(environ.get('MONGODB_URI'))

    collection = c[environ.get('MONGODB_DB')]['sample_data']

    print('Querying halve of the sample documents')

    start = time()
    filter_ = {'type': 'A', 'timestamp': {'$gt': 0}}
    cursor = collection.find(filter_, None)

    result = []
    for res in cursor:
        result.append(res)

    duration_seconds = time() - start
    print('Done, fetched {} documents in {} seconds'.format(len(result), duration_seconds))

main()

