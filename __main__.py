from urllib.parse import urljoin
import re
import pdb

import requests
from bs4 import BeautifulSoup

import scrapit


BASE_URL = 'http://www.azlyrics.com/lyrics/'


class SongsByArtist:
    def __init__(self, artist, songs):
        self.artist = artist
        self.songs = songs


def construct_rel_url(artist, song):
    return artist.replace(' ', '') + '/' + song.replace(' ', '') + '.html'


def construct_url(artist, song):
    return urljoin(BASE_URL, construct_rel_url(artist, song))


def scrape_song_lyrics(artist, song):
    url = construct_url(artist, song)
    content = scrapit.get_content(url)
    soup = BeautifulSoup(content)    

    t = soup.prettify()
    t = t.split("start of lyrics", 1)[-1]
    t = t.split("end of lyrics", 1)[0]

    t1 = t.replace('<br>', '')
    t1 = t1.replace('\n', 'thisisanewline')

    rex = re.compile(r'\W+')
    result = rex.sub(' ', t1)

    t2 = t1.replace('thisisanewline', '\n')

    t3 = t2.split('\n')

    t4 = []
    for each in t3:
        t4.append(each.strip())

    t5 = []
    for each in t4[1:-1]:
        if each != '':
            t5.append(each)

    t6 = '\n'.join(t5)

    return t6    


def process_list(songlist):
    pass

def parse_list():
    f = open('songlist', 'r')

    array1 = f.read().split('@')[1:]
    # print (array1)

    array2 = []
    for each in array1:
        t1 = each.split('\n')
        tarray = []
        for each in t1[1:-1]:
            if each != '':
                tarray.append(each)
        dict1 = { t1[0] : tarray }

        array2.append(dict1)

    artists = []
    for each in array2:
        print (each)

        # print (each)

if __name__ == '__main__':
    # artist = 'john frusciante'
    # song = 'heaven'

    # lyrics = scrape_song_lyrics(artist, song)

    # filename = artist + ' - ' + song + '.txt'

    # f = open(filename, 'w')
    # f.write(lyrics)
    # f.close()

    # print ('Writing ' + artist + ' - ' + song + ':\n' + lyrics)

    parse_list()


# pdb.set_trace()

# johnfrusciante/heaven.html