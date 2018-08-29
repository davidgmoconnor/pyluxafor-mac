from pyluxafor import LuxaforFlag
from time import sleep

import codes as c

flag = LuxaforFlag()
flag.off()
flag.fade_colour(
    leds=[c.LED_TAB_1, c.LED_BACK_1, c.LED_BACK_2],
    r=10, g=10, b=0,
    duration=255
)
flag.static_colour(leds=c.LED_BACK_3, r=0, g=0, b=100)

sleep(3)
flag.off()

flag.pattern(c.PATTERN_POLICE, 3)
