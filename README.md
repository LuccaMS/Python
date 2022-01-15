# Python
That is a backend project using the python Library "Flask" and a few cryptographic libraries
You can use the command below to install all requirements to be able to run the project.
# pip3 install -r requirements.txt

# Warning : That project has 2 branches, which one of them contains different methods and routes

# Part 1

There are 2 main routes, the first one which is the home route '/' and the route '/sha-256', keep in mind that you can acess directly from your browser without using any API Plataform test, as you can see in the image below, you will be able to select a file from your computer and then the server will return the sha-256 hash of the file that you uploaded, there is a list of extensions that are allowed, {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

![image](https://user-images.githubusercontent.com/64712028/148701161-59309102-c47e-4eaa-b6c2-c1244d7d8422.png)

Main page where you can select the file that you want to upload.

![image](https://user-images.githubusercontent.com/64712028/148701178-6d9e2e27-2441-48d0-b75e-06795705d1c2.png)

The hash that the server will return to you, you can click in the button to return to the first page and keep using the site :)

# Part 2
The second part of the code is used to generate either a 1024 or 2048 RSA keys , you have 3 routes to work with, the main one is the home '/' that will contain two buttons, one to generate a 1024 and the other a 2048 key, both are using the public_exponent 65537 , keep in mind that the public key is being written in a file called key.pem

![image](https://user-images.githubusercontent.com/64712028/148701558-e0c2ea32-05e6-4827-9990-4df4f23ceb4e.png)

Main area

![image](https://user-images.githubusercontent.com/64712028/148701562-f44d288c-6847-4ec8-b711-eb479dfa54a9.png)

Generated key
