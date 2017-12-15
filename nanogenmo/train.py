from textgenrnn import textgenrnn
import os

# Files for weights and stripped text
H5ORIG='weights_original.hdf5'
H5FILE = 'weights_08lestrygonians.hdf5'
DATFILE = 'ulysses_08lestrygonians.dat'

# Rounds of training
n = 20

for i in range(n):

    # For each round of training, 
    # either load the existing weights
    # or start from the provided 
    # pretrained weights.
    if os.path.exists(H5FILE):
        t = textgenrnn(weights_path=H5FILE)
    else:
        t = textgenrnn(weights_path=H5ORIG)
    
    print("\n\nTraining round %d of %d...\n\n\n"%(i+1, n))
    t.train_from_file(DATFILE, num_epochs=20)
    
    # It better be better
    t.save(weights_path=H5FILE)

