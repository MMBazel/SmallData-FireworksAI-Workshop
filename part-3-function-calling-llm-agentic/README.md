# Part 3: Deploying a Function-Calling LLM as Part of an Agentic Workflow

## Task/Activity:
In this part of the workshop, you will:
- Deploy a **function-calling LLM** that can invoke external functions based on a prompt.
- Integrate the LLM into an **agentic workflow** where the model can autonomously trigger actions based on user inputs and responses.

---

## Relevant Concepts/Skills:
By completing this task, you will:
- Learn how **function-calling LLMs** work and how they interact with external functions.
- Understand how to set up an **agentic workflow**, where an LLM can autonomously call functions and perform actions.
- Gain experience in integrating LLMs with external systems (like APIs or databases) to create interactive, decision-driven workflows.

---

## Background Information:
- **What is a Function-Calling LLM?**: A function-calling LLM can identify when specific actions are needed (like fetching data, performing calculations, or making API calls) and can execute pre-defined functions to fulfill that task.
  
- **Agentic Workflow**: This refers to a system where the LLM acts as an agent, taking actions autonomously based on the given prompts. This setup allows the LLM to interact with external systems and APIs to complete tasks automatically.

- **Use Case Example**: A customer service chatbot that not only responds to queries but can also book appointments, fetch weather data, or handle transactions using APIs.

---

## Fireworks-Specific Information:
Fireworks AI allows you to integrate **function-calling LLMs** into workflows seamlessly. The platform provides tools for defining and mapping functions that the LLM can call. This is ideal for creating intelligent, responsive agents that can act independently based on user prompts.

  - **Guide to Function-Calling with Fireworks**: [Using Function-Calling](https://docs.fireworks.ai/guides/function-calling)
  - **Fireworks Python Client Setup**: [Install the Fireworks Python Client](https://docs.fireworks.ai/tools-sdks/python-client/installation)

Fireworks' function-calling feature allows the LLM to interact with other external services or systems, which enhances the model’s ability to perform complex workflows. Whether it’s making API calls, pulling data from a database, or automating tasks, function-calling enables the LLM to act in an agentic way.

---

## Steps to Accomplish the Task:
1. **Set up Fireworks Python Client**: Ensure that the Fireworks Python Client is installed and configured to interact with function-calling models.
2. **Define Functions**: Write or identify external functions that the LLM will be able to call. For example, these functions might interact with APIs, perform calculations, or fetch external data.
3. **Integrate Function-Calling**: Use Fireworks' tools to map the defined functions to the LLM so that it can call them autonomously based on user input.
4. **Create a User Input Pipeline**: Set up an input pipeline where users can prompt the LLM. The LLM will analyze the input and call the appropriate functions in the workflow.
5. **Test the Workflow**: Run several test cases to ensure that the LLM is correctly invoking the functions and returning valid responses. Debug any issues that arise during testing.
6. **Optimize the Workflow**: Review the results and make any necessary adjustments to improve the decision-making and response-generation processes within the workflow.

---

By the end of this part of the workshop, you will have a working **agentic workflow** where the LLM can autonomously trigger actions and interact with external systems based on user inputs.