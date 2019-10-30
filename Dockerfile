FROM centos:7

LABEL MAINTANER="Abhinav Chelluri <chelluri.abhinav@gmail.com>"

RUN yum -y update
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm
RUN yum -y update
RUN yum install -y python36u python36u-libs python36u-devel python36u-pip
RUN yum groupinstall -y "Development Tools"
RUN yum install -y vim


WORKDIR /FlaskJWTApp

ADD . /FlaskJWTApp

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /FlaskJWTApp/requirements.txt

RUN pip3.6 install -r requirements.txt

RUN chown $USER:$USER /FlaskJWTApp

EXPOSE 5000

CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:5000", "--log-file=app.log", "--capture-output", "--log-level=debug", "wsgi:app"]
