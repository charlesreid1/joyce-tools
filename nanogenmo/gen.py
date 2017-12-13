from textgenrnn import textgenrnn

t = textgenrnn(weights_path='weights_08lestrygonians.hdf5')
###print(t.generate(5, return_as_list=True))
t.generate_to_file('fake_lestrygonians.txt',n=100)
