# Seerat-e-Nabi Model with Llama Index

This project is a web application that uses a FastAPI backend to provide responses to questions about the Seerat-e-Nabi model using the Llama Index for vector storage and querying.

## Features

- **FastAPI Integration**: A lightweight web framework to handle API requests.
- **Llama Index**: Utilizes Llama Index for storing and querying document vectors.
- **Dynamic Model Loading**: Automatically loads and persists the index, ensuring efficient querying.

## File Structure

- `main.py`: Main application file using FastAPI to set up endpoints.
- `llama_model.py`: Script to load data, create an index, and query it using Llama Index.
- `clean.py`: Preprocesses raw data for creating a clean dataset suitable for indexing.

## Key Components

### FastAPI Application (`main.py`)

- **Endpoints**:
  - `GET /`: Simple health check returning "OK".
  - `GET /response/{question}`: Accepts a question and returns the model's response.
- **Server Configuration**: Runs the server on `port 8000` with reload enabled.

### Llama Model (`llama_model.py`)

- **Data Loading and Indexing**:
  - Loads documents from a specified directory.
  - Creates and persists a vector store index.
- **Query Handling**:
  - Provides a function to query the index and fetch responses.

### Data Preprocessing (`clean.py`)

- **Data Cleaning**:
  - Removes non-alphanumeric characters and empty lines.
  - Filters out lines with fewer than three words.
- **Save Clean Data**: Saves the preprocessed data to a new file.

## Challenges and Solutions

- **Model Integration**: Ensuring seamless integration of the Llama Index with FastAPI required careful handling of data loading and indexing.
- **Data Preprocessing**: Cleaning and preparing the data to create a meaningful index involved multiple preprocessing steps.
- **Efficient Querying**: Implementing a system to efficiently query the index and provide responses demanded robust indexing and query handling mechanisms.

## Getting Started

1. Clone the repository.
2. Install the required dependencies.
3. Run the FastAPI app.

```bash
git clone https://github.com/faisal-fida/seerat-e-nabi-model-llama-index.git
cd seerat-e-nabi-model-llama-index
pip install -r requirements.txt
uvicorn main:app --reload
```

## Conclusion

This project demonstrates the integration of FastAPI with Llama Index for creating a responsive web application capable of answering questions based on indexed data. It highlights the complexities of model integration, data preprocessing, and efficient querying.

Feel free to contribute or raise issues if you encounter any problems!
