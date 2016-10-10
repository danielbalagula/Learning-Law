#Learning Law

The goal of this project is to develop a machine learning model that will be able to help sort and categorize law documents.

##Overview

	Train a model on the features with each label (scikit-learn): see results obtained from using just the local classifier on unlabeled 

	Active Learning: for new instances, check each confidence rating, ask user if it is low, then retrain

##Instructions

The feature extractor will look at a [directory] and look for .txt and .json files.

Make sure there is a '/features/' subdirectory, as this is the place where the output features will be placed.

```
python get_local_features.py [directory]
python get_global_features.py [directory]
```

This will generate .json files [directory/features] that have the following names: '[file-name]_features.json'

After, export the features to a .csv file using

```
python export_to_csv.py [directory] [output_file_name]
```

##Local Features

The following features are either implemented or are being on planned later:

	[Implemented] N-grams 

	[Implemented] Sentence/paragraph location

	[Implemented] Number of times each party is mentioned

	[Implemented] Presence of key words/phrases

	[Implemented] Which party is appealing

	Tokens between important words/phrases

	Label sentences as facts/proceedings/background/etc.


##Global Features

	Most common n-grams

##Papers to look at
	
	http://jurix.nl/pdf/j04-05.pdf

	http://jurix.nl/pdf/j04-03.pdf

	http://aclweb.org/anthology/P/P14/P14-1104.pdf
