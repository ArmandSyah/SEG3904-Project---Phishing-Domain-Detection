import json

filepath = 'C:\\Users\\Armand Syahtama\\Dropbox\\Final Year\\Innovation Project\\project\\PhishJson\\verified_online.json'

phish_urls = []

with open(filepath) as json_file:
    data = json.load(json_file)
    for phish_url in data[:500]:
        phish_urls.append(phish_url['url'])
    
with open('../Datasets/retrieved_phish_urls.txt', 'w', encoding="utf-8") as txt_file:
    for url in phish_urls:
        txt_file.write(url + '\n')    
