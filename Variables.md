# Variables [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)
Variables are used to allow scripts or code for that matter to be reused. A variable within a script allows us to replace the data on demand thereby allowing the reuse of parts of or entire templates. Variables may be defined in a couple of ways but the data entered will either numerical or string. A numerical value is just that a number where as a string is either a line of text or perhaps just a name.

## Velocity Variables
In this section we will go into the various aspects of Velocity Variables and nomenclature.

```vtl
    Variable reference:     #set( $monkey = $bill )
    String literal:         #set( $monkey.Friend = 'monica' )
    Property reference:     #set( $monkey.Blame = $whitehouse.Leak )
    Method reference:       #set( $monkey.Plan = $spindoctor.weave($web) )
    Number literal:         #set( $monkey.Number = 123 )
    Range operator:         #set( $monkey.Numbers = [1..3] )
    Object list:            #set( $monkey.Say = ["Not", $my, "fault"] )
    Object map:             #set( $monkey.Map = {"banana" : "good", "roast beef" : "bad"})
```

### Variable Notation
The Notation used in variables is as follows: 

   $[{]identifier.identifier[|alternate value][}]

Usage:
   * identifier: variable name
   * alternate value: alternate expression to use if the property is null, empty, false or zero

Types of Notation:

```vtl
    $[{]identifier.identifier([ parameter list... ])[|alternate value][}]
    
    Formal Notation.        ${Switch} 
    Regular Notation:       $Switch
    Alternate Value:        ${Switch.name|'ASW-C9300-ACCESS'}
```

Data may be set to the variables via a set command

```vtl
#set( $StringVariable = "text" )
#set( $NumericVariable = 10 )
```

### Arrays (aka Ordered Lists): 
It is possible to create arrays as well which can be iterated through with Foreach loop constructs. In Velocity we call an array a list. You can set a list up in two ways:

* Define all the elements of the list in one line comma delimited 
* Define each element of the list with an identifier

Both examples follow:
```vtl
#set( $L2Bgps = ["10" , "18"] )
```

```vtl
#set( $L2Bgps = [] )
#set( $L2Bgps[0] = 10 )
#set( $L2Bgps[1] = 18 )
```

Additional set commands available are the following:

```vtl
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

```vtl
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

### Modifiers
With variables there are modifiers that can be used to do specific operations with regard to variables. Modifiers can be used to determine size, split, add or even replace data. Take a look at the following:


1. An example that splits a string result using on a specific character as a delimeter and fills an array $StackPIDs.
   ```vtl
   #set( $StackPIDs = $ProductID.split(",") )
   ```

2. This example determines the number of elements in an array.
   ```vtl
   #set( $StackMemberCount = $StackPIDs.size() )
   ```

3. This example uses a regular expression to reduce the PID of a switch to either 24 or 48 to reflect port count.
   ```vtl
   #set( $PortCount = $Model.replaceAll("C9300L?-([2|4][4|8]).*","$1") )
   ```

4. This last example adds the value of $PortCount as a new element appending it within the array $PortTotal
   ```vtl
     #set( $foo = $PortTotal.add($PortCount) )
   ```

## Jinja2 Variables
In this section we will go into the various aspects of Jinja2 Variables and nomenclature as they are used on DNA Center for templating.

```j2
    Variable reference:     {% set( monkey = bill ) %}
    String literal:         {% set( monkey.Friend = 'monica' ) %}
    Property reference:     {% set( monkey.Blame = whitehouse.Leak ) %}
    Method reference:       {% set( monkey.Plan = spindoctor.weave($web) ) %}
    Number literal:         {% set( monkey.Number = 123 ) %}
    Range operator:         {% set( monkey.Numbers = [1..3] ) %}
    Object list:            {% set( monkey.Say = ["Not", $my, "fault"] ) %}
    Object map:             {% set( monkey.Map = {"banana" : "good", "roast beef" : "bad"}) %}
    Dictionary Object:      {% set Deployment_Codes =[{'port':'1/0/1','code':'S028'},{'port':'1/0/2','code':'S020'}]%}
```

### Variable Notation
The Notation used in variables is as follows: 

   [{{]identifier.attribute|modifier|['attribute'][}}]

It’s important to know that the outer double-curly braces are not part of the variable, but the print statement. If you access variables inside tags don’t put the braces around them.

Usage:
   * identifier: variable name
   * attribute value: attributes are variables within a variable creating a variable set if used

Types of Notation:

```vtl
    {{ identifier.attribute|modifier|['attribute'] }}
    
    Formal Notation.        {{ Switch }} 

```

Data may be set to the variables via a set command

```vtl
#set( $StringVariable = "text" )
#set( $NumericVariable = 10 )
```

### Arrays (aka Ordered Lists): 
It is possible to create arrays as well which can be iterated through with Foreach loop constructs. In Velocity we call an array a list. You can set a list up in two ways:

* Define all the elements of the list in one line comma delimited 
* Define each element of the list with an identifier

Both examples follow:
```vtl
#set( $L2Bgps = ["10" , "18"] )
```

```vtl
#set( $L2Bgps = [] )
#set( $L2Bgps[0] = 10 )
#set( $L2Bgps[1] = 18 )
```

Additional set commands available are the following:

```vtl
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

```vtl
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

### Modifiers
With variables there are modifiers that can be used to do specific operations with regard to variables. Modifiers can be used to determine size, split, add or even replace data. Take a look at the following:


1. An example that splits a string result using on a specific character as a delimeter and fills an array $StackPIDs.
   ```vtl
   #set( $StackPIDs = $ProductID.split(",") )
   ```

2. This example determines the number of elements in an array.
   ```vtl
   #set( $StackMemberCount = $StackPIDs.size() )
   ```

3. This example uses a regular expression to reduce the PID of a switch to either 24 or 48 to reflect port count.
   ```vtl
   #set( $PortCount = $Model.replaceAll("C9300L?-([2|4][4|8]).*","$1") )
   ```

4. This last example adds the value of $PortCount as a new element appending it within the array $PortTotal
   ```vtl
     #set( $foo = $PortTotal.add($PortCount) )
   ```


## DNA Center & Working with Variables
As with anything DNA Center the UI allows for flexibility and the ability to not only further define how the Variables are populated but how they are used during the provisioning workflows. 

![json](images/TemplateEditor.png?raw=true "Import JSON")

Once Variables have been scripted within the Template, You can click on the **form editor button** *(middle icon)* at the top right of the template form.

![json](images/Input-Form.png?raw=true "Import JSON")

Within the input form select the variables within the script and one at a time edit the form that they will take during provisioning on the right.

#### Variable Naming and Instructional Text
On each variable the form will appear in the with the name of the text used in the script pasted. The variable $hostname would appear as the following:

![json](images/variable-basic.png?raw=true "Import JSON")

At that point start by choosing a *Field Name* to be used in the form, perhaps something more descriptive of meaningful. For this variable you might capitalize it to read Hostname.

The next field is *Tool Tip* which is a text box allowing for the entry of information to describe what to enter for the variable, and would appear as ALT text when moused over on the UI.

![json](images/variable-instructionaltext.png?raw=true "Import JSON")

Additionally fill in perhaps the *Default Value* if not provided in the script. The default value will be populated in the form for submission during provisioning. This field is used when a string text entry variable is defined. *Instructional Text* appears if the default value is not used, or is deleted, and gives guidenace to how to fill in the required data. *Maximum Characters* is the maximum number of ascii characters that may be entered. This can be used for uniform lengths of data.

#### Defining Variables
The next step is *Variable Definition*. Similarly to the scripting and using the set command, we define variables as numeric or string type variables. Additionally though we have IP Address and MAC Address formats. In the UI this selection process is done through a dropdown selection menu.

![json](images/variable-definition.png?raw=true "Import JSON")

To the right is the *Display Type* field which again is a dropdown selection menu allowing for the text, single and multi select types of entry within the form shown below.

![json](images/variable-data-entry.png?raw=true "Import JSON")

**Text** allows for text entries and will use the default value field if entered. **Single** and **Multi Select** will allow you to select a data point as a default value within the data added as shown. each time the add button is clicked another choice is entered to the single choice list. 

![json](images/variable-singlechoice.png?raw=true "Import JSON")

The first line is by default blank at first and as the only line is the *Default* but that may be moved to any other line added. The *Key* field is what appears as your selection but this may be the data you want used on the device or may be just a representative value in the list. The *Value* is the value used by the script on the device.

![json](images/variable-selections.png?raw=true "Import JSON")

#### Bind Variables
Within DNA Center it is possible to Bind Variables to devices. Within DNA Center versions 1.2 and 1.3 this can only be used and populated by the device for use in **DayN Templates**. When used in **Onboarding Templates** the variable is not populated at this time although we believe that to be a roadmap item. Once the device is in the inventory this data populated by the dvice during onbaording may be used throughout the script to make decisions. For example if it is a 48 port 9300 the product ID would be populated with C9300-48U and so you can make decision trees to program 48 ports based off that value. See DayN Templates for more information.

##### Building a Bind Variable
1. Build the variable as single select variable

![json](images/variable-binding.png?raw=true "Import JSON")

2. Select the option *Bind to Source* as above
3. Choose the *Source* use the drop down and select from as shown in image below:
   - Network Profile     *-use this option for SSID*
   - Common Settings     *-use this option to poll settings like ntp, dns*
   - Cloud Connect       *-use this option to poll tunnel information*
   - Inventory           *-use this option for device information*
   
![json](images/variable-bind-inventory.png?raw=true "Import JSON")

4. Choose the *Entity* to poll within the Source as shown below

![json](images/variable-bind-device.png?raw=true "Import JSON")

5. Choose the *Attribute* as shown below

![json](images/variable-bind-platformid.png?raw=true "Import JSON")

6. Save the Input Form through Actions menu on Input Form

#### System Variables
Within DNA Center it is possible to utilize Built-in System type variables for a number of values allowing you to address network settings within the design, to other interface information from devices. This example of code utilizes the `$__interface` built in variable to determine the characteristics of a port and then apply a macro to each port for a specific device.

```vtl
#foreach( $interface in $__interface )
  #if( $interface.portMode == "trunk" && $interface.interfaceType == "Physical")
    interface $interface.portName
     #uplink_physical
  #end
#end
```

If you found this repository or any section helpful please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

Special mention to: https://explore.cisco.com/dnac-use-cases/apache-velocity as examples and extrapolations were made using this documentation.
