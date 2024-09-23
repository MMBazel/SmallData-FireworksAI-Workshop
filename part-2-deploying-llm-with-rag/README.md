# Part 2: Deploying an LLM with Retrieval-Augmented Generation (RAG)

## Objectives:
In this part of the workshop, you will:
- Deploy a **Retrieval-Augmented Generation (RAG)** system using an LLM from Fireworks.
- Connect to a **vector store** (to be decided) to retrieve relevant documents and use the LLM to generate contextually accurate responses based on the retrieved data.

---

## Relevant Concepts/Skills:
By completing this task, you will:
- Learn how **RAG** works and how combining retrieval with generation improves model responses.
- Understand how to connect to and query a **vector store** for document retrieval.
- Gain experience in building AI systems that combine retrieval and generation to handle more complex queries.

---

## General Background Information:
[TODO] Add links to interesting resources at the bottom, like Vicki's embeddings book

### **A. Embeddings**
- **What They Are**: Vector representations of text, images, or other data types. These vectors capture semantic meaning and are used in retrieval systems (e.g., vector stores) to find similar data points.
- **Why It Matters**: Embeddings allow you to search large datasets for semantically similar documents or content, which is critical for tasks like RAG, recommendation systems, or even advanced search applications.

[TODO] Add image

### **B. Retrieval-Augmented Generation (RAG)**
- **What It Is**: A combination of a retrieval mechanism (like a vector store) and a generative model (like an LLM). This approach allows a model to pull in external knowledge or context when generating responses, making its output more accurate and relevant.
- **Why It Matters**: Standard LLMs are limited by their training data and context window. RAG enhances these models by fetching relevant information from a database or document store before generating a response, improving accuracy and contextual understanding.

[TODO] Add image

### **C. Vector Databases**
- **What They Are**: Databases that store embeddings (vectors) and allow for similarity searches. These are used in retrieval systems to find documents or data points most similar to a given query.
- **Why It Matters**: In RAG systems, vector databases (like Pinecone, Weaviate, or FAISS) enable quick and efficient retrieval of relevant information to feed into an LLM for more contextually aware responses.

[TODO] Add image

### Additional Considerations:

- **LLM Selection**: Depending on the task, you might choose different types of models from Fireworks (e.g., models fine-tuned for technical answers versus general knowledge generation).
- **Document Ingestion**: In production systems, you would likely batch process and pre-process large datasets before ingesting them into a vector store. The ingestion process for this workshop will be kept simple for learning purposes.
- **Query Complexity**: You can extend the complexity of queries by using more advanced techniques like query expansion or document chunking to improve retrieval results.

---

## Fireworks-Specific Information:
In a Retrieval-Augmented Generation (RAG) application, **Fireworks** fits in two primary areas:

1. **Embeddings Generation**: Fireworks offers a range of embedding models that transform input text into high-dimensional vectors. These embeddings represent the semantic meaning of documents or queries, which is crucial for efficient retrieval in a RAG system. In a typical RAG pipeline, Fireworks is responsible for generating embeddings from the query and relevant documents.
2. **Language Model Inference**: Fireworks also provides powerful large language models (LLMs) such as Meta Llama, Mixtral, and Google Gemma. These models synthesize the retrieved information and generate responses based on the context provided by the embeddings. Fireworks is used to query these models to enhance the quality and relevance of the final generated response.


In short, Fireworks AI allows you to query LLMs easily and integrates well with retrieval systems. You can combine Fireworks models with vector stores to build a RAG system.
  - **Text Models Querying Guide**: [Querying Text Models](https://docs.fireworks.ai/guides/querying-text-models)
  - **Fireworks Python Client Setup**: [Install the Fireworks Python Client](https://docs.fireworks.ai/tools-sdks/python-client/installation)


### Minimum Viable RAG Q&A App with Fireworks:
This setup allows you to build a lightweight RAG system where Fireworks handles both embedding generation and LLM inference.

- Vector Store: A database that stores document embeddings for efficient retrieval based on similarity to the user’s query.
- Embeddings Generation: Use Fireworks embedding models to convert user queries and documents into embeddings.
- Query Processing: The query is first embedded and then used to retrieve the most relevant documents from the vector store.
- Response Generation: The retrieved documents are passed to an LLM hosted on Fireworks, which generates a coherent answer by leveraging both the query and the retrieved information.

## Steps to Accomplish the Task:

1. **Step 1: Set Up Fireworks API and Choose a Model**:
    - Install the Fireworks Python client and authenticate using your API key:
    ```bash
    pip install fireworks
    ```
    - In your Python code:
    ```python
    import fireworks

    # Initialize Fireworks client
    client = fireworks.Client(api_key="your_api_key")

    # Choose a model from Fireworks (e.g., a text generation model)
    model_name = "your_llm_model"
    ```

2. **Step 2: Set Up the Vector Store**:
    - Depending on the chosen vector store (e.g., Pinecone), you’ll need to initialize the store and add documents.
    ```python
    import pinecone

    # Initialize Pinecone
    pinecone.init(api_key="your_pinecone_api_key", environment="us-west1-gcp")

    # Create or connect to an index
    index = pinecone.Index("your_index_name")
    ```

3. **Step 3: Ingest Documents into the Vector Store**:
    - Generate embeddings for your documents and store them in the vector store:
    ```python
    documents = ["Document 1 text...", "Document 2 text..."]
    embeddings = [generate_embedding(doc) for doc in documents]
    
    # Insert documents into the vector store
    for doc, embedding in zip(documents, embeddings):
        index.upsert([{"id": doc_id, "values": embedding, "metadata": {"text": doc}}])
    ```

4. **Step 4: Query the Vector Store and Pass Data to the LLM**:
    - Retrieve relevant documents based on the user's query and pass them to the LLM:
    ```python
    query = "How to optimize model training?"
    
    # Generate embedding for the query
    query_embedding = generate_embedding(query)

    # Retrieve relevant documents
    result = index.query(queries=[query_embedding], top_k=3)
    relevant_docs = [match['metadata']['text'] for match in result['matches']]
    
    # Pass retrieved data to the LLM
    prompt = f"Based on the following documents: {relevant_docs}, answer the query: {query}"
    response = client.generate(model_name=model_name, prompt=prompt)
    print(response['text'])
    ```

5. **Step 5: Perform a Vibe Check on the RAG System**:
    - Test the system with different queries and retrieved documents to verify that the LLM generates more contextually accurate responses based on the retrieved information.