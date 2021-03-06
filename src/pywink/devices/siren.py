from pywink.devices.base import WinkDevice


class WinkSiren(WinkDevice):
    """
    Represents a Wink Siren.
    """

    def state(self):
        return self._last_reading.get('powered', False)

    def mode(self):
        return self._last_reading.get('mode', None)

    def siren_volume(self):
        return self._last_reading.get('siren_volume', None)

    def chime_volume(self):
        return self._last_reading.get('chime_volume', None)

    def auto_shutoff(self):
        return self._last_reading.get('auto_shutoff', None)

    def strobe_enabled(self):
        return self._last_reading.get('strobe_enabled', None)

    def chime_strobe_enabled(self):
        return self._last_reading.get('chime_strobe_enabled', None)

    def siren_sound(self):
        return self._last_reading.get('siren_sound', None)

    def chime_mode(self):
        return self._last_reading.get('activate_chime', None)

    def chime_cycles(self):
        return self._last_reading.get('chime_cycles', None)

    def set_siren_volume(self, volume):
        """
        :param volume: one of [low, medium, high]
        """
        values = {
            "desired_state": {
                "siren_volume": volume
            }
        }
        response = self.api_interface.set_device_state(self, values)
        self._update_state_from_response(response)

    def set_chime_volume(self, volume):
        """
        :param volume: one of [low, medium, high]
        """
        values = {
            "desired_state": {
                "chime_volume": volume
            }
        }
        response = self.api_interface.set_device_state(self, values)
        self._update_state_from_response(response)

    def set_mode(self, mode):
        """
        :param mode:  a str, one of [siren_only, strobe_only, siren_and_strobe]
        :return: nothing
        """
        values = {
            "desired_state": {
                "mode": mode
            }
        }
        response = self.api_interface.set_device_state(self, values)
        self._update_state_from_response(response)

    def set_siren_strobe_enabled(self, enabled):
        """
        :param enabled:  True or False
        :return: nothing
        """
        values = {
            "desired_state": {
                "strobe_enabled": enabled
            }
        }
        response = self.api_interface.set_device_state(self, values)
        self._update_state_from_response(response)

    def set_chime_strobe_enabled(self, enabled):
        """
        :param enabled:  True or False
        :return: nothing
        """
        values = {
            "desired_state": {
                "chime_strobe_enabled": enabled
            }
        }
        response = self.api_interface.set_device_state(self, values)
        self._update_state_from_response(response)

    def set_siren_sound(self, sound):
        """
        :param sound: a str, one of ["doorbell", "fur_elise", "doorbell_extended", "alert",
                                     "william_tell", "rondo_alla_turca", "police_siren",
                                     ""evacuation", "beep_beep", "beep"]
        :return: nothing
        """
        values = {
            "desired_state": {
                "siren_sound": sound
            }
        }
        response = self.api_interface.set_device_state(self, values)
        self._update_state_from_response(response)

    def set_chime(self, sound, cycles=None):
        """
        :param sound: a str, one of ["doorbell", "fur_elise", "doorbell_extended", "alert",
                                     "william_tell", "rondo_alla_turca", "police_siren",
                                     ""evacuation", "beep_beep", "beep", "inactive"]
        :param cycles: Undocumented seems to have no effect?
        :return: nothing
        """
        desired_state = {"activate_chime": sound}
        if cycles is not None:
            desired_state.update({"chime_cycles": cycles})
        response = self.api_interface.set_device_state(self,
                                                       {"desired_state": desired_state})
        self._update_state_from_response(response)

    def set_auto_shutoff(self, timer):
        """
        :param timer: an int, one of [None (never), -1, 30, 60, 120]
        :return: nothing
        """
        values = {
            "desired_state": {
                "auto_shutoff": timer
            }
        }
        response = self.api_interface.set_device_state(self, values)
        self._update_state_from_response(response)

    def update_state(self):
        """
        Update state with latest info from Wink API.
        """
        response = self.api_interface.get_device_state(self)
        return self._update_state_from_response(response)

    def set_state(self, state):
        """
        :param state:   a boolean of true (on) or false ('off')
        :return: nothing
        """
        values = {"desired_state": {"powered": state}}
        response = self.api_interface.set_device_state(self, values)
        self._update_state_from_response(response)
