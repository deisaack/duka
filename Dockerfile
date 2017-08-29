FROM python:3.5 -onbuild

COPY start.sh /start.sh

EXPOSE 8000

CMD ["/start.sh"]
