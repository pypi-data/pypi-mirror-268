SIZE_PATTERN = r'[0-9a-zA-Z/|().\[\]\-*]+'
SIZE_SYMBOLS = [
    ['/', '-'],
    ['/', 'R'],
    ['/', 'D'],
    ['-', None],
    ['X', None],
    ['X', 'X'],
    ['X', '-'],
    ['X', 'D'],
]
SIZE_MIN_ASPECT_RATIO = 30
SIZE_MAX_ASPECT_RATIO = 105
SIZE_MAX_RIM_SIZE_INCH = 70
SIZE_MAX_SECTION_WIDTH_INCH = 70
# 最大印制直径
# 目前参考 65/65-65
SIZE_MAX_DIAMETER_INCH = 65
RATIO_RW_TO_SW = .8
RATIO_NSD_TO_SW = .07
SIZE_DEFAULT_ASPECT_RATIO = .95
SIZE_DEFAULT_ASPECT_RATIOS = {
    "5.00-8": 100,
    "5.50-16": 110,
    "10-16.5": 70,
    "11L-16": 70,
    "11.2-24": 95,
    "11.2-28": 95,
    "12-16.5": 70,
    "12.4-28": 95,
    "13.6-24": 90,
    "13.6-28": 95,
    "14.9-24": 90,
    "14.9-28": 95,
    "16.9-24": 90,
    "16.9-28": 95,
    '18.4/15-30': 89,
    "19.5-24": 70,
    "37.25-35": 80,
    "40.00-57": 100,
    "165R16": 75,
    "175R16": 75,
}
