# Uyghur regex searcher

This repository contains corpora created from three Uyghur websites:
* [Uyghur Akademiyisi](https://www.akademiye.org/ug/) (Uyghur Academy): A legal research organization that publishes articles on Uyghur culture and politics. Retrieved July 2022.
* [Uyghur Awazi](http://uyguravazi.kazgazeta.kz/) (Uyghur Voice): An Uyghur-language newspaper published in Almaty, Kazakhstan. Retrieved January 2020.
* [Radio Free Asia](https://www.rfa.org/uyghur) (RFA): A US-sponsored non-profit news organization, Uyghur language website. Retrieved July 2022.

The `corpora` folder contains each of the corpora. The `XX_documents.zip` file in each directory contains the raw text of every article, and the `metadata.csv` file contains the listing of articles and corresponding metadata. The corpora are stored in zip files for space and efficiency reasons. The scripts that operate on this data automatically zip/unzip them.

The `regex_searcher.py` script can be modified to search all the corpora for sentences containing a specified regular expression. It returns a .csv file containing all the sentences with matches. Keep in mind that this script removes punctuation before searching.

If you find this repository useful, please cite the following items:

> Mayer, C. (2021). Issues in Uyghur backness harmony: Corpus, experimental, and computational studies (Unpublished doctoral dissertation). University of California, Los Angeles. 

