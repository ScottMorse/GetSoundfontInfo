from sf2utils.sf2parse import Sf2File
from pprint import pprint
from pyaudio import PyAudio

FILE_PATH = "../../Documents/niceKeys23.sf2"

with open(FILE_PATH,'rb') as f:
    sf2 = Sf2File(f)

pprint(sf2.raw.pdta['Phdr'][1])
pprint(sf2.raw.pdta['Shdr'][24])