FROM python:3.6-slim

RUN apt-get update && apt-get install -y git gcc make curl

ADD ./actions/actions.requirements.txt /tmp/

RUN pip install --upgrade pip && \
    pip install -r /tmp/actions.requirements.txt

ADD ./actions/actions.py /bot/actions/actions.py
ADD ./Makefile /bot/Makefile

WORKDIR .

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

EXPOSE 5055
HEALTHCHECK --interval=300s --timeout=60s --retries=5 \
  CMD curl -f http://0.0.0.0:5055/health || exit 1

CMD make run-actions
