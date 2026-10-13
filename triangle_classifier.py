def triangle_type(a, b, c):
    sides = (a, b, c)
    if any(not isinstance(x, int) or isinstance(x, bool) for x in sides):
        return "Invalid"

    if any(x < 1 or x > 200 for x in sides):
        return "Invalid"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"

    
    if a == b == c:
        return "Equilateral"
    
    if a == b or b == c or a == c:
        return "Isosceles"
    return "Scalene"