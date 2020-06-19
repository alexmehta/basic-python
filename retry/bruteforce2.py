
from itertools import product


def findPassword(chars, function, show=50, format_="%s"):
    password = None
    attempts = 0
    size = 1
    stop = False

    while not stop:

        for pw in product( chars, repeat=size ):

            password = "".join( pw )

            if attempts % show == 0:
                print( format_ % password )

            if function( password ):
                stop = True
                break
            else:
                attempts += 1
        size += 1

    return password, attempts


def getChars():

    chars = []


    for id_ in range( ord( "A" ), ord( "Z" ) + 1 ):
        chars.append( chr( id_ ) )

    for id_ in range( ord( "a" ), ord( "z" ) + 1 ):
        chars.append( chr( id_ ) )


    for number in range( 10 ):
        chars.append( str( number ) )

    return chars


if __name__ == "__main__":

    import datetime
    import time


    pw = input( "\n Type a password: " )
    print( "\n" )


    def testFunction(password):
        global pw
        if password == pw:
            return True
        else:
            return False



    chars = getChars()

    t = time.process_time()


    password, attempts = findPassword( chars, testFunction, show=3999, format_=" Trying %s" )

    t = datetime.timedelta( seconds=int( time.process_time() - t ) )
    input( "\n\n Password found: {}\n Attempts: {}\n Time: {}\n".format( password, attempts, t ) )
