# Managing Complex Environments with Catalyst Center [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)

The **Catalyst Center** is a powerful platform designed to manage and optimize network environments, particularly in complex settings. Understanding the nuances of these environments, including **brownfield** and **greenfield** scenarios, is crucial for effective network management.

## Complex Environment

A complex environment refers to a network infrastructure that involves multiple devices, configurations, and policies. These environments often include legacy systems, various hardware types, and differing compliance requirements, making management challenging. The Catalyst Center aims to simplify this complexity through centralized management and automation.

![Managing Complex Environments](../ASSETS/TUTORIALS/MANAGEMENT/COMPLEX.png?raw=true "Complex Environment")

### Brownfield vs Greenfield

- **Brownfield**: This term describes environments where existing infrastructure and systems are already in place. In brownfield scenarios, organizations must integrate new technologies with legacy systems, often leading to compatibility issues and increased complexity. A perfect example of which is Authentication, Authorization and Accounting (AAA) as well as DOT1X configurations.

- **Greenfield**: In contrast, greenfield environments refer to new deployments where no prior infrastructure exists. This allows organizations to implement the latest technologies and best practices without the constraints of legacy systems.

---

## Objectives of Catalyst Center

The objectives of the Catalyst Center are influenced by whether the environment is brownfield or greenfield. Key objectives include:

### Policy

- **Brownfield**: Integrating new policies into existing frameworks can be challenging due to legacy configurations, which may not align with modern policy requirements.
  
- **Greenfield**: Organizations can establish clear and consistent policies from the outset, ensuring that all devices adhere to the latest standards.

### Compliance

- **Software Compliance**: Ensuring that all devices run approved software versions.
- **Configuration Compliance**: Adhering to configuration standards to maintain security and performance.
- **Policy Compliance**: Implementing policies that meet regulatory and organizational standards.

In brownfield environments, achieving compliance may require extensive auditing and remediation of existing configurations. In greenfield settings, compliance can be built into the initial design.

### Consistency

- **Complicated Configurations**: Brownfield environments often suffer from inconsistent configurations due to historical changes and ad-hoc modifications. The risk of misconfigurations increases, leading to potential downtime.

- **Greenfield environments** allow for standardized configurations, ensuring consistency across all devices from the start.

### Reusability

- **Eliminating Snowflakes**: In IT, "snowflake" refers to unique configurations that are difficult to replicate. Brownfield environments often have many snowflake configurations due to previous customizations.

- In greenfield scenarios, organizations can design reusable templates and configurations, reducing the number of unique setups and simplifying management.

### Scale

- **Brownfield**: Scaling in a brownfield environment can be complicated due to the need to integrate new devices with existing infrastructure, potentially leading to performance bottlenecks.

- **Greenfield**: Organizations can design for scale from the beginning, allowing for seamless growth and expansion without the constraints of legacy systems.

---

## Per Device Configuration Path

### Challenges, Caveats, and Benefits

**Per Device** refers to the strategy of ensuring that each device has a dedicated path for data traffic. 

- **Challenges**: Implementing this strategy can be complex, requiring careful planning to avoid network congestion and ensure optimal performance. Additionally, it may necessitate significant investment in hardware.

- **Caveats**: While this approach enhances performance and reliability, it may not be feasible for all organizations, particularly those with budget constraints or limited resources.

- **Benefits**: The primary advantage is improved network performance and reliability, as each device operates on its dedicated path, reducing the risk of bottlenecks and ensuring consistent throughput.

> [!CAUTION]
> Per Device Configuration **cannot be used with** Network Profiles its one or the other
---

## Intent Based Configuration Path

### Challenges, Caveats, and Benefits

**Intent** refers to the concept of defining a single, clear intent for how data should flow through the network.

- **Challenges**: Establishing a clear intent can be difficult in complex environments, especially when multiple stakeholders are involved. Additionally, ensuring that all devices adhere to this intent requires robust policy enforcement mechanisms.

- **Caveats**: While this approach simplifies network management, it may limit flexibility in adapting to changing business needs or unexpected network conditions. Additionally, **Brownfield** devices sometimes has pre-existing configurations which may need to be modified and in some instances removed. This sometimes requires either a **Normalization** script **or** alternatively the device being **erased** and **reloaded**.

- **Benefits**: The primary benefit is enhanced clarity and efficiency in network operations. By having a single intent, organizations can streamline decision-making and reduce the risk of misconfigurations.

---

> [!TIP]
> For many reasons and specifically with Wireless the Wireless Settings, and Feature Templates in the UI are the best way I can recommend for managing Wireless controllers at scale, with or without Fabric. The reason, is that Per Device Configuration is just as it sounds iterating through settings on multiple controllers, whicch will never be as quick or nimble at scale as the UI. I also do not advocate for building templates for controllers as often the radio resets become painful at scale. This is elegantly solved by Wireless Intent.

---

## Catalyst Center Scaleability and Deployment

### Form Factors 

Catalyst Center is today offered in the following environments:

* **Amazon Web Services (AWS)** - as a virtual appliance (sized to Medium HW Appliance Specifications)
* **Virtual Appliance** - as a virtual appliance for VMware ESXi (sized to Medium HW Appliance Specifications)
* **Hardware Appliances** - as dedicated Hardware Appliances (Medium, Large and Extra Large Sized Appliances)

> [!WARNING]
> Virtual Appliances cannot be joined to a cluster for HA nor can they be used in a DR scenario as they were designed to use VMwares software redundancy mechanisms.

### Sizing of Appliances

In this chart below you will see all the form factors that Catalyst Center is offered in along with the scale of those appliances in numerical form. Consider each of these numberss carefully and try not to build catalyst center to close to the numbers and allow for growth. Issues can occur when the appliance is overloaded.

![SIZING Chart](../ASSETS/TUTORIALS/MANAGEMENT/SIZING.png?raw=true "Catalyst Center Sizing")

> [!TIP]
> In this chart please be aware that only in an Extra Large Appliance Cluster can we increase scalability to the numbers of devices and Endpoints. Issues can occur when the appliance is overloaded.

### High Availability (HA) & Disaster Recovery (DR)

If when building Catalyst Center **High Availability** is desired, then we should build the following:

* For a Hardware Appliance Deployment, we should build a **3-Node Cluster**
* For a Virtual Appliance, we will rely on VMwares Software Redundancy techniques.

#### 3-Node Cluster

When building a 3-node Cluster be aware that **10 ms** of latency is the requirement between nodes with Layer 2 adjacency. Building a 3-node Cluster which extends across between two DC's is not supported by TAC and not recommended by Cisco. 

Extra Large Appliance 3-node Clusters can increase scalability to the numbers of devices and Endpoints that can be managed and so well placed Geo located Catalyst Centers can reduce the number of Catalyst Centers Deployed.

### High Availability (HA) vs Disaster Recovery (DR)

When deciding to build a Disaster recovery site, remember that the DR site of Catalyst Centers is not managing devices when in standby. The Deployment can be made in the following ways:

* 1:1 DR
* 3:3 DR

As depicted below:

![DR 1:1](../ASSETS/TUTORIALS/MANAGEMENT/1-1DR.png?raw=true "Catalyst 1:1 DR")
![DR 3:3](../ASSETS/TUTORIALS/MANAGEMENT/3-3DR.png?raw=true "Catalyst 3:3 DR")

Deciding on whether to forgoe HA for DR, please refer to this chart to understand the Recovery Time Objectives to understand whether this will meet your needs, and consider the scale of the appliances. Notice that between the DR sites lower bandwidth is supported than between nodes in a cluster with the option of IPSEC encryption. The Recovery time though is about double that of HA.

![DR HA Recovery Chart](../ASSETS/TUTORIALS/MANAGEMENT/HAvsDR.png?raw=true "Catalyst HA vs DR Comparison")

### Geographic Deployments and Constraints

Catalyst Center must be deployed within the following Latency Specifications. Exceeding these Specifications can result in abnormal management behaviour and customer frustration. Catalyst Center must be within **200 ms** of all managed equipment, except the Access Point managed by a controller as shown below.

![DR HA Recovery Chart](../ASSETS/TUTORIALS/MANAGEMENT/LATENCY.png?raw=true "Catalyst HA vs DR Comparison")

#### National Deployment Model

When considering Geographic coverage sizing may be taken into account as in this deployment for example, it might be that perhaps the following sizing needs to be accounted for:

|Parameters     |East Coast|West Coast|Total   |
|---------------|----------|----------|--------|
|Network Devices| 7000     | 1500     | 8500   |
|Access Points  | 16000    | 3000     | 19000  |
|Endpoints      | 75000    | 25000    | 100000 |

In this case while you could put all of this on 1 XL cluster probably, it would not be able to take any growth at all so standing up replacement network equipment could become a real problem as network refreshes occurred. Thus splitting the load on the East Cluster with a 3:3 HA set of XL appliances and DR, and on the West Cluster a 1:1 DR design with a set of L appliances is used. 

![DR HA Recovery Chart](../ASSETS/TUTORIALS/MANAGEMENT/NATIONAL.png?raw=true "Catalyst HA vs DR Comparison")

#### Global Geo Diverse Deployment Model

When considering Geographic coverage sizing may be taken into account as in this deployment for example, it might be that perhaps the following sizing needs to be accounted for:

|Parameters     |AMER   |APJC   |EMEA   |Total   |
|---------------|-------|-------|-------|--------|
|Network Devices| 7000  | 1500  | 1500  | 10000  |
|Access Points  | 16000 | 3000  | 3000  | 22000  |
|Endpoints      | 75000 | 25000 | 25000 | 125000 |

In this case the RTT over 200 ms to managed equipment across the WAN is an issue. While from a sizing point of view a smaller deployment may work Geographical constraints come into play. Thus splitting the load on the AMER Cluster with a 3:3 HA set of XL appliances and DR, and in both APJC and EMEA Clusters a 1:1 DR design with a set of L appliances is used. 

![DR HA Recovery Chart](../ASSETS/TUTORIALS/MANAGEMENT/GLOBAL.png?raw=true "Catalyst HA vs DR Comparison")

## Conclusion

The Catalyst Center provides a comprehensive solution for managing complex network environments. By understanding the implications of brownfield and greenfield scenarios, organizations can better align their objectives with their network management strategies. Key objectives such as policy, compliance, consistency, reusability, and scalability can be effectively addressed, leading to a more efficient and reliable network infrastructure.

> [!TIP]
> Carefully weigh the **Caveats**, **Challenges**, and Benefits before you go down a path. Remember a wise person once said ***"Once you start down the path forever will it dominate your destiny"***

---

> [!IMPORTANT]
> **Feedback:** If you found this set of **labs** or **content** helpful, please fill in comments on this feedback form [give feedback](https://github.com/kebaldwi/DNAC-TEMPLATES/discussions/new?category=feedback-and-ideas).</br></br>
**Content Problems and Issues:** If you found an **issue** on the **lab** or **content** please fill in an [issue](https://github.com/kebaldwi/DNAC-TEMPLATES/issues/new) include what file, along with the issue you ran into. 

> [**Return to Main Menu**](../README.md)