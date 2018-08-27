# -*- coding: utf-8 -*-
import hid

import codes as c


class LuxaforFlag(object):

    def __init__(self):
        self.device = None

    def off(self):
        """
        Turn off all LEDs.
        """
        self.static_colour(c.LED_ALL, 0, 0, 0)

    def static_colour(self, leds, r, g, b):
        """
        Set a single LED or multiple LEDs immediately to the specified colour.
        """
        self._do_multi_led_command(
            self.create_static_colour_command, leds, r, g, b
        )

    def fade_colour(self, leds, r, g, b, duration):
        """
        Fade a single LED or multiple LEDs from their current colour to a new
        colour over the supplied duration.
        """
        self._do_multi_led_command(
            self.create_fade_colour_command, leds, r, g, b, duration
        )

    def strobe(self, led, r, g, b, duration, repeat):
        """
        Flash the specified LED a specific colour, giving the duration of each
        flash and the number of times to repeat.
        """
        command = self.create_strobe_command(led, r, g, b, duration, repeat)
        self._write(command)

    def wave(self, wave_type, r, g, b, duration, repeat):
        """
        Animate the flag with a wave pattern of the given type, using the
        specified colour, duration and number of times to repeat.
        """
        command = self.create_wave_command(
            wave_type, r, g, b, duration, repeat
        )
        self._write(command)

    def pattern(self, pattern, repeat):
        """
        Execute a built in pattern a given number of times.
        """
        command = self.create_pattern_command(pattern, repeat)
        self._write(command)

    """
    
    Command functions: turn commands into byte arrays for sending to device

    """

    def create_static_colour_command(self, led, r, g, b):
        return [c.MODE_STATIC_COLOUR, led, r, g, b]

    def create_fade_colour_command(self, led, r, g, b, duration=20):
        return [c.MODE_FADE_COLOUR, led, r, g, b, duration]

    def create_strobe_command(self, led, r, g, b, duration=20, repeat=2):
        return [c.MODE_STROBE, led, r, g, b, duration, 0, repeat]

    def create_wave_command(self, wave_type, r, g, b, duration=20, repeat=1):
        return [c.MODE_WAVE, wave_type, r, g, b, duration, 0, repeat]

    def create_pattern_command(self, pattern_id, repeat=1):
        return [c.MODE_PATTERN, pattern_id, repeat]

    """
    
    Device interactions

    """

    def _get_device(self):
        """
        Retrieve a HID device for the Luxafor Flag.
        """
        if not self.device:
            h = hid.device()
            h.open(c.DEVICE_VENDOR_ID, c.DEVICE_PRODUCT_ID)
            h.set_nonblocking(1)
            self.device = h
        return self.device

    def _write(self, values):
        """
        Send values to the device. (Not intended for direct use)
        """
        self._get_device().write(values)

    def _do_multi_led_command(
        self, create_command_function, leds, *args, **kwargs
    ):
        try:
            iter(leds)
        except TypeError:
            command = create_command_function(leds, *args, **kwargs)
            self._write(command)
        else:
            for led in leds:
                command = create_command_function(led, *args, **kwargs)
                self._write(command)