'''
Binning data
Get a list of data (x, y) and find the average for every five of them.
Use these averages will be the new xs and ys, saved in bin file.
'''


def aver5(a1, a2, a3, a4, a5):
    sum = a1 + a2 + a3 + a4 + a5
    return sum/5

def readNwrite(file_to_read, file_to_write):
    fread = open(file_to_read,"r")

    if fread.mode == 'r':
    	contents = fread.read()

    words = contents.split()
    size = len(words)

    fwrite = open(file_to_write,"w+")

    i=0
    while (i+10 < size):
        xs = aver5(float(words[i]), float(words[i+2]), float(words[i+4]), float(words[i+6]), float(words[i+8]))
        ys = aver5(float(words[i+1]), float(words[i+3]), float(words[i+5]), float(words[i+7]), float(words[i+9]))
        fwrite.write("%f " % xs)
        fwrite.write("%f\r\n" % ys)
        i = i+10


if __name__ == '__main__':
    arxeiaIN = open("files.lis", "r")           # list of input file names to open
    arxeiaOUT = open("files_binned.lis", "r")   # list of output file names to open

    if (arxeiaIN.mode == 'r') and (arxeiaOUT.mode == 'r'):
        conIN = arxeiaIN.read(); conOUT = arxeiaOUT.read()

    files_in = conIN.split()
    files_out = conOUT.split()
    size = len(files_in)

    for i in range(0, size):
        readNwrite(files_in[i], files_out[i])
