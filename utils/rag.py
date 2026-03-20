from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Function to create a vector store from input text
def create_vectorstore(text):
    # Initialize the text splitter with chunk size and overlap
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    # Split the text into chunks
    chunks = splitter.split_text(text)

    # Create embeddings using HuggingFace model
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Create and return FAISS vector store from chunks and embeddings
    return FAISS.from_texts(chunks, embeddings)