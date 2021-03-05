import matplotlib.pyplot as plt
import numpy as np

'''
This code creates a hanning window fit on the NUMBER of data given
https://en.wikipedia.org/wiki/Hann_function 

FOR MULTIPLE FILES
'''


def file_len(fname):
    #https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
    i=0;
    with open(fname, "r") as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def hann(file_to_read, file_to_write):
    fl = file_len(file_to_read,)
    
    window = np.hanning(fl)
    myplot =  plt.plot(window)
    
    plt.title("Hann window")
    plt.ylabel("Amplitude")
    plt.xlabel("Sample")
    plt.show()

    # save values in txt
    xvalues = myplot[0].get_xdata()
    yvalues = myplot[0].get_ydata() 

    fwrite = open(file_to_write, "w+")

    for i in range(len(xvalues)):
        fwrite.write("%f " % xvalues[i])
        fwrite.write("%f\r\n" % yvalues[i])


if __name__ == '__main__':
    arxeiaIN = open("int.dat", "r")
    arxeiaOUT = open("hann.dat", "r")

    if (arxeiaIN.mode == 'r') and (arxeiaOUT.mode == 'r'):
        conIN = arxeiaIN.read(); conOUT = arxeiaOUT.read()

    files_in = conIN.split()
    files_out = conOUT.split()
    size = len(files_in)

    for i in range(0, size):
        hann(files_in[i], files_out[i])