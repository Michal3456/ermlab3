class AddSpace():
    @staticmethod
    def add_space(a: int) -> str:
        """Creating white characters dependent on ,,a''."""
        if a <= 9:
            string = "      "
        elif a <= 99:
            string = "     "
        elif a <= 999:
            string = "    "
        elif a <= 9999:
            string = "   "
        elif a <= 99999:
            string = "  "
        elif a <= 999999:
            string = "  "
        elif a <= 9999999:
            string = " "
        else:
            string = "  "
        return string
