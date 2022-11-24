import csv
import io
import os
import pandas as pd
import re

from zipfile import ZipFile

LATIN_DOCS_ZIP = 'lat_documents.zip'
PA_DOCS_ZIP = 'pa_documents.zip'
METADATA_FILENAME = "metadata.csv"

def clean_document(doc):
    """
    Removes punctuation and other characters from corpus file
    """
    doc = doc.strip()
    doc = re.sub(r"[,،\/#$%\^&\*;:{}=_`~()\"<>–“—”«»]", "", doc)
    doc = re.sub(r"[\u200d\u200f\xa0\r\n]", "", doc)
    doc = [x.strip() for x in re.split('[!.?]', doc) if x]
    return doc

def search_corpus_regex(corpora, parent_dir, search_regex, latin=False):
    matches = [('word', 'corpus', 'sentence')]
    for corpus in corpora:
        corpus_dir = parent_dir.format(corpus)
        metadata = pd.read_csv(os.path.join(corpus_dir, METADATA_FILENAME))
        if latin:
            zip_file = os.path.join(corpus_dir, LATIN_DOCS_ZIP)
        else:
            zip_file = os.path.join(corpus_dir, LATIN_DOCS_ZIP)

        with ZipFile(zip_file) as corpus_zip:
            for index, row in metadata.iterrows():
                if index % 100 == 0:
                    print("Processing file {}: {}".format(index, row['filename']))
                doc_file = corpus_zip.open(row['filename'])
                document = io.TextIOWrapper(doc_file, 'utf-8').read()

                clean_doc = clean_document(document)
                for sent in clean_doc:
                    result = re.findall(search_regex, sent)
                    if result:
                        for match in result:
                            matches.append((match, corpus, sent))

    return matches

if __name__ == "__main__":
    corpora = ['rfa', 'awazi', 'akademiye']

    # Change this to the appropriate path
    corpora_dir = "/home/connor/git_repos/tag-sequence-searcher/corpora/{}"

    # Note that if you want to retrieve entire words, your regex needs to match 
    # entire words, not just the subparts you're interested in.

    # This regex matches all words ending in ghan
    regex = r'([^ ]+ghan)\b'
    results = search_corpus_regex(
        corpora, corpora_dir, regex, latin=True
    )

    with open('./results.csv', 'w') as f:
        writer = csv.writer(f)
        for result in results:
            writer.writerow(result)
