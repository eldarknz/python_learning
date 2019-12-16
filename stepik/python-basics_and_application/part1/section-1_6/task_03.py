# https://stepik.org/lesson/24462/step/9?unit=6768

class LoggableList(list, Loggable):
    def append(self, item):
        super().append(item)
        super().log(item)
