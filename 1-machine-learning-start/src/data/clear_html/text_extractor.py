from bs4 import BeautifulSoup

# Returns the text from a HTML file based on specified tags
def parse_html(html_path):
    with open(html_path, 'r') as fr:
        html_content = fr.read()
        soup = BeautifulSoup(html_content, 'html.parser')

        # Check that file is valid HTML
        if not soup.find():
            raise ValueError("File is not a valid HTML file")

        # Check the language of the file
        tag_meta_language = soup.head.find("meta", attrs={"http-equiv": "content-language"})
        if tag_meta_language:
            document_language = tag_meta_language["content"]
            if document_language and document_language not in ["en", "en-us", "en-US"]:
                raise ValueError("Language {} is not english".format(document_language))

        # Get text from the specified tags. Add more tags if necessary.
        TAGS = ['p']
        return ' '.join([remove_newline(tag.text) for tag in soup.findAll(TAGS)])