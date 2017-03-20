from random import shuffle
import math

def LinearSearch(Names, Search):
    print(Names,"Names")
    print(Search,"Search")
    Length = len(Names)
    Found = False
    counter = 0
    while counter < Length and Found == False:
        if Names[counter] == Search:
            Found = True
        else:
            print(Names[counter])
            counter = counter + 1
    if Found == True:
        return True
    else: return False

###Bubble Sort
def BubbleSort(List):
    counter = 0
    noswaps = 0
    N = len(List)
    while noswaps != 1:
        count = 1
        noswaps = 1
        for count in range(N-1):
            print("Count 1")
            print(List[count])
            for count2 in range(N-1):
                print("Count2")
                print(List[count])
                if List[count] > List[count + 1]:
                    temp = List[count]
                    List[count] = List[count + 1]
                    List[count + 1] = temp
                    noswaps = 0
                    counter = counter + 1
    return List, counter

def binary_search(List, itemSought):
    First = 0
    Last = len(List)-1
    itemfound = False
    searchfailed = False
    while not itemfound and not searchfailed:
        midPoint = math.ceil((First + Last)/2)
        print(midPoint)
        if List[midPoint] == itemSought:
            itemfound = True
        elif First >= Last:
            searchfailed = True
        elif List[midPoint] > itemSought:
            print(List[midPoint])
            Last = midPoint
        else:
            First = midPoint+1
            print(List[midPoint])
    if itemfound == True:
        print("Found")
    else:
        print("Not Found")

def binary_search_2d(List, itemSought):
    First = 0
    Last = len(List)-1
    itemfound = False
    searchfailed = False
    print(List)
    print(itemSought)
    while not itemfound and not searchfailed:
        midPoint = math.ceil((First + Last)/2)
        print(midPoint)
        if List[midPoint][0] == itemSought:
            itemfound = True
        elif First >= Last:
            searchfailed = True
        elif List[midPoint][0] > itemSought:
            Last = midPoint - 1
        else:
            First = midPoint + 1
    if itemfound == True:
        print("Found")
    else:
        print("Not Found")

if __name__ == "__main__":
    Names = ["Dan", "Dom", "Sam", "Harry", "Toms", "Bobby", "Poop", "Garry", "Jeremy", "JustEat", "BigUp", "Kareem"]
    Length = len(Names)
    #names2 = [["Dan","Sam"],["Josh","Caroline"],["harry","Sophie"]]
    #search2 = input("Search: ")

    shuffle(Names)
    print(Names)

    #print("")
    #print("bubblesort")
    #Names = (BubbleSort(Names))
    #print(Names)
    ###Linear Search
    Search = input("What would you like to search: ")
    print("linear search")
    print(LinearSearch(Names, Search))
    print("")
    #print("binary search")
    #print(binary_search(names2,search2))
    #print("")
    #print("binary search 2d array")
    #print(binary_search_2d(names2,search2))

