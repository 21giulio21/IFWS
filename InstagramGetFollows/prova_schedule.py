import schedule
import time

def job(t):
    tempo = time.time()
    print("I'm working..." + str(tempo), t)
    return

#schedule.every().day.at("15:42").do(job,'It is 01:00')
schedule.every().minute.do(job,'MINUTO')
schedule.every().second.do(job,'SECONDO')

while True:
    schedule.run_pending()
    time.sleep(6) # wait one minute