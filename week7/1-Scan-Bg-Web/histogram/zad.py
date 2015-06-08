import requests
from bs4 import BeautifulSoup
from histogram import Histogram
import json
import matplotlib.pyplot as plt


def histogram_of_the_results():
    hist = Histogram()
    r = requests.get("http://register.start.bg/")

    soup = BeautifulSoup(r.text)

    allsites = []
    for link in soup.find_all('a'):
        allsites.append(link.get('href'))

    for item in allsites:
        try:
            """
            current_req = requests.get("http://register.start.bg/{}".format(item), timeout=1)
            hist.add(current_req.headers['Server'])
            #print(current_req.headers['Server'])
            """
            current_req = requests.head("http://register.start.bg/{}".format(item), timeout=1)
            hist.add(current_req['Server'])
            print(current_req['Server'])
        except:
            print("error")

"""
    text_file = open("histogramOfTheResults.txt", "w")
    hist_to_json = json.dumps(hist.dict)
    text_file.write(hist_to_json)
    text_file.close()
    """

def helper(txt):

    servers = {
        "apache": "Apache",
        "nginx": "nginx",
        "iis": "IIS",
        "lighttpd": "lighttpd"
    }
    h = Histogram()

    histogram = open(txt, "r")
    file_text = histogram.read()
    json_hist = json.loads(file_text)
    for each in json_hist:
        if



"""
def visualization():
    labels = []
    sizes = []
    for key, value in hist.dict.iteritems():
        labels.append(key)
        sizes.append(value)

    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']


    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')

    plt.show()

"""
if __name__ == '__main__':
    histogram_of_the_results()
