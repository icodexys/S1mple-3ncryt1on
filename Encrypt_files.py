import os# we need to get the size of the file
def encrypt(filename,passwd):
    char_ciphered="";y=0
    #we will add into that variable "fsize" the total size in byt  of the file
    fsize=os.stat(filename).st_size
    #open  2 files as bytes reading, "Fr" will read each  and "fw" will write that byte to the second new file after being XORed
    Fr=open(filename,"rb")
    fw=open("x"+filename,"wb+")
    for b in range(fsize):
        #since  will read the file in bytes we need to convert it to list where items will become integers and those integers represent an ASCII code
        #being a list with one item integer we need to convert it to simple integer by using [0] next to list(Fr.read(1))
        #after that will operate with a character from passwd usinr XOR=^
        char_ciphered=list(Fr.read(1))[0]^(255-ord(passwd[y]))
        y+=1
        if y==len(passwd):y=0
        #the character encrypted will be written in the file fw
        fw.write(bytes([char_ciphered]))
    Fr.close
    fw.close




#example--------------------------------------------------------
#encrypt it with a password
encrypt("example.txt","jewel")
#decrypt it with thesame password
encrypt("xexample.txt","jewel")




#by Jeff Alberty
