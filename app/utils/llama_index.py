from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex

# Global index variable (to be built/initialized at startup)
INDEX = None

def build_index(documents_path):
    """
    Builds an index from documents located in the given directory.
    """
    documents = SimpleDirectoryReader(documents_path).load_data()
    index = GPTSimpleVectorIndex(documents)
    return index

def initialize_index(documents_path="docs/mental_health"):
    """
    Initializes the global index.
    """
    global INDEX
    INDEX = build_index(documents_path)

def get_relevant_info(query):
    """
    Queries the global index for information related to the query.
    """
    global INDEX
    if INDEX is None:
        initialize_index()
    result = INDEX.query(query)
    return result.response
