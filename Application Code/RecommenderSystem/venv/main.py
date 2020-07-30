# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 00:33:50 2019

@author: personal
"""
import lxml
import bs4
import requests
from fake_useragent import UserAgent
import browserhistory as bh
from datetime import datetime, timedelta
import time
from flask import Flask, render_template
import numpy as npw
import pandas as pd
from os import listdir

app = Flask(__name__)


@app.route('/')
def root():
    dict_obj = bh.get_browserhistory()
    date_N_days_ago = datetime.now() - timedelta(days=3)
    t1 = 1
    ac = 0
    g = 0
    d = 0
    l = 0
    tw = 0
    m = 0
    r = 1
    cost = 0
    x = 0
    max1 = 0
    costf = []
    maxf = 0
    listf = []
    dict_obj.keys()
    # dict_keys(['safari', 'chrome', 'firefox'])
    for t in dict_obj['chrome']:
        newdate = datetime.strptime(t[2][0:10], "%Y-%m-%d")
        if t1 == 1 and newdate >= date_N_days_ago:
            # print(t[0])
            if 'amazon.in' in t[0]:
                url = t[0]
                ua = UserAgent()
                pagea = requests.get(url, {'user_agent': ua.chrome})
                dataa = pagea.text
                soupa = bs4.BeautifulSoup(dataa, 'lxml')
                inp = soupa.find('input', attrs={'type': 'text', 'id': 'twotabsearchtextbox'})
                spana = soupa.find('span', attrs={'id': 'priceblock_ourprice'})
                if spana is not None:
                    if spana.string is not None:
                        print(spana.string)
                if 'gaming' in t[0].lower():
                    g = 1
                if 'laptop' in t[0].lower():
                    l = 1
                if 'desktop' in t[0].lower():
                    d = 1
                if 'monitor' in t[0].lower():
                    m = 1
                if 'accessories' in t[0].lower():
                    ac = 1

            if 'hp.com' in t[0] and 'https://store.hp.com/in-en/default/' != t[0]:
                urlh = t[0]
                ua2 = UserAgent()
                time.sleep(1)
                pageh = requests.get(urlh, {'user_agent': ua2.chrome})
                datah = pageh.text
                souph = bs4.BeautifulSoup(datah, 'lxml')
                spanhp = souph.find('span', attrs={'class': 'price'})
                spanhs = souph.find('span', attrs={'class': 'base', 'data-ui-id': 'page-title-wrapper'})
                strongdif = souph.find('strong', attrs={'role': 'heading'})
                if strongdif is not None:
                    if strongdif.string is not None:
                        if 'options' in strongdif.string.lower():
                            if spanhs is not None:
                                if spanhs.string is not None:
                                    sp = spanhs.string.lower()
                                    if 'laptops' in sp:
                                        l = 1
                                    if 'gaming' in sp:
                                        g = 1
                                    if 'accessories' in sp:
                                        ac = 1
                                    if 'desktop' in sp:
                                        d = 1
                                    if 'monitor' in sp:
                                        m = 1
                    ahp = souph.find('div', attrs={'class': 'customer-category-banner-box'})
                    if ahp.h1 is not None:
                        if ahp.h1.string is not None:
                            if 'laptop' in ahp.h1.string.lower():
                                l = 1
                            if 'gaming' in ahp.h1.string.lower():
                                g = 1
                            if 'desktop' in ahp.h1.string.lower():
                                d = 1
                            if 'monitor' in ahp.h1.string.lower():
                                m = 1
                            if 'accessories' in ahp.h1.string.lower():
                                ac = 1

                else:
                    if spanhp is not None:
                        if spanhp.string is not None:
                            np = spanhp.string[1:].replace(',', '')
                            cost = cost + int(np)
                            x = x + 1
                            if max1 < int(np):
                                max1 = int(np)
                spanstrh = souph.find('strong')
                if spanstrh is not None:
                    if spanstrh.string is not None:
                        strhtag = spanstrh.string.lower()
                        if 'spectre' in strhtag:
                            tw = 1

            if 'flipkart.com' in t[0]:
                urlf = t[0]
                ua1 = UserAgent()
                time.sleep(10)
                pagef = requests.get(urlf, {'user_agent': ua1.chrome})
                dataf = pagef.text
                soupf = bs4.BeautifulSoup(dataf, 'lxml')
                inpf = soupf.find('input', attrs={'type': 'text', 'class': 'LM6RPg'})
                spanf = soupf.find('span', attrs={'class': '_35KyD6'})
                if inpf is not None:
                    if inpf['value'] != '':
                        sf = inpf['value'].lower().lstrip().rstrip()
                        if 'gaming' in sf:
                            g = 1
                        if 'laptop' in sf:
                            l = 1
                        if 'under' in sf:
                            max1 = int(sf[21:])
                        if 'accessories' in sf:
                            ac = 1
                        if 'monitor' in sf:
                            m = 1
                        if 'desktop' in sf:
                            d = 1
                        if 'two-in-one' in sf:
                            tw = 1

                if spanf is not None:
                    print(spanf.text)
                    if spanf.text is not None:

                        if 'Gaming Laptop' in spanf.text:
                            divf = soupf.find('div', attrs={'class': '_1vC4OE _3qQ9m1'})
                            print(divf.string)
                            cf = divf.string[1:].replace(',', '')
                            cost = cost + int(cf)
                            x = x + 1
                            if max1 < int(cf):
                                max1 = int(cf)

    #
    #    else:
    #        t1=0
    # ('https://mail.google.com', 'Mail', '2018-08-14 08:27:26')
    # Write the data to csv files in the current working directory.
    # safari_browserhistory.csv, chrome_browserhistory.csv, and firefox_browerhistory.csv.
    # bh.write_browserhistory_csv()
    # bh.write_browserhistory_csv()
    # Create csv files that contain broswer history
    # print(costf)
    # print(maxf1)
    # print('g' , str(g))
    # print('l' , str(l))
    print(max1)
    print(cost / x)
    aver = cost / x
    print(g)
    print(l)
    print(m)
    print(d)
    print(tw)
    print(ac)
    # Importing the dataset
    dataset = pd.read_csv('gaming1.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 2].values

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    '''# Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)'''

    # Fitting Random Forest Classification to the Training set
    from sklearn.ensemble import RandomForestClassifier
    classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
    classifier.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = classifier.predict(X_test)

    # print(npw.shape(X_test))

    # Making the Confusion Matrix
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred)

    if max1 == 0 and cost == 0:
        r = 6
    else:
        test_data = npw.array([aver, max1])
        r = classifier.predict(test_data.reshape(1, -1))
    print(r)

    list_of_files = listdir('C:\\Users\\personal\\PycharmProjects\\RecommenderSystem\\venv\\static\\G' + str(r[0]))
    for index, link in enumerate(list_of_files):
        list_of_files[index] = "G" + str(r[0]) + "/" + list_of_files[index]
    print(list_of_files)
    return render_template("index.html", result=list_of_files, group=r)


if __name__ == '__main__':
    app.run(debug='true')
