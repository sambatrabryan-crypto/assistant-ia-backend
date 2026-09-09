FROM ubuntu:latest
LABEL authors="Bry"

ENTRYPOINT ["top", "-b"]