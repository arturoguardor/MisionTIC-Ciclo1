import operator

def read_file(path):
    data = []
    with open(path, "r") as f:
        i = 0
        for line in f.readlines():
            if i != 0:
                line = line.split(',')
                line[3], line[5], line[6], line[7] = int(line[3]), int(line[5]), int(line[6]), int(line[7])
                data.append(line)
            i += 1
    return data

def sortedcash(totalcash):
    menor = 0
    totalcash.sort(reverse=True)
    menor = totalcash[0]
    for j in range(len(totalcash)):
        if totalcash[j] != 0:
            if totalcash[j] < menor:
                menor = totalcash[j]
    return menor


def counter(city,data):
    etniasname = ["sin reconocimiento", "afrodescendiente", "indigena", "raizal", "palenquero", "gitano"]
    totalcontinue = 0
    totalcash = []
    total = 0
    mincash = 0
    maxcash = 0
    meancash = 0
    countetnia = {"sin reconocimiento": 0, "afrodescendiente": 0, "indigena": 0, "raizal": 0, "palenquero": 0, "gitano": 0}
    j = 0
    for k in range(len(data)):

        totalcash.append(0)

        if data[j][2] == city:

            if data[j][7]:
                totalcontinue += 1
                totalcash[k] = data[j][6]

                meancash += data[j][6]
                total += 1

                if data[j][6] > maxcash:
                    maxcash = data[j][6]

            if data[j][4] == etniasname[etniasname.index(data[j][4])]:
                countetnia[data[j][4]] += data[j][7]
        
        j += 1
    mincash = sortedcash(totalcash)
    # import pdb; pdb.set_trace()
    return totalcontinue, mincash, maxcash, meancash/total, countetnia


def run():
    data = read_file("data.csv")
    city = (input().title())
    
    totalcontinue,mincash,maxcash,meancash,countetnia = counter(city,data)
    print(totalcontinue)
    print(f"{mincash} {maxcash} {meancash:.2f}")
    countetnia = dict(sorted(countetnia.items(), reverse=False))
    countetnia = dict(sorted(countetnia.items(), key=operator.itemgetter(1), reverse=True))
    # countetnia = dict(sorted(countetnia.keys(), reverse=True))
    for key,value in countetnia.items():
        print(key,value)
        
    

if __name__ == '__main__':
    run()
