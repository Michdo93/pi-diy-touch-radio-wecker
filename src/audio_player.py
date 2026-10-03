import subprocess

class AudioPlayer:
    """
    Steuert Audio-Ausgabe und Frequenz-Anpassungen (Tinnitus-Filter).
    """
    def __init__(self):
        print("Audio-Player initialisiert")

    def play_weckton(self):
        print("Weckton wird abgespielt...")
        # Beispielhafter Aufruf von aplay oder mpv
        # subprocess.Popen(["aplay", "/pfad/zu/weckton.wav"])

    def stop(self):
        print("Audio gestoppt")

    def set_lautstaerke(self, prozent):
        """Setzt die System-Lautstärke über ALSA am HiFiBerry MiniAmp."""
        print(f"Setze Lautstärke auf {prozent}%")
        try:
            subprocess.run(["amixer", "-c", "0", "set", "Master", f"{prozent}%"], check=True)
        except Exception as e:
            print("Fehler beim Einstellen der Lautstärke:", e)
