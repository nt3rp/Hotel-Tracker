#!/usr/bin/env python
import argparse
import cookielib
import logging
import sys
from models import HotelWebsite
from util import create_url_opener

def main():
    #Hooray! It appears that the parameters don't really change!
    # Parse arguments
    parser = argparse.ArgumentParser(description='Try to find out if there is vacancy at a hotel.');
    parser.add_argument('--arrival',   required=True, help="The day you will be arriving")
    parser.add_argument('--departure', required=True, help="The day you will be departing")
    parser.add_argument('--frequency', type=float, default=5, help="How often (in minutes) to check for hotel availability. Defaults to every 5 minutes.")
    parser.add_argument('--config',    default="hotels.json", help="Configuration file to use.")
    parser.add_argument('--log',       default="critical", help="Set the log level of the application")

    # Convert from namespace to dictionary
    arguments = vars(parser.parse_args());

    # Set logger
    log_level = getattr(logging, arguments.get("log").upper(), None)
    logging.basicConfig(level=log_level)

    logging.info("Creating cookie jar and URL opener")
    cookie_jar = cookielib.CookieJar()
    opener = create_url_opener(cookie_jar)

    logging.info("Getting list of hotels")
    hotels = HotelWebsite.from_json_file(opener, arguments["config"])

    for hotel in hotels:
        hotel.check_availability(**arguments)

if __name__ == "__main__":
    sys.exit(main())