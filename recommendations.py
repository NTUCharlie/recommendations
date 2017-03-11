critics={'Lisa Rose':{'Lady in the water':2.5, 'Snakes on a plane':3.5, 'Just my luck':3.0,
                      'Superman Returns':3.5, 'You Me and dupree':2.5, 'The night listener':3.0},
         'Gene Seymour':{'Lady in the water':3.0, 'Snakes on a plane':3.5, 'Just my luck':1.5,
                      'Superman Returns':5.0, 'You Me and dupree':3.5, 'The night listener':3.0},
         'Michael Phillips':{'Lady in the water':2.5, 'Snakes on a plane':3.0,
                      'Superman Returns':3.5,  'The night listener':4.0},
         'Claudia Puid':{ 'Snakes on a plane':3.5, 'Just my luck':3.0,
                      'Superman Returns':4.0, 'You Me and dupree':2.5, 'The night listener':3.0},
         'Mick Lasalle':{'Lady in the water':3.0, 'Snakes on a plane':4.0, 'Just my luck':2.0,
                      'Superman Returns':3.0, 'You Me and dupree':2.0, 'The night listener':3.0},
         'Jack Matthews':{'Lady in the water':3.0, 'Snakes on a plane':4.0,
                      'Superman Returns':5.0, 'You Me and dupree':3.5, 'The night listener':3.0},
         'Toby':{ 'Snakes on a plane':4.5,
                      'Superman Returns':4.0, 'You Me and dupree':1.0}}

from math import sqrt
def sim_distance(prefs, person1, person2):
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
    if len(si)==0:
        return 0
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item], 2)
                        for item in prefs[person1] if item in prefs[person2]])
    return 1/(1+sum_of_squares)

def sim_pearson(prefs, person1, person2):
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
    print(si)
    n=len(si)
    if n==0: return 0
    sum1=sum([prefs[person1][item] for item in si])
    sum2=sum([prefs[person2][item] for item in si])

    sum1sp=sum([pow(prefs[person1][it], 2) for it in si])
    sum2sq=sum([pow(prefs[person2][it], 2) for it in si])
    psum=sum([prefs[person1][it]*prefs[person2][it] for it in si])

    num=psum-(sum1*sum2/n)
    den=sqrt((sum1sp-pow(sum1,2)/n)*(sum2sq-pow(sum2,2)/n))

    if den==0: return 0

    r= num/den
    return r
def topmatches(prefs,person,n=5,similarity=sim_pearson):
    scores=[(similarity(prefs,person,other), other) for other in prefs if other!=person]
    scores.sort()
    scores.reverse()
    return scores[:]