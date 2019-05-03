FROM rasa/rasa_core_sdk:0.13.1

RUN apt update && apt install -y git curl

ADD actions.requirements.txt /tmp/

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/actions.requirements.txt


COPY . /app/actions

HEALTHCHECK --interval=300s --timeout=60s --retries=5 \
CMD curl -f http://0.0.0.0:5055/health || exit 1
