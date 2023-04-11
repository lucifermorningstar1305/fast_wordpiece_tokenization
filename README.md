# Fast WordPiece Tokenization


Tokenization is a fundamental part of almost all NLP tasks. BERT uses WordPiece tokenization to tokenize sentences/words before modeling on it. Song et al. came up with a more efficient algorithm (Fast WordPiece Tokenization) for the WordPiece algorithm used by BERT which can be applied to a single word as well as general text. 

In this repository I have implemented just the single word tokenization of this algorithm. Reading the paper and analyzing was kind of difficult therefore I have created a simplified version of this algorithm using vanilla python. 


The main code is present in the file `linmaxmatch.py`. I am working on the general text part of this algorithm and will upload it as soon as it's ready.

# Running the Program
To run this algorithm simply run 
```{bash}
python linmaxmatch.py
```

Make sure to update the vocabulary in the `__main__` function of the `linmaxmatch.py` script.

For more details about this algorithm you can find it in [Google Research](https://ai.googleblog.com/2021/12/a-fast-wordpiece-tokenization-system.html)



