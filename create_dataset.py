import os
import pandas as pd

output_root_directory = 'gutenberg_downloaded_test\data'  

records = []

for subdir, dirs, files in os.walk(output_root_directory):
    author_id = os.path.basename(subdir)  
    for filename in files:
        if filename.endswith('_cn.txt'):  
            file_path = os.path.join(subdir, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                records.append({'author_id': author_id, 'text': text})

df = pd.DataFrame(records)

output_dataset_path = os.path.join(output_root_directory, 'dataset_cn_authors.csv')
df.to_csv(output_dataset_path, index=False, encoding='utf-8')

print(f"Dataset bol úspešne vytvorený a uložený do {output_dataset_path}")


#pip install --upgrade --force-reinstall numpy pandas