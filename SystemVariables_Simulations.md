#### Simulations

  If you want to verify that the template is going to operate as expected, you can use the Simulator to run through the logic of your template and generate the output configuration for a target device.  This will not make any changes to your devices and can be a good way to test your templates as you work through them.  

You can access the Simulator by clicking on the "play" icon in the top left.

![json](./images/play_icon.png?raw=true "Import JSON")

Next, click **Create Simulation**.  When you reach the Simulation Input Page, you'll have to give the simulation a name and then supply values for any variables.  For our bound variables to work, we also need to supply a target device to test against.

![json](./images/create_simulation.png?raw=true "Import JSON")

When you reach the Simulation Input Page, you'll have to give the simulation a name and then supply values for any variables.  For our bound variables to work, we also need to supply a target device to test against.

![json](./images/simulation_input.png?raw=true "Import JSON")

Once you've selected a device, then you'll see our **selected_interfaces** options and can select the ones you want to test with:

![json](./images/interfaces_options.png?raw=true "Import JSON")

Once you have completed your selections, click the run button at the bottom right of the screen.

If your Simulation was successful, meaning that there were no syntax errors that caused the simulation to fail to render configuration, the resulting configuration will show in the right-hand side of the window:

![json](./images/simulation_output.png?raw=true "Import JSON")

Note that due to Jinja2 whitespace handling, the configuration may look messy or misaligned, but these whitespace issues will not affect provisioning.

This output provides highly beneficial detail on what configuration would be pushed to a target device based on our template logic and allows the architect to ensure that the template will render as expected when it is time to provision.
