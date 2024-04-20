import hebill

bums = ['123.1', '123', '1,123.1', '1,123', 123, 123.1]

for bum in bums:
    Num = hebill.numeric.Numeric(bum)
    print(f'O->原始字串：{Num.input}')
    print(f'R->转化数字：{Num.capitalize_cn_num}')
