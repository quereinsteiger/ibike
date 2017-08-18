import numpy as np
import matplotlib.pyplot as plt
import logging
from time import clock

logging.basicConfig(
    filename="./test.log",
    filemode="w",
    level=logging.DEBUG,
    format = "%(asctime)s [%(levelname)-8s] %(message)s",
    datefmt = "%Y.%M.%D %H:%M:%S"
)

def square(x=10):
    t=clock()
    logging.info("Aufruf")
    x=np.arange(0,x)
    y=x**2
    f=plt.figure()
    plt.plot(x,y)
    elapsed=clock()-t
    logging.info("Ende| Bearbeitungszeit: "+str(t))
    plt.show()
    logging.shutdown()
    return

if __name__ == "__main__":

    square()
