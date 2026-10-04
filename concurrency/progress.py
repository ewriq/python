from multiprocessing import Process

def work():
    print("Working")
    
if __name__ == "__main__":
    p = Process(target=work)

    p.start()
    p.join()

    print("Main process finished")