#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def rotate(char,key):
    encrypted =""
    if (char.isupper()):
        FirstChar = ord("A") #return ASCII for A
        encrypted = chr((ord(char) + key - FirstChar) % 26 + FirstChar)
    else:
        FirstChar = ord("a")
        encrypted = chr((ord(char) + key - FirstChar) % 26 + FirstChar ) 
    return encrypted


# In[3]:


def Caesar(PlainText,Key):
    encrypted =""
    Text = ''.join(PlainText.split()) #remove all spaces
    for i in range (len(Text)):
        encrypted += rotate(Text[i],Key)
    return encrypted


# In[4]:


def Vigenere(PlainText,Key,mode):
    Alphabet = {'A':0, 'a':0, 'B':1, 'b':1, 'C':2, 'c':2, 'D':3, 'd':3, 'E':4, 'e':4, 'F':5, 'f':5, 'G':6, 'g':6, 'H':7, 'h':7, 'I':8, 'i':8, 'J':9, 'j':9, 'K':10, 'k':10, 'L':11, 'l':11, 'M':12, 'm':12, 'N': 13, 'n':13, 'O':14, 'o':14, 'P':15, 'p':15, 'Q':16, 'q':16, 'R':17, 'r':17, 'S':18, 's':18, 'T':19, 't':19, 'U':20, 'u':20, 'V':21, 'v':21, 'W':22, 'w':22, 'X':23, 'x':23, 'Y':24, 'y':24, 'Z':25, 'z':25 }
    encrypted =""
    Text = ''.join(PlainText.split()) #remove all spaces
    Key = ''.join(Key.split())
    
    if(mode == True):
        for i in range (len(Text)):
            if(len(Key)<len(Text)):
                Key+=Text[i]
            encrypted += rotate(Text[i],Alphabet[Key[i]])

        
    elif(mode == False):
        for i in range (len(Text)):
            if(len(Key)<len(Text)):
                Key+=Key[i]
            encrypted += rotate(Text[i],Alphabet[Key[i]])
    return encrypted


# In[5]:


def Vernam(PlainText,Key):
    #same as Vigenere but random key and same length
    Alphabet = {'A':0, 'a':0, 'B':1, 'b':1, 'C':2, 'c':2, 'D':3, 'd':3, 'E':4, 'e':4, 'F':5, 'f':5, 'G':6, 'g':6, 'H':7, 'h':7, 'I':8, 'i':8, 'J':9, 'j':9, 'K':10, 'k':10, 'L':11, 'l':11, 'M':12, 'm':12, 'N': 13, 'n':13, 'O':14, 'o':14, 'P':15, 'p':15, 'Q':16, 'q':16, 'R':17, 'r':17, 'S':18, 's':18, 'T':19, 't':19, 'U':20, 'u':20, 'V':21, 'v':21, 'W':22, 'w':22, 'X':23, 'x':23, 'Y':24, 'y':24, 'Z':25, 'z':25 }
    encrypted =""
    Text = ''.join(PlainText.split()) #remove all spaces
    Key = ''.join(Key.split())
    for i in range (len(Text)):
        encrypted += rotate(Text[i],Alphabet[Key[i]])
    return encrypted


# In[6]:


def GetPosition(finalmatrix,char):
    x=y=0
    for i in range(5):
        for j in range(5):
             if finalmatrix[i][j]==char:
                    x=i
                    y=j         
    return x,y


# In[7]:


def CreateMatrix(PlainText,Key):
    Key = Key.replace("j","i")
    Key = Key.upper()
    Key = ''.join(Key.split())
    Alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" 
    matrix = []
    Text = ''.join(PlainText.split())
    Text = Text.upper()
    

    for i in range(len(Key)):
        if not Key[i] in matrix:
            matrix.append(Key[i])
    for i in range(len(Alphabet)):
        if not Alphabet[i] in matrix:
            matrix.append(Alphabet[i])    
    
    finalmatrix = [matrix[i:i+5] for i in xrange(0, 25, 5) ]
    
    return finalmatrix


# In[8]:


def Playfair(PlainText,Key):
    encrypted=""
    Key = Key.replace("j","i")
    Key = Key.upper()
    Key = ''.join(Key.split())
    Text = ''.join(PlainText.split())
    Text = Text.replace("j","i")
    Text = Text.upper()
    
    message=[]

    for i in Text:
        message.append(i)
    
    finalmatrix = CreateMatrix(PlainText,Key)
    
    for i in range(0,len(message)-1,2):
        if(message[i]==message[i+1]):
            message.insert(i+1,'X')
            
    if(len(message)%2 != 0 ):
        message.append('X')

    for i in range (0,len(message)-1,2):
        x1,y1= GetPosition(finalmatrix,message[i])
        x2,y2= GetPosition(finalmatrix,message[i+1])
        if(x1==x2):
            encrypted += finalmatrix[x1][(y1+1) %5] 
            encrypted += finalmatrix[x2][(y2+1) %5] 
        elif(y1==y2):
            encrypted += finalmatrix[(x1+1)%5][y1] 
            encrypted += finalmatrix[(x2+1)%5][y2] 
        else:
            encrypted += finalmatrix[x1][y2]
            encrypted += finalmatrix[x2][y1]

    return encrypted.lower()


# In[9]:


def CreateHillMatrix(PlainText,KeyMatrix):
    
    Alphabet = {'A':0, 'a':0, 'B':1, 'b':1, 'C':2, 'c':2, 'D':3, 'd':3, 'E':4, 'e':4, 'F':5, 'f':5, 'G':6, 'g':6, 'H':7, 'h':7, 'I':8, 'i':8, 'J':9, 'j':9, 'K':10, 'k':10, 'L':11, 'l':11, 'M':12, 'm':12, 'N': 13, 'n':13, 'O':14, 'o':14, 'P':15, 'p':15, 'Q':16, 'q':16, 'R':17, 'r':17, 'S':18, 's':18, 'T':19, 't':19, 'U':20, 'u':20, 'V':21, 'v':21, 'W':22, 'w':22, 'X':23, 'x':23, 'Y':24, 'y':24, 'Z':25, 'z':25 }
    matrix = []
    Text = ''.join(PlainText.split())
    Text = Text.upper()
    message = []
    finalmatrix=[]

    for i in Text:
        message.append(i)
        
    if(len(KeyMatrix)==2):
        if(len(Text)%2 != 0 ):
            message.append('X')
        for i in range(len(message)):
                matrix.append(Alphabet[message[i]])
        finalmatrix = [matrix[i:i+2] for i in xrange(0, len(message), 2) ]
        B = [[0 for x in range(len(finalmatrix))] for y in range(2)]    
        for i in range(2): 
            for j in range(len(finalmatrix)): 
                B[i][j] = finalmatrix[j][i] 
        
    elif(len(KeyMatrix)==3):
        if(len(Text)%3 == 1):
            message.append('X')
            message.append('X')
        if(len(Text)%3 == 2 ):
            message.append('X')
    
        for i in range(len(message)):
                matrix.append(Alphabet[message[i]])
        finalmatrix = [matrix[i:i+3] for i in xrange(0, len(message), 3) ]
        
        B = [[0 for x in range(len(finalmatrix))] for y in range(3)]    
        for i in range(3): 
            for j in range(len(finalmatrix)): 
                B[i][j] = finalmatrix[j][i] 
    return B


# In[10]:


def GetCipherText(matrix):
    encrypted=""
#     Alphabet = { 0:'A', 0: 'a', 1:'B', 1:'b', 2:'C', 2:'c', 3:'D',3:'d',4:'E',4:'e',5:'F',5:'f',6:'G',6:'g',7:'H',7:'h',8:'I',8:'i',9:'J',9:'j',10:'K',10:'k',11:'L',11:'l',12:'m',12:'M',13:'N',13:'n',14:'O',14:'o',15:'P',15:'p',16:'Q',16:'q',17:'r',17:'R',18:'S',18:'s',19:'T',19:'t',20:'u',20:'U',21:'V',21:'v',22:'w',22:'W',23:'X',23:'x',24:'y',24:'Y',25:'Z',25:'z'}
    Alphabet = { 0:'A', 1:'B', 2:'C', 3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}

    for i in range(len(matrix[0])):  
        for j in range(len(matrix)):
            encrypted+=Alphabet[matrix[j][i]]
    return encrypted


# In[11]:


def Hill(PlainText,KeyMatrix):
    
    finalmatrix=CreateHillMatrix(PlainText,KeyMatrix)
    size = len(finalmatrix[0])
    
    if(len(KeyMatrix)==2):
        matrix = [[0 for x in range(size)] for y in range(2)]
        for i in range(len(KeyMatrix)):  
            for j in range(len(finalmatrix[0])):  
                for k in range(len(finalmatrix)):  
                    matrix[i][j] += (KeyMatrix[i][k] * finalmatrix[k][j])
                    matrix[i][j] = matrix[i][j] %26
                  
    elif(len(KeyMatrix)==3):
        matrix = [[0 for x in range(size)] for y in range(3)]
        for i in range(len(KeyMatrix)):  
            for j in range(len(finalmatrix[0])): 
                for k in range(len(finalmatrix)):  
                    matrix[i][j] += (KeyMatrix[i][k] * finalmatrix[k][j] )
                    matrix[i][j] = matrix[i][j] %26
    encrypted = GetCipherText(matrix)
    return encrypted


# In[12]:


def main():
   #CAESAR CIPHER
   f=open("caesar_plain.txt", "r")
   f1=f.readlines()
   f2= open("caesar_cipher.txt","w+")
   
   f2.write("KEY=3")
   f2.write('\n')
   f2.write('\n')
   for x in f1:
       f2.write(Caesar(x,3))#key=3
       f2.write('\n')
       
   f2.write('\n')
   f2.write("KEY=6")
   f2.write('\n')
   f2.write('\n')
   for x in f1:
       f2.write(Caesar(x,6))#key=6
       f2.write('\n')
   f2.write('\n')
   f2.write("KEY=12")
   f2.write('\n')
   f2.write('\n')
   for x in f1:
       f2.write(Caesar(x,12))#key=6
       f2.write('\n')

   #PLAY FAIR CIPHER
   f=open("playfair_plain.txt", "r")
   f1=f.readlines()
   f2= open("playfair_cipher.txt","w+")
   
   f2.write("KEY=rats")
   f2.write('\n')
   f2.write('\n')
   for x in f1:
       f2.write(Playfair(x,"rats"))#key=rats
       f2.write('\n')
       
   f2.write('\n')
   f2.write("KEY=archangel") #key=archangel
   f2.write('\n')
   f2.write('\n')
   for x in f1:
       f2.write(Playfair(x,"archangel"))#key=archangel
       f2.write('\n')
  
    #HILL CIPHER 2X2
   f=open("hill_plain_2x2.txt", "r")
   f1=f.readlines()
   f2= open("hill_cipher_2x2.txt","w+")
   
   f2.write("KEY=[[5,17],[8,3]]")
   f2.write('\n')
   f2.write('\n')
   for x in f1:
       f2.write(Hill(x,[[5,17],[8,3]]))
       f2.write('\n')
       

  
    #HILL CIPHER 3X3
   f=open("hill_plain_3x3.txt", "r")
   f1=f.readlines()
   f2= open("hill_cipher_3x3.txt","w+")
       
   f2.write('\n')
   f2.write("KEY=[[2,4,12],[9,1,6],[7,5,3]]") 
   f2.write('\n')
   f2.write('\n')
   for x in f1:
       f2.write(Hill(x,[[2,4,12],[9,1,6],[7,5,3]]))
       f2.write('\n')
       
       
   #VIGENERE CIPHER 
   f=open("vigenere_plain.txt", "r")
   f1=f.readlines()
   f2= open("vigenere_cipher.txt","w+")
       
   f2.write('\n')
   f2.write("KEY=pie") #key pie repeating mode
   f2.write('\n')
   f2.write('\n')
   for x in f1:
       f2.write(Vigenere(x,"pie",False)) #repeating mode = False
       f2.write('\n')
       
       
   f2.write('\n')
   f2.write("KEY=aether") #key aether auto mode
   f2.write('\n')
   f2.write('\n')
   for x in f1:
       f2.write(Vigenere(x,"aether",True)) #auto mode = True
       f2.write('\n')
       
    #VERNAM CIPHER 
   f=open("vernam_plain.txt", "r")
   f1=f.readlines()
   f2= open("vernam_cipher.txt","w+")
       
   f2.write('\n')
   f2.write("KEY=SPARTANS") #key 
   f2.write('\n')
   f2.write('\n')
   for x in f1:
       f2.write(Vernam(x,"SPARTANS")) 
       f2.write('\n')
       
       
       
   a = raw_input("Enter Plain Text for Caesar Cipher : ")
   b = input("Enter Key for Caesar Cipher : ")
   
   print(Caesar(a,b))
   
   c = raw_input("Enter Plain Text for Play Fair Cipher : ")
   d = raw_input("Enter Key for Play Fair Cipher : ")
   print(Playfair(c,d))
   
   e = raw_input("Enter Plain Text for Hill Cipher : ")
   lst = [ ] 
   f = int(input("Enter number of rows of the hill matrix : ")) 
   if (f==2):
       for i in range(0, f): 
           row = [int(input()),int(input())] 
           lst.append(row)  
   elif (f==3):
       for i in range(0, f): 
           row = [int(input()),int(input()),int(input())] 
           lst.append(row)  
   
   print(Hill(e,lst))
   
   g = raw_input("Enter Plain Text for Vernam Cipher : ")
   h = raw_input("Enter Key for Vernam Cipher : ")
   print(Vernam(g,h))
   
   i = raw_input("Enter Plain Text for Vigenere Cipher : ")
   j = raw_input("Enter Key for Vigenere Cipher : ")
   k = raw_input("Enter mode for Vigenere Cipher,False for repetitve mode or True for auto mode : ")
   if(k=="False"):
       print(Vigenere(i,j,False))
   elif(k =="True"):
       print(Vigenere(i,j,True))
       
   input()


# In[ ]:


if __name__=="__main__":
    main()


# In[ ]:





# In[ ]:




