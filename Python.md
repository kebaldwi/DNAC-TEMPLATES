# Python and Cisco DNA Center [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)

## Python and DNA Center
It is no secret that Python programming language has gained tremendous popularity in the developer community. 
As reported by 2021 Stack Overflow Developer Survery, Python was identified as the number one most wanted language among developers who are not currently using it. DNA Center has a large number of very powerful automation workflows already built into the product (ie Plug and Play, SWIM, SDA, Templates etc), which are also exposed to the operator via programmable API interfaces which can be leverged to further integrate DNA Center into more complex or customized automation workflows.
Given Python popularity, it makes sense to review how you can apply basic programming practices to automate common tasks in your own network with DNA Center APIs.

DNA Center programmable REST API capabilities are covered in our previous tutorial section, [REST API](./RestAPI.md) - REST API and Cisco DNA Center. This section will build upon API foundational concepts introduced in that earlier section

In this section we will cover Python integrations with Cisco DNA Center's "Business and Network Intent APIs".


## Prerequisites
> It is assumed that the reader has basic level familiarity with Python language before proceeding with examples outlined in this section. 
> Please ensure that you have Python v3.x installed on your machine 

![json](images/dnac_python_automation.png?raw=true "Business and Network Intent APIs")

### Python installation, MacOS

> Install Homebrew package manager
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

> Install PyEnv using HomeBrew. PyEnv is a CLI utility that helps you manage Python installations on your computer.
```
brew install pyenv
pyenv init

nano ~/.zshrc
Paste the eval line at the end of the file
eval "$(pyenv init -)"

press Control + X, type Y and press Enter when prompted for the file name

Now that PyEnv is installed and configured, exit and reload the Terminal
```

With PyEnv is installed and configured, we can install Python. Example below is installing Python version 3.9.1

```
pyenv install 3.9.1
pyenv global 3.9.1
```

And finally, verification of installed Python environment

```
pyenv version
```

### Python installation, Windows
> [Installing Python](https://www.python.org/downloads/) - Python distributions


> **Feedback:** If you found this repository please fill in comments and [**give feedback**](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

> [**Return to Main Menu**](./README.md)