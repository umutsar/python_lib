import threading
import time

# İş parçacığı işlevi
def thread_function(name):
    print(f"İş parçacığı {name} başladı")
    time.sleep(2)
    print(f"İş parçacığı {name} bitti")

if __name__ == "__main__":
    # İş parçacığı oluşturma ve başlatma
    t1 = threading.Thread(target=thread_function, args=("1",))
    t2 = threading.Thread(target=thread_function, args=("2",))
    t1.start()
    t2.start()

    # Ana iş parçacığının bitmesini bekleme
    t1.join()
    t2.join()

    print("Tüm iş parçacıkları tamamlandı")
