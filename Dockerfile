FROM python:3
USER root

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

ADD ../CircleBot/wcdi-Discord-Slack-bot/requirements.txt /
ADD ../CircleBot/wcdi-Discord-Slack-bot/bot.py /

RUN pip3 install -r requirements.txt

CMD ["python3", "bot.py"]
