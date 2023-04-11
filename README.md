# Fast WordPiece Tokenization


Tokenization is a fundamental part of almost all NLP tasks. BERT uses WordPiece tokenization to tokenize sentences/words before modeling on it. Song et al. came up with a more efficient algorithm (Fast WordPiece Tokenization) for the WordPiece algorithm used by BERT which can be applied to a single word as well as general text. 

In this repository I have implemented just the single word tokenization of this algorithm. Reading the paper and analyzing was kind of difficult therefore I have created a simplified version of this algorithm using vanilla python. 


The main code is present in the file `linmaxmatch.py`. 

[Update: 2023-04-12] I have implemented the end-to-end tokenization function module described in the paper. 

# Running the Program [Update: 2023-04-12]

To run this program you will need to run the following command in your terminal:

```{bash}
python main.py --vocabulary <custom-vocabulary file> --text "single word/complete text"
```
This will execute the Fast WordPiece Tokenization algorithm by creating a Trie of your vocabulary and using that vocabulary to tokenize the text.

For more details about this algorithm you can find it in [Google Research](https://ai.googleblog.com/2021/12/a-fast-wordpiece-tokenization-system.html)





