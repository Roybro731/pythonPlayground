import logging

def startHere():
    fmtstr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
    logging.basicConfig(filename="log.log", 
                        level=logging.DEBUG, format=fmtstr)
    logging.info("using logging")
    logging.warning("this is warning")
        
def write(*args):
    for arg in args:
        print(arg)