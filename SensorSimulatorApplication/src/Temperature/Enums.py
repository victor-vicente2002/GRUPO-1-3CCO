from enum import Enum

class Ocean(Enum):
    PACIFIC = 'PACIFIC'
    ATLANTIC = 'ATLANTIC'
    INDIAN = 'INDIAN'
    ARCTIC = 'ARCTIC'
    SOUTHERN = 'SOUTHERN'

class Unit(Enum):
    Fahrenheit= '°F'
    Celsius = 'C°'
    Kelvin = 'K'
    Rankine = '°R'
    Newton = 'N'
    
class DateFormat(Enum):
    DMY = '%d/%m/%Y %H:%M:%S'
    YMD	 = '%Y/%m/%d %H:%M:%S'
    MDY = '%m/%d/%Y %H:%M:%S'