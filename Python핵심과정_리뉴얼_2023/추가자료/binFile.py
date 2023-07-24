import struct

def main(argv=None):
    binfile = open('c:\\work\\bin.dat', 'wb')
    for num in range(50):
        data = struct.pack('i', num)
        binfile.write(data)
    binfile = open('c:\\work\\bin.dat', 'rb')
    intsize = struct.calcsize('i')
    while 1:
        data = binfile.read(intsize)
        if data == '':
            break
        num = struct.unpack('i', data)
        print(num)


if __name__ == '__main__':
    main()
    
