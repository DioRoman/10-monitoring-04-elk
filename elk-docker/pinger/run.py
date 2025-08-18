#!/usr/bin/env python3

import logging
import random
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

while True:
    number = random.randrange(0, 4)

    if number == 0:
        logging.info('Process started successfully.')
    elif number == 1:
        logging.warning('Unexpected input received.')
    elif number == 2:
        logging.error('Failed to connect to the database.')
    elif number == 3:
        logging.exception(Exception('Unhandled exception occurred.'))

    time.sleep(3)