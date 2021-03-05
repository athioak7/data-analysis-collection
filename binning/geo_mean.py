import numpy as np

'''
Binning data (without taking the average5 like bin.py)
Calculate the geometrical mean of the points in the grid
Use these averages will be the new xs and ys, saved in bin file.
'''


def gmean(file_to_read, file_to_write):
    x,y = np.loadtxt(file_to_read, skiprows=0, unpack=True)
    
    # check if you got enough input files
    if len(x) < 2:
        print("Error: unable to process file:", file_to_read)
        return
    
    a = []
    b = []
    e = []      # error list

    #initialize w/ the first element of each list
    multX = x[1]
    sumY = np.log10(y[1])
    n = 1           # count no of elements
    min = 1.6 * x[1]
    for i in range(2, len(x)):
        if x[i] <= min :
            multX = multX * x[i]
            sumY = sumY + np.log10(y[i])
            n += 1
        else:         
            a.append( multX ** (1.0/n) )       #nth root of multX
            b.append( sumY / n )
            e.append( (0.31/n) ** (1.0/2) )
            
            # set unused x[i],y[i] as the new base  
            multX = x[i]
            sumY = np.log10(y[i])
            n = 1
            min = 1.6 * x[i]
                   
    a.append( multX ** (1.0/n) )
    b.append( sumY / n )
    e.append( 0.31 / n )

    # save in txt
    fwrite = open(file_to_write, "w+")

    for i in range(len(a)):
        fwrite.write("%.15f " % a[i])
        fwrite.write("%.15f " % b[i])
        fwrite.write("%.15f\r\n" % e[i])


if __name__ == '__main__':
    arxeiaIN = open("data.dat", "r")    # list of input file names to open
    arxeiaOUT = open("bin.dat", "r")    # list of output file names to open

    if (arxeiaIN.mode == 'r') and (arxeiaOUT.mode == 'r'):
        conIN = arxeiaIN.read(); conOUT = arxeiaOUT.read()

    files_in = conIN.split()
    files_out = conOUT.split()

    for i in range(len(files_in)):
        gmean(files_in[i], files_out[i])
