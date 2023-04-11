import pickle
import os
import argparse

from linmaxmatch import e2eWordPiece, linmaxmatch, precompute

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--vocabulary", "-v", type=str, required=True, help="Defines the vocabulary")
    parser.add_argument("--text", "-t", type=str, help="The text to be tokenized")

    args = parser.parse_args()

    vocab = list()
    with open(os.path.join(".", args.vocabulary), "r") as fp:
        vocab = fp.readlines()

    for idx in range(len(vocab)):
        vocab[idx] = vocab[idx].strip("\n")

    if not os.path.exists(f"./trie/"):
        os.mkdir("./trie")    

    pkl_fn = ''.join(args.vocabulary.split('.')[:-1])

    if not os.path.exists(f"./trie/{pkl_fn}.pkl"):
        with open(f"./trie/{pkl_fn}.pkl", "wb") as fp:
            R, RH = precompute(vocab)
            pickle.dump({"R":R, "RH":RH}, fp, pickle.HIGHEST_PROTOCOL)
    
    if args.text is not None:
        
        with open(f"./trie/{pkl_fn}.pkl", "rb") as fp:
            pkl_cnts = pickle.load(fp)
            R, RH = pkl_cnts["R"], pkl_cnts["RH"]

        if len(args.text.split(" ")) < 2:
            tokens = linmaxmatch(args.text, R, RH)
        
        else:
            tokens = e2eWordPiece(args.text, R, RH)

        print(tokens)
    
