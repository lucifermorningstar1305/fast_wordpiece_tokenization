from typing import List, Tuple, Dict, Any, Optional
from trie import Trie

def precompute(V: List):
    """
    This function is an implementation of the precompute stage mentioned in the 
    paper Fast WordPiece Tokenization https://aclanthology.org/2021.emnlp-main.160/

    The function takes in the vocabulary and compute the failure links(f) and 
    Failure Pops (F) of the trie.

    :param V: the vocabulary

    :returns: the root of the trie. 
    """

    tr = Trie()
    r, r_hash = tr.build(V)

    if r != r_hash:
        queue = [r, r_hash]
    else:
        queue = [r]

    while len(queue) > 0:
        u = queue.pop(0)

        for c, v in u.children.items():
            if v == r_hash:
                continue
                
            if v.chiv in V:
                v.f = r_hash
                v.F = [v.chiv]
            else:
                z, Z = u.f, []
                while z is not None and c not in z.children:
                    Z.extend(z.F)
                    z = z.f
                
                if z is not None:
                    v.f, v.F = z.children[c], u.F + Z
            
            queue.append(v)
    
    return r, r_hash

def matchloop(s: str, i: int):
    """
    This function is an implementation of the MATCHLOOP(s, i) 
    defined in the paper Fast WordPiece Tokenization https://aclanthology.org/2021.emnlp-main.160/

    :param s: a string
    :param i: an index corresponding to the string start

    :returns: tokens, nodes and corresponding indices
    """

    u, tokens = R, []

    while i < len(s):
        while s[i] not in u.children:
            if u.f is None:
                return tokens, u, i

            tokens.extend(u.F)
            u = u.f
        
        u = u.children[s[i]]
        i += 1
    
    return tokens, u, i


def originalWordPiece(u: str):
    """
    The wordpiecepiece algorithm of bert defined by google. 
    Source: https://github.com/google-research/bert/blob/master/tokenization.py#L335-L358

    :param u: a text

    :returns: tokens
    """
    is_bad = False

    start = 0
    sub_tokens = []
    
    output_tokens = []

    while start < len(u):
        end = len(u)
        cur_substr = None
        while start < end:
            substr = u[start:end]

            if start > 0:
                substr = "##" + substr
            
            if substr in vocab:
                cur_substr = substr
                break
            end -= 1

        if cur_substr is None:
            is_bad = True
            break

        sub_tokens.append(cur_substr)
        start = end
    
    if is_bad:
        output_tokens.append("<unk>")
    else:
        output_tokens.extend(sub_tokens)

    return output_tokens


def linmaxmatch(w: str):
    """
    This function performs the LinMaxMatch as described in
    the paper Fast WordPiece Tokenization : https://aclanthology.org/2021.emnlp-main.160/

    :param w: a word

    :returns: sub-tokens for the word 
    """
    
    tokens, u, i = matchloop(w+" ", 0)

    if i < len(w) or u not in [R, RH]:
        tokens = ["<unk>"]

    elif u == RH and len(tokens) == 0:
        tokens = originalWordPiece(u.chiv)

    return tokens



if __name__ == "__main__":
    
    
    vocab = ["a", "abcdx", "##b", "##c", "##cdy", "##dz"]
    R, RH = precompute(vocab)

    print(linmaxmatch("##bc"))
    print(linmaxmatch("abcdz"))
    print(linmaxmatch("##"))

