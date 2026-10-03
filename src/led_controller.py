import time
try:
    from rpi_ws281x import PixelStrip, Color
    HAS_LED_HARDWARE = True
except ImportError:
    HAS_LED_HARDWARE = False

class LEDSteuerung:
    """
    Steuert die WS2812B LEDs über die rpi_ws281x Bibliothek.
    Verwendet GPIO 10 (SPI MOSI) nach dem Level Shifter.
    """
    def __init__(self, num_leds=12, gpio_pin=10):
        self.num_leds = num_leds
        self.an = False
        
        if HAS_LED_HARDWARE:
            # 800kHz Frequenz, DMA Kanal 10, Signal nicht invertieren, Helligkeit max 255
            self.strip = PixelStrip(num_leds, gpio_pin, 800000, 10, False, 255, 0)
            self.strip.begin()
            print("LED-Streifen erfolgreich initialisiert.")
        else:
            print("WARNUNG: rpi_ws281x nicht installiert oder nicht auf Raspberry Pi. LED-Funktionen werden simuliert.")

    def umschalten(self):
        """Schaltet das Licht um (An/Aus)."""
        if self.an:
            self.ausschalten()
        else:
            self.einschalten_warmweiss()

    def einschalten_warmweiss(self):
        self.an = True
        print("LEDs: Warmweiß eingeschaltet")
        if HAS_LED_HARDWARE:
            # Gemäßigtes Warmweiß (R:255, G:140, B:20)
            for i in range(self.num_leds):
                self.strip.setPixelColor(i, Color(255, 140, 20))
            self.strip.show()

    def ausschalten(self):
        self.an = False
        print("LEDs: Ausgeschaltet")
        if HAS_LED_HARDWARE:
            for i in range(self.num_leds):
                self.strip.setPixelColor(i, Color(0, 0, 0))
            self.strip.show()
