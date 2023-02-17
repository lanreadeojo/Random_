import unittest
from os import path
import os
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import re


def get_lyrics(lyrics_url, tag):
    ''' Takes a url for a azlyrics.com, a tag and a tag name searches for that tag
    in the urls HTML that has the tag_name passed in. Returns the song lyrics found.
    :param lyrics_url: string lyrics.wikia lyrics e.g http://lyrics.wikia.com/wiki
    /TheBeatles:Lucy_In_The_Sky_With_Diamonds
    :param tag:string HTML tag to look for lyrics in e.g. "div"
    :param tag_name: string name of HTML tag for lyrics in e.g lyricbox
    :return : string song lyrics
    '''
    response = requests.get(lyrics_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup.prettify())
    the_lyrics = soup.find_all(tag,)
    for line in the_lyrics:
        if re.search("Picture yourself in a boat on a river", line.text,flags=0):
            return line.text


def create_wordcloud(lyrics_url,tag, file_name = os.path.basename('/root/file.ext')):
    ''' Takes a url for a lyrics page of lyrics.com then creates a wordcloud from the lyrics.
   :param wiki_url: string lyrics.wikia lyrics url e.g
   http://lyrics.wikia.com/wiki/The_Beatles:Girl.
    '''
    lyrics = get_lyrics(lyrics_url, tag)
    wordcloud = WordCloud().generate(lyrics)
    image = wordcloud.to_image()
    image.show()
    image.save(path.dirname(__file__)+'/wordcloud.jpg')


get_lyrics('https://www.azlyrics.com/lyrics/beatles/lucyintheskywithdiamonds.html','div' )
create_wordcloud('https://www.azlyrics.com/lyrics/beatles/lucyintheskywithdiamonds.html','div')



class TestLyricsWordCloud(unittest.TestCase):

    def test_lyrics(self):
        ''' Test that a string gets a return from get_lyrics()'''
        the_url = 'https://www.azlyrics.com/lyrics/beatles/lucyintheskywithdiamonds.html'
        self.assertIsInstance(get_lyrics(the_url, 'div'), str)

    def test_wordcloud_creation(self):
        ''' Test that a new file is created when create_wprldcloud() is called'''
        the_url = 'https://www.azlyrics.com/lyrics/beatles/lucyintheskywithdiamonds.html'
        filecount_before = len(os.listdir())
        the_url = 'https://www.azlyrics.com/lyrics/beatles/lucyintheskywithdiamonds.html'
        create_wordcloud(the_url,'div')
        self.assertEqual(filecount_before + 1, len(os.listdir()))



tests = TestLyricsWordCloud()
tests.test_lyrics()
tests.test_wordcloud_creation()



