FROM python:3.10
WORKDIR /cnn_project
COPY requirements.txt .
RUN apt-get update && \
    apt-get install -y python3-tk && \
    pip install --no-cache-dir -r requirements.txt
COPY . /cnn_project
CMD ["/bin/bash"]