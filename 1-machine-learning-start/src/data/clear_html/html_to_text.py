import os
import re
from boilerpy3 import extractors

# Condenses all repeating newline characters into one single newline character
def condense_newline(text):
    return '\n'.join([p for p in re.split('\n|\r', text) if len(p) > 0])

# Returns the text from a HTML file
def parse_html(html_path):
    # Text extraction with boilerpy3
    html_extractor = extractors.ArticleExtractor()
    return condense_newline(html_extractor.get_content_from_file(html_path))

# Extracts the text from all html files in a specified directory
def html_to_text(folder):
    parsed_texts = []
    filepaths = os.listdir(folder)

    for filepath in filepaths:
        filepath_full = os.path.join(folder, filepath)
        if filepath_full.endswith(".html"):
            parsed_texts.append(parse_html(filepath_full))
    return parsed_texts

# Your directory to the folder with scraped websites
scraped_dir = './scraped_pages'
parsed_texts = html_to_text(scraped_dir)