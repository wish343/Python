__author__ = "Vishal Garg(vg3660)"

import collections
import mergeSort

""" Creating class which contains:
    x and y as Position for the laser
    Score tells the best score
    Directions tells the direction of the best score
"""
Point = collections.namedtuple('LaserPoint',['x','y','score','direction'])

""" Reader function takes input from a given fileName
    it returns a list of list of the integers in the file
"""
def reader(fileName):
    #List of lists
    outerList=[]
    #List of integers
    innerList=[]
    with open(fileName) as f:
        for line in f:
            #Removing extra whitespaces and newline character
            line=line.strip()
            #Splitting the line delimited by a space
            lisa=line.split(' ')
            innerList=[]
            #Taking the elements from the list,converting them to integers
            #and appending them to another list
            for x in lisa:
                innerList.append(int(x))
            #Appending the earlier list into a list of lists
            outerList.append(innerList)
        return outerList

""" This function traverses the 2-d list
    Finds the max score for each of the elements if possible otherwise 0
    Returns a list of LaserPoint objects
"""
def calculateScore(list):
    #List of laserPoint objects
    laserPositions=[]
    #No of rows
    size1=len(list)
    #No of columns
    size2=len(list[0])

    for i in range(size1):
        for j in range(size2):
            score=0
            #Checking for the conditions where Laser is not possible
            if (i==0 or i==size1-1) and (j==0 or j== size2-1):
                direction='none'
            else:
                #Finding the scores in 4-possible directions
                asum1=sum1(i,j,list)
                asum2=sum2(i,j,list)
                asum3=sum3(i,j,list)
                asum4=sum4(i,j,list)
                #Checking for the highest Score
                if(asum1>score):
                    score=asum1
                    direction='South'
                if(asum2>score):
                    score=asum2
                    direction='North'
                if(asum3>score):
                    score=asum3
                    direction='West'
                if(asum4>score):
                    score=asum4
                    direction='East'
            #Appending a new LaserPoint object in the list
            laserPositions.append(Point(i,j,score,direction))
    return laserPositions

""" Side:South
    This function checks for the score in South direction if it is possible
    Otherwise returns 0
"""
def sum1(i,j,list):
    if j-1>=0:
        try:
            sum=list[i][j-1]+list[i][j+1]+list[i+1][j]
        except:
            sum=0
    else:
        sum=0
    return sum

""" Side:North
    This function checks for the score in North direction if it is possible
    Otherwise returns 0
"""
def sum2(i,j,list):
    if j-1>=0 and i-1>=0:
        try:
            sum=list[i][j-1]+list[i][j+1]+list[i-1][j]
        except:
            sum=0
    else:
        sum=0
    return sum

""" Side:West
    This function checks for the score in West direction if it is possible
    Otherwise returns 0
"""
def sum3(i,j,list):
    if j-1>=0 and i-1 >=0:
        try:
            sum=list[i][j-1]+list[i-1][j]+list[i+1][j]
        except:
            sum=0
    else:
        sum=0
    return sum

""" Side:East
    This function checks for the score in East direction if it is possible
    Otherwise returns 0
"""
def sum4(i,j,list):
    if i-1>=0:
        try:
            sum=list[i][j+1]+list[i-1][j]+list[i+1][j]
        except:
            sum=0
    else:
        sum=0
    return sum

"""
    The main function
"""
def main():
    list=reader('input.txt')
    Lasers=calculateScore(list)
    Lasers=mergeSort.mergeSort(Lasers)
    pointsNeeded=int(input("Please input the number of best moves needed"))
    for i in range(pointsNeeded):
        print(Lasers[i].x,Lasers[i].y,'facing',Lasers[i].direction,' and score is ',Lasers[i].score )

if __name__=='__main__':
    main()