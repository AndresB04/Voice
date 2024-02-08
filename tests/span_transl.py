from googletrans import Translator

# Initialize the translator
translator = Translator()

# Open the Spanish dictionary file
with open('spanish_words.txt', 'r') as file:
    spanish_words = file.readlines()

# Open a file to write the translations
with open('translated_words.txt', 'w') as output_file:
    for word in spanish_words:
        # Translate each word
        translated_word = translator.translate(word.strip(), src='es', dest='en').text
        # Write the translation to the output file
        output_file.write(translated_word + '\n')
