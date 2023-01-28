def digit(num,digit):
    out = str(round(num/10**digit))
    if len(out)<2:
        return str(round(float(num/10**digit),1))
    else:
        return str(round(float(num/10**digit)))

sub = int(input())
if sub>= 10**9:
    print(digit(sub,9)+'B')
elif sub>= 10**6:
    print(digit(sub,6)+'M')
elif sub>= 10**3:
    print(digit(sub,3)+'K')
else:
    print(sub)