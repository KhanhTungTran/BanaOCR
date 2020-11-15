import os
import pprint

inputsDir = 'inputs'
resultsDir = 'outputs'
path = os.listdir(inputsDir)

dict = {'ð': 'ơ̆', 'ẽ': 'ĕ', '¡': 'i', 'mĩ': 'mĭ', 'ợ': 'ơ', 'ồ': 'ŏ', 'ố': 'ơ̆', 'ỗ': 'ô̆', 'ơi': 'ơĭ', 'ổi': 'ôĭ', 'š': 'ĕ', 'Š': 'ê̆', 'ủ': 'ŭ', 'Ủ': 'Ŭ', 'ũ': 'ŭ', 'Ũ': 'Ŭ'}

for txt in path:
    txtFile = open(inputsDir + '/' + txt, encoding='utf-8', errors='ignore').read()
    for original, replace in dict.items():
        txtFile = txtFile.replace(original, replace)
    
    with open(resultsDir + '/' + txt, 'w', encoding='utf-8') as f:
        f.write(txtFile) 
        