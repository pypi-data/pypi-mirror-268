from openai import AsyncOpenAI
from paper2vec.abc import Vectorizer
from argparse import ArgumentParser
import dbm
import os
import json


class TextEmbedding(Vectorizer):
    @staticmethod
    def add_arguements(parser: ArgumentParser):
        parser.add_argument("--api_key", type=str, required=True, help="Your OpenAI API key.")
        parser.add_argument("--model",
                            choices=['text-embedding-3-small', 'text-embedding-3-large', 'text-embedding-ada-002'],
                            default='text-embedding-3-small',
                            help="Which model do you want to use.")
        parser.add_argument("--cache", type=str, default="openai_cache", help="Your cache file for embeddings.")

    def __init__(self, args):
        self.client = AsyncOpenAI(api_key=args.api_key)
        self.model = args.model
        self.cache = os.path.join(args.cache, args.model)
        os.makedirs(args.cache, exist_ok=True)
        with dbm.open(self.cache, 'c'):
            pass

    async def get_cache(self, sentences):
        with dbm.open(self.cache, 'r') as db:
            return [json.loads(db[content]) if content in db else None for content in sentences]

    async def put_cache(self, sentences, vectors):
        with dbm.open(self.cache, 'w') as db:
            for sentence, vector in zip(sentences, vectors):
                db[sentence] = json.dumps(vector)

    async def vectorize(self, *contents):
        sentences = [text.replace("\n", " ") for text in contents]
        vectors = await self.get_cache(sentences)
        if None in vectors:
            uncached_sentences = [sentence for sentence, vector in zip(sentences, vectors) if vector is None]
            resp = await self.client.embeddings.create(input=uncached_sentences, model=self.model)
            embeddings = [d.embedding for d in resp.data]
            await self.put_cache(uncached_sentences, embeddings)
            for i in range(len(vectors)):
                if vectors[i] is None:
                    vectors[i] = embeddings[0]
                    embeddings = embeddings[1:]
        return vectors
