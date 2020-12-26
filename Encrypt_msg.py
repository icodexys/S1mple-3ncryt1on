def encrypt(msg,passwd):
  msg_cifrado=""; y=0
  for x in msg:
    #each character from msg will be processed with each password's character  using XOR operator "^"
    #after  that will convert it from integer value to a character and add it to msg_cifrado and so on....
    msg_cifrado+=chr(ord(x) ^ (256-ord(passwd[y])))
    y=y+1 
    if(y == len(passwd)):  y=0   
  return msg_cifrado

#example------------------------------------------------------
msg="cipher is an algorithm for performing encryption or decryption—a series of well-defined steps that can be followed as a procedure"

msgx=encrypt(msg,"carol")

print(msgx)

print(encrypt(msgx,"carol"))



