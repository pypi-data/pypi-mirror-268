import os.path
import sys

import hebill

'''tyre = hebill.tyre.Tyre('520/85R24|20.5-25')
print(f'---------{tyre.size}---------')
for name, value in tyre.items():
    print(name, value)
print(f'---------{tyre.primary.size}---------')
for name, value in tyre.primary.items():
    print(name, value)
print(f'---------{tyre.secondary.size}---------')
for name, value in tyre.secondary.items():
    print(name, value)'''

sizes = {
    '40.00-57': ({
                     'diameter': 3590,
                     'section_width': 1075,
                     'non_skid_depth': 60,
                     'rim_width': 737.6,
                 }, {
                     'diameter': 3730,
                     'height': 1251,
                     'upper_inner_diameter': 1345,
                     'lower_inner_diameter': 1190,
                 }),
}
'''    '27.00-49': {

    }, '25.5-25': {

    }, '17.5-25': {

    }, '12.00-24': {

    }, '10.00-20': {

    }, '7.50-16': {

    }'''

for size, (tyre_dims, mould_dims) in sizes.items():
    tyre_mould = hebill.mould.TyreMould2PS(hebill.tyre.Tyre(size, tyre_dims), mould_dims)

    print(f'实际重量计算：{round(tyre_mould.weight(0, 7.8) / 1000000, 2)}')
    print(f'标准重量计算：{round(tyre_mould.primary_weight(0, 7.8) / 1000000, 2)}')
