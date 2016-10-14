from binascii import unhexlify      
a = unhexlify('1234')
infile = open('new1.bin', 'wb')
infile.write(a)
infile.close()

b = unhexlify('2345')
infile = open('new2.bin', 'wb')
infile.write(b)
infile.close() 
