FROM ubuntu
MAINTAINER Jim Yeh <lemonlatte@gmail.com>

RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl
RUN ln -sf /bin/false /usr/sbin/policy-rc.d

RUN apt-get update -y
RUN apt-get -y -q install python-pip git python-dev
RUN pip install virtualenv

RUN git clone --recursive git://github.com/mozilla/moztrap
RUN cd /moztrap && git checkout 1.5.4

RUN apt-get install -y libmysqlclient-dev build-essential
RUN apt-get install -y mysql-client
RUN apt-get clean

RUN cd moztrap && virtualenv .venv
ADD tools/with_venv.sh moztrap/
RUN chmod 755 moztrap/with_venv.sh
RUN cd moztrap && ./with_venv.sh easy_install distribute==0.6.28
RUN cd moztrap && ./with_venv.sh ./bin/install-reqs
ADD local.py moztrap/moztrap/settings/

ADD setup_admin.py moztrap/
ADD run.sh /
RUN chmod 740 run.sh

EXPOSE 8000
CMD ["/run.sh"]
