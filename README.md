# pi-diy-touch-radio-wecker (DIY Smart Alarm Clock)

Ein maßgeschneiderter, intelligenter Nachttisch-Wecker im edlen Pappelholz-Gehäuse. Angetrieben von einem **Raspberry Pi Zero 2 WH**, ausgestattet mit einem **Waveshare 5.5" AMOLED-Display**, **HiFiBerry MiniAmp** Audio, **WS2812B LED-Ambientebeleuchtung**, **Qi-Wireless-Ladefunktion** und einer massiven **Holz-Tasterleiste (Klingel-Stempel-Prinzip)**.

---

## Hardware-Komponenten & Einkaufsliste

1. **Recheneinheit:** Raspberry Pi Zero 2 WH
2. **Display:** Waveshare 5.5" AMOLED (1080x1920)
3. **Sound:** HiFiBerry MiniAmp
4. **Stromversorgung:** USB-C 5V / 4A Netzteil + USB-C auf Terminalblock Adapter
5. **Stromverteilung:** 2x Wago-Klemmen 221 (5-fach)
6. **Kondensator (Puffer):** 1000 µF / 25V Elektrolytkondensator (Elko)
7. **LED-Pegelwandler:** 74HCT125 IC (3.3V zu 5V Level Shifter) + 330 Ohm Widerstand
8. **Beleuchtung:** WS2812B LED-Streifen (5V)
9. **Kabelloses Laden:** Qi-Ladeplatine (5V-Eingang)
10. **Taster-Mechanik:** Industrie-Mikroschalter mit Rollenhebel + 2x Druckfedern + Pappelholz-Führungsstempel

---

## Die Mechanik: Die "Klingel-Stempel"-Lösung

Statt fragiler Tastatur-Stabilisatoren nutzt die große Holz-Snoozetaste das bewährte **Prinzip einer Haustürklingel**:
* **Der Stempel:** Unter die Holz-Taste ist ein passgenauer Holzklotz (1,5 cm tief) geleimt.
* **Die Führung:** Der Klotz gleitet in einem präzisen Schacht im Holzgehäuse, was Verkanten verhindert.
* **Rückstellung:** Ziffern-Druckfedern drücken die Taste nach oben.
* **Schalter:** Unter dem Klotz sitzt ein Mikroschalter mit Rollenhebel, der Ungenauigkeiten beim Drücken problemlos verzeiht.

---

## Schaltplan & Verkabelung

Die Stromverteilung erfolgt zentral über zwei Wago-Klemmen (5V und GND), um Spannungsabfälle zu vermeiden.

![Schaltplan](assets/schaltplan.png)

### Wago-Verteilung (Power-Zentrale)
* **Wago (+) 5V:** Netzteil (+) $\rightarrow$ **1000 µF Elko (+)** $\rightarrow$ Pi Pin 2, AMOLED-Display (5V), Qi-Lader (+), WS2812B (+), 74HCT125 Pin 14 (VCC).
* **Wago (-) GND:** Netzteil (-) $\rightarrow$ **1000 µF Elko (-)** $\rightarrow$ Pi Pin 6, AMOLED-Display (GND), Qi-Lader (-), WS2812B (GND), 74HCT125 Pin 1 & 7, Mikroschalter Pin COM.

### Signal-Verbindungen
* **Mikroschalter NO:** Geht an **Raspberry Pi Pin 11 (GPIO 17)**.
* **LED-Signal:** Pi Pin 19 (GPIO 10 / MOSI) $\rightarrow$ 74HCT125 Pin 2 (In) | Pin 3 (Out) $\rightarrow$ 330 Ohm Widerstand $\rightarrow$ WS2812B DIN.

---

## Erstinstallation (Software)

### 1. SD-Karte vorbereiten
1. DietPi auf die MicroSD-Karte flashen.
2. Kopiere die Konfigurationsdateien aus dem `/config`-Ordner dieses Repos in die Boot-Partition der SD-Karte:
   * `config.txt`
   * `cmdline.txt`
   * `dietpi.txt`
3. Trage deine WLAN-Zugangsdaten in `dietpi-wifi.txt` ein.

### 2. Erster Bootvorgang & SSH
Stecke die Karte in den Pi und schalte den Strom ein. DietPi installiert automatisch das Basissystem. Logge dich nach einigen Minuten per SSH ein:
```bash
ssh root@<IP-DEINES-PI>
# Standard-Passwort: dietpi
