# !/usr/bin/env python
# coding=utf-8

import random, time

def displayIntro():
    print '你来到了一个龙之大陆，在你的正前方，'
    print '有两个洞穴。其中一个洞穴里住着一个友善的龙，'
    print '他会给你一些宝藏。儿另一个洞穴里，'
    print '住着一条贪婪、饥饿的龙，一旦看到你，就会马上把你吃掉！'
    print ''

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print '你想进哪个洞穴寻宝（1 or 2）？'
        cave = raw_input()
        return cave

def checkCave(chosenCave):
    print '你来到了洞穴...'
    time.sleep(2)
    print '这里潮湿、阴暗...'
    time.sleep(2)
    print '一条巨大的龙跳到了你的面前！它张开了血盆大嘴，然后...'
    print ''
    time.sleep(2)

    friendlyDragon = random.randint(1, 2)

    if chosenCave == str(friendlyDragon):
        print '它给了你它的宝藏！'
    else:
        print '你被它当点心吃掉了！'

playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print ('重新开始游戏？（yes or no）')
    playAgain = raw_input()