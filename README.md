# mtiGPT 🚀

mtiGPT is a versatile chat assistant built using the Llama2 architecture 🦙, with the capability to be configured to use other language models. It is fine-tuned using your own data through Retrieval-Augmented Generation (RAG) 📚 and Prompt Engineering techniques. The assistant is designed to provide accurate and contextually relevant responses, making it a powerful tool for various applications.

## Features 🌟

- **Flexible Model Configuration**: Easily switch between Llama2 and other supported language models.
- **Custom Fine-Tuning**: Fine-tune the model using your own data with RAG for improved contextual understanding.
- **Prompt Engineering**: Utilize advanced prompt engineering techniques to optimize model responses.
- **Python-Based**: Developed entirely in Python for seamless integration and customization.

## Installation 🛠️

1. **Clone the Repository**
   ```bash
   git clone https://github.com/messeiry/mtiGPT.git
   cd mtiGPT
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   Create a `.env` file in the root directory and add the following:
   ```env
   MODEL_TYPE=llama2
   RAG_ENDPOINT=<your_rag_endpoint>
   ```

## Usage 🚀

### Basic Usage

To start the chat assistant, run:
```bash
python chat.py
```

### Switching Models

To switch the underlying language model, modify the `MODEL_TYPE` in the `.env` file:
```env
MODEL_TYPE=your_preferred_model
```
Ensure you have the necessary configurations and dependencies for the selected model.

### Fine-Tuning with RAG

To fine-tune the model using your own data, prepare your dataset and configure the RAG endpoint in the `.env` file. Then, run the fine-tuning script:
```bash
python train_from_data.py --data data/your_dataset.json
```

### Prompt Engineering

Customize prompts to enhance model performance. Edit the `chat_genops.py` file to define your prompts and strategies. Example:
```python
def generate_prompt(user_input):
    return f"Here is the response to your query: {user_input}"
```

## Configuration ⚙️

### Model Configuration

The model configuration can be managed in the `config.py` file. Example:
```python
MODEL_CONFIG = {
    'llama2': {
        'model_path': 'path_to_llama2_model',
        'tokenizer_path': 'path_to_llama2_tokenizer'
    },
    'other_model': {
        'model_path': 'path_to_other_model',
        'tokenizer_path': 'path_to_other_model_tokenizer'
    }
}
```

### Logging 📋

Logging settings can be configured in the `logging.conf` file to monitor and debug the assistant's operations.

## Contributing 🤝

We welcome contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact 📧

For questions or support, please contact [your_email@example.com](mailto:your_email@example.com).

---

**Note**: Replace placeholders like `your_preferred_model`, `your_dataset.json`, and `your_email@example.com` with actual values specific to your project.
