from PACFunction import PACFunction


class TimeRange(PACFunction):
    earliest: int
    latest: int
    template_filename = "pac-function_time-range.template"

    def validate(self) -> bool:
        if (not isinstance(self.earliest, int) or
                self.earliest not in range(0, 24) or
                not isinstance(self.latest, int) or
                self.latest not in range(0, 24)):
            return False
        return True
