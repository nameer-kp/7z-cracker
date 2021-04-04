import  subprocess
isPass = False
words = []
length = 0
file_path=''
with open('wordlist.txt', 'r') as word_list:
    texts = word_list.readlines()
    for i in range(len(texts)):
        words.append(texts[i].rstrip('\n'))
while (length < len(words)):

    process=subprocess.run(["7z", "x",file_path,"-p"+words[length],"-oOutput"],capture_output=True)
    if(process.returncode==0):
        passwd=words[length]
        isPass=True
        break
    else:
        length += 1
if(isPass):
    print("Password is: ",passwd)
else:
    print("Wordlist Doesnt Have the Correct Password")