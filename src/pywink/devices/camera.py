from pywink.devices.base import WinkDevice


class WinkCamera(WinkDevice):
    """
    Represents a Wink camera.
    """

    def __init__(self, device_state_as_json, api_interface):
        super(WinkCamera, self).__init__(device_state_as_json, api_interface)

    def state(self):
        return self.mode()

    def mode(self):
        return self._last_reading.get('mode')

    def private(self):
        return self._last_reading.get('private')

    def set_mode(self, mode):
        """
        :param mode:  a str, one of [armed, disarmed, privacy]
        :return: nothing
        """
        values = {"desired_state": {"mode": mode}}
        response = self.api_interface.set_device_state(self, values)
        self._update_state_from_response(response)

    def set_privacy(self, state):
        """
        :param state: True or False
        :return: nothing
        """
        values = {"desired_state": {"private": state}}
        response = self.api_interface.set_device_state(self, values)
        self._update_state_from_response(response)
