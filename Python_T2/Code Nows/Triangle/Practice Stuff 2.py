from IrvingPerez_triangle import *
class triangle(object):
    """
    Our basic test class
    """

    def test___validate(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        angleA = 60
        angleB = 60
        angleC = 60
        
        if sum(self.__angleA, self.__angleB, self.__angleC) == 180:
            return True
        else:   
            return False

    def __str__( self ):
        """
        Return a string (the representation of a Triangle).
        """
        s = ""
        s += "   /\ \n"
        s +="   /  \ \n"       
        s +="  /    \ \n"
        s +="  _______ "
        print s
        return s
        

#if __name__ == '__main__':
#   unittest.main()