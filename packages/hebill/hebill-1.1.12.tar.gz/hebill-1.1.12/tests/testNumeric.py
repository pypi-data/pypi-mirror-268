import hebill

bums = ['123.1', '123', '1,123.1', '1,123', '-1,123.1', '-1,123']

for bum in bums:
    Num = hebill.string.String(bum)
    print(Num.digitize())
