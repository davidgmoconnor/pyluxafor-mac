from pyluxafor import LuxaforFlag
from time import sleep

flag = LuxaforFlag()
flag.off()
flag.fade_colour(
    leds=[LuxaforFlag.LED_TAB_1, LuxaforFlag.LED_BACK_1, LuxaforFlag.LED_BACK_2],
    r=10, g=10, b=0,
    duration=255
)
flag.static_colour(leds=LuxaforFlag.LED_BACK_3, r=0, g=0, b=100)

sleep(3)
flag.off()

flag.pattern(LuxaforFlag.PATTERN_POLICE, 3)