from django.urls import register_converter


class YearConverter:
    regex = r"20\d{2}"


    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


register_converter(YearConverter, 'year')