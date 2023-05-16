"""Test ElasticSearch functionality."""

import pytest
from langchain.docstore.document import Document
from steamship import Steamship

from steamship_langchain.vectorstores import SteamshipVectorStore


@pytest.mark.usefixtures("client")
@pytest.mark.parametrize("model", ["text-embedding-ada-002", "text-similarity-davinci-001"])
def test_steamship_vector_store_from_texts(client: Steamship, model: str) -> None:
    """Test end to end construction and search."""
    texts = ["foo", "bar", "baz"]
    docsearch = SteamshipVectorStore.from_texts(
        client=client, texts=texts, embedding=model, index_name="test-index"
    )
    output = docsearch.similarity_search("foo", k=1)
    assert output == [Document(page_content="foo")]


@pytest.mark.usefixtures("client")
@pytest.mark.parametrize("model", ["text-embedding-ada-002", "text-similarity-davinci-001"])
def test_steamship_vector_store_with_metadatas_from_text(client: Steamship, model: str) -> None:
    """Test end to end construction and search."""
    texts = ["foo", "bar", "baz"]
    metadatas = [{"page": i} for i in range(len(texts))]
    docsearch = SteamshipVectorStore.from_texts(
        client=client,
        texts=texts,
        embedding=model,
        metadatas=metadatas,
        index_name="test-index",
    )
    output = docsearch.similarity_search("foo", k=1)

    assert output == [Document(page_content="foo", metadata={"page": 0})]


@pytest.mark.usefixtures("client")
@pytest.mark.parametrize("model", ["text-embedding-ada-002", "text-similarity-davinci-001"])
def test_steamship_vector_store_add_texts(client: Steamship, model: str) -> None:
    """Test end to end construction and search."""
    texts = ["foo", "bar", "baz"]
    docsearch = SteamshipVectorStore(client=client, embedding=model, index_name="test-index")
    docsearch.add_texts(texts=texts)
    output = docsearch.similarity_search("foo", k=1)
    assert output == [Document(page_content="foo")]


@pytest.mark.usefixtures("client")
@pytest.mark.parametrize("model", ["text-embedding-ada-002", "text-similarity-davinci-001"])
def test_steamship_vector_store_with_metadatas_add_text(client: Steamship, model: str) -> None:
    """Test end to end construction and search."""
    texts = ["foo", "bar", "baz"]
    metadatas = [{"page": i} for i in range(len(texts))]
    docsearch = SteamshipVectorStore(client=client, embedding=model, index_name="test-index")
    docsearch.add_texts(texts=texts, metadatas=metadatas)

    output = docsearch.similarity_search("foo", k=1)
    assert output == [Document(page_content="foo", metadata={"page": 0})]
