blocks = [
{
    "gym": False,
    "school": True,
    "store": False,
},
{
    "gym": True,
    "school": False,
    "store": False,
},
{
    "gym": True,
    "school": True,
    "store": False,
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
reqs = ["gym", "school", "store"]
def apartmentHunting(blocks, reqs):
    import statistics
    lt=list()
    for i in range(len(blocks)):
            for j in reqs:
                if(blocks[i][j]==True):
                    lt.append(i)
    print(statistics.mode(lt))
