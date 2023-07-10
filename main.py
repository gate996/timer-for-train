import time
import winsound

def sound_alert(duration):
    frequency = 440  # Частота звука (440 Гц - стандартная высота звука "Ля")
    winsound.Beep(frequency, duration * 1000)  # Проигрываем звуковой сигнал

while True:
    print("Работа...")
    time.sleep(30)  # Задержка на 30 секунд (работа)
    
    print("Отдых!")
    sound_alert(30)  # Проигрываем звуковое оповещение на отдых длительностью 30 секунд
    
    time.sleep(30)  # Задержка на 30 секунд (отдых)
