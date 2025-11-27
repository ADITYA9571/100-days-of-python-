# Microsoft Windows [Version 10.0.26100.4946]
# (c) Microsoft Corporation. All rights reserved.

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
parser.add_argument("url", help = "urlto dowmload the file ")
parser.add_argument("OUTPUT", help = "Enter the name to save the file as the output ")
args = parser.parse_args()
print(args.url)
print(args.OUTPUT)
download_file(args.url, args.OUTPUT)

