from sf2utils.sf2parse import Sf2File
import sf2utils
from pprint import pprint
from pyaudio import PyAudio
import pymusician as pm

FILE_PATH = "../../Documents/niceKeys23.sf2"

with open(FILE_PATH,'rb') as f:
    binary = f.read(10)

with open(FILE_PATH,'rb') as f:
    sf2 = Sf2File(f)

def read_range(start,end,file=FILE_PATH):
    with open(file,'rb') as f:
        f.seek(start)
        return f.read(end - start)

data = sf2.raw.pdta
phdr = data['Phdr']
shdr = data['Shdr']

#grand pianos: 96-98
grand_piano_data = phdr[98] 