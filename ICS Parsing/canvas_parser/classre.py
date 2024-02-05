import re
from exceptions import ParseException


def parse_class(name: str) -> str:
    """Parses Canvas ICS event name|description for class title AT END OF STRING
     Example:
     'Review your Presentation #3 | Career Options [SP24-BL-INFO-I301-8506]'
         Returns:
    'INFO-I301'

     Args:
         name (str): event name

     Raises:
         NoParseException: Thrown if name does not contain output for pattern.

     Returns:
         str: Class Code within Input String
    """

    # Example Class Name
    # [SP24-BL-INFO-I301-8506]
    # Pattern Grabs 'INFO-I301'
    pattern = r"\[\w+-\w+-(\w+-\w+)-\d+\]$"

    class_code_match = re.search(pattern, name)
    if class_code_match:
        class_code = class_code_match.group(1)
        return class_code
    else:
        raise ParseException("No Class Code Found")


if __name__ == "__main__":
    strings = [
        "Failure Case",
        "Garbage Information is right there [SP24-BL-INFO-I301-8506]",
    ]

    for string in strings:
        try:
            print(parse_class(string))
        except ParseException:
            print(f"Error Caught for String, '{string}'")
