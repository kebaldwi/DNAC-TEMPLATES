 
Contents
Cisco’s Multi-Domain Automation and Orchestration Engine Your Customer Already Has	3
Introduction	3
Lab Preparation	3
Lab 2A: Set Up Connectivity into Meraki	6
Lab 2B: Add a JSONPath Query Activity	13
Lab2C: Logic Functions	18
Lab2D: Take Inventory	28
Lab2E: Share the Table with Webex	32
Lab2F: Send Something Useful This Time	39
Lab2G: Make the Webex an Atomic Workflow	44
Appendix: Useful Workflows Resources	54

 
Cisco’s Multi-Domain Automation and Orchestration Engine Your Customer Already Has
Introduction
Welcome to the ‘Simple Network Automation – The Added Value of Cisco Workflows’ session.
Meraki has added a well-established Cisco tool to the dashboard: Workflows. But let’s be very clear, it’s not just for Meraki. Customers can use this powerful automation and orchestration engine on pretty much anything. In addition to Meraki, it can be used for automating Cisco controllers like Catalyst Center, SDWAN, ISE, ThousandEyes, ACI, Nexus Dashboard, Intersight, Webex, IOT, and everything Cisco. Use it with third-party tools and other vendors. If it has a REST API or an SSH adapter, Workflows can automate it.
If you went through the beginner level hands-on labs, you should now be familiar with the general feel and flow of Workflows for Cisco Networking. Build it, validate it, run it. We used the output of an early step as the input for a later step. You’ve now got the basics to go and build pretty much anything you can think of. In this intermediate level lab, let’s go through a few more concepts and build something useful in the real world. Perhaps something you could even give to a customer. We’re ultimately going to create an inventory of Meraki devices and their current firmware versions.
Lab Preparation
Lab Environment
Let’s take a moment to clearly describe the environment we’re going to be playing in because it might get a little confusing. If things went smoothly, your regular Meraki account has Workflows Automation enabled. We need consistency of environments across all participants, so everyone has the same experience. We will use your Cisco Workflows-enabled Meraki account to build automation against the Meraki Self-Serve Lab environment. Put another way, for the purposes of this lab, you’re going to be automating a Meraki organization that is separate from your own Meraki organization.  
Hopefully this doesn’t get too confusing. It highlights an important takeaway from today. You can automate pretty much anything from your own Meraki organization and that includes other Meraki organizations. How many Meraki organizations do your customers have? Some have more than one! If it has an API or an SSH interface, you can automate it without writing a single line of code with Cisco Workflows.
Meraki Self-Serve Lab
If you’re not aware, Cisco has Meraki Self-Serve Labs. It’s a great environment in which to learn and demo to customers. It’s real Meraki gear. When you check out a pod, it dynamically creates an organization with two networks. Each network has an MX gateway, an MS switch, and an MR access point. The team has automated the entire Meraki stack such that it can be completely reset to a known good state in about 10 min. You can go do pretty much anything you want with the gear without worrying about messing things up for the next person. 
NOTE: Cisco has 75 of these pods. Given the number of people in the room, we will do our best to distribute an API key per table.  As of the time of this writing, the Tech Elevate @ GSX logistics are not final so there may be some in-room instructions and coordination.
When you have been added to a Self-Serve Meraki pod, look for an email stating you have been added as an organization administrator.
  
API Key
You need the API key for this Meraki organization. It may arrive as this session begins.
•	If instructed, generate an API key by navigating to Organization, Configure, API & Webhooks
•	If instructed, click the API Keys and Access tab and generate your API key. Store the key for future reference.
Follow the guidance provided in this Tech Elevate @ GSX session to gain access. You will see a Meraki screen that looks like this.
 
 
Details for distributing accounts and API keys is not finalized as of this writing, so hopefully at this point you have an API key for Self-Serve Labs. If not – flag down a proctor for assistance.
 
Lab 2A: Set Up Connectivity into Meraki
Task 1: Access your Workflows environment and navigate to Automation and then Account Keys.
 
Task 2: Click New Account Key and enter details and your Meraki Self-Serve API key.
NOTE: In earlier versions, there was also a Cisco Meraki Token. For this lab you want to use Meraki Credentials.
 
Task 3: Click Save and navigate to Automation.
Task 4: Select Targets, click New Target, and fill in the details as follows.
Task 5: Click Save.
     
You often have to worry about things like tokens for authentication when writing network automation against APIs. You do not have to write code with Cisco Workflows and it handles things like tokens for you. You’ve set up your key and target. Now, all you have to do is write whatever automation and orchestration against your target that you can dream up. SCORE!
Task 6: Access your workspace and create a new Blank Custom Workflow. I’m going to call mine Meraki Inventory.
 
Task 7: Let’s set a default target for this workflow. Scroll down the properties panel to locate Target.
 
Cisco Workflows allows you to define a default target for the entire workflow. Not being required to configure this for every step saves several clicks and your time. You can of course override the target for a particular step if you wish.
Let’s start with something simple and list the Meraki organizations we belong to. 
Task 8: In the top left, enter organizations to quickly and easily locate Meraki – Get Organizations. Drag it onto your canvas.  
 
Let’s pause and explore the concept of Atomic Workflows
Note that the icon on the canvas is a stack. This indicates that this is an Atomic Workflow. An Atomic Workflow is meant to be a smaller workflow that can be run within a larger workflow. Yes, workflows running workflows. Cisco has already provided 1000+ atomic workflows for you right out of the box, but you can also create your own custom atomics. If you’ve ever coded in python, you’ve probably written a Def or a function. Defs are common things that you write once and call over and over again. Same concept with atomics. If you do a task over and over, consider writing it as an atomic and simply drag it into your larger diverse workflows.
Task 9: Hover your mouse over the Atomic Workflow you just added to your canvas, and you’ll notice three dots. Click View Atomic Summary
Task 10: Click See Atomic Details to view the Atomic Workflow itself and how it was built.  
You can see each step that Cisco (or anyone else) added to their atomics. You can also see some Workflows Best Practices, down to the specific configuration of every step.
     
 
We will cover conditionals later, but even if we run out of time, now you have working examples of how to build them. Thank you, Cisco Workflows team!
Task 11: Click Back to parent Workflow.
This function is usually ridiculously simple, so let’s run it.
     

Task 12: Validate it and then click Run. Let’s see some green!

Task 13: Click Meraki - Get Organizations step and check out the result. SUCCESS!
     
Pay attention to the structure of the result, because we’re going to pull the Org ID for the next step. The JSON path for the result above is a list, and I want the first “0” entry in that list. Then I want the dictionary key ID. In JSON path queries, this would be [0][“id”]. Note that if you use an email with multiple orgs, your self-serve organization may not be first.
TIP: If you have multiple organizations in your response, one option would be to use a slightly more complex JSONPath Query that looks for the ID of the organization name that starts with “Org”, like this one: $[?(@.name =~ /^Org.*/)].id
Task 14: Click Modify to return to the workflow editor.
 
Lab 2B: Add a JSONPath Query Activity
Just like we did in Lab1, we must give it a source JSON and tell it what to extract.
     

You can test it to make sure you pulled the Org ID correctly.  Go ahead and test if you prefer. I’m feeling a bit reckless, so I’m going to add another step.	 

Task 1: Search for Meraki – Get Organization Networks and drag the activity onto the canvas below the JSONPath Query.
 
Guess what Get Organization Networks requires? Let’s find out.
Task 2: Click View Atomic Summary
 
Guess who we provide an org ID? Our friend the mapping icon.
     
Let’s run it. Hopefully you remember the Validate step by now – this is the last reminder.

Important: Using the mapping function allows use of the output of a step for the input of a later step.
     
 
Lab 2C: Logic Functions
For most of this exploration of Workflows, we’re not going to validate every step like you would in the real world. This is intentional so we can cover more of the mechanics of Workflows in the time we have today. Still, let’s do one validation step so you can see why it is important.
Task 1: Navigate to the Logic tab on the left-hand bar.
 
Task 2: Drag the Condition Block onto the canvas and place it after your first Meraki – Get Organizations.
 
Let’s ensure the first step was successful.  
Important: Imagine you had a complex workflow that hit 50 APIs or took a lot of time due to required approvals or inputs from others. Perhaps you were using workflows to automate a software upgrade on a switch or router. In those scenarios, you want to verify every step and be notified if something went wrong.
In this lab, a successful API call will have a return code of 200. Therefore, the conditional will continue only if the return code is 200.
Task 3: Rename the conditional to help others follow your logic.
 
Task 4: Click the block on the left and name it 200 Successful. Name the other block something like Not 200.
 
Task 5: Click 200 Successful and configure the logic in the panel on the right. Start with our best friend, the mapping function.
     
Important: Note the Add Condition option. You can create complex conditionals where everything must be true, or one thing true and another false, or only one condition must be true. There are lots of options.
Task 6: Configure the other conditional box.
    TIP: Another option to easily configure additional conditional branches is to duplicate the first branch, switch the comparison operator, and update the name.
 
Now we need to tell the workflow what to do in each case (or branch) by dragging and dropping the appropriate actions. Let’s create an output variable that we will set in the event of an error. It’s best practice, that if anything fails, try to exit gracefully and provide a useful error message.
Task 7: Click the canvas outside of the workflow and scroll down to Variables.
     
Task 8: Add an output variable by selecting Output in the Scope field. It will be a potential error message, so select String in the Data Type field.
     
Task 9: Find the Set Variables activity and drag it into the Not 200 conditional block. 
This will set the error message in the event of a failure.
 
Task 10: Add the Completed logic activity so we can exit the workflow if there is a problem.
 
Task 11: In the Completed Logic activity, you can select Success or Failed as the Completion Type and then map a useful message to the workflow result message.
In this example, we have selected the error message from the previous Get Organizations activity. Try out the activity.
 
Note that the 200 Successful condition branch did not have to contain activities. The conditional logic could have tested only the Not 200 case because that was the only branch that required activities. However, including the 200 Successful branch makes the workflow more easily understood by others and helps to visually document the logic and flow.	 


Task 12: Let’s test it to be sure the error kicks in like we expect.  Navigate back to the workflow and change the evaluation fields from 200 to something else. 
Don’t forget to change both blocks and run the workflow again.
     
Nice. Graceful exit and a useful error message. You could add a Webex message, or email, or text yourself. Drop anything you like into the success or failure blocks. Pretty sweet aye? Don’t forget to change the conditional expressions back to your 200 code and then we’ll head to the next section of this lab.
  
Lab2D: Take Inventory
Task 1: Drag-and-drop the task titled Meraki – Get Organization Devices at the bottom of our workflow.
Scroll down the configuration panel. Guess what’s required – the org. Good thing you already pulled that with the previous JSON query. This is an easy configuration with our friendly puzzle icon for mapping.
 
This step returns a JSON table with some good info about each device in the org. Now let’s create a table that we can use in a later step.  
 
Task 2: Navigate back to the workflow editor, find the Read Table from JSON activity, and drag-and-drop it at the bottom of the workflow.
We are going to create a table dynamically based on what was returned in that previous step. The first step is to specify the JSON Path to read
Task 3: Enter $ in the JSON Path field.

Task 4: Select Persist Table so we can use it later.
     
A nice feature is that you get to pick and choose what fields are interesting to you to add to your Table for your workflow. If you need to go back and reference the JSON result, you can leverage View Runs under the More Actions drop down menu.
Task 5: Click Add five times and enter the key values from the JSON into the Name fields.
You can leave the Type as String for all of these.
Let’s get the following fields:
•	Serial
•	Mac
•	Product Type
•	Model
•	Firmware	 

Task 6: Map the Source JSON to the previous output.	 
Task 7: Run it and check the result.
You’ve got a nice, neat table with exactly what you wanted.

Congratulations. You’re doing useful productive workflows and haven’t written a single line of code (yet).
     
 
Lab2E: Share the Table with Webex
At the time of this writing, Workflows is still in early preview and there are a couple of functions that still need a little more love.  Webex happens to be one of those, so this guide will do a few things. 
We will create our own functions from scratch, proving that Workflows can truly automate and orchestrate anything. Customers can automate other vendors, which isn’t exactly what we want. However, would you rather Cisco be the control mechanism for a customer, or our competition?
The easiest way to get this communications channel up and running is by creating a Webex Bot. You could also send and receive direct IMs if you signed up for Webex OAUTH, but that involves a few extra steps. 
Task 1: Open a web browser, go to developer.webex.com, and log in.  

Task 2: Click your user icon in the top right corner and click My Webex Apps

Task 3: Click Create New App.	 

Task 4: Select Create a Bot and complete the fields shown here.
     
NOTE: Make sure to copy your token someplace easy to access and secure
     

Knowledge Check: What do you need to interact with another API?  You need (potentially) an API Key and a Target. In this case, I want to highlight another approach, so we’ll create the Target but use our API key as a secure string within the workflow.
Task 5: Navigate Targets and enter HTTP Endpoint in the Target Type field.  
Name it whatever you want and use the following details for the remaining fields.
     


Task 6: Navigate to your workflow editor and add HTTP Request.  

This is an important function because you can do any REST function. Anything with an API is fair game in Cisco Workflows.

You’re going to need your bot’s ID and your token here.

Task 7: Select Override Workflow Target in the HTTP Request properties because this isn’t against the Meraki API.
     
Task 8: Add the API path, the method, and the request body.

Here is the format so you can copy/paste, but use your own Bot ID.


{
    "toPersonEmail": "ENTER YOUR CISCO EMAIL HERE",
    "markdown": "Hey there!"
  }

     
Task 9: For headers, select Content Type “Application JSON”, and a custom header called “Authorization” and “Bearer”.
We’re not done yet. You could add in your API key right there after Bearer, but we’re going to store it as a secure string so not everyone will see it.
Task 10: Navigate to Automation and select Variables.
     
Task 11: Create a new variable. Enter Secure String in the Data Type field, name it in the Display Name field, and add your API key.
     
Task 12: Navigate to your workflow and map the secure string into the custom header.
     
Your headers section should look similar to this.
     
Other people can use your API key in Workflows, but they will not be able to see it and take it elsewhere. This will become even more useful when Cisco Workflows adds more granular RBAC.
Task 13: Open Webex and run the workflow.

Status Code 200!  
     
Score!  
     
Lab2F: Send Something Useful This Time
Let’s send ourselves the Meraki inventory table we created earlier.
Task 1: Navigate to your workflow, select the HTTP request you just created, and navigate to the Request Body section.  
How can you map-in the inventory table? We could try editing the message we want our bot to send. For example, we could add two carriage returns (the code for a carriage return is \n) and then map in our table.
WARNING: It’s not going to work. Try to figure out why it won’t work by trying to run it like this.  It will serve as a good example of troubleshooting workflows.
 
The JSON contained quotes.  So that ended up being a very malformed Request Body.  (That’s a bad thing).  

What can we do to be able to achieve what we want?  

We want to replace the offensive JSON characters that are raining on our parade.
     
Task 2: Navigate to the workflow and see if you can find an action that will replace the problematic characters. 
The quotes are causing issues, so let’s get rid of them.  There are three examples of the problem in this screenshot.  There are two more examples, but they are not included in the screenshot.
 


Replaced String	Replacement String
[{"	
"}]	
":"	:
","	\n
"},{"	\n\n

So – lets replace these with something that still gives us the table structure.
 
Task 3: Navigate to the HTTP Call and use the new string.
     
Task 4: Run it again and see if we achieve the desired result.	 
NICE!!! Look at that!  Building useful workflows and sending the output to your Webex account. That’s some really cool stuff right there!


Maybe take one more step and clean up the name of that HTTP Request.

     

Lab 2G: Make the Webex an Atomic Workflow
Task 1: Navigate to your workspace.
 
Task 2: Click the three dots to the right of your workflow and select Duplicate.
 
Task 3: Rename the new copy “Send to my Meraki BOT.
Task 4: Delete everything except the final send step based on the generic HTTP Request.  
It should look like this when you’re ready.
 
Since this workflow started as a Meraki workflow, we set the workflow Target Type to Meraki and then overrode the workflow target in the HTTP Request.  We need to fix this.

Task 5: Reconfigure the workflow Target Type to be HTTP Endpoint.
      
Task 6: Reconfigure the HTTP Request Target to be Use Workflow Target.
Task 7: Navigate to Variables and add input variables to the Atomic Workflow. 
Task 8: Add an output variable for the response code.
         
Task 9: Navigate to the HTTP Request and replace some of it with these new mapped input variables.
Important: We touched on this a little bit, but let’s reinforce it.  One of the nice features of our friend the mapping icon (x) is you can highlight something, and it will automatically replace what’s highlighted with the mapped variable.
Task 10: Access the Request Body and highlight the email address.
 
Task 11: Click the mapping icon and navigate to the input variables.
 
Task 12: Click Save and then do the same for the message payload.
 
 
Task 13: Map the result code to the output variable
 
Task 14: Validate the workflow, click the canvas to access the general workflow properties, and set it as an Atomic Workflow.  
Task 15: You can save it under an existing category or create a new custom category.  For this example, I’ll create a new one and save it there.
 
Congratulations.  Now you have a “send to Meraki” atomic to use again and again whenever you need it.

Task 16: Click the Atomics tab to view the new workflow.
     
Task 17: Return to your Meraki Inventory workflow. You should see your new adapter category.
     

Task 18: Drag it over to the canvas, configure it to send Have a Nice Day, override the target, and run it.
         
How easy was that?  How easy will it be next time?
Important: While Atomics are awesome, there are some things you should be aware of.
•	In the previous example, your API key is available to other workflow users (until RBAC enhancements roll out).  Maybe this is OK, but be aware of potentially sensitive things you include in your workflows.
•	Exporting/importing may have issues.  Workflows and custom Atomics each have a unique UUID for the platform.  Currently the standard Workflows Export function does not include custom Atomics when exporting a workflow.  Note that you can export your custom Atomic separately from your workflow.  If another user imports your workflow, the platform looks for the Atomics to already be present with the identical UUID.  In other words, if you plan to export your workflows so others can import them, it’s best practice to *not* leverage custom atomics.  
Wow!  That was a lot of stuff.  Congratulations on making it to the end.
There is a third section, but it is much smaller.  The goal is to just make you aware of a few more features of this awesome automation and orchestration platform.  Stand up and stretch.  You’re nearly done!
 
