# Template Deployment Python Pipeline

In this section of the tutorial, we will continue using a simple REST-API set, which has been grouped into a **Python** program. We will then construct a Jenkins Pipeline to automate the template build and deployment to devices that may be modified in the **YML** file for Cisco DNA Center.

## Template Deployment Python Program 

These **Python** program files are groupings of API, which allow us to have workflows defined for specific tasks. Programs also have modules included in them which allows for the reusability of code. 

To investigate this collection, follow these steps:

1. On the **script server** do the following:

   1. Open the program using NANO in Read Only

```SHELL
      sudo nano -v /root/DEVWKS-2176/deploy_templates.py
```

   2. As you scroll through the lines of the program take note of the following:

      - **import** statements for dependant modules and libraries
      - **YAML** a YAML file is used for environment settings
      - **YAML** a YAML file is also used for template deployment data
      - **definitions** functions are defined to build API interactions 

      ![json](./images/.png?raw=true "Import JSON")
   
   3. Unlike the first module this set of **REST-API** are built utilizing the [**DNA Center SDK**](https://dnacentersdk.readthedocs.io/en/latest/) a python library used to help integrate Cisco DNA Center more easily using **Python**. This may still be augmented with **REST API** built using the developer site [**developer.cisco.com/docs/dna-center/**](https://developer.cisco.com/docs/dna-center/). This documentation is kept up to date with the latest **REST-API**. Take a few momennts to review the similarities and differences between the two approaches.

## Jenkins Pipeline

During this section we will construct a Jenkins Pipeline to work with the given **Python** and the **YML**.

### Jenkins Preparation

Login to Jenkins but first connecting to the URL **[http://198.18.134.28:8080](http://198.18.134.28:8080)** with the credentials:

         - username: `root`
         - password: `C1sco12345`

Once logged in you should see this **Jenkins dashboard**.

![json](./images/.png?raw=true "Import JSON")

#### Step 1 - *Adding required plugins*

Previously we added the following plugins which are dependancies into Jenkins:

   1. Pipeline
   2. Python
   3. Pipeline Utility Steps

> **Note:** To review installing the plugins from the Jenkins web interface go to **Manage Jenkins > Manage Plugins > Available** page, and searching for them one by one. Once you find the plugin, **select it** and click on **Install without restart** button.

#### Step 2 - *Building the Pipeline*

We now need to build the **Pipeline** which will monitor the files in the directories and automate the build of the hierarchy.

1. To create a new **Pipeline** job: 

   1. Go to the **Jenkins dashboard** and click on **New Item** 
   2. Give your job the name `DNAC-Templates`
   3. Select **Pipeline** as the job type
   4. Click **OK**.

2. In the pipeline job configuration, you can define the pipeline script that will monitor a local directory and run a local Python program. You can use the `dir` command to change to the desired directory and use shell commands to execute the Python program.

3. To configure the **pipeline script** click **configure** within the **Pipeline** just created and on the left click **Pipeline**. This will scroll to the **Pipeline Script** section. Leave all the defaults as is and paste the following **Groovy Script**:

```GROOVY
pipeline {
    agent any

    stages {
        stage('Monitor Template Directory') {
            steps {
                script {
                    def previousModifiedTime = null
                    def currentModifiedTime = null

                    while (true) {
                        // Retrieve the previous modified time from a file or environment variable
                        println 'Monitoring Template Directory for changes'
                        def storedModifiedTime = readFile('/root/DEVWKS-2176/timestamp/previous_modified_time_templates.txt').trim()
                        if (storedModifiedTime) {
                            previousModifiedTime = storedModifiedTime.toLong()
                        }

                        // Check if any files exist in the subdirectory except placeholder.txt
                        def filesExist = sh(script: 'find /root/DEVWKS-2176/templates -type f ! -name "placeholder.txt" | wc -l', returnStdout: true).trim().toInteger() > 0

                        if (filesExist) {
                            // Execute a shell command to retrieve the last modified timestamp of any files except placeholder.txt
                            def lastModifiedOutput = sh(script: 'find /root/DEVWKS-2176/templates -type f ! -name "placeholder.txt" -exec stat -c %Y {} \\; | sort -n | tail -n 1', returnStdout: true).trim()
                            currentModifiedTime = lastModifiedOutput.toLong()
                            println "Current Timestamp: ${currentModifiedTime}"

                            if (previousModifiedTime == null || currentModifiedTime != previousModifiedTime) {
                                // Execute your desired steps or stages here
                                println 'Files changed'
                                dir('/root/DEVWKS-2176') {
                                    sh 'python3 /root/DEVWKS-2176/deploy_templates.py'
                                }
                            } else {
                                println 'No changes'
                            }
                        } else {
                            println 'No files found in the subdirectory'
                        }

                        // Store the current modified time for future comparisons
                        writeFile file: '/root/DEVWKS-2176/timestamp/previous_modified_time_templates.txt', text: currentModifiedTime.toString()
                        sleep 180
                    }
                }
            }
        }
    }
}
```

4. Finally click **Apply** and **Save** to save the new configurated **Pipeline**.

> [**Next Section**](./04-deploy.md)
>