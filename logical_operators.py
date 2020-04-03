high_income = False
good_credit = False
criminal_record = True

if high_income or good_credit :
    print("Eligible for loan")



# AND  - both conditions should be true
# OR   - any one should be true
# NOT -  inverses the value

if good_credit and not criminal_record :
    print("Eligible for loan")

