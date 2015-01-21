FROM maksim77/base
MAINTAINER Maksim Syomochkin <maksim77ster@gmail.com>

ADD http://download.getsyncapp.com/endpoint/btsync/os/linux-x64/track/stable /opt/btsync/
ADD http://stedolan.github.io/jq/download/linux64/jq /bin/
COPY btsync.conifg /opt/btsync/
COPY startup.sh /startup.sh
COPY add.sh /bin/add
RUN cd /opt/btsync/ && tar xzvf stable && \
	rm -f /opt/btsync/stable /opt/btsync/README /opt/btsync/LICENSE.TXT && \
	touch /FIRSTRUN && \
	chmod +x /bin/jq

EXPOSE 55555
VOLUME ["/data"]

ENTRYPOINT ["/startup.sh"]
