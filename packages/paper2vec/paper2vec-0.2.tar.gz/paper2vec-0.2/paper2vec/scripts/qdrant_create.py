import asyncio
from argparse import ArgumentParser
from paper2vec.datadestination import QdrantDatabase
parser = ArgumentParser()
parser.add_argument("--size", type=int, default=1536, help=f'Size of Qdrant collection.')
QdrantDatabase.add_arguements(parser)
args = parser.parse_args()
db = QdrantDatabase(args)
asyncio.get_event_loop().run_until_complete(db.create_collection(args.size))
