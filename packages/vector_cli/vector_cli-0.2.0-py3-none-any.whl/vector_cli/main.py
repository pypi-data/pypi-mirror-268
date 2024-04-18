import click
import os
from .app import upsert_faiss_index, get_openai_response, index_documents

@click.group()
def cli():
    pass

@cli.command()
@click.argument('folder_path', type=click.Path(exists=True))
def add(folder_path):
    """ Lists all files in the given folder """
    index_documents(folder_path)
    

@cli.command()
@click.argument('question')
def ask(question):
    """ Echoes the question """
    get_openai_response(question)

if __name__ == "__main__":
    cli()
