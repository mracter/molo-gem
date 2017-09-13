FROM praekeltfoundation/molo-bootstrap:5.10.0-onbuild

ENV DJANGO_SETTINGS_MODULE=gem.settings.docker \
    CELERY_APP=gem

RUN pip install https://github.com/mracter/hvac/archive/b0811f0446760125baefea6383711035104e6df1.zip#hvac-0.2.17-git.b817da4
RUN pip install https://github.com/praekeltfoundation/vaultkeeper/archive/dev-debug.zip
RUN pip install https://github.com/mracter/django-postgresql-setrole/archive/master.zip
RUN pip install https://github.com/praekeltfoundation/django-vaultkeeper-adaptor/archive/master.zip

COPY vaultkeeper/vaultkeeper_cfg.json \
     /etc/vaultkeeper/vaultkeeper_cfg.json

#This should eventually be generated by Mission Control/Xylem
COPY vaultkeeper/secrets_cfg.json \
     /etc/vaultkeeper/secrets_cfg.json

COPY vaultkeeper/vaultkeeper-entrypoint.sh \
     /scripts/vaultkeeper-entrypoint.sh

RUN LANGUAGE_CODE=en django-admin compilemessages && \
    django-admin collectstatic --noinput && \
    django-admin compress

RUN ["chmod", "+x", "/scripts/vaultkeeper-entrypoint.sh"]

RUN mkdir -p /creds/

ENTRYPOINT ["tini", "--", "vaultkeeper-entrypoint.sh"]
#CMD ["gem.wsgi:application", "--timeout", "1800"]