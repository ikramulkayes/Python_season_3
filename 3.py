def func(lst):
    dic1 = {}
    for elm in lst:
        year = "20"+ elm[:2]
        deptcode = elm[3:5]
        if deptcode == "01":
            dept = "CSE"
        elif deptcode == "21":
            dept = "EEE"
        elif deptcode == "41":
            dept = "CS"
        else:
            dept = "Other"
        if year not in dic1.keys():
            dic1[year] = {dept:[elm]}
        else:
            if dept not in dic1[year].keys():
                dic1[year][dept] =[elm]
            else:
                dic1[year][dept].append(elm)
    return dic1
print(func(['20201199','21121347','20141052','20341121','21241369','21272199','19241187','19101007','20101035', '21121875', '19141534', '19301552', '21141135', '21365001']))

