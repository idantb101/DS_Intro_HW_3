#A
def read_line(n, file):
    if not isinstance(n, int):
        return("invalid input detected")
    try:
        f=open(file)
    except FileNotFoundError:
        return("file not found")
    else:
        lines=f.readlines()
        if( len(lines) < (n-1)):
            return("line "+ str(n) +" doesn't exist")
        return(lines[n-1])
#print(read_line(4, 'ex3_text.txt')) 
#print(read_line(9, 'ex3_text.txt')) 
#print(read_line(29, 'ex3_text.txt')) 
#print(read_line("c", 'ex3_text.txt'))
#print(read_line(9, 'ex4_text.txt'))  

#B
import re
def longest_words(file):
    try:
        my_file = open(file, "r")
    except FileNotFoundError:
        print('file not found')
        return([])
    else:
        data = my_file.read()
        data_into_list = data.replace('\n', ' ')
        regex = re.compile('[^a-zA-Z]')
        data =re.sub("[^a-zA-Z]+", " ", data_into_list).split(' ')
        maxlength1 = max(data, key=len)
        while maxlength1 in data: data.remove(maxlength1)  
        maxlength2 = max(data, key=len)
        while maxlength2 in data: data.remove(maxlength2)
        maxlength3 = max(data, key=len)
        while maxlength3 in data: data.remove(maxlength3)
        maxlength4 = max(data, key=len)
        while maxlength4 in data: data.remove(maxlength4)
        maxlength5 = max(data, key=len)
        while maxlength5 in data: data.remove(maxlength5) 
        return([maxlength1,maxlength2,maxlength3,maxlength4,maxlength5])       
#print(longest_words('ex3_text.txt'))
#longest_words('ex4_text.txt') 