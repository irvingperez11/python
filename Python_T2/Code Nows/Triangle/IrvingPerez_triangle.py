import math

################################################################################
## Class Triangle
################################################################################

class Triangle( object ):
    
    def __init__( self, sideA=0.0, sideB=0.0, sideC=0.0,angleA=0.0, angleB=0.0, angleC=0.0 ):
        """
        Initialize an object of type Triangle.
        """
        
        self.__sideA = sideA
        self.__sideB = sideB
        self.__sideC = sideC
        self.__angleA = angleA
        self.__angleB = angleB
        self.__angleC = angleC
        self.__valid = False

        pass # REPLACE
    
    
    def __validate( self ):
        # Check the three sides to determine if a Triangle is valid.

      if sum(self.__sideA, self.__sideB, self.__sideC) == 180:
        return " it is a triangle"
      else:
        return " it isn't a triangle"
   
    def __repr__( self ):
        """
        Return a string (the representation of a Triangle).
        """
        s = ""
        s += "   /\ \n"
        s +="   /  \ \n"       
        s +="  /    \ \n"
        s +="  _______ "
        return s

    def __str__( self ):
        """
        Return a string (the representation of a Triangle).
        """
        s = ""
        s += "   /\ \n"
        s +="   /  \ \n"       
        s +="  /    \ \n"
        s +="  _______ "
        return s
        print "sideA", self.__sideA,"sideB", self.__sideB, "sideC", self.__sideC 
        

    def is_valid( self ):
        """
        Return a Boolean (is the Triangle valid?).
        """
        if sum(self.__angleA, self.__angleB, self.__angleC) == 180:
            return True
        else:   
            return False
        #attempt at validation of the triangle

    def is_equilateral( self ):
        """
        Return a Boolean (is the Triangle an equilateral triangle?)
        """
        if self.__sideA == self.__sideB == self.__sideC: 
            return True
        else:
            return False
        #Boolean attempt for the equilateral triangle
        
    def is_isosceles( self ):
        """
        Return a Boolean (is the Triangle an isosceles triangle?)
        """
        if self.__sideA == self.__sideB or self.__sideA == self.__sideC or self.__sideB == self.__sideC:
            return True
        else:
            return False
        #Boolean attempt for the isosceles triangle

    def is_scalene( self ):
        """
        Return a Boolean (is the Triangle a scalene triangle?)
        """
        if self.__sideA != self.__sideB and self.__sideA != self.__sideC and self.__sideB != self.__sideC:
            return True
            
        else:
            return False
         #Boolean attempt for the scalene triangle   

    def sides( self ):
        """
        Return a tuple containing the Triangle's three sides.
        """
    
        tup1 = tuple(self.__sideA, self.__sideB, self.__sideC);
        return tup1
        #the attempt at tuple for the sides
    def angles( self ):
        """
        Return a tuple containing the Triangle's three angles (in degrees) 
        """
        tup2 = tuple(self.__angleA, self.__angleB, self.__angleC);
        return tup2
        
        #the attempt at the tuple for the angles

    def perimeter( self ):
        """
        Return a float representing the Triangle's perimeter.
        """
        print "self.__sideA + self.__sideB + self.__sideC =", float(sum(self.__sideA, self.__sideB, self.__sideC))
        #attempts to show the preimeter
        
    def area( self ):
        """
        Return a float representing the Triangle's area.
        """
    
        print "Area is", float(2*(self.__sideA/self.__sideB)*self.__sideB/2)
        #is showing the are
    def scale( self, factor=1.0 ):
        """
        Scale all three of a Triangle's sides by the same factor.
        """
        print sum(self.__sideA, self.__sideB, self.__sideC)*float(1.00)
        #multiplies it by the float to scale the sum
