from binascii import unhexlify      

# unhexilify takes a hex string and converts it into a large int

a = unhexlify('1234')

# I am writing the value back into a binary
infile = open('new1.bin', 'wb')
infile.write(a)
infile.close()

b = unhexlify('2345')
infile = open('new2.bin', 'wb')
infile.write(b)
infile.close() 

a = 0x1234
b = 0x2345
'{:x}'.format(a)
'{:x}'.format(b)
