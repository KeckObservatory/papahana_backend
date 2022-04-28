
import random
import string
from itertools import product


seed = 1984739
random.seed(seed)

INST_MAPPING = {
                 'DEIMOS': {'DE', 'DF'},
                 'ESI': {'EI'},
                 'HIRES': {'HI'},
                 'KCWI': {'KB', 'KF'},
                 'LRIS': {'LB', 'LR'},
                 'MOSFIRE': {'MF'},
                 'OSIRIS': {'OI', 'OS'},
                 'NIRES': {'NR', 'NI', 'NS'},
                 'NIRC2': {'N2', 'NC'},
                }

pis = {
    "Michael Bluth": 5555,
    "Lindsay Bluth-Fünke": 7766,
    "Gob Bluth": 8877,
    "George Michael Bluth": 8899,
    "Maeby Fünke": 7799,
    "Buster Bluth": 8765,
    "Tobias Fünke": 9998,
    "George Bluth Sr.": 1144,
    "Lucille Bluth": 7644,
}

keck_ids = [5555, 7766, 8877, 8655, 2613, 3342, 8899,
            7799, 8765, 9998, 1144, 7644]

observers = ["Narrator", "Oscar Bluth", "Lucille Austero", "Barry Zuckerkorn",
             "Kitty Sanchez", "Steve Holt", "Lupe", "Annyong Bluth",
             "Carl Weathers", "Maggie Lizer", "Stefan Gentles", "Marta Estrella",
             "Cindi Lightballoon", "John Beard", "Ann Veal", "Wayne Jarvis",
             "Dr. Fishman", "Stan Sitwell", "Sally Sitwell", "Mort Meyers",
             "Starla", "Tony Wonder", "Gene Parmesan", "Terry Veal", "Rita Leeds",
             "Larry Middleman", "Bob Loblaw", "Ron Howard", "DeBrie Bardeaux",
             "Rebel Alley", "Herbert Love", "Marky Bark", "Argyle Austero",
             "Paul 'P-Hound' Huan", "Mark Cherry", "Murphy Brown Fünke",
             "Lottie Dottie Da", "Dusty Radler"
]


containers = ['Standard Stars', 'Seeing <1" and no clouds', 'IQ > 1.5"',
              'Cloudy', 'Back-up targets', 'Clear skies good seeing']

comments = [
    "Conditions = seeing < 1 arcsecond,  clear",
    "Observe at midnight",
    "Observe on the first run of the semester.",
    "Observing remotely in 2022B",
    "Calibration Stars",
    "High Priority",
]


wrap_str = ['north', 'south']

status = [0, 1, 2, 3, 4]

timeConstraint = [
    None, ['2021-01-01 08:00:00', '2021-01-01 10:00:00'],
    ['2021-02-02 09:00:00', '2021-02-03 18:00:00'],
    ['2021-05-01 08:00:00', '2021-06-01 10:00:00'],
    ['2021-06-01 08:00:00', '2021-06-07 10:00:00']
]

spectral_types = ['V', 'R', 'I', 'J', 'H', 'K']

sem_ids = ["2022A_K338", "2022A_K166",  "2022B_K111",  "2022B_U043",
           "2022A_U042",  "2022A_U043",  "2022A_U044",  "2022A_U045",
           "2022B_U016",  "2022B_U064",  "2022A_N020",  "2022A_U123",
           "2022A_U124",  "2022B_U158",  "2022B_U159",  "2022B_U160",
           "2022A_N028",  "2022A_U169",  "2022B_U048",  "2022B_U049",
           "2022B_U082",  "2022B_N133",  "2022A_U046",  "2022A_U073",
           "2022A_N140",  "2022B_U056",  "2022B_N057"]

sem_id_tail = ["_U033", "_U050",  "_U042",  "_U043", "_U042",  "_U043",
               "_U044",  "_U045", "_U016",  "_U064",  "_N020",  "_U123",
               "_U124",  "_U158",  "_U159",  "_U160", "_N028",  "_U169",
               "_U048",  "_U049", "_U082",  "_N133",  "_U046",  "_U073",
               "_N140",  "_U056",  "_N057"]

randContainerName = lambda: random.choice(containers)


NOBS = 100 # number of observation blocks


semesters = [str(x)+y for x, y in product(range(2019,2022), ['A', 'B'])]
letters = string.ascii_lowercase

# random generators
randString = lambda x=4: ''.join(random.choice(letters) for i in range(x))
randFloat = lambda mag=10: mag * random.uniform(0,1)
randInt = lambda lr=0, ur=100: random.randint(lr, ur)
randArrStr = lambda x=1, y=1: [randString(x) for _ in range(random.randint(1, y)) ]
optionalRandString = lambda x=4: random.choice([None, randString(x)])
optionalRandArrString = lambda x, y=1: random.choice([None, randArrStr(x, y)])
sampleInst = lambda: random.choice(list(INST_MAPPING.keys()))

randPI = lambda: random.choice(list(pis))
randObserver = lambda: random.choice(observers)
randKeckId = lambda: random.choice(keck_ids)
randSemId = lambda: random.choice(sem_ids)
randSemIdTail = lambda: random.choice(sem_id_tail)
randObserverList = lambda x=1: list(np.random.choice(observers, size=random.randint(1, x), replace=False))
randComment = lambda: random.choice(comments)
optionalRandComment = lambda: random.choice([None, randComment()])
z_fill_number = lambda x, zf=2: str(x).zfill(2)
raDeg = z_fill_number(randInt(0, 360))
arcMinutes = z_fill_number(randInt(0, 60))
arcSeconds = z_fill_number(randInt(0, 60))

decDeg = z_fill_number(randInt(0, 90))
elevation = random.choice(['+', '-'])