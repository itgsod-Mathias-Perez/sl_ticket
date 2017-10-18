def fares(age, adult=False, student=False,gubbe=False):
    if age>=20 and age <65:
        if adult==True:
            return "20kr"


        elif student==True or gubbe==True:
             return "15kr"

        elif age>=20 and age <=65:
         return 'Adult pays 20 corwns'
    else:
        return 'Student or old people pays 15 crowns'


print fares(78)
print fares(20)
print fares(65)
print fares(18)










