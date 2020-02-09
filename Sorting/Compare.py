def less( element1, element2):
        if float(element1['vote_average']) <  float(element2['vote_average']):
            return True
        return False

def greater( element1, element2):
        if float(element1['vote_average']) >  float(element2['vote_average']):
            return True
        return False

