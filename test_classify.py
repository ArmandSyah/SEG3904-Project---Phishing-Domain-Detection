import pickle

with open('BuiltModels\\decision_tree.pkl', 'rb') as dt_pickle:
    dt = pickle.load(dt_pickle)

with open('BuiltModels\\random_forest.pkl', 'rb') as rf_pickle:
    rf = pickle.load(rf_pickle)

with open('BuiltModels\\naive_bayes.pkl', 'rb') as nb_pickle:
    nb = pickle.load(nb_pickle)

# # Legit
# print('Decision Tree Results\n')
# dt.predict_url('https://www.reddit.com/r/Games/comments/dmgu22/sources_the_last_of_us_2_delayed_to_spring/')
# dt.predict_url('https://stackoverflow.com/questions/16729574/how-to-get-a-value-from-a-cell-of-a-dataframe')
# dt.predict_url('https://towardsdatascience.com/feature-selection-with-pandas-e3690ad8504b')
# # Not Legit
# dt.predict_url('https://qiita.com/UEFA-Europa-LeaguS/items/5c4ed0ed45b104eb877a')
# dt.predict_url('https://www439.promocao-master.club/pt-psl6208734115db/smart-tv-led-40-samsung-ultra-hd-4k-40nu7100-com-conversor-digital-3-hdmi-2-usb-wi-fi-hdr-premium-smart-tizen/133756442/pr')
# dt.predict_test_set()

print('\nRandom Forest Results\n')
# Legit
rf.predict_url('https://www.reddit.com/r/Games/comments/dmgu22/sources_the_last_of_us_2_delayed_to_spring/')
rf.predict_url('https://stackoverflow.com/questions/16729574/how-to-get-a-value-from-a-cell-of-a-dataframe')
rf.predict_url('https://stackoverflow.com/questions/39839112/the-easiest-way-for-getting-feature-names-after-running-selectkbest-in-scikit-le')
rf.predict_url('https://www.statisticshowto.datasciencecentral.com/rmse')
rf.predict_url('https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/regression-analysis')
# Not Legit
rf.predict_url('https://qiita.com/UEFA-Europa-LeaguS/items/5c4ed0ed45b104eb877a')
rf.predict_url('https://www439.promocao-master.club/pt-psl6208734115db/smart-tv-led-40-samsung-ultra-hd-4k-40nu7100-com-conversor-digital-3-hdmi-2-usb-wi-fi-hdr-premium-smart-tizen/133756442/pr')
rf.predict_test_set()

# print('\nNaive Bayes Results\n')
# # Legit
# nb.predict_url('https://www.reddit.com/r/Games/comments/dmgu22/sources_the_last_of_us_2_delayed_to_spring/')
# nb.predict_url('https://stackoverflow.com/questions/16729574/how-to-get-a-value-from-a-cell-of-a-dataframe')
# # Not Legit
# nb.predict_url('https://qiita.com/UEFA-Europa-LeaguS/items/5c4ed0ed45b104eb877a')
# nb.predict_url('https://www439.promocao-master.club/pt-psl6208734115db/smart-tv-led-40-samsung-ultra-hd-4k-40nu7100-com-conversor-digital-3-hdmi-2-usb-wi-fi-hdr-premium-smart-tizen/133756442/pr')
# nb.predict_test_set()
