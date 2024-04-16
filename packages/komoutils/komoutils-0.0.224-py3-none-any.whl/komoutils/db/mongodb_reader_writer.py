import logging
from typing import Union

import pymongo

from komoutils.core import KomoBase


class MongoDBReaderWriter(KomoBase):

    def __init__(self, uri: str, db_name: str):
        self.client: pymongo.MongoClient = pymongo.MongoClient(uri)
        self.db = self.client[db_name]

    @property
    def name(self):
        return "mongodb_reader_writer"

    def start(self):
        pass

    def read(self, collection: str, filters=None, omit=None, limit: int = 1000000):
        if filters is None:
            filters = {}
        if omit is None:
            omit = {}

        records: list = list(self.db[collection].find(filters, omit).sort('_id', -1).limit(limit=limit))
        return records

    def write(self, collection: str, data: Union[list, dict]):
        if len(data) == 0:
            self.log_with_clock(log_level=logging.INFO,
                                msg=f"0 records to send for collection {collection}. ")
            return
        # print(f"++++++++++++++++++++++++++++++++++++++++++++++++")
        try:
            if isinstance(data, dict):
                self.db[collection].insert_one(data)
            elif isinstance(data, list):
                self.db[collection].insert_many(data)

            self.log_with_clock(log_level=logging.DEBUG, msg=f"Successfully sent {collection} with size "
                                                             f"{len(data)} data to database. ")
            return 'success'
        except Exception as e:
            self.log_with_clock(log_level=logging.ERROR, msg=f"Unspecified error occurred. {e}")

    def updater(self, collection: str, filters: dict, updater: dict):
        if len(updater) == 0:
            self.log_with_clock(log_level=logging.INFO,
                                msg=f"0 records to send for {self.db.upper()} for collection {collection}. ")
            return

        result = self.db[collection].update_one(filter=filters, update=updater, upsert=True)
        return result
