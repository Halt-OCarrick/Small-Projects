# Ernest Schelp, 5/22/22
import re
from winotify import Notification
import requests
from bs4 import BeautifulSoup
import os


def get_soup():
    filepath = os.path.join(THIS_DIR, "archive_list.txt")

    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    h1tags = soup.find_all('h1')
    most_recent_header = h1tags[0].get_text()

    with open(filepath, 'r+', encoding='utf-8', errors='replace') as file:
        archive_file = str(file.read())
        if most_recent_header not in archive_file:
            file.write(str(most_recent_header) + "\n")
            notify(most_recent_header)
    assert file.closed


def get_article_url(a):
    a = re.sub(r'[^A-Za-z\d ]+', '', a)
    return URL + a.lower().replace(" ", "-") + "/"


def notify(article):
    icon_path = os.path.join(THIS_DIR, "icon.png")
    toast = Notification(app_id='0 A.D. - Empires Ascendant',
                         title="New 0 A.D. Article",
                         msg=article,
                         icon=icon_path)
    toast.add_actions(label="View Article", launch=get_article_url(article))
    toast.show()


def test(is_test=False):
    if is_test:
        with open("archive_list.txt", 'r', encoding='utf-8', errors='replace') as file:
            test_header = file.readlines()[-1]
        notify(test_header)


if __name__ == '__main__':
    URL = 'https://play0ad.com/'
    THIS_DIR = os.path.dirname(__file__)
    get_soup()
    test()  # pass parameter True to enter test mode
