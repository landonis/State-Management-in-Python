#import classes and methods
#create the concrete state objects
#create the context object
#have the context iterate through all the states and methods

#import classes and methods
import file_context
#

#create the concrete state objects
func_A = file_context.Concrete_State_A()
func_B = file_context.Concrete_State_B(1)
func_B_2 = file_context.Concrete_State_B(10)

itr = (func_A, func_B, func_B_2)
#

#create the context object
context = file_context.Context(func_A)
#

#have the context iterate through all the states and methods
for obj in itr:
    context.transition_to(obj)
    context.hello()
    context.say('this is a string')
    print(f"My integer value is {context.get_integer_attribute()}")
#