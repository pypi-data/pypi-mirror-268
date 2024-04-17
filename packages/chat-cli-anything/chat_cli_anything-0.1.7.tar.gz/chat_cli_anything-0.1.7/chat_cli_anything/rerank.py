from typing import Sequence
from chat_cli_anything.config import Config
import requests

def build_reranker():
    from FlagEmbedding import FlagReranker
    # Setting use_fp16 to True speeds up computation with a slight performance degradation
    reranker = FlagReranker('BAAI/bge-reranker-base', use_fp16=True) 
    return reranker

def rerank(
    query: str,
    docs: Sequence[str],
    topk: int = 4,
) -> Sequence[str]:
    """Rerank the documents using BGE-Reranker."""
    config = Config()
    active_embedding = config.get('active_embedding', None)

    if not active_embedding:
        click.secho(f'{SERVICE_NAME} is not configured.', fg='red')

    base_url = config.get('embeddings')[active_embedding]['base_url']
    response = requests.post(
        f"{base_url}/rerank",
         json={"query": query, "documents": docs, "topk": topk}
    )
    return response.json()['documents']
