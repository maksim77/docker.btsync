FROM debian:stable
MAINTAINER Maksim Syomochkin <maksim77ster@gmail.com>

ADD http://download.getsyncapp.com/endpoint/btsync/os/linux-x64/track/stable /opt/btsync/
COPY btsync.conifg /opt/btsync/
RUN rm -rf /etc/localtime && ln -s /usr/share/zoneinfo/Europe/Moscow /etc/localtime && \
	cd /opt/btsync/ && tar xzvf stable && \
	rm -f /opt/btsync/stable /opt/btsync/README /opt/btsync/LICENSE.TXT

EXPOSE 55555
VOLUME /data

ENTRYPOINT ["/opt/btsync/btsync","--config","/opt/btsync/btsync.conifg","--nodaemon"]
