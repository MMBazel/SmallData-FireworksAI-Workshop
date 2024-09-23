
# Fireworks AI Workshop: Building and Deploying Compound AI Systems

Welcome to the repository for the **Building and Deploying Compound AI Systems** workshop on Fireworks AI! This repo contains all the materials, code, and resources you'll need to follow along during the workshop.

## Table of Contents
1. [Overview](#overview)
2. [Pre-requisites](#pre-requisites)
3. [Workshop Agenda](#workshop-agenda)
4. [Setup Instructions](#setup-instructions)
5. [Workshop Content](#workshop-content)
6. [Resources](#resources)
7. [FAQ](#faq)

---

## Overview
In this workshop, we'll try to cover how to:
- Connect to different models using Fireworks and build a Streamlit app for model comparison.
- Deploy an LLM as part of a simple Retrieval-Augmented Generation (RAG) system.
- Deploy a function-calling LLM as part of an agentic workflow.
- Fine-tune a base LLM and understand how to fine-tune function-calling models.

After the workshop, check back later for more resources on how to: 
- Develop a minimum viable compound AI system and learn best practices for scaling from development to production.
- Understand the "Ops" side of maintaining and scaling compound AI systems in production.
- Advanced topics about the post-training side of things, including: fine-tuning, evaluation, LoRAs, etc.

---

## Pre-requisites
Before attending the workshop (or asap), make sure you have:
- Signed up for an account on Fireworks.ai
- Messaged me your account ID so I can add credits to your account
- **Installed [tools, dependencies]**: See the [Setup Instructions](#setup-instructions) for installation steps.

And while this is helpful, this isn't required: 
- **Basic knowledge of Generative AI concepts**: Understanding of LLMs, multimodal models, and function-calling models.


---

## Workshop Agenda
- **Part 0**: Using LLMs 101
- **Part 1**: Connecting to Fireworks & Building a Model Comparison App
- **Part 2**: Deploying an LLM with RAG
- **Part 3**: Deploying a Function-Calling LLM as part of an Agentic Workflow
- **Part 4**: Fine-tuning a Base and Function-Calling LLM
- **Part 5**: Developing a Minimum Viable Compound AI System
- **Part 6**: The "Ops" Side of Compound AI Systems

---


## Setup Instructions

### 1. Clone this repository
```bash
git clone https://github.com/MMBazel/SmallData-FireworksAI-Workshop.git
cd SmallData-FireworksAI-Workshop
```

### 2. Create and activate a virtual environment
To avoid dependency conflicts, it's recommended to create a virtual environment. Here's how to do it:

**For macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**For Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
Once your virtual environment is activated, install the required libraries:
```bash
pip install -r requirements.txt
```

### 4. Set up your API keys
To set up your Fireworks API key, follow these steps:

1. Make a copy of the `.env.template` file in the root of the repository:
   ```bash
   cp .env.template .env
   ```

2. Open the `.env` file and set your Fireworks API key:
   ```bash
   FIREWORKS_API_KEY="your-fireworks-api-key"
   ```

3. Save the file. The environment variables will now be automatically loaded when running the code.

### 5. Fireworks AI Installation/Setup
- [Quickstart with Fireworks AI](https://docs.fireworks.ai/getting-started/quickstart)

Additional details:
- [firectl](https://docs.fireworks.ai/tools-sdks/firectl/firectl)
- [Python Client](https://docs.fireworks.ai/tools-sdks/python-client/installation)
- [Quickstart with Fireworks AI](https://docs.fireworks.ai/getting-started/quickstart)

Additional details on: 
- [firectl](https://docs.fireworks.ai/tools-sdks/firectl/firectl)
- [Python Client](https://docs.fireworks.ai/tools-sdks/python-client/installation)

---

## Workshop Content
Each section of the workshop is accompanied by a README, a notebook, and some information about Fireworks.

- **[Part 0: Using LLMs 101]**
  - Basic introduction to LLMs and setting up the Fireworks connection.
  
- **[Part 1: Connecting to Fireworks & Building a Model Comparison App]**
  - Build a Streamlit app to connect and compare models hosted on Fireworks.
  - [Guide to Querying Text Models](https://docs.fireworks.ai/guides/querying-text-models)
  - [Guide to Querying Embedding Models](https://docs.fireworks.ai/guides/querying-embeddings-models)

- **[Part 2: Deploying an LLM with RAG]**
  - Use an LLM as part of a simple Retrieval-Augmented Generation (RAG) system with a vector store.

- **[Part 3: Deploying a Function-Calling LLM as Part of an Agentic Workflow]**
  - Deploy a function-calling LLM that interacts with external APIs and functions.
  - [Guide to Using Function-Calling with Fireworks](https://docs.fireworks.ai/guides/function-calling)

- **[Part 4: Fine-tuning a Base and Function-Calling LLM]**
  - Kick off the fine-tuning process and explore alternatives like prompt engineering and pre-tuned models.

- **[Part 5: Developing a Minimum Viable Compound AI System]**
  - Learn best practices for scaling compound AI systems from development to production.

- **[Part 6: The "Ops" Side of Compound AI Systems]**
  - Understand MLOps processes like monitoring, retraining, scaling, and maintaining AI systems in production.

---

## Resources
- [Official Fireworks AI Documentation](https://docs.fireworks.ai/getting-started/introduction)
- [Fireworks AI Blog](https://fireworks.ai/blog)
- [Fireworks AI YouTube](https://www.youtube.com/channel/UCHCffBTGYa1Ut72h03ldtGA)
- [Fireworks AI Twitter](https://x.com/fireworksai_hq)
- [Join the Workshop Discord](https://discord.gg/YPZsyFAC)

---

## FAQ
**Q: Do I need prior experience with Fireworks AI?**  
A: Basic familiarity with generative models will be helpful, but we’ll cover foundational concepts in the early parts of the workshop.

**Q: What should I do if I encounter an issue?**  
A: Review the setup instructions and consult the Fireworks documentation. You can also reach out for support during the workshop.

**Q: Can I continue to access these materials after the workshop?**  
A: Yes, the materials will remain available on this repository, and you are welcome to clone or fork the repo for personal use.

---

## License
This workshop is licensed under the [MIT License](LICENSE). Feel free to use and modify the materials.
