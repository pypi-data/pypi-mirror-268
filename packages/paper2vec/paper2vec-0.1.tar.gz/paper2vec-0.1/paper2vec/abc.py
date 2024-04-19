import abc
from typing import List, Dict, AsyncGenerator
from argparse import ArgumentParser


class Config(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def add_arguements(parser: ArgumentParser) -> None:
        pass


class Content:
    def __init__(self, id: str, text: str, payload: Dict):
        self.id: str = id
        self.text: str = text
        self.payload: Dict = payload


class DataSource(Config):
    @abc.abstractmethod
    async def get_contents(self) -> AsyncGenerator[Content, None]:
        yield


class Vectorizer(Config):
    @abc.abstractmethod
    async def vectorize(self, *contents: str) -> List[List[float]]:
        pass


class Point:
    def __init__(self, id: str, vector: List[float], payload: Dict):
        self.id: str = id
        self.vector: List[float] = vector
        self.payload: Dict = payload


class DataDestination(Config):
    @abc.abstractmethod
    async def write_vectors(self, *vectors: Point) -> None:
        pass


async def run(datasource: DataSource, vectorizer: Vectorizer, datadestination: DataDestination, batch_size: int):
    batch: List[Content] = []
    async for content in datasource.get_contents():
        batch.append(content)
        if len(batch) >= batch_size:
            vectors = await vectorizer.vectorize(*[c.text for c in batch])
            points = [
                Point(id=content.id, vector=vector, payload=content.payload) for vector, content in zip(vectors, batch)
            ]
            await datadestination.write_vectors(*points)
            batch = []
    if len(batch) > 0:
        vectors = await vectorizer.vectorize(*[c.text for c in batch])
        points = [
            Point(id=content.id, vector=vector, payload=content.payload) for vector, content in zip(vectors, batch)
        ]
        await datadestination.write_vectors(*points)
