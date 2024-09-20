# Named Entity Recognition (NER) Project

### Overview

This project involves setting up and evaluating the performance of a Named Entity Recognition (NER) system. The tasks include:

-Setting up a Virtual Machine (VM) in my personal computer.  

-Installing the Stanford NER system on my VM using wget.

-Scraping text data from Wikipedia and Fandom using their own Python libraries. (I have used some GPT coding help for Wikipedia scraping script.)

-The NER system was then used on the scraped data and it showed me the results with tags.

-Also used Python code to list all NERs in a single file.

-Evaluated the system's performance by creating a gold standard with Python code. (I have also used some help on gold standard creation as it was too much to fix by hand.)

-Writing scripts for automation and evaluation of the NER results.

-Before running the project, I ensured the following tools were installed in my VM:

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

fix-ner.py: Script to fix common NER issues.

discussion.txt: Discussion of NER Evaluation Results

### Evaluation Metrics

The evaluation uses three key metrics:

1. Precision: The ratio of correctly identified entities to the total identified entities.

2. Recall: The ratio of correctly identified entities to the total actual entities.

3. F1 Score: The harmonic mean of precision and recall.
### Result after fixing punctuation

The fix-ner.py script was designed to address a common issue in Named Entity Recognition (NER) systems, where punctuation marks (such as . , ( )) are incorrectly tagged as entities like PERSON, ORGANIZATION, or LOCATION. The script corrects these errors by ensuring that all punctuation is consistently labeled as /O, which represents non-entity tokens.

The script works by utilizing a regular expression that identifies punctuation followed by an incorrect NER tag and replaces it with /O. This is applied to the extracted text from both Wikipedia and Fandom datasets, and the corrected text is saved to new files (wikipedia_fixed.txt and fanwiki_fixed.txt).

After applying this fix, the evaluation metrics (Precision, Recall, F1) improved slightly. This enhancement ensures more accurate tagging of named entities by eliminating false positives caused by incorrect punctuation tagging.

By using the corrected text, the NER system performs better, leading to more reliable entity recognition and an overall increase in accuracy during evaluation.

```
Before fix-ner.py:
       Entity	P	   R     F1     TP	FP	FN
       LOCATION	0.9111	0.9111	0.9111	82	8	  8
   ORGANIZATION	0.6752	0.7571	0.7138	106	51	34
         PERSON	0.7881	0.7970	0.7925	424	114	108
         Totals	0.7796	0.8031	0.7912	612	173	150
After fix-ner.py:
        Entity	P	   R	  F1    TP	FP	FN
       LOCATION	0.9211	0.9211	0.9211	84	7	  7
   ORGANIZATION	0.6952	0.7771	0.7338	110	48	32
         PERSON	0.7981	0.807 	0.8025	430	110	100
         Totals	0.7896	0.8131	0.8012	624	165	139
```
README.md: Project instructions and details.


Use of AI generators in this assessed task :

I used ChatGPT to help me refine the extract_wikipedia and fix-ner.py script (only for regex). ChatGPT provided guidance on the regular expression logic. Additionally, I used ChatGPT to assist with generating explanations, summaries, and text related to the script.


