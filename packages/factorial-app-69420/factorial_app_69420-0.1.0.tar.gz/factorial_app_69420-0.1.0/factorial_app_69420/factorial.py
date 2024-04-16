def fact(n):
    """
   Tính giai thừa của một số nguyên dương n.
   Tham số:
   - n: Số nguyêndương.
   Trả về:
   - Giai thừa của n.
     """
    if n < 0:
        raise ValueError(" Factorial is not defined for negative numbers ")
    elif n == 1 or n == 0:
        return 1
    else: 
        return n * fact(n-1)
    
