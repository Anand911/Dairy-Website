/*const scanner=new Html5QrcodeScanner('reader',{
    qrbox:{
        height:250,
        width:250
    },
    fps:20
})
scanner.render(success,error);
function success(result) {
    console.log(result);
    scanner.clear()
}

function error(err) {
    scanner.stop();
    console.error(err);
}*/ 
const scanBtn=document.getElementById("SwitchScan")
const switchCam=document.getElementById("camera")
let currState=false
const couponForm=document.forms["couponForm"]

const html5QrCode = new Html5Qrcode("reader");
Html5Qrcode.getCameras().then(devices => {
    /**
     * devices would be an array of objects of type:
     * { id: "id", label: "label" }
     */
    //console.log(devices);
    if (devices && devices.length) {
        var cameraId = devices[0].id;
        devices.forEach(device => {
            switchCam.innerHTML +=`<option value="${device.id}">${device.label}</option>`
        });
        // .. use this to start scanning.
    }
}).catch(err => {
    // handle err
});
const qrCodeSuccessCallback = (decodedText, decodedResult) => {
    /* handle success */
    console.log(decodedText);
    couponForm.coupon_id.value=decodedText
    
    html5QrCode.stop()
    couponForm.submit()
   
    
    
};
const qrCodeErrorCallback=(err)=>{
    
};
const config = { fps: 20, qrbox: { width: 250, height: 250 } };


scanBtn.addEventListener('click', () => {
    if (!currState)
    {
        // If you want to prefer back camera
        html5QrCode.start({ facingMode: "environment" }, config, qrCodeSuccessCallback, qrCodeErrorCallback);
        scanBtn.innerHTML='Stop Scanning'
        currState=true
    }
    else {
        if (html5QrCode.isScanning)
        html5QrCode.stop()
        scanBtn.innerHTML = 'Start Scanning'
        currState = false
    }
})
//Switch Camera
switchCam.addEventListener('change',()=>{
    let cameraId = switchCam.value
    if (html5QrCode.isScanning)
        html5QrCode.stop().then((ignore) => {
            // QR Code scanning is stopped.
            if (cameraId != '') {
                html5QrCode.start(cameraId, config, qrCodeSuccessCallback, qrCodeErrorCallback);
                scanBtn.innerHTML = 'Stop Scanning'
                currState = true
            }
            else {
                currState = false
                scanBtn.innerHTML = 'Start Scanning'
            }
        }).catch((err) => {
            // Stop failed, handle it.
            console.log(err);
        });
    else{
        if (cameraId != '') {
            html5QrCode.start(cameraId, config, qrCodeSuccessCallback, qrCodeErrorCallback);
            scanBtn.innerHTML = 'Stop Scanning'
            currState = true
        }
        else {
            currState = false
            scanBtn.innerHTML = 'Start Scanning'
        }
    }
    
})


//File Input
const fileinput = document.getElementById('qr-input-file');
fileinput.addEventListener('change', e => {
    if(html5QrCode.isScanning)
    html5QrCode.stop()

    if (e.target.files.length == 0) {
        // No file selected, ignore 
        return;
    }
    //html5QrCode.stop()
    const imageFile = e.target.files[0];
    // Scan QR Code
    html5QrCode.scanFile(imageFile, true)
        .then(qrCodeSuccessCallback)
        .catch(qrCodeErrorCallback);
});