# text-to-image-bca
Using flask and pillow library. 
The folder names will be unique(using uuid4) and the image folder will be deleted once downloaded. 

/home:    returns index page
/convert: takes in file uploaded as input and converts each question and answer into ordered images(instead of saving, can store imaage objects in a dictionary and           send it to another endpoint)
/download:converts the folder to zip file, downloads and deletes the original as well as zip file

###Improvements: 
- Heavily assumes that file will be in a particular format.  
- No error handling
- Make an API instead of upload endpoint
- Give user ability to modify text and image size
