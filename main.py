import sys
import pygame
import time
from keybert import KeyBERT
import random

from pygame import QUIT

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
screen.fill((255, 255, 255))
pygame.display.update()
kw_model = KeyBERT()

eragon = """Eragon has changed and informed what and how I read. As the first book that really spoke to me and one that 
I have reread many times since I first read it It has really defined me as a reader and taught me how to read and 
what I enjoy reading. It has made me realize that I love fantasy and an escape from reality. It has also taught me 
that I really enjoy reading and analyzing how authors write to make a story better. Every time I reread the book I 
see more details and more little points that at first seem to be unimportant to the story but as you reread and 
understand the story better those points become more and more important to the story. This has taught me to read 
stories closer so that I can pick up on those points. One of my favorite things like this in Eragon is the fact that 
in the first book the ending is predicted and a scene from it is shown to the reader. This is stuck by throughout the 
whole series and never once does the author waiver from his original vision for the series. This to me is one of the 
best details in the book. """

psych = """Psych has also changed me as a person and informed how I watched shows and took in texts. As a combination 
of serious and funny Psych talks about difficult topics in a very light and fun way while not making them a joke. One 
of the most important things that Psych taught me was how important it is to change as a person. It also showed me 
how to. In one episode “The Polarizing Express” the main character Shawn Spencer goes on an introspective journey to 
see how he has changed the lives of the people around him. He sees that while he has improved their lives in some 
ways he also is hurting them. He then takes this new knowledge and changes how he acts with them so that he is a 
better person. This taught me how to change as a person and to be aware of how i affect the people around me. 
"""

chess = """Chess and learning it through interactions with other people and videos on how to play it has been a large 
impact in my life. Not only has it taught me to change how I view the world and how I analyze problems and make 
decisions. It has also been a part of many things in my life including my computer programming projects and other 
parts of my learning. The learning and changing that I have done from my interactions with chess and related content 
have really changed me as a person and made me a better thinker. It has also advanced my social interactions as it 
has changed with how i interact with people and who I interact with. I have made friends through it I never would 
have without it. """

keywords = kw_model.extract_keywords(eragon)
keyword = kw_model.extract_keywords(psych)
keywor = kw_model.extract_keywords(chess)

key = []
start = True

for keyword1 in keywords:
    print(keyword1)
    key.append(keyword1)
for keyword2 in keyword:
    print(keyword2)
    key.append(keyword2)
for keyword3 in keywor:
    print(keyword3)
    key.append(keyword3)


def displayWords():
    for word in key:
        font_obj = pygame.font.Font('freesansbold.ttf', int(200 * (word[1] ** 1.5)))
        text_obj = font_obj.render(
            word[0], True, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        y = random.randint(100, 800)
        if int(y/100) < 5:
            change = 8 - int(y/100)
        else:
            change = -1 + int(y/100)
        x = random.randint(int(0 + (change*37.5)), int(700 - (change*37.5)))
        screen.blit(text_obj, (x, y))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if start is True:
                start = False
            elif start is False:
                start = True
            #displayWords()
            #pygame.display.update()
    if start:
        time.sleep(.1)
        displayWords()
        pygame.display.update()
