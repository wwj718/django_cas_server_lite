# django_cas_server_lite
精简版的cas服务器，尽量减少依赖

# install
* git clone https://github.com/wwj718/django_cas_server_lite
*  open http://127.0.0.1:8000/django_cas/login

# todo
*  是remote database backend变为可选功能，采用配置文件实现


# 部署
直接用django跑：

`python manage.py runserver --settings=django_cas_server_lite.production 0.0.0.0:8000`


### gunicorn
时候用gunicorn：

`gunicorn django_cas_server_lite.wsgi:application --bind 127.0.0.1:8001`，之后用nginx反向代理

`gunicorn django_cas_server_lite.wsgi:application --bind 0.0.0.0:8001 -w 4` ：跑4个worker，gunicorn可以先跑在tmux里，如果需要将其设为守护进程，使用Supervisor

### nginx
```

```

# 对Open edX用户
如果你未使用Open edX，可以忽视这条

如果你使用Open edX，你可以利用Open edX的edxapp env，这样一来依赖都是完备的

