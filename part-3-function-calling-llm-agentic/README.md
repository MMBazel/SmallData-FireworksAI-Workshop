
# Part 3: Deploying a Function-Calling LLM as Part of an Agentic Workflow

## Task/Activity:
In this part of the workshop, you will:
- Deploy a **function-calling LLM** that can invoke external functions based on a prompt.
- Integrate the LLM into an **agentic workflow** where the model can autonomously trigger actions based on user inputs and responses.

## Relevant Concepts/Skills:
By completing this task, you will:
- Learn how **function-calling LLMs** work and how they interact with external functions.
- Understand how to set up an **agentic workflow**, where an LLM can autonomously call functions and perform actions.
- Gain experience in integrating LLMs with external systems (like APIs or databases) to create interactive, decision-driven workflows.

## Background Information:
- **What is a Function-Calling LLM?**: A function-calling LLM can identify when specific actions are needed (like fetching data, performing calculations, or making API calls) and can execute pre-defined functions to fulfill that task.
  
- **Agentic Workflow**: This refers to a system where the LLM acts as an agent, taking actions autonomously based on the given prompts. This setup allows the LLM to interact with external systems and APIs to complete tasks automatically.

- **Use Case Example**: A customer service chatbot that not only responds to queries but can also book appointments, fetch weather data, or handle transactions using APIs.

## Fireworks-Specific Information:
- Fireworks AI allows you to integrate **function-calling LLMs** into workflows seamlessly. The platform provides tools for defining and mapping functions that the LLM can call.
  - **Guide to Function-Calling with Fireworks**: [Using Function-Calling](https://docs.fireworks.ai/guides/function-calling)
  - **Fireworks Python Client Setup**: [Install the Fireworks Python Client](https://docs.fireworks.ai/tools-sdks/python-client/installation)

## Steps to Accomplish the Task:

1. **Step 1: Set Up Fireworks API and Choose a Function-Calling Model**:
    - Install the Fireworks Python client and authenticate using your API key:
    ```bash
    pip install fireworks
    ```
    - In your Python code:
    ```python
    import fireworks

    # Initialize Fireworks client
    client = fireworks.Client(api_key="your_api_key")

    # Choose a function-calling model from Fireworks
    model_name = "your_function_calling_llm"
    ```

2. **Step 2: Define the Functions the LLM Can Call**:
    - Set up the functions the LLM will be able to call based on the user's input:
    ```python
    def get_weather(location):
        return f"The weather in {location} is sunny."

    def book_meeting(time, date):
        return f"Meeting scheduled for {date} at {time}."
    
    function_map = {
        "get_weather": get_weather,
        "book_meeting": book_meeting
    }
    ```

3. **Step 3: Deploy the Agentic Workflow**:
    - When the LLM receives an input that requires a function call, it will trigger the appropriate function:
    ```python
    prompt = "What's the weather in New York?"

    # Send the prompt to the LLM and get the function call if necessary
    response = client.generate(model_name=model_name, prompt=prompt, function_map=function_map)

    # Execute the function if it's called by the LLM
    if response['function_call']:
        function_name = response['function_call']['name']
        function_args = response['function_call']['arguments']
        
        # Call the corresponding function
        result = function_map[function_name](**function_args)
        print(result)
    ```

4. **Step 4: Test the Agentic Workflow**:
    - Test the system with various prompts and scenarios where the LLM will autonomously call different functions (e.g., checking weather, scheduling meetings) to validate its performance in handling function-driven tasks.
