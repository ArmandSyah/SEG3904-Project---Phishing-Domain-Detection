import os
import requests

dirname = os.getcwd()

urlhaus_urls = os.path.join(dirname, 'Datasets\\urlhaus_malware_urls.txt')

with open(urlhaus_urls, 'r', encoding='utf8') as phish_file:
    phish_urls = phish_file.readlines()

correct, incorrect = 0,0

for u in phish_urls:
    response = requests.post('http://127.0.0.1:5000/predict', data={'url': u})
    json_r = response.json()
    result = json_r['predicted result']
    correct = correct + 1 if result == 'phish' else correct
    incorrect = incorrect + 1 if result == 'legit' else incorrect

print(f'\nCorrect: {correct} out of {len(phish_urls)} - {(correct/len(phish_urls))*100}%')
print(f'\nIncorrect: {incorrect} out of {len(phish_urls)} - {(incorrect/len(phish_urls))*100}%')
