import configparser

import cloudinary
import cloudinary.uploader
import cloudinary.api

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()




# https://docs.python.org/3/library/configparser.html

cloudinary.uploader.upload("my_image.jpg")