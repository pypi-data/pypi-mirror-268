import os
import json
from fastapi import WebSocketDisconnect
from gai.common.http_utils import http_post, http_delete,http_get
from gai.common.logging import getLogger
logger = getLogger(__name__)
from gai.common.errors import ApiException
import asyncio
from gai.lib.ClientBase import ClientBase
import threading
import websockets
import time
from threading import Thread

import asyncio
from urllib.parse import urlsplit

from gai.common.StatusListener import StatusListener
async def run_listener(server_uri, progress_updater):
    listener = StatusListener(server_uri)
    await listener.listen(callback=progress_updater)

class RAGClientBase(ClientBase):
    
    def __init__(self,config_path=None):
        super().__init__(config_path)
        self.base_url = os.path.join(
            self.config["gai_url"], 
            self.config["generators"]["rag"]["url"].lstrip('/'))
        logger.debug(f'base_url={self.base_url}')

    def _prepare_files_and_metadata(self, collection_name, file_path, metadata):
        mode = 'rb' if file_path.endswith('.pdf') else 'r'
        with open(file_path, mode) as f:
            files = {
                "file": (os.path.basename(file_path), f if mode == 'rb' else f.read(), "application/pdf"),
                "metadata": (None, json.dumps(metadata), "application/json"),
                "collection_name": (None, collection_name, "text/plain")
            }
            return files

class RAGClientSync(RAGClientBase):

    def __init__(self,config_path=None):
        super().__init__(config_path)

# Indexing Transaction -------------------------------------------------------------------------------------------------------------------------------------------


    # synchronous version of index_file_async
    def index_file(self, 
        collection_name, 
        file_path, 
        title="",
        source="",
        authors="",
        publisher="",
        published_date="",
        comments="",
        keywords=""):
        url = os.path.join(self.base_url,"index-file")
        metadata = {
            "title": title,
            "source": source,
            "authors": authors,
            "publisher": publisher,
            "published_date": published_date,
            "comments": comments,
            "keywords": keywords
        }

        # We will assume file ending with *.pdf to be PDF but this check should be done before the call.
        mode = 'rb' if file_path.endswith('.pdf') else 'r'
        with open(file_path, mode) as f:
            files = {
                "file": (os.path.basename(file_path), f.read(), "application/pdf"),
                "metadata": (None, json.dumps(metadata), "application/json"),
                "collection_name": (None, collection_name, "text/plain")
            }
            logger.info(f"RAGClient.index_file: {url}")            
            response = http_post(url=url, files=files)
        
        # {document_id: "document_id"}
        return json.loads(response.text)

    def retrieve(self, collection_name, query_texts, n_results=None):
        url = os.path.join(self.base_url,"retrieve")
        logger.info(f"RAGClient.retrieve: {url}")
        data = {
            "collection_name": collection_name,
            "query_texts": query_texts
        }
        if n_results:
            data["n_results"] = n_results

        response = http_post(url, data=data)
        return response

#Collections-------------------------------------------------------------------------------------------------------------------------------------------

    def list_collections(self):
        url = os.path.join(self.base_url,"collections")
        logger.info(f"RAGClient.list_collections: {url}")
        response = http_get(url)
        return json.loads(response.text)

    def purge_all(self):
        url = os.path.join(self.base_url,"purge")
        logger.info(f"RAGClient.purge_all: {url}")
        response = http_delete(url)
        return json.loads(response.text)

    def delete_collection(self, collection_name):
        url = os.path.join(self.base_url,"collection",collection_name)
        logger.info(f"RAGClient.delete_collection: {url}")
        try:
            response = http_delete(url)
        except ApiException as e:
            if e.code == 'collection_not_found':
                return {"count":0}
            logger.error(e)
            raise e
        return json.loads(response.text)

#Documents-------------------------------------------------------------------------------------------------------------------------------------------

    def list_documents(self):
        url = os.path.join(self.base_url,"documents")
        logger.info(f"RAGClient.list_documents: {url}")
        response = http_get(url)
        return json.loads(response.text)

    def list_documents_by_collection(self,collection_name):
        url = os.path.join(self.base_url,f"documents/{collection_name}")
        logger.info(f"RAGClient.list_documents_by_collection: {url}")
        response = http_get(url)
        return json.loads(response.text)

    def get_document_header(self,collection_name,doc_id):
        url = os.path.join(self.base_url,f"document/{collection_name}/{doc_id}")
        logger.info(f"RAGClient.get_documents: {url}")
        response = http_get(url)
        return json.loads(response.text)

    def delete_document(self,collection_name,doc_id):
        url = os.path.join(self.base_url,f"document/{collection_name}/{doc_id}")
        logger.info(f"RAGClient.delete_documents: {url}")
        response = http_delete(url)
        return json.loads(response.text)

    def get_document_id(self,collection_name, file_path):
        url = os.path.join(self.base_url,f"document/exists/{collection_name}")
        logger.info(f"RAGClient.document_exists: {url}")
        with open(file_path, "r") as f:
            text = f.read()        
        files = {
            "file": (file_path, text, "text/plain"),
            "collection_name": (None, collection_name, "text/plain")
        }        
        response = http_post(url, files=files)
        return json.loads(response.text)    


#chunks-------------------------------------------------------------------------------------------------------------------------------------------

    def list_chunks(self,collection_name=None,doc_id=None):

        if collection_name and not doc_id or doc_id and not collection_name:
            raise Exception("Both collection_name and doc_id must be provided or neither.")
        
        if not collection_name and not doc_id:
            url = os.path.join(self.base_url,"chunks")
            logger.info(f"RAGClient.list_chunks: {url}")
            try:
                response = http_get(url)
                return json.loads(response.text)
            except Exception as e:
                if e.detail['code'] == 'collections_not_found':
                    return []
                raise e

        url = os.path.join(self.base_url,f"chunks/by_document/{collection_name}/{doc_id}")
        logger.info(f"RAGClient.list_chunks: {url}")
        response = http_get(url)
        if response.status_code == 404:
            return []

        return json.loads(response.text)

    
    def get_chunk(self,collection_name, chunk_id):

        url = os.path.join(self.base_url,f"chunk/{collection_name}/{chunk_id}")
        logger.info(f"RAGClient.get_chunk: {url}")
        response = http_get(url)
        return json.loads(response.text)
