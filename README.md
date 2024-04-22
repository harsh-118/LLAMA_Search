
# Document Indexing and Querying with Anthropic API

### Description:
* Python script demonstrating document indexing and querying using the Anthropic API.
* Utilizes libraries for document loading **(PyMuPDFReader)**, vector indexing **(VectorStoreIndex)**, and query processing **(query_engine)**.
* Requires setting up Anthropic API key as an environment variable.
### Usage:
* Replace **"Your API"** with your Anthropic API key.
* Ensure the necessary libraries **(llama_index, llma_index.llms.anthropic, llama_index.core**, etc.) are installed and accessible.
* Provide a PDF file path **(file_path)** to load documents for indexing.
* Customize query strings **(query_engine.query(...))** for specific document inquiries.


## Installation

### 1.Python:
Ensure you have Python installed on your system. You can download and install Python from the official website.

### 2.pip:
pip is the package installer for Python. It usually comes installed with Python versions 3.4 and above. You can upgrade pip to the latest version using:
```bash
 python -m pip install --upgrade pip
```

### 3.llama_index:
Install the llama_index library and its dependencies. This might include other required packages like numpy, torch, etc
```
pip install llama_index
```

### 4.PyMuPDF:
For PDF file parsing, you'll need PyMuPDF:
```
pip install PyMuPDF
```

### 5.Anthropic API:
You'll need an API key from Anthropic. If you haven't already, sign up on the Anthropic website to obtain your API key.

    
## Deployment

### 1.Setting Environment Variable:

```
  os.environ['ANTHROPIC_API_KEY'] = "Your API"

```
This line sets an environment variable ANTHROPIC_API_KEY to your Anthropic API key. Replace "Your API" with your actual API key.

### 2.Initializing Anthropic Model:
```
llm = Anthropic(model="claude-3-opus-20240229", temperature=0.0)
```
Here, you're initializing an instance of the Anthropic class from the llma_index.llms.anthropic module with a specific model (claude-3-opus-20240229) and setting the temperature parameter to 0.0.

### 3.Setting Global Settings:
```
Settings.llm = llm
Settings.embed_model = "BAAI/bge-m3"
```
You're configuring global settings for the indexing process, setting the llm and embedding model according to your choice.

### 4.Loading Documents:
```
loader = PyMuPDFReader()
documents = loader.load(file_path="harry_potter.pdf")
```
This part uses PyMuPDFReader from llama_index.readers.file to load a PDF file (harry_potter.pdf) and extract its content into documents.

### 5.Creating Vector Store Index:
```
vector_index = VectorStoreIndex.from_documents(documents)
```
Using the documents loaded from the PDF file, you're creating a VectorStoreIndex, which presumably builds a vector representation of the document content for efficient querying.

### 6.Setting up Query Engine:
```
query_engine = vector_index.as_query_engine(response_mode="compact")
```
This prepares a query engine (query_engine) using the vector_index with a specified response_mode of "compact".

### 7.Performing Query:
```
response = query_engine.query("who is ron?")
```
You're querying the prepared query_engine with the question "who is ron?".

### 8.Displaying Response:
```
print("===================================")
print(response)
```
Finally, you're printing the response obtained from the query engine.