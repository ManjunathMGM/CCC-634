i_ishan = int(input("Enter Ishan's Income"))
i_hari = int(input("Enter Hari's Income"))
i_charu = int(input("Enter Charu's Income"))
i_william = int(input("Enter William's Income"))

com1 = i_ishan + i_hari < i_charu + i_william
com2 = i_ishan + i_hari == i_charu + i_william
com3 = i_ishan + i_hari > i_charu + i_william

print(f"1. {com1} \n2. {com2} \n3. {com3}")
