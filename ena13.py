def calculate_ean13_checkdigit(ean):
    if len(ean) != 12 or not ean.isdigit():
        raise ValueError(f"{ean} geçerli bir 12 basamaklı EAN barkodu değil.")
    

    odd_sum = sum(int(ean[i]) for i in range(0, 12, 2))  
    even_sum = sum(int(ean[i]) for i in range(1, 12, 2))  
    
  
    total_sum = odd_sum + (even_sum * 3)
    
  
    checkdigit = (10 - (total_sum % 10)) % 10
    
    return checkdigit


ean_list = [
    "978020137962"
]


for ean in ean_list:
    try:
        checkdigit = calculate_ean13_checkdigit(ean)
        print(f"{ean} barkodunun checkdigit'i: {checkdigit}")
    except ValueError as e:
        print(e)
print("Done!!")
