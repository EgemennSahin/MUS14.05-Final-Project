from transformers import GPT2Tokenizer, GPT2LMHeadModel
import time

# Set the model and tokenizer paths

model_path="drake_model"
tokenizer_path="drake_tokenizer"

# Instantiate the tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

# Set the model to evaluation mode
model.eval()

# Generate text based on a prompt
prompt = "Hi"
input_ids = tokenizer.encode(prompt, return_tensors='pt')
output = model.generate(input_ids, max_length=512, do_sample=True)

# Convert output tensor to string
output_str = tokenizer.decode(output[0], skip_special_tokens=True)

# Write the generated string into a file
# Create a unique id using the time
unique_id = time.time()


with open(f"prompt_responses/{unique_id}.txt", 'w', encoding='utf-8') as output_file:
    # Write the modified text to the output file
    output_file.write(output_str)