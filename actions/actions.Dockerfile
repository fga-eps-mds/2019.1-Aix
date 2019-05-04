FROM rasa/rasa_core_sdk:0.13.1

RUN apt update -qq && apt -q -y -o Dpkg::Use-Pty=0 install -y git curl

ADD actions.requirements.txt /tmp/

RUN pip install --upgrade pip && \
    pip install --quiet --progress-bar off --no-cache-dir -r /tmp/actions.requirements.txt

HEALTHCHECK --interval=300s --timeout=60s --retries=5 \
CMD curl -f http://0.0.0.0:5055/health || exit 1
