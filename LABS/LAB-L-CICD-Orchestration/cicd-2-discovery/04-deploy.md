# Device Discovery Deployment

## Pipeline Overview

In the previous step we pasted a **Groovy Script** into the **Pipeline Configuration**. This script tells Jenkins what to do when the **Pipeline** is initiated.

Let's examine the **Groovy Script** in more detail:

```GROOVY
pipeline {
    agent any

    stages {
        stage('Device Discovery') {
            steps {
                script {
                    def previousModifiedTime = null
                    def currentModifiedTime = null

                    while (true) {
                        // Retrieve the previous modified time from a file or environment variable
                        println 'Monitoring Hierarchy Build for changes'
                        def storedModifiedTime = readFile('/root/DEVWKS-2176/timestamp/previous_modified_time_discovery.txt').trim()
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
                                    sh 'python3 /root/DEVWKS-2176/device_discovery.py'
                                }
                            } else {
                                println 'No changes'
                            }
                        } else {
                            println 'No files found in the subdirectory'
                        }

                        // Store the current modified time for future comparisons
                        writeFile file: '/root/DEVWKS-2176/timestamp/previous_modified_time_discovery.txt', text: currentModifiedTime.toString()
                        sleep 180
                    }
                }
            }
        }
    }
}
```

First thing we should note is that the indentation **does** matter with **Groovy Scripting**. Secondarily, it is important that when using various methods, the correct **Plugins** are installed. 

The way this script is generally designed to work is that when initiated it loops until you cancel it. Persistently it checks for the **CSV** file in the `/root/DEVWKS-2176` directory and then gathers the **timestamp** from that file and compares it to the previous collected **timestamp**. If the **timestamp** has **changed**, the file has been modified and the **Pipeline** automatically runs the **Python** program to **discover devices** on Cisco DNA Center and then **assigns them** to the **site** in the **CSV**.

## Device Discovery Deployment

We will now **discover** the **devices** using the **CSV** variables previously discussed.

Follow these steps:

1. Ensure the previous pipeline **DNAC-Hierarchy** is **stopped** and not running, if not **stop** it.

2. Navigate and open the desired **Pipeline** within the **Jenkins Dashboard**:

   ![json](./images/Jenkins_Dashboard_2.png?raw=true "Import JSON")

3. Click **Build** 

   ![json](./images/Jenkins_Item_Discovery_1.png?raw=true "Import JSON")

4. To observe the **Pipeline** run of the programs, do the following:

   1. Click on the most recent small number in the **Build History** 

   ![json](./images/Jenkins_Item_Discovery_Build.png?raw=true "Import JSON")

   2. Within that window click on **Console Output**

5. To stop the **Pipeline** click the small red X in the **top right** of either the **Build** or the **Build History Number**

      ![json](./images/Jenkins_Item_Discovery_console.png?raw=true "Import JSON")

> [**Next Section**](./05-verify.md)
