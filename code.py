reqs = ["gym", "school", "store"]
blocks = [
{
    "gym": False,
    "school": True,
    "store": True,
},
{
    "gym": True,
    "school": False,
    "store": False,
},
{
    "gym": True,
    "school": True,
    "store": True,
},
{
    "gym": False,
    "school": True,
    "store": False,
},
{
    "gym": False,
    "school": True,
    "store": True,
}
]
count=0
def apartmentHunting(blocks, reqs):
    count=0
    lt=list()
    for i in range(0,len(blocks)):
        for j in reqs:
            if(blocks[i][j]==True):
                lt.append(i)
    for i in lt:
        freq = lt.count(i)
        if(freq> count):
            count = freq
            num = i
    print(num)
apartmentHunting(blocks,reqs)
