import os
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '?', ',', '<', '>', '/', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '[', ']', '{', '}', '\\', '|', '"', "'", ':', ';', '~', '`', ' ','''
''']

def makeFile(name, data):
  file = open(name, 'w')
  file.write(data)

def makeFolder(name):
  try:
    os.makedirs(name)
  except:
    x = 1

def encode(data,amount):
  output = ''
  for i in range(0,len(data)):
    for x in range(0, len(alphabet)):
      encoded = x + amount + i
      while encoded >= len(alphabet):
        encoded -= len(alphabet)
      if alphabet[x] == data[i]:
        output = output + alphabet[encoded]
  return output

def decode(data,amount):
  output = ''
  for i in range(0,len(data)):
    for x in range(0, len(alphabet)):
      encoded = x - amount - i
      while encoded < 0:
        encoded += len(alphabet)
      if alphabet[x] == data[i]:
        output = output + alphabet[encoded]
  return output

#database: the file name you want to make. data: what data you want on it. encrypt: this is a bool input asking if you want to encrypt the file or not
def save(database, data, encrypt):
    makeFolder('database')
    if encrypt:  
        makeFile('database/'+database, encode(data, 100))
    else:
        makeFile('database/'+database, data)

#database: the file name you want to open. backupdata: if the file is not found, it will be made with this data. decrypt: this is a bool input asking if the file is encrypted or not
def load(database, backupdata, decrypt):
    try:
        if decrypt:  
            return decode(open('database/'+database).read(), 100)
        else:
            return open('database/'+database).read()
    except:
        makeFile('database/'+database,backupdata)