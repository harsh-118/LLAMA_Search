import os
from llama_index.llms.anthropic import Anthropic
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex
from llama_index.core.indices import SummaryIndex
from llama_index.readers.file import PyMuPDFReader


os.environ['ANTHROPIC_API_KEY'] = "Your API"
llm = Anthropic(model="claude-3-opus-20240229", temperature=0.0)

Settings.llm = llm
Settings.embed_model = "BAAI/bge-m3"

loader = PyMuPDFReader()
documents = loader.load(file_path="harry_potter.pdf")

vector_index = VectorStoreIndex.from_documents(documents)
query_engine = vector_index.as_query_engine(response_mode="compact")
#here different type of mode for chunks 

response = query_engine.query("who is ron?")
print("===================================")
print(response)