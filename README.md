<h3>This repository is used to deploy Python Selenium in AWS Lambda, and extract results of the student from SPM official website.</h3>  
  
<b>IMPORTANT! </b>  
<b>DO NOT RUN IT DIRECTLY LOCALLY</b>  
The runtime MUST be <b>Python 3.7</b>.

---
<b>Deployment of Python selenium</b>  

Steps to deploy:  
    1. Create two layers in AWS Lambda console, with the zip files in "layers/" folder.  
    2. Create a lambda function  
    3. Upload "main.py" in a zip to the function  
    4. Add the layers to the function.  
The function should now able to run Python selenium in AWS Lambda function.  

You may refer to the tutorial video below for the deployment of python selenium:  
https://youtu.be/b49Y3NGJX68  

---
<b>Function testing</b>  
To test the function, please include the JSON body below:  
```
{
    "url": "",
    "ag": ""
}
```

`"url"` is the URL obtained from the certificate's QR code,  
`"ag"` is the SPM examination number <em>(Angka Giliran)</em> of the student.  

The response will contain the text extracted from the URL provided.  