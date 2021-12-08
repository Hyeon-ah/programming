# 1_4 Word Tokenization
## Text Normalization
Every NLP task requires text normalization:
  1. Tokenizing (segmenting) words
  2. Normalizing word formats
  3. Segmenting sentences
  
## Space-based tokenization
```
R에서 하는 것처럼 스페이스로 단어들 나누고 token을 알 수 있음.
각종 command를 사용해서 "대문자를 소문자로 변경", "빈도수가 많은 것부터 나열" 등이 가능.
```
A very simple way to tokenize
  + for languages that use space characters between words
    - Arabic, Cyrillic, Greek, Latin, etc., based writing systems
  + Segment off a token between instances of spaces
Unix tools for space-based tokenization
  + The "tr" command
  + Inspired by Ken Church's UNIX for Poets
  + Givern a text file, output the word tokens and their frequencies
