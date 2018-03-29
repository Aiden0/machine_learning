FROM jupyter/scipy-notebook


USER root


RUN pip install --upgrade jupyter_contrib_nbextensions
RUN jupyter contrib nbextension install --sys-prefix
RUN jupyter nbextension enable toc2/main
RUN jupyter nbextension enable spellchecker/main
#RUN jupyter nbextension enable codefolding/main

RUN jupyter nbextension enable --py widgetsnbextension

USER jovyan

ENV PYTHONPATH $PYTHONPATH:/home/jovyan/work