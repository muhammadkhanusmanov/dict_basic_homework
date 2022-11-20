def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    i=0
    a=0
    for j in list(txt):
        if j.isalpha():
            i+=1
        elif j.isdigit():
            a+=1 
    return {"LETTERS": i, "DIGITS": a}
