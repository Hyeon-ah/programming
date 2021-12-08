# 1_6 Word Normalization and other issues
+ How to put all words in a standard format a process called **Word Normalization**
+ Sentence segmentation = breaking up your text corpora into larger discourse unit like sentences reading in paragraph.

## Normalization decisions
## Word Normalization
Putting words/tokens in a standard format
  + U.S.A. or USA
  + uhhuh or uh-huh
  + Fed or fed
  + am, is, be, are

## Case folding
Applications like IR: reduce all letters to lower case
  + Since users tend to use lower case
  + Possible exception: upper case in mid-sentence?
    - e.g. _**General Moters**_
    - _**Fed**_ vs. _**fed**_
    - _**SAIL**_ vs. _**sail**_

For sentiment analysis, MT, Information extraction
  + Case is helpful( _**US**_ vs. _**us**_ -> 다른 의미)

## Lemmatization
Represent all words as their lemma, their shared root <br>
  = dictionary headword form:
  + am, are, is -> be
  + car, cars,car's, cars' -> car
  + Spanish `quiero`('I want'), `quieres`('you want') -> `querer`('want')
  + He is reading detective stories -> He be read detective story

## Lemmatization is done by Morphological Parsing
**Morphemes(형태소)**:
  + The small meaning units that make up words
  + **Stems**: The core meaning-bearing units
  + **Affixes**: Parts that adhere to stems, often with grammatical functions

**Morphological Parsers**:
  + Parse _cats_ into 2 morphemes _cat_ and _s_
 
 ## Stemming
 Reduce terms to stems, chopping off affixes crudely
  + 잘 stemming하는 경우도 있지만, 과하게 이루어질때도 있음.

## Porter Stemmer
Based on a series of rewrite rules run in series
  + A cascade, in which output of each pass fed to next pass
 
Some sample rules:
  + ATIONAL -> ATE (e.g., relational -> relate)
  + ING -> 삭제(단, stem이 모음을 포함할 경우만) (e.g., motoring -> motor)
  + SSES -> SS (e.g., grasses -> grass

+ Dealing with complex morphology is necessary for many lanuages

## Sentence Segmentation
!, ? mostly unambiguous but **period** "." is very ambigous 
  + Sentence boundary
  + Abbreviations like Inc. of Dr.
  + Numbers like .02% or 4.3


Common alogorithm:<br>
Tokenize first: use rules of ML(Machine Learning) to calssify a period as either <br>
(a) part of a word <br>
or <br>
(b) a sentence-boundary.
  + An abbreviation dictionary can help

Sentence segmentation can then often be done by rules based on this tokenization.
