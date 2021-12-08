# 1_5 Byte Pair Encoding(BPE algorithm)
+ Used in corpus statistic to decide how to segment a text into tokens.😊
+ BYE algorithm is a set of corpus based tokenizers that are extremeley wisely used in NLP

## Another option for text tokenization
Instead of 
  + white-space segmentation
  + single-character segmentation
 
**Use the data** to tell us how to tokenize.
**Subword tokenization** (because tokens can be parts of words as well as whole words)

## Subword tokenization
3 common algorithms:
  + Byte-Pair Encoding(BPE) (Sennrich et al., 2016)
  + Unigram language modeling tokenization (Kudo, 2018)
  + WordPiece(Schuster and Nakajima, 2012)

All have 2 parts:
  + A token **learner** that takes a raw training corpus and induces a vocabulary (a set of tokens).
  + A token **segmenter** that takes a raw test sentence and tokenizes it according to that vocabulary

## Byte Pair Encoding(BPE) token learner
Let vocabulary be the set of all individual characters
```
= {A, B, C, D, ..., a, b, c, d, ...}
```

Repeats:
  + Choose the two symbols that are most frequently adjacent in the training corpus(say "A", "B")
  + Add a new merged symbol "AB" to the vocabulary
  + Replace every adjacent "A", "B" in the corpus with "AB".
  
Until _k_ merges have been done.

## BPE token learner algorithm
![BPE token learner algorithm](https://user-images.githubusercontent.com/72482724/145234294-91e91c0b-fb57-4c2f-af77-f1aba96b7c10.jpg)

## Byte Pair Encoding(BPE) Addendum
Most subword algorithms are run inside space-separated tokens. <br>
So we commonly first add a special end-of-word symbol `'__'` before space in training corpus. <br>
Next, separate into letters.
