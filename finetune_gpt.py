# Finetuning the GPT-2 model from the data from lyric_data_preprocessing.py:
from lyric_data_preprocessing import preprocess_into_data
from transformers import GPT2Tokenizer, GPT2LMHeadModel, DataCollatorForLanguageModeling, Trainer, TrainingArguments

def train_model(processed_lyrics, name):
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')

    # Get Drake lyrics as a list of strings with max length of 512
    drake_data = preprocess_into_data(processed_lyrics)

    encoded_drake_data = []

    # Tokenize and encode each string in the drake_data list
    for text in drake_data:
        encoded = tokenizer.encode(text)
        encoded_drake_data.append(encoded)

    # Use a DataCollatorForLanguageModeling to collate the data into batches
    data_collator = DataCollatorForLanguageModeling(tokenizer, mlm=False)

    # Set training arguments
    training_args = TrainingArguments(
        output_dir='./results',          # output directory
        num_train_epochs=2,              # total number of training epochs
        per_device_train_batch_size=1,   # batch size per device during training
        per_device_eval_batch_size=1,    # batch size for evaluation
        warmup_steps=500,                # number of warmup steps for learning rate scheduler
        weight_decay=0.01,               # strength of weight decay
        logging_dir='./logs',            # directory for storing logs
        logging_steps=10,
    )

    # Set up the Trainer for training
    trainer = Trainer(
        model=model,                         # the instantiated Transformers model to be trained
        args=training_args,                  # training arguments, defined above
        data_collator=data_collator,         # data collator for batching and padding the data
        train_dataset=encoded_drake_data,    # preprocessed training dataset
    )

    # Train the model
    trainer.train()

    model_path=f"{name}_model"
    tokenizer_path=f"{name}_tokenizer"
    model.save_pretrained(model_path)
    tokenizer.save_pretrained(tokenizer_path)


train_model("processed_Kanye West_lyrics.txt", "kanye")