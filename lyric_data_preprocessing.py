# The second part in a series of scripts to generate data froms lyrics from Genius.com
import re

def remove_text(text):
    # Remove "See Drake LiveGet tickets" line that may end in "You might also like" or "{number}Embed"
    text = re.sub(r'See Drake LiveGet tickets as low as \$(\d+)(You might also like|\d+(\.\d+)?K?Embed)?', '', text)
    

    # Remove any number and Embed after it such as: "506Embed", "1.1KEmbed", "3KEmbed", "Embed"
    text = re.sub(r'\d+(\.\d+)?K?Embed', '', text)
    text = re.sub(r'Embed', '', text)

    # Remove "You might also like" line that may end in "You might also like" or "{number}Embed"
    text = re.sub(r'You might also like(\d+(\.\d+)?K?Embed)?', '', text)

    # Remove translation words that come after the space after Embed such as: "TranslationsTürkçePortuguês"
    text = re.sub(r'\bTranslations\w*\s*', '', text)

    # Remove the lines that start with [
    text = re.sub(r'^\[[^\]]*\].*$', '', text, flags=re.MULTILINE)

    # Remove the lines that end with ]
    text = re.sub(r'^.*\].*$', '', text, flags=re.MULTILINE)

    

    return text.strip()

def process_lyrics_file(input_file_path, output_file_path):
    # Open the input file
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        # Read the contents of the file
        text = input_file.read()

    # Pass the text through the remove_text function
    new_text = remove_text(text)

    # Open the output file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        # Write the modified text to the output file
        output_file.write(new_text)


def preprocess_into_data(input_file_path):
    with open(input_file_path, 'r', encoding="utf-8") as f:
        text = f.read()

    data = text.split("[")

    data = [d.replace("]", "") for d in data]

    # Remove empty strings
    data = [d for d in data if d]

    # Split string into a list of strings that are of length SPLIT_LENGTH
    SPLIT_LENGTH = 512
    return_data = []
    for d in data:
        return_data.extend([d[i:i+SPLIT_LENGTH] for i in range(0, len(d), SPLIT_LENGTH)])
    
    return return_data


# Process the Drake lyrics file
# process_lyrics_file('Drake_lyrics.txt', 'processed_Drake_lyrics.txt')

# Process the Kanye West lyrics file
process_lyrics_file('Kanye West_lyrics.txt', 'processed_Kanye West_lyrics.txt')