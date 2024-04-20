import logging

from citmre.citmre_fun import rmre_data

logging.basicConfig(level=logging.INFO)

def main():
    logging.info(rmre_data())

if __name__ == '__main__':
    logging.debug('>>> We are starting the execution of the package.')

    main()

    logging.debug('>>> We are finishing the execution of the package.')