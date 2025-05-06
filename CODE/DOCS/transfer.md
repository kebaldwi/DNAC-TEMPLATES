var jsonData = JSON.parse(responseBody);
setTimeout(function(){}, 15000);

function setCredential(descriptionKey, globalKey, siteKey, dataArray, type) {
    const description = pm.iterationData.get(descriptionKey);
    if (description) {
        const credential = dataArray.find(item => item.description === description);
        if (credential) {
            pm.environment.set(globalKey, credential.id);
            pm.environment.set(siteKey, credential.id);
            pm.test(`${type} credentials acquired`, () => {
                pm.expect(pm.response.text()).to.include(type.toLowerCase());
            });
        }
    } else {
        pm.environment.set(siteKey, pm.environment.get(globalKey));
    }
}

if (pm.iterationData.get("HierarchyParent") === "Global") {
    setCredential("DcloudSnmpRO-Desc", "GlobalCredentialSnmpRO", "SiteCredentialSnmpRO", jsonData.snmp_v2_read, "SNMP RO");
    setCredential("DcloudSnmpRW-Desc", "GlobalCredentialSnmpRW", "SiteCredentialSnmpRW", jsonData.snmp_v2_write, "SNMP RW");
    setCredential("DcloudUser", "GlobalCredentialCli", "SiteCredentialCli", jsonData.cli, "CLI");
} else {
    setCredential("DcloudSnmpRO-Desc", "GlobalCredentialSnmpRO", "SiteCredentialSnmpRO", jsonData.snmp_v2_read, "SNMP RO");
    setCredential("DcloudSnmpRW-Desc", "GlobalCredentialSnmpRW", "SiteCredentialSnmpRW", jsonData.snmp_v2_write, "SNMP RW");
    setCredential("DcloudUser", "GlobalCredentialCli", "SiteCredentialCli", jsonData.cli, "CLI");
}

postman.setNextRequest("Assign Credentials");
