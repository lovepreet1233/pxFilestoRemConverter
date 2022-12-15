import os
    
    
allFilesInFolder = []   
    
def getOnlyFilesInFolder(path, listToAppend):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            listToAppend.append(os.path.join(path, file))
                        
getOnlyFilesInFolder('./pxFiles', allFilesInFolder)


if 'remFiles' not in os.listdir('./'):
    os.mkdir('./remFiles')


for fileName in allFilesInFolder:
    file = open(fileName, 'r+')
    fout  = open('./remFiles/' + file.name.split('/')[-1], 'w+')
    for line in file:
        listOfWords = line.split(' ') # contains - all words including '\n' and spaces
        if '@import' not in listOfWords and '@media' not in listOfWords:
            for word in listOfWords:
                if '\n' in word: #we need to end these words with '\n' # word can be - '\n', '42px;\n', 'something;\n' something --> {, }, 600, $red // it will always have new line character
                    if 'px' in word: #if word have px in it; it will be split into value like 170 --> 17.0 and ends with 'rem;\n'; we add new character cause in above condition we need to have new line character always in the above if statement
                        valueInPx = int(word.split('px')[0])
                        valueInRem = valueInPx * 1/10
                        if str(valueInRem)[-1] == '0': # if value ends with 0 like 5800 ==> 580.0 > eh end wali 0 di gal kr rhe
                            fout.write(str(valueInRem)[:-2] + 'rem;\n')
                        else:
                            fout.write(str(valueInRem) + 'rem;\n')
                    else:
                        fout.write(word)
                else: # we need to end word with space character
                    if 'px' in word:
                        valueInPx = int(word.split('px')[0])
                        valueInRem = valueInPx * 1/10
                        if str(valueInRem)[-1] == '0':
                            fout.write(str(valueInRem)[:-2] + 'rem ')
                        else:
                            fout.write(str(valueInRem) + 'rem ')
                    else:
                        fout.write(word + ' ')
        else:
            for word in listOfWords:
                if '\n' in word:
                    fout.write(word)
                else:
                    fout.write(word + ' ')
    file.close()