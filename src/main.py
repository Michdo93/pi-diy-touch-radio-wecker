import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt
from button_handler import TasterThread
from led_controller import LEDSteuerung
from audio_player import AudioPlayer

class WeckerHauptfenster(QWidget):
    def __init__(self):
        super().__init__()
        
        # Hardware-Module laden
        self.leds = LEDSteuerung()
        self.audio = AudioPlayer()
        
        # UI-Setup (Schwarz für AMOLED-Display)
        self.setStyleSheet("background-color: black; color: white;")
        self.setWindowTitle("Holz-Wecker GUI")
        
        # Zeitanzeige
        self.zeit_label = QLabel(self)
        self.zeit_label.setAlignment(Qt.AlignCenter)
        self.zeit_label.setStyleSheet("font-size: 80pt; font-weight: bold; color: #FF9900;")
        
        # Statusanzeige
        self.status_label = QLabel("Wecker bereit", self)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("font-size: 20pt; color: #888888;")

        layout = QVBoxLayout()
        layout.addWidget(self.zeit_label)
        layout.addWidget(self.status_label)
        self.setLayout(layout)

        # Timer für Uhrzeit-Aktualisierung
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.aktualisiere_uhrzeit)
        self.timer.start(1000)
        self.aktualisiere_uhrzeit()

        # Taster-Thread starten
        self.taster_thread = TasterThread(pin=17)
        self.taster_thread.kurzer_druck.connect(self.handle_kurzer_druck)
        self.taster_thread.langer_druck.connect(self.handle_langer_druck)
        self.taster_thread.start()

    def aktualisiere_uhrzeit(self):
        aktuell = QTime.currentTime().toString("hh:mm")
        self.zeit_label.setText(aktuell)

    def handle_kurzer_druck(self):
        print("GUI Event: Kurzer Druck -> Licht umschalten / Snooze")
        self.status_label.setText("Licht umgeschaltet")
        self.leds.umschalten()

    def handle_langer_druck(self):
        print("GUI Event: Langer Druck -> Wecker Scharf/Unscharf")
        self.status_label.setText("Wecker-Status geändert")

    def closeEvent(self, event):
        self.taster_thread.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Im Vollbild starten (Kiosk-Modus für AMOLED)
    fenster = WeckerHauptfenster()
    fenster.showFullScreen()
    
    sys.exit(app.exec_())
