#!/bin/bash
# Run ner.sh with fanwiki-dio.txt and append output to fanwiki-output.txt

cd stanford-ner-2020-11-17; ./ner.sh ../fanwiki.txt >> ../stanford-fanwiki.txt

cd stanford-ner-2020-11-17; ./ner.sh ../wikipedia.txt >> ../stanford-wikipedia.txt

