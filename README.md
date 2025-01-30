# eKNOW_2025

## Features

- Ontology-driven / Vocabulary-driven knowledge graph construction
- Fine-grained access control mechanisms
- LLM-powered intelligent output filtering
- ArangoDB integration for multi-modal graph storage
- Domain-specific knowledge organization

## Architecture

The system consists of three main components:

1. Knowledge Extractor: Processes natural language text using LLMs and domain ontologies
2. Graph Constructor: Builds and maintains the knowledge graph structure
3. Access Controller: Manages fine-grained access control and output filtering

## Run RAG


`pip install graphrag`

The graphrag library includes a CLI for a no-code approach to getting started. Please review the full CLI documentation for further detail.

### Running the Indexer
We need to set up a data project and some initial configuration. First let's get a sample dataset ready:

`mkdir -p ./ragtest/input`

### Set Up Your Workspace Variables
To initialize your workspace, first run the graphrag init command. Since we have already configured a directory named ./ragtest in the previous step, run the following command:


`graphrag init --root ./ragtest`
This will create two files: .env and settings.yaml in the ./ragtest directory.

`.env` contains the environment variables required to run the GraphRAG pipeline. If you inspect the file, you'll see a single environment variable defined, GRAPHRAG_API_KEY=<API_KEY>. This is the API key for the OpenAI API or Azure OpenAI endpoint. You can replace this with your own API key. If you are using another form of authentication (i.e. managed identity), please delete this file.
settings.yaml contains the settings for the pipeline. You can modify this file to change the settings for the pipeline.
