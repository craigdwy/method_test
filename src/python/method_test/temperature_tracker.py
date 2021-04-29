# No Shebang line. This file is meant to be imported
import numbers
import statistics  # Python 3.4 +


class TempTracker(object):
    """ Tracks temperature and records max, min and mean values"""
    # Temperature constants
    MIN_ALLOWED_TEMPERATURE = 0
    MAX_ALLOWED_TEMPERATURE = 110

    def __init__(self):
        self.max_temperature = 0
        self.min_temperature = 0
        self.mean_temperature = 0.0
        self.temperature_list = []

    def insert(self, input_temperature):
        """
        Takes an input temperature in the range of 0-110 and sets the min, max value
        :param input_temperature: int value in Fahrenheit
        :return: None
        """
        if not isinstance(input_temperature, numbers.Number):
            raise TypeError("Temperature Input needs to be numeric")

        # Check if within allowed range and
        if self.MIN_ALLOWED_TEMPERATURE <= input_temperature <= self.MAX_ALLOWED_TEMPERATURE:
            self.temperature_list.append(int(input_temperature))
            self.min_temperature = min(self.temperature_list)
            self.max_temperature = max(self.temperature_list)
            self.mean_temperature = statistics.mean(self.temperature_list)
            inserted = True
        else:
            inserted = False
            print(
                "Allowed temperature range {0} - {1} F".format(
                    self.MIN_ALLOWED_TEMPERATURE, self.MAX_ALLOWED_TEMPERATURE
                )
            )

        return inserted

    def calculate_mean(self):
        """
        Alternate method for python < 3.4 without the statistics module
        :return: float mean temperature value
        """
        try:
            # Casting float for python 2.7
            self.mean_temperature = sum(self.temperature_list)/float(len(self.temperature_list))
        except ZeroDivisionError:
            print("No temperature values recorded")
            self.mean_temperature = 0.0
        return self.mean_temperature

    def get_min(self):
        """
        Get's the minimum temperature
        :return: int min_temperature
        """
        return self.min_temperature

    def get_max(self):
        """
        Get's the maximum temperature
        :return: int max_temperature
        """
        return self.max_temperature

    def get_mean(self):
        """
        Get mean temperature
        :return: float mean temperature
        """
        return self.mean_temperature
