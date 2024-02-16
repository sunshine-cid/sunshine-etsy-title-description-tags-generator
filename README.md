# Be aware that Google transitioning Bard to Gemini has (and breaking bardapi) rendered this project mostly inoperable. I will update the project once we get a working API for Google Gemini 

# sunshine-etsy-title-description-tags-generator
This program is made to simplify the process of requesting Google Bard responses for Etsy products. It take a standard AI descriptor and returns potential product titles, descriptions, and etsy tags

---------------------------------------------------------

Install the latest version of Python from:
>https://www.python.org/downloads/
Be sure to check the "Add to PATH" checkbox when installing

For the time being, in 64-bit Windows, a special version of BardAPI is required. If you're runnign 64-bit Windows use: 
>pip install bardapi==0.1.23a

Otherwise you can use the standard:
>pip install bardapi

From the command line navigate to where you've downloaded the main.py file nad execute it with 
>python main.py

![EtsyBard](https://github.com/sunshine-cid/sunshine-etsy-title-description-tags-generator/assets/7285352/3f45cfe2-bab8-4683-bf19-eaf6c53e842d)

From there login to the bard interface at https://bard.google.com in an incognito window.

In Chrome hit F12, select Application, on the left navigate to Cookies under storage. Select bard.google.com. Inside you should find the associated text strings you need to copy into the appropriate text fields.

In Firefox hit F12, select Storage. Inside select Cookies, and select bard.google.com. Inside you should find the associated text strings you need to copy into the appropriate text fields.
