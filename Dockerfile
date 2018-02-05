FROM jupyter/scipy-notebook:11be019e4079

USER root

RUN echo deb http://ftp.debian.org/debian jessie-backports main >> /etc/apt/sources.list

RUN apt-get -y update && apt-get -t jessie-backports -y install ffmpeg

RUN pip install line-profiler

USER jovyan

ENV PYTHONPATH $PYTHONPATH:/home/jovyan/work