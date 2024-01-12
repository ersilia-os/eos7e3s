FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit==2023.9.2
RUN pip install pandas==2.0.3
RUN pip install flaml==2.1.1
RUN pip install numpy==1.24.4
RUN pip install scikit-learn==1.3.2
RUN pip install matplotlib==3.7.4
RUN pip install -U pip==23.3.2
RUN pip install -U setuptools wheel==0.41.2
RUN pip install mxnet==1.9.1
RUN pip install autogluon==1.0.0
RUN pip install -U ipykernel
RUN pip install eosce==0.1.0

WORKDIR /repo
COPY . /repo
