
# Part 1: Connecting to Fireworks & Building a Model Comparison App

## Objectives:
In this part of the workshop, you will:
- Connect to Fireworks AI's platform to access a list of hosted models.
- Utilize a **Streamlit app** that allows users to compare different models from Fireworks via a dropdown menu.
- Perform initial “vibe checks” by querying the selected models.

---

## Relevant Concepts/Skills:
By completing this task, you will:
- Learn how to use Fireworks' API to interact with and query LLMs and multimodal models.
- Gain hands-on experience with building interactive apps using **Streamlit**.

We'll also cover:
- The different types of models (text vs multimodal).
- The difference between chat vs completion models.
- Some key parameters for text models versus visual-language models.


--- 

## Background Information:
- **Model Types**: Fireworks AI offers multiple types of models:
  - **Text Models**: These are used for tasks like text generation, completion, or Q&A.
  - **Multimodal Models**: These handle multiple data types, such as text and images.
  - **Chat vs Completion Models**: Chat models are optimized for back-and-forth conversations, while completion models generate a single block of text from a given prompt.
  
<insert images of Fireworks here>

- **Streamlit**: A Python-based framework for building and deploying simple web apps. You’ll use Streamlit to create a user-friendly interface to interact with the models.

<insert architectural diagram of Streamlit + Fireworks>

---

# Task 1: Explore models available on Fireworks via the model playground:
## Background





---
# Task 2: Connect to Fireworks model APIs using streamlit
## Background
- **Fireworks API**: Fireworks provides a simple API to query its hosted models. You can interact with the API to retrieve available models, send queries, and get results from LLMs.
  - **Text Models Querying Guide**: [Querying Text Models](https://docs.fireworks.ai/guides/querying-text-models)
  - **Embedding Models Querying Guide**: [Querying Embedding Models](https://docs.fireworks.ai/guides/querying-embeddings-models)
  - **Python Client Setup**: [Install the Fireworks Python Client](https://docs.fireworks.ai/tools-sdks/python-client/installation)

  --- 

## Steps

1. **Step 1: Set Up Fireworks API Connection**:
    - Install the Fireworks Python client and authenticate using your API key:
    ```bash
    pip install fireworks
    ```
    - In your Python code:
    ```python
    import fireworks

    # Initialize Fireworks client
    client = fireworks.Client(api_key="your_api_key")

    # Fetch the list of available models
    models = client.get_models()
    print(models)
    ```

2. **Step 2: Build the Streamlit App**:
    - Install **Streamlit**:
    ```bash
    pip install streamlit
    ```
    - Create a basic Streamlit app to select and compare models:
    ```python
    import streamlit as st
    import fireworks

    # Initialize Fireworks client
    client = fireworks.Client(api_key="your_api_key")

    # Fetch available models
    models = client.get_models()

    # Create a dropdown to select a model
    model_name = st.selectbox("Select a model:", [model['name'] for model in models])

    # Display model information
    st.write(f"Selected model: {model_name}")
    ```

3. **Step 3: Query the Selected Model**:
    - Once a model is selected, add functionality to query it:
    ```python
    prompt = st.text_input("Enter a prompt:")
    if prompt:
        result = client.generate(model_name=model_name, prompt=prompt)
        st.write(f"Model Output: {result['text']}")
    ```

4. **Step 4: Perform Initial Vibe Check**:
    - Test the models by providing different prompts and analyzing their responses to evaluate their capabilities.
