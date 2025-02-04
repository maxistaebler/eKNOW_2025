
# VAULT: Verified Access Using Layered Text-to-Knowledge Translation Implementation

This repository contains an implementation and evaluation framework for GraphRAG, focusing on knowledge graph construction and retrieval-augmented generation.

## Overview

GraphRAG enhances traditional RAG architectures by incorporating knowledge graph structures for improved multi-hop reasoning and contextual understanding. This implementation includes tools for:

- Knowledge graph construction from documents
- Multi-modal graph storage using ArangoDB
- Fine-grained access control mechanisms
- LLM-powered query processing and response generation
- Comprehensive evaluation framework

## Prerequisites

- Python 3.10+
- ArangoDB
- OpenAI API key or Azure OpenAI endpoint
- Required Python packages (see requirements.txt)

## Installation

1. Install the package:
```bash
pip install graphrag
```

2. Set up your workspace:
```bash
mkdir -p ./ragtest/input
graphrag init --root ./ragtest
```

3. Configure authentication:
- Edit `.env` file with your OpenAI/Azure API key
- Modify `settings.yaml` for pipeline configuration

## Project Structure

### /notebooks
The notebooks directory contains Jupyter notebooks for different aspects of the GraphRAG pipeline:

1. **graphrag_results_processing.ipynb**
- Knowledge graph construction and storage
- ArangoDB integration
- Entity and relationship processing
- Semantic embedding generation

2. **graphrag_response_evaluation.ipynb**
- Response analysis framework
- Model performance evaluation
- Comparative analysis of different approaches

3. **graphrag_query_retrieval.ipynb**
- Query processing implementation
- Context building and retrieval
- LLM integration for response generation

4. **graph_examples.ipynb**
- Example implementations and use cases
- Visualization of knowledge graphs
- Query pattern demonstrations

### /benchmark
The benchmark directory contains evaluation frameworks and results:

1. **Input Processing**
- Document preprocessing
- Text chunking and analysis
- Entity extraction

2. **Output Analysis**
- Model response evaluation
- Performance metrics
- Comparative analysis

3. **LLM Output**
- Generated responses
- Quality assessments
- Error analysis


## Evaluation Framework

The evaluation framework is implemented in the notebooks directory. Key components:

1. **Response Analysis**
Reference:
```notebooks/graphrag_response_evaluation.ipynb
startLine: 144
startLine: 202
```

2. **Query Processing**
Reference:
```notebooks/graphrag_query_retrieval.ipynb
startLine: 9
endLine: 20
```

## ArangoDB Integration

The system uses ArangoDB for graph storage and retrieval. Configuration and setup:

Reference:
```notebooks/graphrag_results_processing.ipynb
startLine: 247
endLine: 269
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Microsoft GraphRAG team for the original implementation
- ArangoDB team for database support
