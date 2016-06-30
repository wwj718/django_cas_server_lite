# django_cas_server_lite
精简版的cas服务器，尽量减少依赖

# install
*  git clone https://github.com/wwj718/django_cas_server_lite
*  virtualenv cas_env
*  . env/bin/activate.fish
*  cd django_cas_server_lite
*  pip install -r requirements.txt //如果网络不便，也可以手动安装 requirements.txt里的依赖，我已经把依赖控制到最精简了
*  python manage.py runserver 

# todo
*  是remote database backend变为可选功能，采用配置文件实现


# 部署
依然需要先进入cas_env

### gunicorn
时候用gunicorn：

`gunicorn django_cas_server_lite.wsgi:application --bind 127.0.0.1:8001 -w 4`, `-w 4` 表示4个worker，之后用nginx反向代理

gunicorn可以先跑在tmux里，如果需要将其设为守护进程，使用Supervisor

### nginx
```
:::text
server {
        listen 80;             #端口
        server_name cas.just4fun.site;   #访问域名
        #root /home/bob/dylan/;
        access_log /tmp/access.log;
        error_log /tmp/access.log;
        location / {
                proxy_set_header X-Forward-For $proxy_add_x_forwarded_for;
                proxy_set_header Host $http_host;
                proxy_redirect off;
                if (!-f $request_filename) {
                        proxy_pass http://127.0.0.1:8001;  #这里是flask应用的gunicorn端口
                        break;
                }
        }
}
```

# 对Open edX用户
如果你未使用Open edX，可以忽视这条

如果你使用Open edX，你可以利用Open edX的edxapp env，这样一来依赖都是完备的,不需要额外安装

```bash
git clone https://github.com/wwj718/django_cas_server_lite
cd django_cas_server_lite
. /edx/app/edxapp/edxapp_env
gunicorn django_cas_server_lite.wsgi:application --bind 127.0.0.1:8001 -w 4
```

之后配置nginx即可
