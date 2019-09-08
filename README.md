# Name and shame
## PDF scrape, text convert and entity recognition

The goal is to create a network dataframe of connections which shows who mentioned who over time.

This repo is a basic scrape of PDF transcripts which identifies the names of individuals and ranks them accordingly in a dataframe. It's focused on the state capture commission in South Africa.

## Motivation

The motivation for this project comes at the back of the [state capture commission](https://www.sastatecapture.org.za/site/transcripts) which is a massive repository of talk and source for NLP analysis.

The main libraries used are:

```bash
import bs4
import glob
import spacy
import nltk
import pandas
import numpy
```

## Notebooks include

- download_pdfs.ipynb

Downloads pdf files using bs4.

- pdf_to_text.ipynb

Converts pdf files to strings (used as module with pdf_to_text.py).

- text_analysis.ipynb

Extracts person names using [Spacy](https://spacy.io/). Outputs dfs named with date of transcript and ranked according to name frequencies.

- concat_csv_files.ipynb

Concatenates dfs.

## Going forward
- Entity and name recognition needs to be cleaned up and be more concise.
- Network visualisation needs to be implemented.
