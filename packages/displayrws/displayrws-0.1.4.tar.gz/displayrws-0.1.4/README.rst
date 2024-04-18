##########
displayrws
##########

Dit project beschrijft hoe een 1,3 inch HD_IPS_TFT_LCD display van Joy-IT aangesloten kan worden op een ESP32.

Benodigdheden:
.. begin-inclusion-intro-marker-do-not-remove

- ESP32 (type ESP-WROOM-32) bijv. van Joy-IT
- kabeltjes
- micro USB kabel
- Display 240x240 pixel (SBC-LCD01)

Verder is een computer met Python nodig.
Toegang tot het USB device is noodzakelijk.

############
 Stappenplan
############

Installeer Python
===================

Windows
~~~~~~~

  Klik op de Windows knop (Start).

  Type in:

  ```cmd```

  vervolgens:

  ```curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py```

  vervolgens:

  ```python get-pip.py```

  Wanneer Python nog niet geinstalleerd is, verschijnt er een Windows Store dialoog.
  In dit Windows Store dialoog, klik op Downloaden van Python.


Voor Linux:
~~~~~~~~~~~

  ```sudo apt install python3```
  ```sudo apt install python3-pip```


Installeer esphome:
=====================

  ```pip install esphome```

  ```pip install pillow==10.2.0```

  ```pip install python-magic-bin``` (voor Windows)

  In Windows:
  wanneer deze melding te zien is:

  ```WARNING: The script esphome.exe is installed in C:\Users\<username>\AppData\Local\Packages\PythonSoftwareFoundation.Python..3.12_...\LocalCache...```

  Voer dan uit:
  ```set PATH="%PATH%;C:\your\path\here\"```

  Vervang C:\your\path\here\ door het path in de warning: C:\Users\<username>\AppData\Local\Packages\PythonSoftwareFoundation.Python....

  Sluit het Opdrachtprompt en start een nieuw Opdrachtprompt.


Zorg ervoor dat er genoeg rechten zijn om van het USB apparaat:
===============================================================

  Voor Linux:

  ```sudo usermod -a -G dialout [gebruikersnaam]```

  vervang: [gebruikersnaam] met jouw systeem gebruikersnaam.

  Restart jouw computer of log opnieuw in om deze rechten te effectueren.

Verbind met de kabeltjes van het ESP32 development board met het display:
=========================================================================

  SDA -> D13

  SCL -> D14

  DC -> D19

  BLK -> D21 (optioneel)

  RES -> D23

  GND -> GND (pin boven 3.3V)

  3V3 -> 3.3V (pin rechtsonder)


.. image:: figs/pinouth.png

Verbind de USB kabel met het ESP32 board.
=========================================

Het rode lampje moet branden.

In de USB devices controleer het USB apparaat
=============================================

In Linux:
  ```ls /dev/ttyU* -la```

meestal staat er een nieuw USB device genaamd: ttyUSB01 of ttyUSB02 bij.

Voer uit:
=========

  ```git clone https://gitlab.com/rwsdatalab/public/codebase/tools/displayrws.git```

  ````cd displayrws```

Voer uit:
=========

  ```esphome run spi-display-image.yaml```

  Wanneer wordt gevraagd hoe te verbinden met het de ESP32 selecteer dan het USB apparaat bijv. /dev/USB01
  In Windows heet dit apparaat COM4.

  Nadat het flashen van de chip klaar is verschijnt er een blauwe vierkant met de tekst: RWS Datalab.

  Maak bijv. een cirkel.

  Gebruik deze handleiding:
  https://esphome.io/components/display/index.html

#################
Handleiding ESP32
#################

https://joy-it.net/files/files/Produkte/SBC-NodeMCU-ESP32/SBC-NodeMCU-ESP32-Manual-2021-06-29.pdf


.. end-inclusion-intro-marker-do-not-remove



.. begin-inclusion-license-marker-do-not-remove


License
=======

Copyright (c) 2024, Rijkswaterstaat


This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


.. end-inclusion-license-marker-do-not-remove
