def find_missing(sequence):
    maxelm = None
    prevelm = None
    for elm in sequence:
        if prevelm == None:
            prevelm = int(elm)
        else:
            elm = int(elm)
            sum1 = elm - prevelm
            if maxelm == None:
                maxelm = sum1
            elif sum1 >=0:
                if sum1 < maxelm:
                    maxelm = sum1
            else:
                if sum1 > maxelm:
                    maxelm = sum1

            prevelm = elm
    prevelm = None
    
    for elm in sequence:
        elm = int(elm)
        if prevelm == None:
            prevelm = elm
        else:
            sum1 = elm - prevelm
            if sum1 != maxelm:
                return prevelm + maxelm
            else:
                prevelm = elm