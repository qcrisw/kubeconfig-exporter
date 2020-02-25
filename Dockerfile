FROM python:3.8

RUN pip3 install --upgrade pip && \
    pip3 install pyyaml

COPY . /home/

ENTRYPOINT ["/home/export-kubeconfig.py"]
