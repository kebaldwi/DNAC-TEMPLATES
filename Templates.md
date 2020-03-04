# Building Templates
In this section we will explain how to build a template in DNA Center.

## Phylosophies
There are a number of coding paradigms which various programmers use when building, maintaining and publishing programming code which are extremely useful when trying to integrate programmability for use in modern day infrastructure use cases. Lets deal with each concept in turn:

  - imperative in which the programmer instructs the machine how to change its state
      - procedural which groups instructions into procedures
      - object-oriented which groups instructions together with the part of the state they operate on
  - declarative in which the programmer merely declares properties of the desired result, but not how to compute it
      - functional in which the desired result is declared as the value of a series of function applications
      - logic in which the desired result is declared as the answer to a question about a system of facts and rules
      - mathematical in which the desired result is declared as the solution of an optimization problem
        
## Modular Programming    
Modular programming is a software design technique that emphasizes separating the functionality of a program into independent, interchangeable modules, such that each contains everything necessary to execute only one aspect of the desired functionality.

A module refers to high-level decomposition of the code of an entire program into pieces: structured programming to the low-level code use of structured control flow, and object-oriented programming to the data use of objects, a kind of data structure.

This calls out two very key points: 

  1. **Functionality**
     Code segmented into small chunks to reduce complexity 
  2. **Reusability**
     Modular code designed for reuse as parts of functions

## Parsing IOS Configurations
As you begin your builds of Templates it helps to analyze the various IOS configurations and group logical syntactic components and where we see reusability, for example in service statements, we can create groupings of commands and put those into either separate templates (modules) to be used in a composite template or separate them into a separate template you can reuse.

Remember the DNA Center **Network Profile** that you will build offers a couple of options, additional templates or in the Day N role, a composite template. Either is available for use.

Once you have grouped configuration snippets into separate logical constructs you can then see what additional platforms you might apply them too, as this will steer you in the direction of whether multiple modules (snippets) are required or whether you will need a complete duplication of certain functions.

Once we have identified all the various modules we will need, we can then start to analyze which of the codes the Design App can facilitate, and ensure the design has those settings and remove them from the modules.

## Templates
We have two templates offered in DNA Center. A standard template which is designed to stand alone for a specific function and a composite template which will group standard templates and which can only be used in Day N Projects.

As we build out a Standard Template we can either as has previously been mentioned put all the IOS commands which makes the configuration within the template more complex to maintain, or we can separate out the various sections into separate templates and call them as additional templates in either the Onboarding or Day N flows.

Once you have created a new template and pasted the IOS configurations into the template editor you can then look for values which can be replaced by variables. 

### Variables
Variables are used to allow scripts or code for that matter to be reused. A variable within a script allows us to replace the data on demand thereby allowing the reuse of parts of or entire templates. Variables may be defined in a couple of ways but the data entered will either numerical or string. A numerical value is just that a number where as a string is either a line of text or perhaps just a name.

Analyse your configuration to make optimium use of variables which will allow reuse. Please refer to [Variables](./Variables.md).

### Velocity Scripting
To further simplify your IOS configuration analyze your IOS template for manipulations that might occur if it were a 24 port switch as opposed to a 48 port switch, and then build logical constructs to allow for one template to address multiple platforms.

While it is possible to take a CLI script for one device and create a template for one device at a time, that would leave us with a lot of templates and make it harder to make changes on an ongoing basis. Using the techniques of Velocity Scripting will allow us to deploy equipment with scripts which can be reused on a broader basis, allowing us to keep configurations similar for conformity reasons but also to reduce the number of places where changes would have to be made. For additional information please see [Velocity Scripting](./Velocity.md).

Within these logical constructs you have many tools, please review each section as needed:
[If Statements](./Velocity.md#if-statements)
[Macros](./Velocity.md#macros)
[Loops](./Velocity.md#foreach-loops)
[Multiline commands](./Velocity.md#multi-line-commands)

## Examples
Specific examples of Templates are available in the following folders:

* [PnP Onboarding](./ONBOARDING) - Examples of PnP/ZTP Templates explained in [Onboarding Templates](./Onboarding.md)
* [DayN](./DAYN) - Examples of DayN Templates explained in [DayN Templates](./DayN.md)
