FROM python:3.6-slim

RUN apt-get update && apt-get install -y git gcc make curl

ADD ./bot/requirements.txt /tmp
ADD ./bot /bot
ADD ./scripts /scripts

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    python -c "import nltk; nltk.download('stopwords');"

WORKDIR /bot

ENV TRAINING_EPOCHS=20                     \
    ROCKETCHAT_URL=rocketchat:3000         \
    MAX_TYPING_TIME=4                      \
    MIN_TYPING_TIME=1                      \
    WORDS_PER_SECOND_TYPING=5              \
    ROCKETCHAT_ADMIN_USERNAME=admin        \
    ROCKETCHAT_ADMIN_PASSWORD=admin        \
    ROCKETCHAT_BOT_USERNAME=bot            \
    ROCKETCHAT_BOT_PASSWORD=bot            \
    ENVIRONMENT_NAME=localhost             \
    BOT_VERSION=last-commit-hash           \
    ENABLE_ANALYTICS=False                 \
    ELASTICSEARCH_URL=elasticsearch:9200

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
    
CMD python /scripts/bot_config.py -r $ROCKETCHAT_URL                        \
           -an $ROCKETCHAT_ADMIN_USERNAME -ap $ROCKETCHAT_ADMIN_PASSWORD    \
           -bu $ROCKETCHAT_BOT_USERNAME -bp $ROCKETCHAT_BOT_PASSWORD     && \
    make train && make run-rocketchat
