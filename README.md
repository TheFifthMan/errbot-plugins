# slackbot
Plugins for slackbot. Basic on [errbot](http://errbot.io/en/latest) 

# How to deploy your server
## 1. Install supervisor
```
pip install supervisor
``` 
## 2. Configure supervisor
```
echo_supervisord_conf > <your-config-path>/supervisord.conf

----
[unix_http_server] 
file=/var/run/supervisor.sock ; (the path to the socket file) 
[inet_http_server] ; inet (TCP) server disabled by default 
port=127.0.0.1:9001 ; (ip_address:port specifier, *:port for ;all iface) 
username=user ; (default is no username (open server)) 
password=123 ; (default is no password (open server))
[supervisord]
logfile=/var/log/supervisor/supervisord.log 
logfile_maxbytes=50MB 
logfile_backups=10          
loglevel=info               
pidfile=/var/run/supervisord.pid 
nodaemon=false              
minfds=1024                 
minprocs=200  
[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface
[supervisorctl]
serverurl=unix:///var/run/supervisor.sock 
serverurl=http://127.0.0.1:9001 
username=anonymous           
password=wzw01@1992          
[include]
files = <your-path-to-config>/*.conf

```
## 3. Install Python3
## 4. Deploy Code
```
python3 -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
```
## 5. slackbot for supervisor
```
[program:slackbot]
command = <your-path-source-code>/slackbot/venv/bin/errbot
user=www-data
stdout_logfile=/var/log/supervisor/errbot.log
stderr_logfile = /var/log/supervisor/errbot_err.log
redirect_stderr = true
directory =<your-path-to-source-code>/slackbot/
startsecs = 3
autorestart = true
environment = ADMIN=xxx,SLACKTOKEN=xxxx
```

## 6. start 

```
$supervisorctl -c supervisor.conf
$reread
$add slackbot
$status
```

# summary
pretty easy.