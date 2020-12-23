#
# プロセス監視やってみた
#
import processObserver
import os, time

def main():
    # keyWordsは単なる識別子
    if(processObserver.hasAlreadyExecuted("KeyWords")):
        print("This program has already launched.")
        return
    else:
        print("No process which moves this program found.")
        print("Current PID will be registered to pid log.")
        processObserver.register("KeyWords")

    # ま、何もしないんですけどね
    while True:
        print("ラピュタは滅びぬ!何度でも蘇るさ!")
        time.sleep(5)

    pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("SIGINT received")
        exit(0)
    
