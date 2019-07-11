import pickle
phonbook = {
    'sajib':343434,
    'al-amin':343434,
    'latif':343434,
    'anowar':87876,
    'saifullah':73847,
    'mubarok':4343,
    'naoser':3847384
    }
with open('phonbook.txt','wb') as file:
    file = pickle.dump(phonbook,file)


with open('phonbook.txt','rb') as file_read:
    print(pickle.load(file_read))
