
# https://docs.djangoproject.com/en/4.2/topics/http/urls/#registering-custom-path-converters
class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return f"{value:04d}"