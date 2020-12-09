FROM alpine:edge

RUN apk add --no-cache \
    chromium \
    chromium-chromedriver \
    bash \
    python3 \
    git \
    py3-pip \
    docker \
    curl \
    ca-certificates

RUN pip3 install selenium \
pip install pytest \
pip install webdriver-manager

COPY main.py /bin/

WORKDIR  ./

ENV CHROME_BIN=/usr/bin/chromium-browser \
    CHROME_PATH=/usr/lib/chromium/
RUN chmod +x /bin/main.py

CMD pytest /bin/main.py
