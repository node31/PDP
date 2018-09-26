**FACADE PATTERN**
This pattern is used to simplify the system which is underneath.
Facade pattern has complete knowledge of the the lower system and it has most of the objects for that.
It also has actual intelligence built in. 

Thus, generally facade patterns are not simple wrappers. They have intelligence of order of operations.


People often misunderstand SingleAdaptorForMultipleInterfaces as FacadePattern because they look similar.
Indeed, they are similar looking but are extremely different. 
           
They are different in intent.
Facade patterns are present to simplify the underlying subsystem interfaces. They are used to achieve loose coupling and
principle of lease knowledge(LAW of DEMETER) i.e. the client should not have much knowledge about the systems underneath
Adaptor patterns are used to convert one kind of interface to other.
Facade patterns are used to simplify the interfaces.