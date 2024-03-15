from pinecone import Pinecone as PineconeClient
import asyncio
from langchain.document_loaders.sitemap import SitemapLoader
from langchain_community.vectorstores import Pinecone
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

# Functions to Fetch data from website
def get_sitemap(sitemap_url):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loader = SitemapLoader(sitemap_url)
    docs = loader.load()
    return docs

#Function to split data into smaller chunks
def split_data(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunck_size = 1000,
        chuck_overlap = 200,
        length_function = len
    )
    docs_chunks = text_splitter.split_text(docs)
    return docs_chunks

# to create embeddings by choosing model 
def create_embeddings():
    embeddings = SentenceTransformerEmbeddings(model = "all-MiniLM-L6-v2")
    return embeddings

# to push the embeddings into the vector database
def push_to_pinecone(pinecone_api_key, pinecone_environment,pinecone_index_name, embedding,doc,):
    PineconeClient(
        api_key = pinecone_api_key,
        environment = pinecone_environment
    )
    index_name = pinecone_index_name
    index = Pinecone.from_document(doc, embedding, index_name = pinecone_index_name)
    return index


# pulling embedding from vector database
def pull_from_pinecone(pinecone_apikey,pinecone_environment,pinecone_index_name,embeddings):
    
    PineconeClient(
    api_key=pinecone_apikey,
    environment=pinecone_environment
    )

    index_name = pinecone_index_name
    #PineconeStore is an alias name of Pinecone class, please look at the imports section at the top :)
    index = Pinecone.from_existing_index(index_name, embeddings)
    return index

# to search quesry and get result on the basis of semantic search
def get_similar_docs(index, query, k=2):
    similar_docs = index.similarity_search(query, k=k)
    return similar_docs

