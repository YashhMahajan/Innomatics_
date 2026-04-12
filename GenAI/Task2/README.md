# LangChain Fundamentals Project

A comprehensive introduction to LangChain - a powerful framework for building applications powered by large language models (LLMs). This project demonstrates the core concepts and components of LangChain through practical examples.

## 🚀 Overview

This project serves as a learning resource and reference for understanding LangChain's fundamental building blocks. It covers the essential components needed to create sophisticated LLM-powered applications, from basic model invocation to complex agent-based systems.

## 📋 Features

- **LLM Integration**: Direct interaction with OpenAI's language models
- **Prompt Templates**: Structured prompt engineering and formatting
- **Chains**: Sequential processing workflows
- **Memory**: Conversation context management
- **Agents**: Tool-enabled autonomous reasoning
- **Vector Search**: FAISS integration for similarity search

## 🛠️ Tech Stack

- **LangChain**: Core framework for LLM application development
- **OpenAI**: GPT-4o-mini model for language understanding
- **FAISS**: Vector similarity search library
- **Python 3.12+**: Programming environment

## 📦 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Task2
```

2. Install the required dependencies:
```bash
pip install langchain langchain-openai openai faiss-cpu
```

3. Set up your OpenAI API key:
```python
import os
os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"
```

## 🏗️ Project Structure

```
Task2/
├── README.md                 # This file
├── langchain-simple.ipynb    # Jupyter notebook with examples
└── requirements.txt          # Python dependencies (optional)
```

## 📚 Core Concepts Demonstrated

### 1. Large Language Models (LLMs)
Basic interaction with language models for text generation and understanding.

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")
response = llm.invoke("Explain LangChain in simple terms")
```

### 2. Prompt Templates
Structured templates for consistent and reusable prompt formatting.

```python
from langchain.prompts import PromptTemplate

template = PromptTemplate.from_template("Explain {topic} in simple terms")
formatted_prompt = template.format(topic="AI")
```

### 3. Chains
Sequential workflows that combine prompts and models for complex tasks.

```python
from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=template)
result = chain.run("Machine Learning")
```

### 4. Memory
Conversation context management for maintaining dialogue history.

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)
```

### 5. Agents
Autonomous agents that can use tools to solve complex problems.

```python
from langchain.agents import initialize_agent, load_tools

tools = load_tools(["llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description")
```

## 🚀 Getting Started

### Prerequisites
- Python 3.12 or higher
- OpenAI API key
- Jupyter Notebook or JupyterLab

### Quick Start

1. Open the Jupyter notebook:
```bash
jupyter notebook langchain-simple.ipynb
```

2. Set your OpenAI API key in the first code cell
3. Run the cells sequentially to explore each concept
4. Experiment with different prompts and parameters

### Running the Examples

Each section in the notebook demonstrates a specific LangChain concept:

1. **Cell 2**: Basic LLM invocation
2. **Cell 3**: Prompt template creation
3. **Cell 4**: Chain implementation
4. **Cell 5**: Memory and conversation management
5. **Cell 6**: Agent with mathematical tools

## 🎯 Use Cases

This project is ideal for:
- **Learning LangChain**: Understanding core concepts through practical examples
- **Quick Reference**: Copy-paste ready code snippets for common tasks
- **Prototype Development**: Starting point for building LangChain applications
- **Teaching Resources**: Educational material for workshops and tutorials

## 🔧 Configuration

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key (required)

### Model Configuration
- Default model: `gpt-4o-mini`
- Can be customized based on requirements and budget

## 📖 Advanced Topics

While this project covers the fundamentals, LangChain offers many advanced features:

- **Document Loaders**: Ingest data from various sources
- **Text Splitters**: Chunk documents for processing
- **Vector Stores**: Semantic search capabilities
- **Retrievers**: Information retrieval systems
- **Custom Tools**: Domain-specific agent tools
- **Multi-agent Systems**: Collaborative AI agents

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Update documentation for new features
- Test your changes thoroughly

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) - For the amazing framework
- [OpenAI](https://openai.com/) - For providing powerful language models
- [FAISS](https://faiss.ai/) - For efficient vector similarity search

## 🔗 Resources

- [Official LangChain Documentation](https://python.langchain.com/)
- [LangChain GitHub Repository](https://github.com/langchain-ai/langchain)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [FAISS Documentation](https://faiss.ai/)

---

**Happy Building with LangChain! 🚀**
