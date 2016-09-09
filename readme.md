# django_cas_server_lite
精简版的cas服务器，尽量减少依赖

# install
*  git clone https://github.com/wwj718/django_cas_server_lite
*  virtualenv cas_env
*  . cas_env/bin/activate.fish
*  cd django_cas_server_lite
*  pip install -r requirements.txt //如果网络不便，也可以手动安装 requirements.txt里的依赖，我已经把依赖控制到最精简了
*  python manage.py runserver 

# uasge
/django_cas/login

# todo
*  是remote database backend变为可选功能，采用配置文件实现


# 部署
依然需要先进入cas_env


