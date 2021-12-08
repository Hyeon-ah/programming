# 1_4 Word Tokenization
## Text Normalization
Every NLP task requires text normalization:
  1. Tokenizing (segmenting) words
  2. Normalizing word formats
  3. Segmenting sentences
  
## Space-based tokenization
A very simple way to tokenize
  + for languages that use space characters between words
    - Arabic, Cyrillic, Greek, Latin, etc., based writing systems
  + Segment off a token between instances of spaces
Unix tools for space-based tokenization
  + The "tr" command
  + Inspired by Ken Church's UNIX for Poets
  + Givern a text file, output the word tokens and their frequencies
