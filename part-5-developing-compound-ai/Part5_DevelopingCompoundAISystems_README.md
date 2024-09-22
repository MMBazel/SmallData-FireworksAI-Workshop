
# Part 5: Developing a Minimum Viable Compound AI System

## Task/Activity:
In this part of the workshop, you will:
- Learn how to develop a **Minimum Viable Compound AI System (MVCAS)** that integrates multiple AI models or components into a working system.
- Understand the process of taking a compound AI system from development to production, covering the best practices for scaling projects from small to large.

## Relevant Concepts/Skills:
By completing this task, you will:
- Understand how to build an MVCAS that leverages multiple models (e.g., LLMs, retrieval systems, function-calling models) to work together.
- Learn best practices for taking AI systems from development to production, including versioning, scaling, and system orchestration.
- Gain insights into project management when scaling AI systems, such as automating deployments and monitoring performance.

## Background Information:
- **What is a Compound AI System?**: A compound AI system combines different AI models and components that work together to solve complex tasks. For example, a compound system might include an LLM for language understanding, a retrieval system (like RAG), and function-calling models that interact with external APIs.

- **Minimum Viable Compound AI System (MVCAS)**: An MVCAS is a small, deployable version of a compound AI system that focuses on delivering the core functionality. It’s the first step toward building a scalable AI system, allowing for quick iteration and feedback.

- **Best Practices for Scaling**:
  - **Start Small, Scale Gradually**: Begin with a minimal system that solves one core problem and scale up by adding more models and components over time.
  - **Version Control and Testing**: Use versioning for models and systems, with automated tests to ensure new versions don’t break existing functionality.
  - **Orchestration and Automation**: Use orchestration tools to manage multiple models and workflows. Automate deployments, monitoring, and scaling to handle larger workloads.

## Fireworks-Specific Information:
- Fireworks AI provides a platform for deploying and scaling AI models quickly. It supports easy integration of multiple models, pre-tuned models, and serverless deployment options, making it easier to build a compound AI system.
  - **Fireworks Documentation**: [Getting Started with Fireworks AI](https://docs.fireworks.ai/getting-started/introduction)
  - **Pre-Tuned Models on Fireworks**: [Explore Fireworks Models](https://fireworks.ai/models)

## Steps to Accomplish the Task:

1. **Step 1: Plan the Minimum Viable Compound AI System**:
    - Identify the core models or components needed for your MVCAS (e.g., an LLM for answering questions, a RAG system for retrieving documents, and a function-calling model to handle actions).
    - Map out how these components will interact in a workflow.

2. **Step 2: Set Up Fireworks and Connect Models**:
    - Use Fireworks AI to deploy the models you plan to integrate into your system.
    ```python
    import fireworks

    # Initialize Fireworks client
    client = fireworks.Client(api_key="your_api_key")

    # Deploy the core models for the MVCAS
    model_1 = "your_llm"
    model_2 = "your_retrieval_model"
    model_3 = "your_function_calling_model"
    ```

3. **Step 3: Define the Workflow**:
    - Set up the workflow for your system, detailing how inputs move between models and how results are produced.
    ```python
    def workflow(prompt):
        # Query the LLM
        result_llm = client.generate(model_name=model_1, prompt=prompt)
        
        # Retrieve relevant documents using RAG
        retrieved_data = retrieve_data(prompt, model_name=model_2)

        # Use function-calling model to perform an action if needed
        if "action" in result_llm['text']:
            result_func = client.generate(model_name=model_3, prompt=result_llm['text'])

        return result_llm, retrieved_data, result_func
    ```

4. **Step 4: Orchestrate the System**:
    - Use an orchestration tool to manage the models and workflows in your MVCAS, ensuring that each component works together seamlessly.
    - This could involve using cloud orchestration (e.g., Kubernetes) or building a custom orchestration layer.

5. **Step 5: Prepare for Scaling**:
    - Once the MVCAS is functioning, consider the next steps for scaling:
      - Implement logging and monitoring to track performance.
      - Set up versioning for the models to track changes.
      - Implement auto-scaling infrastructure to handle increasing workloads.

6. **Step 6: Iterative Development**:
    - As you receive feedback or discover limitations, iterate on the MVCAS by improving components, adding new models, and expanding system capabilities.
