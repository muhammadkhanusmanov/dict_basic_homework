def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    a=1000
    for j,i in people.items():
        if i>a:
            a=i
            b=j
    return j