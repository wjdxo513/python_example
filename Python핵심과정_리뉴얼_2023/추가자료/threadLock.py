import threading
count = 0

class myThread(threading.Thread):
    def run(self):
        global count
        lock.acquire() # 락을 얻음
        for _ in range(10):
            count += 1 # critical section(임계 영역, 간섭받지않고 실행되어야 할 부분)
            print(count,'->{}'.format(self.getName()))
        lock.release() # 락을 해제함

lock = threading.Lock() # 락 객체를 획득함
threads = []
for i in range(10):
    th = myThread()
    th.start()
    threads.append(th)

for th in threads:
    th.join()
    print('Exiting', count)