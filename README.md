
# VAULT: Verified Access Control for LLM-Based Knowledge Graph Querying

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

## ArangoDB Integration

The system uses ArangoDB for graph storage and retrieval. Configuration and setup:

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
