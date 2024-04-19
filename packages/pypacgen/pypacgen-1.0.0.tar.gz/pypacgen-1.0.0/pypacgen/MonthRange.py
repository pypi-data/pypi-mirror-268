from PACFunction import PACFunction


class MonthRange(PACFunction):
    earliest: str
    latest: str
    template_filename = "pac-function_month-range.template"

    def validate(self) -> bool:
        months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
        if self.earliest not in months or self.latest not in months:
            return False
        return True
