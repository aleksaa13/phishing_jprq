# phishing_jprq

***Idea and instructions

**Install python3, flask and jprq

1) Run a Python (flask) app on port 5000 with *python3 endpoint.py* 
2) Also use Python to run a HTTP server on port 8000 which will contain phishing page. *python3 -m http.server* after entering phishing_jprq directory! 
3) Open tunnels from your localhost to the outer Internet with jprq. *jprq 8000* , *jprq5000*. 
4) Copy the link from jprq to your port 8000 (where your phishing page is) and send it to someone.
5) When the person enters the credentials, phishing page will send them to your application on port 5000 and in it's terminal you will be able to see them.
