import RPi.GPIO as GPIO


class Door:
    def __init__(self, door_pin: int, buzzer_pin: int):
        """Door class.

        Implements a door object, which opens and closes a door via a servo motor.


        Args:
            door_pin (int): The door pin.
            buzzer_pin (int): the buzzer pin.
        """
        self.door_pin = door_pin
        self.buzzer_pin = buzzer_pin

        def open(self, duration: int):
            """Opens the door.

            Args:
                duration (int): The duration of the door opening.
            """
            pass

        def close(self, duration: int):
            """Closes the door.

            Args:
                duration (int): The duration of the door closing. Use 0 for infinite duration.
            """
            pass

        def buzz(self, duration: int):
            """Buzzes the buzzer.

            Args:
                duration (int): The duration of the buzzer buzzing.
            """
            pass