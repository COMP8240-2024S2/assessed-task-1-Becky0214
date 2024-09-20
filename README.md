# Named Entity Recognition (NER) Project

### Overview

This project involves setting up and evaluating the performance of a Named Entity Recognition (NER) system. The tasks include:

-Setting up a Virtual Machine (VM) in GitHub Codespaces.  

-Installing the Stanford NER system.

-Scraping text data from Wikipedia and Fandom.

-The NER system is running on the scraped data.

-Evaluating the system's performance by creating a gold standard.

-Writing scripts for automation and evaluation of the NER results.

-Prerequisites

-Before running the project, I ensured the following tools are installed in my VM:

Java (as the Stanford NER system requires it).

Python (for scripts related to data extraction and evaluation).

Unzip (to extract the NER files).

GitHub Classroom repository setup (for submission).

### File Structure
The repository contains the following important files:

extract-wikipedia.py: Python script to scrape text from Wikipedia.

wikipedia.txt: Scraped Wikipedia data.

extract-fanwiki.py: Python script to scrape data from Fandom.

fanwiki.txt: Scraped Fandom data.

stanford-ner.sh: Script to run the Stanford NER system.

stanford-wikipedia.txt: NER output for Wikipedia data.

stanford-fanwiki.txt: NER output for Fandom data.

ner-list.py: Script to list extracted named entities.

ner-list-wikipedia.txt: List of entities from Wikipedia data.

ner-list-fanwiki.txt: List of entities from Fandom data.

wikipedia-gold.txt: Gold standard annotated version for Wikipedia.

fanwiki-gold.txt: Gold standard annotated version for Fandom.

eval.sh: Script to evaluate NER system performance.

wikipedia-eval.txt: Evaluation results for Wikipedia data.

fanwiki-eval.txt: Evaluation results for Fandom data.

fix-ner.sh: Script to fix common NER issues.

README.md: Project instructions and details.

### Evaluation Metrics

The evaluation uses three key metrics:

1. Precision: The ratio of correctly identified entities to the total identified entities.

2. Recall: The ratio of correctly identified entities to the total actual entities.

3. F1 Score: The harmonic mean of precision and recall.
