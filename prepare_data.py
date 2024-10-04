import os
import json
import random
import glob
import re

def count_words(text):
    return len(text.split())

#V prípade, ak nie je obmedzený počet kníh, táto funkcia vráti books
def select_random_books(books, min_books=60, max_books=62):
    random.shuffle(books)
    selected_books = books[:random.randint(min_books, max_books)]
    return selected_books
    #return books
    
#min_words = minimálny počet slov v odseku
#target_word_count = približný počet slov, ktoré budú vybraté z každého diela 
def select_random_paragraphs(paragraphs, min_words=70, target_word_count=100000):
    random.shuffle(paragraphs)
    selected_paragraphs = []
    word_count = 0
    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        paragraph_word_count = count_words(paragraph)
        if paragraph_word_count < min_words:
            continue
        if word_count + paragraph_word_count > target_word_count:
            break
        selected_paragraphs.append(paragraph)
        word_count += paragraph_word_count
    return selected_paragraphs

base_directory = 'gutenberg_downloaded_test\data'
all_author_folders = glob.glob(os.path.join(base_directory, '*'))

for author_folder in all_author_folders:
    author_books = glob.glob(os.path.join(author_folder, '*.json'))
    selected_books = select_random_books(author_books)

   
    for json_file in selected_books:  
        try:
            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except UnicodeDecodeError:
            try:
                with open(json_file, 'r', encoding='latin-1') as file:
                    data = json.load(file)
            except Exception as e:
                print(f"Failed to read {json_file} with error: {e}")
                continue

        text = data[0]["Text"][0]
        paragraphs = re.split(r',\s?,\s', text)
        selected_paragraphs = select_random_paragraphs(paragraphs)

        output_file_name = os.path.splitext(os.path.basename(json_file))[0] + '_cn.txt'
        output_file_path = os.path.join(os.path.dirname(json_file), output_file_name)

        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write('\n\n'.join(selected_paragraphs))

        print(f"Processed {json_file} and saved selected text to {output_file_name}")
   