import logging

def startHere():
    logging.basicConfig(filename="log.log", level=logging.DEBUG)
    logging.info("using logging")
    logging.warning("this is warning")
        
def write(*args):
    for arg in args:
        print(arg)