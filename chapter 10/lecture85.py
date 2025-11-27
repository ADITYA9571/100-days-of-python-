# C:\Users\KIIT0001>curl
# curl: try 'curl --help' for more information
# C:\Users\KIIT0001>curl https://chatgpt.com
# <!DOCTYPE html><html lang="en-US"><head><title>Just a moment...</title><meta 
# C:\Users\KIIT0001>curl -o page.html https://chatgpt.com
#   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
#                                  Dload  Upload   Total   Spent    Left  Speed
# 100  6956  100  6956    0     0  29246      0 --:--:-- --:--:-- --:--:-- 29854
# C:\Users\KIIT0001>curl -L https://www.youtube.com/watch
# curl -I https://youtube.com
"""
kiit@AdityaJha:~/python$ python3 photo.py 
https://upsc.gov.in/sites/all/themes/upsc/images/emblem-dark.png image.png
https://upsc.gov.in/sites/all/themes/upsc/images/emblem-dark.png
image.png
"""
"""
code 1
import argparse
import requests
def download_file(url, local_filename):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream = True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size = 8192):
                f.write(chunk)
    return local_filename

parser = argparse.ArgumentParser()
parser.add_argument("url", help = "url to dowmload the file ")
parser.add_argument("OUTPUT", help = "Enter the name to save the file as the output ")
args = parser.parse_args()
print(args.url)
print(args.OUTPUT)
download_file(args.url, args.OUTPUT)
"""
import argparse
import requests
def download_file(url, local_filename):
    if local_filename is None:
        local_filename = url.split('/')[-1]
    with requests.get(url, stream = True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size = 8192):
                f.write(chunk)
    return local_filename

parser = argparse.ArgumentParser()
parser.add_argument("url", help = "url to download the file ")
parser.add_argument("-o", "--output", help = "Enter the name of the file", default  = None)
args = parser.parse_args()
print(args.url)
print(args.OUTPUT, type(args.output))
download_file(args.url, args.OUTPUT)
