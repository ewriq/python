import threading

counter = 0
lock = threading.Lock()

def increase():
    global counter

    with lock:
        counter += 10.5

threads = []

for i in range(3):
    t = threading.Thread(target=increase)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(counter - 0.5)