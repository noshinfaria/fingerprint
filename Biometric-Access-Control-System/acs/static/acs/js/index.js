function captureFP() {
    CallSGIFPGetData(SuccessFunc, ErrorFunc);
  }
  
  function SuccessFunc(result) {
    console.log(result);  // Helpful for debugging

    if (result.ErrorCode === 0) {
      if (result && result.BMPBase64.length > 0) {
        const fpImage = document.getElementById("FPImage1").src = "data:image/bmp;base64," + result.BMPBase64;
        document.getElementById('img_base64').value = 'data:image/bmp;base64,' + result.BMPBase64;
        // document.getElementById('submit-button').click();
        // Hide the SVG and show the captured image
        // document.getElementById('captureSVG').style.display = 'none';
        // fpImage.style.display = 'block';
      }
    } else {
      alert("Fingerprint Capture Error Code: " + result.ErrorCode + ".\nDescription: " + ErrorCodeToString(result.ErrorCode) + ".\n\nPlease try again😔");
    }
  }
  
  function ErrorFunc(status) {
    alert("Check if SGIBIOSRV is running; Status = " + status + ":");
  }
  
  function CallSGIFPGetData(successCall, failCall) {
    var uri = "https://localhost:8443/SGIFPCapture";
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function () {
      if (xmlhttp.readyState === 4 && xmlhttp.status === 200) {
        var fpobject = JSON.parse(xmlhttp.responseText);
        successCall(fpobject);
      } else if (xmlhttp.status === 404) {
        failCall(xmlhttp.status);
      }
    };
    var params = "Timeout=10000&Quality=50&licstr=" + encodeURIComponent(secugen_lic) + "&templateFormat=ISO&imageWSQRate=0.75";
    xmlhttp.open("POST", uri, true);
    xmlhttp.send(params);
    xmlhttp.onerror = function () {
      failCall(xmlhttp.statusText);
    };
  }
  
  var secugen_lic = "";
  
  function ErrorCodeToString(ErrorCode) {
    var Description;
    switch (ErrorCode) {
      case 51:
        Description = "System file load failure";
        break;
      case 52:
        Description = "Sensor chip initialization failed";
        break;
      case 53:
        Description = "Device not found";
        break;
      case 54:
        Description = "Fingerprint image capture timeout";
        break;
      case 55:
        Description = "No device available";
        break;
      case 56:
        Description = "Driver load failed";
        break;
      case 57:
        Description = "Wrong Image";
        break;
      case 58:
        Description = "Lack of bandwidth";
        break;
      case 59:
        Description = "Device Busy";
        break;
      case 60:
        Description = "Cannot get serial number of the device";
        break;
      case 61:
        Description = "Unsupported device";
        break;
      case 63:
        Description = "SgiBioSrv didn't start; Try image capture again";
        break;
      default:
        Description = "Unknown error code or Update code to reflect latest result";
        break;
    }
    return Description;
  }
  