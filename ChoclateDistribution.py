import os

def main():
    numofchoclate = int(input('Please provide number of choclate in whole postive number:'))
    numofpeople = int(input('Please provide number of people in whole postive number:'))
    
    numofdistributedchoclate = 0
    dictallocatedchoc = {}

    while (numofdistributedchoclate < numofchoclate):
        for i in range(1,numofpeople+1):
            if((numofchoclate - numofdistributedchoclate) < (i*2)):
                if(i in dictallocatedchoc.keys()):
                    dictallocatedchoc.update({i:dictallocatedchoc.get(i)+(numofchoclate - numofdistributedchoclate)})
                else:
                    dictallocatedchoc.update({i:(numofchoclate - numofdistributedchoclate)})
                numofdistributedchoclate = numofdistributedchoclate + (numofchoclate - numofdistributedchoclate)
                break
            else:
                if(i in dictallocatedchoc.keys()):
                    dictallocatedchoc.update({i:dictallocatedchoc.get(i)+(i*2)})
                else:
                    dictallocatedchoc.update({i:i*2})
                numofdistributedchoclate = numofdistributedchoclate + i*2
                if(numofdistributedchoclate == numofchoclate):
                    break
            

    print('total distributed choclate',numofdistributedchoclate)
    print('distribution across: ',dictallocatedchoc)




if __name__ == "__main__":
    main()