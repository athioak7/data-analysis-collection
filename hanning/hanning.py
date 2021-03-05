import matplotlib.pyplot as plt
import numpy as np

'''
This code creates a hanning window fit on the NUMBER of data given
https://en.wikipedia.org/wiki/Hann_function 
'''


window = np.hanning(817576)
myplot = plt.plot(window)

plt.title("Hann window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.show()

#save these values in a txt file
xvalues = myplot[0].get_xdata()
yvalues = myplot[0].get_ydata() 

fwrite = open("hanning.txt","w+")

for i in range(len(xvalues)):
    fwrite.write("%f " % xvalues[i])
    fwrite.write("%f\r\n" % yvalues[i])
