import abc
import uuid


class Store(abc.ABC):
    def __init__(self, sync_destination):
        self.id = sync_destination.get('id', uuid.uuid4())
        self.name = sync_destination.get('name', '')
        self.modalities = sync_destination.get('sync_modalities', ['SR'])

    @abc.abstractmethod
    def store(self, ds, called_ae=None):
        pass
