from fbchat import Client
from fbchat.models import *
import json
import time
from datetime import datetime  
from datetime import timedelta

class RunMonitoring():
    def __init__(self):
        print("Initializing script...")
        client = Client("wesgibs20@gmail.com", "relictuswbspawn20")
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
                        return_message = self.wbspawntime()
                        client.send(Message(text=return_message), thread_id=thread_id, thread_type=thread_type)
                    elif message.text == "/wbscam":
                        return_message = "Ulol na Ulol"
                        client.send(Message(text=return_message), thread_id=thread_id, thread_type=thread_type)
                    elif "/wbset" in message.text:
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

    def wbspawntime(self):
        return_message = ""
        spawn_loc = {
            "soul": "harvest/elf land",
            "8i": "karben/zahara",
            "saint": "wildland",
            "lake": "dawn/forest",
            "loran": "rift/relic"   
        }
        with open('timestamps.json') as json_file:
            data = json.load(json_file)
            keys = list(data)
            for key in keys:
                return_message = return_message + key + f' ({spawn_loc[key]})' + " - " +data[key] +"\n"
        return return_message

if __name__ == "__main__":
    RunMonitoring()