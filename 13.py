dist=[]
flag=True
maxsum=int(input('Enter integer:'))
while maxsum<=0:
    print('Please enter a number greater than 0!\n')
    maxsum=int(input('Enter integer:'))
while flag:
    answer=raw_input('Do you want to add a distance number to the list?:Y/N\n')
    if (answer=='Y') or (answer =='y'):
        distance=int(input('Enter distance number:'))
        dist.append(distance)
    else:
        flag=False
    dist.sort(reverse=True)

def maxDistance(dist, maxsum):
    sumdist=0
    for i in dist:
        if i<=maxsum:
            if (sumdist+i) <= maxsum:
                sumdist=sumdist+i
    print (sumdist)

maxDistance(dist,maxsum)