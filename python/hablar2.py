#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# prueba de accesible_output2 en python 3.x

import accessible_output2.outputs.auto
from time import sleep

engine = accessible_output2.outputs.auto.Auto()

print("mensaje que se imprime en consola")

sleep(0.1)

engine.speak("hola, este mensaje sera leído por un lector de pantalla.", True)
engine.speak("El string es transformado a voz.", False)
