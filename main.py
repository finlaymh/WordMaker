#Created by Finlay Haggar (husky-prophet)
import random
import time
import keyboard
import subprocess
from tqdm import tqdm
banner = '''##########################################
# Finlay's python word generator v1.6.2  #
##########################################
'''

def readfile(file_to_read):
    wordlist = []
    with open(file_to_read, 'r') as f:
        for line in f:
            wordlist.append(line.strip('\n'))
    return wordlist


def compare(wordlist):
    similar = []
    for i in tqdm(range(len(wordlist))):
        word1 = wordlist[i]

        for z in range(len(wordlist)):
            try:
                word2 = wordlist[z + 1]
            except IndexError:
                word2 = ''

            if word1 == word2:
                break

            for x in range(len(word1 + word2)):
                for y in range(len(word1 + word2)):
                    try:
                        word1char = word1[x] + word1[x + 1]
                        word2char = word2[y] + word2[y + 1]
                        if word1char == word2char:
                            similar.append(str(word1[x] + word1[x + 1]))
                        else:
                            pass
                    except IndexError:
                        pass
    return similar


def generate(similar):
    word = []
    for x in range(random.randint(1, 5)):
        try:
            word.append(random.choice(similar))
        except IndexError:
            print 'list empty'
            break
    word = ''.join(word)
    return word


def main():
    subprocess.call(['clear'], shell=True)
    wordsfile = raw_input('Enter path of wordlist: ')
    try:
        print banner + '\nReading words from file (This will take a while):'
        try:
            compared = compare(readfile(wordsfile))
        except IOError:
            print '***ERROR*** Invalid File, restarting ***ERROR***'
            time.sleep(2)
            main()
        print 'Press Enter to generate a word.'
        while True:
            if keyboard.is_pressed('enter'):
                print 'Word: ' + generate(compared)
                print 'Press Enter to generate a word.'
                time.sleep(0.1)
    except KeyboardInterrupt:
        subprocess.call(['clear'], shell=True)
        print 'Bye!'
        exit(2)

main()
