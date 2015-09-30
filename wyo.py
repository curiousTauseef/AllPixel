from bibliopixel import LEDMatrix
from bibliopixel.drivers.serial_driver import DriverSerial, LEDTYPE, ChannelOrder
from BiblioPixelAnimations.matrix.bloom import Bloom
import bibliopixel.log as log
import time

log.setLogLevel(log.DEBUG)

NUM_LEDS_PER_STRIP = 16
NUM_STRIPS = 8

driver = DriverSerial(LEDTYPE.GENERIC, NUM_LEDS_PER_STRIP*NUM_STRIPS, dev="", c_order=ChannelOrder.RGB,  hardwareID = "16C0:0483")
led = LEDMatrix(driver, width=NUM_LEDS_PER_STRIP, height=NUM_STRIPS, serpentine=False, threadedUpdate=False, masterBrightness=255)
led.setMasterBrightness(32)
try:
    anim = Bloom(led, dir=True)
    anim.run(fps=10)
except:
    led.all_off()
    led.update()
    time.sleep(1)