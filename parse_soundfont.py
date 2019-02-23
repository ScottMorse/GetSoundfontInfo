from sf2utils.sf2parse import Sf2File
from pprint import pprint

from sys import argv

try:
    file_path = argv[1]
except:
    raise ValueError('Missing command line argument for <path-to-sf2-file>')

try:
    with open(file_path,'rb') as f:
        sf2 = Sf2File(f)
except:
    raise FileNotFoundError('Error in reading file. Make sure path is correct and is an sf2 file.')

print("\n\033[1;32mInfo from file:\033[0m")
pprint(sf2.info)
print(f'\n\033[1;32mSample offset (bytes):\033[0m {sf2.raw.smpl_offset}')
print("\n\033[1;32mPresets:\033[0m")
print("\033[0;36mMore options: \033[0m\n-presets (list preset data)\n-samples (list sample data)")
# pprint(sf2.presets)

if '-presets' in argv:
    print("\n\033[1;32mPresets:\033[0m")
    pprint(sf2.presets)
if '-samples' in argv:
    print("\n\033[1;32mSamples:\033[0m")
    pprint(sf2.samples) 