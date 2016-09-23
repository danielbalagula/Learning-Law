||||||||||
#OVERVIEW:

##manually label many instances

##find the features within labels:
	```
	- most common bag of words
	- n-grams
	- possibly: sentences containing parties and sentiment analysis (Dual BOW/Antonymous sentiment: http://aclweb.org/anthology/P/P15/P15-1102.pdf)
	- weight uncommon features based on Delta IDF (http://aclweb.org/anthology/P/P14/P14-1104.pdf)
	- possibly: tokens between important words/phrases
	- label sentences fact/proceedings/background/etc. (http://jurix.nl/pdf/j04-05.pdf... http://jurix.nl/pdf/j04-03.pdf)
	- sentence location/paragraph (http://jurix.nl/pdf/j04-05.pdf) <- Possibly very important/heavy weight
 	- # thematic words in a sentence (http://jurix.nl/pdf/j04-05.pdf)
	- Length/%quotation/Entities (http://jurix.nl/pdf/j04-05.pdf)
	```

train a model on the features with each label (scikit-learn)... this will be the local classifier

see results obtained from using just the local classifier on unlabeled instances... check each point, ask user, then retrain (active learning: http://aclweb.org/anthology/P/P14/P14-1104.pdf)

if not optimal, incorporate global classifier (what will it be?)

incorporate active learning framework

find out if a verdict exists

if it does, find out what it is

data cleaning - what must be done?

|||||||||||||||||||||||||||||
#FEATURE (TARGET VARIABLE(S)):

```
Who appealed (defendant/plaintiff) (verdict exists/what is verdict)

What type of case is it/what does it concern (what is verdict)

bag of words/term-frequency (first paragraph) (verdict exists/what is verdict)

n-grams (first paragraph) (verdict exists/what is verdict)

which paragraph (first/last) AND/OR how far into the document is possible verdict (percentile) (verdict exists)

how many times each entity was mentioned in the document in relation to the entity being an plaintiff/defendant (whole document) (what is verdict)

date (?) (if older, possibly ask user)
```
||||||||||||||
#INSTRUCTIONS:

1) Download (n) bulk data cases from Court Listener API and save in '/unlabeled_cases'
2) Manually sort (m) cases into '/plaintiff_won' and '/defendant_won' (perhaps create and run 'python sort_cases.py' in the future)
3) Run 'python local_feature_extractor.py' => this will populate '/plaintiff_won/first_paragraphs' and '/defendant_won/first_paragraphs' and '/training_data' and '/test_data'
4) Run 'python local_feature_verdict_learner.py' => This will create 'local_feature_learning_results.csv', which will display (n-m) verdict predictions using local features
