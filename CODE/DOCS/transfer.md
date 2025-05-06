var jsonData = JSON.parse(pm.response.text());
var taskId = jsonData.response.taskId;

// Function to check the status of the NETCONF credential creation
function checkCredentialStatus(taskId) {
    const url = `https://${pm.environment.get("CCip")}${taskId}`;
    const token = pm.environment.get("TOKEN");

    pm.sendRequest({
        url: url,
        method: 'GET',
        header: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        }
    }, function (err, res) {
        if (err) {
            console.error(err);
            pm.test("Error in API call", () => { pm.expect.fail("API call failed"); });
            return;
        }

        const responseData = JSON.parse(res.text());
        if (responseData.response.isError) {
            pm.test("NETCONF Credential creation failed", () => {
                pm.expect(responseData.response.progress).to.include("failed");
                pm.expect(responseData.response.failureReason).to.include("Duplicate credential");
            });
        } else {
            pm.test("NETCONF Credential created successfully", () => {
                pm.expect(responseData.response.progress).to.not.include("failed");
            });
        }
    });
}

// Check if the executionId and taskId are present
if (jsonData.executionId && taskId) {
    pm.test("NETCONF Credential creation initiated", () => {
        pm.expect(pm.response.text()).to.include("taskId");
    });
    // Call the function to check the status of the credential creation
    checkCredentialStatus(taskId);
} else {
    pm.test("NETCONF Credential already created", () => {
        pm.expect(pm.response.text()).to.include("taskId");
    });
    postman.setNextRequest("Get CredentialIDs");
}

setTimeout(function() {}, 25000);
postman.setNextRequest("Get CredentialIDs");
