i1=i2=i3=i4=i5=zongshu=1
while i5:
    i4 = i5*5 / 4
    if i4.is_integer():
        i3=(i4*5++4)/4
        if i3.is_integer():
            i2=(i3*5+3)/4
            if i2.is_integer():
                i1=(i2*5+2)/4
                if i1.is_integer():
                    print(i1*5+1)
                    break
    i5+=1