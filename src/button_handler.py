import RPi.GPIO as GPIO
import time
from PyQt5.QtCore import QThread, pyqtSignal

class TasterThread(QThread):
    """
    Überwacht den Mikroschalter an GPIO 17 im Hintergrund.
    Unterscheidet zwischen kurzem und langem Tastendruck.
    """
    kurzer_druck = pyqtSignal()
    langer_druck = pyqtSignal()

    def __init__(self, pin=17):
        super().__init__()
        self.pin = pin
        self.running = True
        GPIO.setmode(GPIO.BCM)
        # Interner Pull-Up Widerstand: Schalter schaltet gegen GND
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def run(self):
        print("Taster-Überwachung gestartet auf GPIO", self.pin)
        while self.running:
            # GPIO.LOW bedeutet, der Taster ist gedrückt
            if GPIO.input(self.pin) == GPIO.LOW:
                start_zeit = time.time()
                
                # Warten, bis der Taster wieder losgelassen wird (Entprellung)
                while GPIO.input(self.pin) == GPIO.LOW:
                    time.sleep(0.02)
                
                dauer = time.time() - start_zeit
                print(f"Taster gedrückt für {dauer:.2f} Sekunden")

                if dauer >= 1.5:
                    self.langer_druck.emit()
                elif dauer > 0.05:  # Signalisiert gültigen Klick (Filter für Prellen)
                    self.kurzer_druck.emit()
            
            time.sleep(0.05)

    def stop(self):
        self.running = False
        self.wait()
