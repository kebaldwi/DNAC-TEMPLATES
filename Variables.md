### Variables
Variables are used to allow scripts or code for that matter to be reused. A variable within a script allows us to replace the data on demand thereby allowing the reuse of parts of or entire templates. Variables may be defined in a couple of ways but the data entered will either numerical or string. A numerical value is just that a number where as a string is either a line of text or perhaps just a name.

``` 
    Variable reference:     #set( $monkey = $bill )
    String literal:         #set( $monkey.Friend = 'monica' )
    Property reference:     #set( $monkey.Blame = $whitehouse.Leak )
    Method reference:       #set( $monkey.Plan = $spindoctor.weave($web) )
    Number literal:         #set( $monkey.Number = 123 )
    Range operator:         #set( $monkey.Numbers = [1..3] )
    Object list:            #set( $monkey.Say = ["Not", $my, "fault"] )
    Object map:             #set( $monkey.Map = {"banana" : "good", "roast beef" : "bad"})
```

#### Variable Notation
The Notation used in variables is as follows: 

   $[{]identifier.identifier[|alternate value][}]

Usage:
   * identifier: variable name
   * alternate value: alternate expression to use if the property is null, empty, false or zero

Types of Notation:

```
    $[{]identifier.identifier([ parameter list... ])[|alternate value][}]
    
    Formal Notation.        ${Switch} 
    Regular Notation:       $Switch
    Alternate Value:        ${Switch.name|'ASW-C9300-ACCESS'}
```

Data may be set to the variables via a set command

```
#set( $StringVariable = "text" )
#set( $NumericVariable = 10 )
```

#### Arrays: 
It is possible to create arrays as well which can be iterated through with Foreach loop constructs. In Velocity we call an array a list. You can set a list up in two ways:

* Define all the elements of the list in one line comma delimited 
* Define each element of the list with an identifier

Both examples follow:
```
#set( $L2Bgps = ["10" , "18"] )
```

```
#set( $L2Bgps[0] = 10 )
#set( $L2Bgps[1] = 18 )
```

Additional set commands available are the following:

```
    Variable reference:    #set( $monkey = $bill )
    String literal:        #set( $monkey.Friend = 'monica' )
    Property reference:    #set( $monkey.Blame = $whitehouse.Leak )
    Method reference:      #set( $monkey.Plan = $spindoctor.weave($web) )
    Number literal:        #set( $monkey.Number = 123 )
    Range operator:        #set( $monkey.Numbers = [1..3] )
    Object list:           #set( $monkey.Say = ["Not", $my, "fault"] )
    Object map:            #set( $monkey.Map = {"banana" : "good", "roast beef" : "bad"})
```

Simple arithmetic expressions can be accomplished as follows:

```
    Addition:       #set( $answer = $number + 1 )
    Subtraction:    #set( $answer = $number - 1 )
    Multiplication: #set( $answer = $number * $mod )
    Division:       #set( $answer = $number / $mod )
    Remainder:      #set( $answer = $number % $mod )

    where $number = 10 and $mod = 2 the answers from above would be for:
    
    Addition:       $answer = 11
    Subtraction:    $answer = 9
    Multiplication: $answer = 20
    Division:       $answer = 5
    Remainder:      $answer = 0
```

#### DNA Center & Working with Variables
As with anything DNA Center the UI allows for flexibility and the ability to not only further define how the Variables are populated but how they are used during the provisioning workflows. 

Once Variables have been scripted within the Template, You can click on the **form editor button** *(middle icon)* at the top right of the template form.

![json](images/TemplateEditor.png?raw=true "Import JSON")

Within the input form 

or alternatively using the UI in DNAC which allows for user interaction during the provisioning process.

![json](images/variable-type.png?raw=true "Import JSON")


Special mention to: https://explore.cisco.com/dnac-use-cases/apache-velocity as examples and extrapolations were made using this documentation.
