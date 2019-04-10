FROM jupyter/base-notebook:65761486d5d3

USER $NB_USER

RUN mkdir -p /home/$NB_USER/.jupyter/custom
ADD custom.js /home/$NB_USER/.jupyter/custom
COPY jupyter_notebook_config.py /home/$NB_USER/.jupyter/
