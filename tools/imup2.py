#!/usr/bin/env python3
# Usage: vdc_iops_cropper.py [OPTIONS] COMMAND [ARGS]...
#
# CLI program that upload and generates Cloudinary URLs for some images
#
# Options 
# *  --files   -f  PATH  File(s) to Upload. [required]
#    --config  -c  TEXT  Config File taht will be used. [default: ./cloudinary.cfg]
#    --help    -h        Show this message and exit.


import configparser

from rich import print
from rich.panel import Panel

from urllib.parse import urlparse

import cloudinary
import cloudinary.uploader
import cloudinary.api

import rich_click as click


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option("--files", "-f", help="File(s) to Upload.", required=True, multiple=True, type=click.Path(exists=True))
@click.option("--config", "-c", default="./cloudinary.cfg", show_default=True, help="Config File taht will be used.")
def upload_and_filter(files, config):
    """Simple program that upload and generates Cloudinary URLs for some images"""
    cfg = configparser.ConfigParser()

    try:
        cfg.read(config)
    except:
        print('ouch')

    if len(files) < 1:
        print('no files :(')
        quit()

    cloudinary.config( 
        cloud_name = cfg['default']['cloud_name'], 
        api_key = cfg['default']['api_key'], 
        api_secret = cfg['default']['api_secret'],
        dest_folder=cfg['default']['dest_folder'],
        secure = True
    )

    for file in files:
        file_name = file.split("/")[-1]

        upload = cloudinary.uploader.upload(file, 
            public_id = file_name.split(".")[0],
            overwrite = True,
            folder=cfg['default']['dest_folder'],
            resource_type = "image")

        presets_urls = []
        for (_, value) in cfg.items('filters'):
            presets_urls.append(_get_preset_url(url=upload['secure_url'], word=value))

        message = "\n"
        for url in presets_urls:
            message += f"[green bold]{url['preset']}:[/]\t {url['url']}\n"

        print(Panel(message, title=file_name))

def _get_preset_url(url, word):
    spl_url = urlparse(url)
    url_path = spl_url.path.split('/')
    url_path.insert(-3, word)

    new_url = "https://" + spl_url[1] + '/'.join(url_path)

    return {'preset':word, 'url': new_url}

if __name__ == '__main__':
    upload_and_filter()