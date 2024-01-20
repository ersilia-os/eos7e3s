FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install rdkit==2022.9.4
RUN pip install pandas==2.0.3
RUN pip install "flaml[automl]"==2.1.1
RUN pip install numpy==1.24.4
RUN pip install scikit-learn==1.3.2
RUN pip install joblib==1.2.0
RUN pip install -U pip==23.3.2
RUN pip install eosce==0.1.0
RUN pip install "ray[tune]"==2.9.1
RUN pip install catboost==1.2.2



WORKDIR /repo
COPY . /repo
