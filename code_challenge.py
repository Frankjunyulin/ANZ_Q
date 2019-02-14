#Implemented by Frank Lin on 14 Feb 2019

#Input: [[1902,1901],[1941,1978],[2004,0],[1957,0],[1989,2008],[1909,2005],[1918,0],[1913,2010],[1979,0],[1961,2002],[1977,2003],[1909,1991]]
#I used list to store the lifespans.


# O(n) solution
def getSolution(lifespans):
    born_lst = {}
    dead_lst = []
    res = set()

    for p in lifespans:
        if p[0] not in born_lst:
            born_lst[p[0]] = 1
        else:
            born_lst[p[0]] += 1

        if p[1] != 0:
            dead_lst.append(p[1])


    for d in dead_lst:
        temp = d + 1
        if temp not in born_lst:
            res.add(temp)
        else:
            born_lst[temp] -= 1
            if born_lst[temp] == 0:
                my_dict.pop(temp)
    return res


#Test function
def main():
    lifespans = [[1902,1991],[1941,1978],[2004,0],[1957,0],[1989,2008],[1909,2005],[1918,0],[1913,2010],[1979,0],[1961,2002],[1977,2003],[1909,1991]]
    res = getSolution(lifespans)
    print(list(res))

if __name__== "__main__":
    main()
