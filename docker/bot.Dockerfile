FROM python:3.6-slim

RUN apt-get update && apt-get install -y git gcc make curl

ADD ./bot/requirements.txt /tmp

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    python -c "import nltk; nltk.download('stopwords');"

RUN apt-get -yq remove --purge --auto-remove -y ${BUILD_PACKAGES}; \
    apt-get -yq clean; \
    apt-get -yq autoclean; \
    apt-get -yq autoremove; \
    rm -rf /tmp/* /var/tmp/*; \
    rm -rf /var/lib/apt/lists/*; \
    rm -rf /var/cache/apt/archives/*.deb \
        /var/cache/apt/archives/partial/*.deb \
        /var/cache/apt/*.bin; \
    find /usr/lib/python3 -name __pycache__ | xargs rm -rf; \
    find /bot -name __pycache__ | xargs rm -rf; \
    rm -rf /root/.[acpw]*;

ADD ./bot /bot
ADD ./scripts /scripts


WORKDIR /bot

ENV TRAINING_EPOCHS=20                     \
    MAX_TYPING_TIME=4                      \
    MIN_TYPING_TIME=1                      \
    WORDS_PER_SECOND_TYPING=5              \
    ENABLE_ANALYTICS=False                 \
    ELASTICSEARCH_URL=elasticsearch:9200


CMD python /scripts/bot_config.py -r $ROCKETCHAT_URL                        \
           -an $ROCKETCHAT_ADMIN_USERNAME -ap $ROCKETCHAT_ADMIN_PASSWORD    \
           -bu $ROCKETCHAT_BOT_USERNAME -bp $ROCKETCHAT_BOT_PASSWORD        \
           -be $ROCKETCHAT_BOT_EMAIL && \
    make train && make run-rocketchat
