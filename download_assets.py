#!/usr/bin/env python3
"""
download_assets.py

Simple helper to download external assets required by the project.

Usage:
  python download_assets.py [--model-url MODEL_URL]

This will download `haarcascade_frontalface_default.xml` from OpenCV's repo
if it's not already present. If you provide `--model-url`, it will also
download `best_model.h5` to the repository root.
"""
from pathlib import Path
import argparse

HAAR_URL = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
ROOT = Path(__file__).parent

def download(url, target_path):
    target_path = Path(target_path)
    target_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        import requests
        r = requests.get(url, stream=True)
        r.raise_for_status()
        with open(target_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    except Exception:
        # fallback to urllib
        import urllib.request
        urllib.request.urlretrieve(url, target_path)

def main():
    parser = argparse.ArgumentParser(description='Download required assets for facial_emotion project')
    parser.add_argument('--model-url', help='URL to download best_model.h5 if not present')
    args = parser.parse_args()

    haar_target = ROOT / 'haarcascade_frontalface_default.xml'
    if haar_target.exists():
        print('haarcascade_frontalface_default.xml already exists, skipping.')
    else:
        print('Downloading Haar cascade...')
        try:
            download(HAAR_URL, haar_target)
            print('Downloaded', haar_target.name)
        except Exception as e:
            print('Failed to download Haar cascade:', e)
            print('You can manually get it from:', HAAR_URL)

    model_target = ROOT / 'best_model.h5'
    if model_target.exists():
        print('best_model.h5 already exists, skipping.')
    else:
        if args.model_url:
            print('Downloading best_model.h5...')
            try:
                download(args.model_url, model_target)
                print('Downloaded best_model.h5')
            except Exception as e:
                print('Failed to download model:', e)
        else:
            print('best_model.h5 not found.')
            print('If you have a URL for the pretrained model, re-run with --model-url <URL>')
            print('Or place best_model.h5 into the repository root.')

if __name__ == '__main__':
    main()
