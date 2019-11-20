import os
import requests

dirname = os.getcwd()

urlhaus_urls = os.path.join(dirname, 'Datasets\\urlhaus_malware_urls.txt')
legit_urls = os.path.join(dirname, 'Datasets\\List_of_benign_sites.txt')

with open(urlhaus_urls, 'r', encoding='utf8') as phish_file:
    phish_urls = [line.rstrip() for line in phish_file]

with open(legit_urls, 'r', encoding='utf8') as legit_file:
    l_u = [line.rstrip() for line in legit_file]

# correct, incorrect = 0,0

# for u in phish_urls:
#     response = requests.post('http://127.0.0.1:5000/predict', data={'url': u})
#     json_r = response.json()
#     result = json_r['predicted result']
#     correct = correct + 1 if result == 'phish' else correct
#     incorrect = incorrect + 1 if result == 'legit' else incorrect

# print(f'\nCorrect Phish Classifications: {correct} out of {len(phish_urls)} - {(correct/len(phish_urls))*100}%')
# print(f'\nIncorrect Phish Classifications: {incorrect} out of {len(phish_urls)} - {(incorrect/len(phish_urls))*100}%')

correct, incorrect = 0,0

for u in l_u:
    response = requests.post('http://127.0.0.1:5000/predict', data={'url': u})
    json_r = response.json()
    result = json_r['predicted result']
    correct = correct + 1 if result == 'legit' else correct
    incorrect = incorrect + 1 if result == 'phish' else incorrect

print(f'\nCorrect Legit Classifications: {correct} out of {len(l_u)} - {(correct/len(l_u))*100}%')
print(f'\nIncorrect Legit Classifications: {incorrect} out of {len(l_u)} - {(incorrect/len(l_u))*100}%')

