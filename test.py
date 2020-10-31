def doSomething():
    returnMessage = ""
    spawn_loc = [
    ['soul', 'harvest/elf land', '0'],
    ['8i', 'karben/zahara', '0'],
    ['saint', 'wildland', '0'],
    ['lake', 'dawn/forest', '0'],
    ['loran', 'rift/relic', '0']
]
    keys = ['20:05', '24:25', '24:03', '24:21', '24:23']
    time = 0
    while time < 5:
        spawn_loc[time][2] = keys[time]
        time = time+1
    for key in range(len(spawn_loc)-1,0,-1):
        for sort in range(key):
            if int(spawn_loc[sort][2][0:2]) >= int(spawn_loc[sort+1][2][0:2]):
                if int(spawn_loc[sort][2][0:2]) == int(spawn_loc[sort + 1][2][0:2]):
                    if int(spawn_loc[sort][2][3:5]) > int(spawn_loc[sort + 1][2][3:5]):
                        temp = spawn_loc[sort]
                        spawn_loc[sort] = spawn_loc[sort + 1]
                        spawn_loc[sort + 1] = temp
                else:
                    temp = spawn_loc[sort]
                    spawn_loc[sort] = spawn_loc[sort + 1]
                    spawn_loc[sort + 1] = temp

    time2 = 0
    print(f'World boss     Location        Time \n')
    returnMessage = f'World boss     Location        Time \n'
    while time2 < 5:
        returnMessage += f'{spawn_loc[time2][0]}       {spawn_loc[time2][1]}       {spawn_loc[time2][2]}\n'
        time2 = time2 + 1
    return returnMessage    
