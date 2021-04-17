---
apiOwner: "AssignMentZentarix"
language: python3
testRunner: pytest
oasVersion: 3
isContainerized: false
webPlatform: Github Repo
dbPlatform: null
authors:
    - Rashid Hamid
date: 17-04-2021
---


Steps to run the program:
    Step 1:
        a. Run the followint command at base directory in one terminal
            python api/localserver.py
    Step 2:
        a. Run the second command at base directory in another terminal
            python cronjob.py


    Details of above steps:
        Step1 will spin up a localserver, which we can then mimic as an api endpoint. inside the localserver file I have used a random function 
        for returning response as either ERROR or SUCCESS. Also the api endpoint will only accept POST request. we can make request to api server
        on localhost address localhost:8000

        Step 2 will run the python script cronjob.py which contains two timers one which run every 60 seconds and the another runs every 5 seconds.
        60 seconds Timer will read data from dataset provided as an input. 
        5 second timer will read data from buffer, Here I have used list to store buffered data.


---

Purpose of edgeprogram script:
    This script contains two functions whose functionality is to make a call to api to post our data read from sensor(here we read from csv file).
    "send_buffered_data" function inside edgeprogram script will post buffered data to server.

---