import fbchat
from fbchat import Client
from fbchat.models import *
from fbchat import Client, Thread, Message, ThreadLocation
import json
import time
from datetime import datetime  
from datetime import timedelta
import test
import re
fbchat._util.USER_AGENTS    = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"]
fbchat._state.FB_DTSG_REGEX = re.compile(r'"name":"fb_dtsg","value":"(.*?)"')
class RunMonitoring():
    def __init__(self):
        print("Initializing script...")
        client = Client("louiejapitan2001@gmail.com", "Permiha101")
        thread_id = "3494311873939189"
        thread_type = ThreadType.GROUP
        prev_messages = []
        spawn_time = {
            "soul": 2,
            "8i": 3,
            "saint": 4,
            "lake": 6,
            "loran": 8
        }
        while(True):
            messages = client.fetchThreadMessages(thread_id=thread_id, limit=10)
            messages.reverse()
            for message in messages:
                read_status = f'{message.text}-{message.timestamp}' in prev_messages
                if read_status == False:
                    prev_messages.append(f'{message.text}-{message.timestamp}')
                    if message.text == "/wbspawn":
                        return_message = self.doSomething()
                        print(self.doSomething())
                        client.send(Message(text=return_message), thread_id=thread_id, thread_type=thread_type)
                    elif message.text == "/wbscam":
                        return_message = "Ulol na Ulol"
                        client.send(Message(text=return_message), thread_id=thread_id, thread_type=thread_type)
                    elif message.text == "/wbset" in message.text:
                        digest = message.text.split(' ')
                        if len(digest) == 3:
                            with open('timestamps.json') as json_file:
                                data = json.load(json_file)
                                keys = list(data)
                                if digest[1] in keys:
                                    new_time = datetime.strptime(digest[2], '%H:%M') + timedelta(hours=spawn_time[digest[1]])
                                    data[digest[1]] = new_time.strftime('%H:%M')
                                    with open('timestamps.json', 'w') as outfile:
                                        json.dump(data, outfile)
                                        client.send(Message(text=f'{digest[1]} spawn time: {data[digest[1]]}'), thread_id=thread_id, thread_type=thread_type)
                    elif message.text == "/sinolooter":
                        return_message = "Zem dakilang looter"
                        client.send(Message(text=return_message), thread_id=thread_id, thread_type=thread_type)
                    elif message.text == "/sinomanyak":
                        return_message = "Lahat kayo pwera kay lulu"
                        client.send(Message(text=return_message), thread_id=thread_id, thread_type=thread_type)
                    elif message.text == "/sinomalakas":
                        return_message = "Relictus lang malakas"
                        client.send(Message(text=return_message), thread_id=thread_id, thread_type=thread_type)
                    elif message.text == "/latestcode":
                        return_message = "Vvxjtpo5Qn (November 1, 2020)"
                        client.send(Message(text=return_message), thread_id=thread_id, thread_type=thread_type)
            time.sleep(3)
    def doSomething(self):
        returnMessage = ""
        spawn_loc = [
        ['soul', 'harvest/elf land', '0'],
        ['8i', 'karben/zahara', '0'],
        ['saint', 'wildland', '0'],
        ['lake', 'dawn/forest', '0'],
        ['loran', 'rift/relic', '0']
    ]
        with open('timestamps.json') as json_file:
            data = json.load(json_file)
            
            spawn_loc[0][2] = data['soul']
            spawn_loc[1][2] = data['8i']
            spawn_loc[2][2] = data['saint']
            spawn_loc[3][2] = data['lake']
            spawn_loc[4][2] = data['loran']
            print(f"spawn_loc->{spawn_loc[0][2] }")

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
        while time2 < 5:
            returnMessage += f'{spawn_loc[time2][0]}    -   {spawn_loc[time2][2]}\n{spawn_loc[time2][1]}\n'
            time2 = time2 + 1
        return returnMessage    

if __name__ == "__main__":
    RunMonitoring()
