import os
import configparser
import argparse
import yaml

from rich import print
from rich.panel import Panel

from urllib.parse import urlparse

import cloudinary
import cloudinary.uploader
import cloudinary.api


parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('-c', '--config', type=str, dest='config_file',
                    default='./cloudinary.cfg', help='Config File taht will be used. Defaults to "cloudinary.cfg" within the same path.')
parser.add_argument('-f', '--files', type=str, dest='files', nargs='+',
                    help='File or Files to Upload')

args = parser.parse_args()
config = configparser.ConfigParser()

try:
    config.read(args.config_file)
except:
    print('ouch')

if len(args.files) > 1:
    print('no files :(')
    quit()

def get_preset_url(url, word):
    spl_url = urlparse(url)
    url_path = spl_url.path.split('/')
    url_path.insert(-3, word)

    new_url = "https://" + spl_url[1] + '/'.join(url_path)

    return {'preset':word, 'url': new_url}

def main():
    cloudinary.config( 
        cloud_name = config['default']['cloud_name'], 
        api_key = config['default']['api_key'], 
        api_secret = config['default']['api_secret'],
        dest_folder=config['default']['dest_folder'],
        secure = True
    )

    for file in args.files:
        file_name = file.split("/")[-1]

        if not os.path.isfile(file):
            print(f"File '{file_name}' does not exist. Skipping")

        upload = cloudinary.uploader.upload(file, 
            public_id = file_name.split(".")[0],
            overwrite = True,
            folder=config['default']['dest_folder'],
            resource_type = "image")

        # print(cloudinary.api.resource(upload['public_id']))

        presets_urls = []
        for (key, value) in config.items('filters'):
            presets_urls.append(get_preset_url(url=upload['secure_url'], word=value))

        # print(presets_urls)

        message = "\n"
        for url in presets_urls:
            message += f"[green bold]{url['preset']}:[/]\t {url['url']}\n"

        print(Panel(message, title=file_name))


if __name__ == "__main__":
    main()