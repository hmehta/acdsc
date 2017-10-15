FROM debian:stretch

RUN dpkg --add-architecture i386 && \
        apt-get update && \
        apt-get install -y python3 python3-click python3-psutil \
            make gpg ca-certificates libgcc1:i386 sudo
RUN useradd steam -p '$1$n1LJMbIk$Mre3bw36eAdnXGWxZBqBY.' -G sudo
RUN mkdir /home/steam && chown steam:steam /home/steam
USER steam
ENV PATH=$PATH:/opt/acdsc/bin
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /home/steam
