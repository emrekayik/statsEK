x = [9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7,4,12,5,4,10,9,6,9,4]

def ortalamaBul(dizi):
    veriAdedi = len(dizi)
    if veriAdedi <= 1:
        return dizi
    else:
        return sum(dizi) / veriAdedi

def medyanBul(dizi):
    dizi = sorted(dizi)
    veriAdedi = len(dizi)
    if veriAdedi % 2 == 1:
        return dizi[veriAdedi // 2]
    else:
        i = veriAdedi // 2
        return (dizi[i - 1] + dizi[i]) / 2

def standartSapmaBul(dizi):
    sd = 0.0 # standart sapma
    veriAdedi = len(dizi)
    if veriAdedi <= 1:
        return 0.0
    else:
        for _ in dizi:
            sd += (float(_) - ortalamaBul(dizi)) ** 2
        sd = (sd / float(veriAdedi)) ** 0.5
        return sd

def varyansBul(dizi):
     return standartSapmaBul(dizi) ** 2

def modBul(dizi):
    dizi = sorted(dizi)
    veriAdedi = len(dizi)
    mod = []
    for i in range(veriAdedi):
        if dizi.count(dizi[i]) > 1:
            if dizi[i] not in mod:
                mod.append(dizi[i])
    return mod

def minBul(dizi):
    return min(dizi)

def maxBul(dizi):
    return max(dizi)


print("Ortalama: ", ortalamaBul(x))
print("Medyan: ", medyanBul(x))
print("Standart Sapma: ", standartSapmaBul(x))
print("Varyans: ", varyansBul(x))
print("Mod: ", modBul(x))
print("Min: ", minBul(x))
print("Max: ", maxBul(x))
