def less( self, element1, element2):
        if int(element1['vote_count']) <  int(element2['vote_count']):
            return True
        return False

def greater( self, element1, element2):
        if int(element1['vote_average']) >  int(element2['vote_average']):
            return True
        return False

