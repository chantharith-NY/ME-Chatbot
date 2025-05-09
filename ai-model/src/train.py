# train.py
from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import load_dataset
from transformers import Trainer, TrainingArguments

# Load pre-trained model and tokenizer from Hugging Face
model_name = "meta-llama/Llama-2-13b-hf"  # Change this to any LLaMA model or other models
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Example: Load a text dataset (replace with your dataset)
dataset = load_dataset("/Users/nychanthrith/Documents/Chantharith/ME-Chatbot/ai-model/data/processed/preprocess_text.txt")

# Tokenize the dataset
def tokenize_function(examples):
    return tokenizer(examples['text'], padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Setup the training arguments
training_args = TrainingArguments(
    output_dir="/Users/nychanthrith/Documents/Chantharith/ME-Chatbot/ai-model/model",  # Where to save the model
    evaluation_strategy="epoch",  # Evaluation strategy
    learning_rate=2e-5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=3,
)

# Trainer setup
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['test'],
)

# Fine-tune the model
trainer.train()

# Save the trained model
model.save_pretrained("/Users/nychanthrith/Documents/Chantharith/ME-Chatbot/ai-model/model")
tokenizer.save_pretrained("/Users/nychanthrith/Documents/Chantharith/ME-Chatbot/ai-model/model")
