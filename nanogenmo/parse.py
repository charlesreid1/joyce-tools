from pprint import pprint
import nltk, re
import numpy as np
# makes unicode easier to deal with
import io

INFILE = 'ulysses_08lestrygonians.txt'
OUTFILE = 'ulysses_08lestrygonians.dat'

"""
Tokenize Text to Sentences

Takes an input text file,
and an output data file.

Parses the sentences in the input file,
and puts them in the output file,
one line per sentence.
"""

def parse_input_sentences(input_filename):
    """Read text from the input file
    and parse it using a Punkt tokenizer.
    """
    # Load file contents
    file_contents = io.open(input_filename,'r').read()
    # Eliminate newlines
    file_contents = re.sub('\n', ' ', str(file_contents))
    # Punkt
    sentences = nltk.sent_tokenize(file_contents)
    return sentences

def write_output_sentences(sentences,output_filename):
    """Write one sentence per line
    to the output file.
    """
    with io.open(output_filename,'w') as f:
        f.writelines("\n".join(sentences))
    # all she wrote

if __name__=="__main__":
    sentences = parse_input_sentences(INFILE)
    write_output_sentences(sentences, OUTFILE)

