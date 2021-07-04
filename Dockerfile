FROM python:3.6-buster

RUN pip install jupyter wand  myqlm myqlm-interop[all] 

RUN python -m qat.magics.install

WORKDIR /myqlm

CMD ["jupyter","notebook","--port=80","--ip=0.0.0.0","--allow-root"]
