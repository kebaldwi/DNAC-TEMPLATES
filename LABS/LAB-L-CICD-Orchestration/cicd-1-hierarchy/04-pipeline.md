# Hierarchy Build Python Pipeline

The **Python** programming language is a powerful tool for building programs related to **REST-API** calls and allows us to utilize several features to accomplish everyday tasks. In this section of the tutorial, we will use a simple REST-API set, which has been grouped into a **Python** program. We will then construct a Jenkins Pipeline to automate the provisioning of the settings that may be modified in the **CSV** on Cisco DNA Center.

## Deploy Hierarchy Python Program

These **Python** program files are groupings of API, which allow us to have workflows defined for specific tasks. Programs also have modules included in them which allows for the reusability of code. 

To investigate this collection, follow these steps:

1. On the **script server** do the following:

   1. Open the program using NANO in Read Only

```SHELL
      sudo nano -v /root/DEVWKS-2176/deploy_hierarchy.py
```

   2. As you scroll through the lines of the program take note of the following:

      - **import** statements for dependant modules and libraries
      - **YAML** a YAML file is used for environment settings
      - **definitions** functions are defined to build API interactions 

      ![json](./images/.png?raw=true "Import JSON")
   
   3. This set of **REST-API** are built utilizing the developer site [**developer.cisco.com/docs/dna-center/**](https://developer.cisco.com/docs/dna-center/). This documentation is kept up to date with the latest **REST-API**.

## Jenkins Pipeline

During this section we will construct a Jenkins Pipeline to work with the given **Python** and the **CSV**.

### Jenkins Preparation

Login to Jenkins but first connecting to the URL **[http://198.18.134.28:8080](http://198.18.134.28:8080)** with the credentials:

         - username: `root`
         - password: `C1sco12345`

Once logged in you should see this **Jenkins dashboard**.

![json](./images/.png?raw=true "Import JSON")

#### Step 1 - *Adding required plugins*

As we will be utilizing file searches within folders and initiating python from within pipelines we need to add the following plugins into Jenkins:

   1. Pipeline
   2. Python
   3. Pipeline Utility Steps

To install the plugins from the Jenkins web interface go to **Manage Jenkins > Manage Plugins > Available** page, and searching for them one by one. Once you find the plugin, **select it** and click on **Install without restart** button.

#### Step 2 - *Building the Pipeline*

We now need to build the **Pipeline** which will monitor the files in the directories and automate the build of the hierarchy.

1. To create a new **Pipeline** job: 

   1. Go to the **Jenkins dashboard** and click on **New Item** 
   2. Give your job the name `DNAC-Hierarchy`
   3. Select **Pipeline** as the job type
   4. Click **OK**.

2. In the pipeline job configuration, you can define the pipeline script that will monitor a local directory and run a local Python program. You can use the `dir` command to change to the desired directory and use shell commands to execute the Python program.

3. To configure the **pipeline script** click **configure** within the **Pipeline** just created and on the left click **Pipeline**. This will scroll to the **Pipeline Script** section. Leave all the defaults as is and paste the following **Groovy Script**:

```GROOVY
pipeline {
    agent any

    stages {
        stage('Monitor Hierarchy Build') {
            steps {
                script {
                    def previousModifiedTime = null
                    def currentModifiedTime = null

                    while (true) {
                        // Retrieve the previous modified time from a file or environment variable
                        println 'Monitoring Hierarchy Build for changes'
                        def storedModifiedTime = readFile('/root/DEVWKS-2176/timestamp/previous_modified_time_hierarchy.txt').trim()
                        if (storedModifiedTime) {
                            previousModifiedTime = storedModifiedTime.toLong()
                        }

                        // Check if any files exist in the subdirectory except placeholder.txt
                        def filesExist = sh(script: 'find /root/DEVWKS-2176 -type f -name "DNAC-Design-Settings.csv" | wc -l', returnStdout: true).trim().toInteger() > 0

                        if (filesExist) {
                            // Execute a shell command to retrieve the last modified timestamp of any files except placeholder.txt
                            def lastModifiedOutput = sh(script: 'find /root/DEVWKS-2176 -type f -name "DNAC-Design-Settings.csv" -exec stat -c %Y {} \\; | sort -n | tail -n 1', returnStdout: true).trim()
                            currentModifiedTime = lastModifiedOutput.toLong()
                            println "Current Timestamp: ${currentModifiedTime}"

                            if (previousModifiedTime == null || currentModifiedTime != previousModifiedTime) {
                                // Execute your desired steps or stages here
                                println 'Files changed'
                                dir('/root/DEVWKS-2176') {
                                    sh 'python3 /root/DEVWKS-2176/deploy_hierarchy.py'
                                    sh 'python3 /root/DEVWKS-2176/deploy_settings.py'
                                }
                            } else {
                                println 'No changes'
                            }
                        } else {
                            println 'No files found in the subdirectory'
                        }

                        // Store the current modified time for future comparisons
                        writeFile file: '/root/DEVWKS-2176/timestamp/previous_modified_time_hierarchy.txt', text: currentModifiedTime.toString()
                        sleep 180
                    }
                }
            }
        }
    }
}
```

4. Finally click **Apply** and **Save** to save the new configurated **Pipeline**.

> [**Next Section**](./05-deploy.md)
>