# 1_4 Word Tokenization
## Text Normalization
+ (21/12/09): 
+ tokenization 안하면: 문장에서 뭐가 동사고, 주어고 형용사인지 알 수 없게 됨.(Lemma를 알아야 함.) -> 형태소 단위로 끊어주어야 함.
+ 데이터가 process에 들어가기 전에 하는 pre-process 단계임.
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
  + Segment off a token between instances of spaces <br>

Unix tools for space-based tokenization
  + The "tr" command
  + Inspired by Ken Church's UNIX for Poets
  + Givern a text file, output the word tokens and their frequencies

## Issues in Tokenization
Can't just blindly remove puntucation:
  + `m.p.h.`, `Ph.D.`, `AT&T`, `cap'n`
  + prices(`$45.45`)
  + dates(`01/02/06`)
  + URLs(`http://www.stanford.edu`)
  + hashtags(`#nlproc`)
  + email addresses(`someone@cs.colorado.edu`)

Clitic: a word that doesn't stand on its own
  + `are` in `we're`, French `je` in `j'ai`, `le` in `l'honneur`

When should multiword expressions(MWE) be words?
  +`New York`, `rock'n'roll` 이런거는 1개 단어? 2개 단어? -> 논란있음.
  
## Word tokenization / segmentation
중국어나 일본어 같이 단어 사이에 스페이스가 없는 경우도 있다. <br>
In Chinese, it's common to just treat each character(zi) as a token.
  + So the segmentation step is very simple

In other languages (like Thai and Japanese), more complex word segmentation is required.
  + The standard algorithims are neural sequence models trained by supervised machind learning.(물론, 다음에 이야기 할 예정)

