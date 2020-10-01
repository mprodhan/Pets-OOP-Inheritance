Although this looks like the extended version of Cat_OOP, it is unique in the regards that
this is a full example of Python Object Orinted Programing, where we are introduced to the 
concept of a parent class that is acts as a class that will create sub class or child class.
The child class are inherited from the parent class Cat, which is the concept of class
inheritance that is also unique to this program. 

We begin this program with a constructor class Pets(). This class initialized an empty list,
so that inherited instantiation of the class Cat is passed onto Pets. Then the parent class Cat
is created, to create its own values, mimicing the pets class. However, note that there are
differences, such as animals list is initialized in Pets and that animals is passed as an attribute
for pets, whereas, for cats, a boolean is passed as class object. To clarify, both animals list and 
boolean are respective class objects. Both Pets and Cat also have their unique functions, however,
they tie from the constructor to the parent class. 

Once the parent class has been created, then the parent class gets passed as an argument to the 
inherited classes, such as Simon, Sally, Felix. This means that the class object and attributes get
passed onto the inherited class. This ensures that no code are repeating itself in the process, 
keeping in step with DRY! Once the inherited class are created then, the interesting part of data 
manipulation takes place.

The data are manipulated from the bottom up. This program creates a list for cats as my_cats variable.
What this is doing is that it is mimicing the animals list from teh constructor class Pets. my_cats
is lisiting the inherited class instantiation by listing the instances of those class in my_cats list.
Then the my_cats list gets passed onto my_pets list via Pets(my_cats), where my_cats is passed as an
argument, with the my_cats list in tact. This list is now passed onto the animals list on the consturctor
class Pets. The output is finally, called on my_pets.walk(), which actually prints the output from the
function on the parent class. The output is the name of the cats walking around. Notice that, it is coming
from class Cat, but that it needed to embed into animals, then go down from there. As confusing, as that
may sound, it is how the program is reading everything from the bottom up, to where the actual function then
lies with the parent class.