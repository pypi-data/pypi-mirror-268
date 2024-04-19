from PACFunction import PACFunction


class WeekdayRange(PACFunction):
    earliest: str
    latest: str
    template_filename = "pac-function_weekday-range.template"

    def validate(self) -> bool:
        weekdays = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
        if self.earliest not in weekdays or self.latest not in weekdays:
            return False
        return True
