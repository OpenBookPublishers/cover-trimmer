FROM python:3.8.0-slim-buster

WORKDIR /cover

RUN apt-get update && \
    apt-get install -y gcc poppler-utils

RUN apt-get install -y git

RUN rm -rf /var/cache/apt/*

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

## replace library version (delete when mutation PR is merged)
RUN git clone -b feature/thoth_8_compatibility \
              https://github.com/lb803/thoth-client
RUN rm -rf /usr/local/lib/python3.8/site-packages/thothlibrary/*
RUN mv ./thoth-client/thothlibrary/* \
       /usr/local/lib/python3.8/site-packages/thothlibrary/
##############################################################

COPY ./src/ ./

ENTRYPOINT ["python3"]

CMD ["thoth_wrapper.py", "--help"]