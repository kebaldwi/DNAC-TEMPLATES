# Template Deployment

## Pipeline Overview

In the previous step we pasted a **Groovy Script** into the **Pipeline Configuration**. This script tells Jenkins what to do when the **Pipeline** is initiated.

Let's examine the **Groovy Script** in more detail:

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

First thing we should note is that the indentation **does** matter with **Groovy Scripting**. Secondarily, it is important that when using various methods, the correct **Plugins** are installed. 

The way this script is generally designed to work is that when initiated it loops until you cancel it. Persistently it checks for new **template files** in the **directory** in the `/root/DEVWKS-2176/templates` and then gathers the **timestamp** from those files and compares it to the previous collected **timestamps**. If the **timestamps** have **changed**, the files have been modified and the **Pipeline** automatically runs the **Python** program to **build templates** on Cisco DNA Center and then **deploy them** to the **devices** in the **YML**.

## Template Deployment

We will now **build** and **deploy** the **templates** to the **devices** using the **templates** in the directory and the **YML** variables previously discussed.

Follow these steps:

1. Ensure the previous pipeline **DNAC-Discovery** is **stopped** and not running, if not **stop** it.

2. Navigate and open the desired **Pipeline** within the **Jenkins Dashboard**:

3. Click **Build** 

   ![json](./images/.png?raw=true "Import JSON")

4. To observe the **Pipeline** run of the programs, do the following:

   1. Click on the most recent small number in the **Build History** 
   2. Within that window click on **Console Output**

5. To stop the **Pipeline** click the small red X in the **top right** of either the **Build** or the **Build History Number**
      ![json](./images/.png?raw=true "Import JSON")

> [**Next Section**](./05-verify.md)
