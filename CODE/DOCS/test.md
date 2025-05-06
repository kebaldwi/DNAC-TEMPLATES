var jsonData = JSON.parse(responseBody);
var DeviceList = pm.iterationData.get("DeviceList");
console.log(DeviceList)
var DeviceList = DeviceList.split(",");
var DeviceId = "";
var DeviceIp = "";
var FLAG = DeviceList.length;
pm.environment.set("FLAG", FLAG);
for (var dl = 0; dl < DeviceList.length; dl++) {
    for (var i = 0; i < jsonData.response.length; i++) {
               if (DeviceList[dl] === jsonData["response"][i]["managementIpAddress"]) {
            
            if (dl === 0){
                DeviceId = jsonData["response"][i]["id"];
                DeviceIp = jsonData["response"][i]["managementIpAddress"];
            }
            else {
                DeviceId = DeviceId + "," + jsonData["response"][i]["id"];
                DeviceIp = DeviceIp + "," + jsonData["response"][i]["managementIpAddress"];
            }
            break;
        }
    }
    
}
pm.environment.set("DeviceId", DeviceId);
pm.environment.set("DeviceIp", DeviceIp);
pm.test("Devices acquired",() => {pm.expect(pm.response.text()).to.include("response");});

postman.setNextRequest("Deploy Template");  
