class Empolyee:

    def __init__( self ):
        print('employee created')

    def __del__(self):
       print("Destructor called")

def Create_obj( ):
    print('Making Object....')
    obj = Empolyee( )
    print('function end......')
    return obj

print('Calling Create_obj( ) function....')
obj = Create_obj( )
print('Program End...')
del obj 