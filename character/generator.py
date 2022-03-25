import os
import random
from copy import copy
from pdfGenerate import pdfGenerator
from .classes import Hero, Bookworm, Geek, Hick, Jock, Popular, Rocker, Troublemaker, Weirdo

archetype = ['Mól książkowy',
                'Geek komputerowy',
                'Prowincjusz',
                'Osiłek',
                'Popularny dzieciak',
                'Rocker',
                'Urwis',
                'Dziwak']


def genArchetype(archetype):
    archetype = random.choice(archetype)
    return archetype


def genAge():
    return random.randint(10, 15)


def genAttribValues(attribVal, age):
    while (sum(attribVal) != age):
        attribVal[0] = random.randint(1, 5)
        attribVal[1] = random.randint(1, 5)
        attribVal[2] = random.randint(1, 5)
        attribVal[3] = random.randint(1, 5)
    return attribVal


def genSkillPoints(sum, maxSkillPoint):
    if sum >= maxSkillPoint:
        points = random.randint(0, maxSkillPoint)
    elif sum < maxSkillPoint:
        points = random.randint(0, sum)
    else:
        points = 0

    return points


def genFromFile(file_name):
    total_bytes = os.stat(file_name).st_size
    random_point = random.randint(0, total_bytes)
    file = open(file_name, encoding='utf-8')
    file.seek(random_point)
    file.readline()
    return file.readline()


def generate():
    # initialize hero and archetype object
    global archetypeHelper
    hero = Hero()

    # randomize archetype and copy archetype object
    hero.archetype = genArchetype(archetype)
    if hero.archetype == 'Mól książkowy':
        archetypeHelper = copy(Bookworm)
    elif hero.archetype == 'Geek komputerowy':
        archetypeHelper = copy(Geek)
    elif hero.archetype == 'Prowincjusz':
        archetypeHelper = copy(Hick)
    elif hero.archetype == 'Osiłek':
        archetypeHelper = copy(Jock)
    elif hero.archetype == 'Popularny dzieciak':
        archetypeHelper = copy(Popular)
    elif hero.archetype == 'Rocker':
        archetypeHelper = copy(Rocker)
    elif hero.archetype == 'Urwis':
        archetypeHelper = copy(Troublemaker)
    elif hero.archetype == 'Dziwak':
        archetypeHelper = copy(Weirdo)

    # set Hero's age
    hero.age = genAge()

    # randomize Hero's attribute points
    attribVal = [0, 0, 0, 0]
    attribVal = genAttribValues(attribVal, hero.age)
    hero.attributes = {'Ciało': attribVal[0],
                       'Technologia': attribVal[1],
                       'Serce': attribVal[2],
                       'Umysł': attribVal[3]}

    # set Hero's luck points
    hero.luckPoints = 15 - hero.age

    # randomize Hero's skill points
    skillSum = 10
    for key in hero.skills.keys():
        if key in archetypeHelper.skills:
            skillPoints = genSkillPoints(skillSum, 3)
            skillSum -= skillPoints
            hero.skills[key] = skillPoints
        elif key not in archetypeHelper.skills:
            skillPoints = genSkillPoints(skillSum, 1)
            skillSum -= skillPoints
            hero.skills[key] = skillPoints
    if skillSum > 0:
        for key in hero.skills.keys():
            if skillSum != 0:
                if key in archetypeHelper.skills and hero.skills[key] < 3:
                    skillSum -= 1
                    hero.skills[key] += 1
                elif key not in archetypeHelper.skills and hero.skills[key] < 1:
                    skillSum -= 1
                    hero.skills[key] += 1
            else:
                break

    # randomize iconic item, problem, drive, pride and anchor
    hero.iconicItem = random.choice(archetypeHelper.iconicItem)
    hero.problem = random.choice(archetypeHelper.problem)
    hero.drive = random.choice(archetypeHelper.drive)
    hero.pride = random.choice(archetypeHelper.pride)
    hero.anchor = random.choice(archetypeHelper.anchor)

    # randomize name
    tempName = genFromFile('names.txt')
    hero.name = tempName[:-1]

    # randomize song
    tempFavSong = genFromFile('songs.txt')
    hero.favSong = tempFavSong[:-1]

    # print(hero.archetype)
    # print(hero.age)
    # print(hero.attributes)
    # print(hero.luckPoints)
    # print(hero.skills)
    # print(archetypeHelper.skills)
    # print(hero.iconicItem)
    # print(hero.problem)
    # print(hero.drive)
    # print(hero.pride)
    # print(hero.anchor)
    # print(hero.name)
    # print(hero.favSong)

    pdfGenerator(hero)