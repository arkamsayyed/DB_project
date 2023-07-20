import logging

logging.basicConfig(filename='Server.log',level=10,
                               format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')
log =  logging.getLogger(str(__file__).split('/')[-1])
log.info("Hello")