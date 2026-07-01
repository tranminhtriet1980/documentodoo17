# Stage 1: build MkDocs site
FROM python:3.11-alpine AS builder

WORKDIR /build
COPY requirements.txt mkdocs.yml ./
COPY docs ./docs
RUN pip install --no-cache-dir -r requirements.txt \
    && mkdocs build --clean

# Stage 2: nginx
FROM nginx:1.27-alpine

ARG TECH_PASSWORD=Edupath2026!

RUN apk add --no-cache openssl python3 \
    && mkdir -p /etc/nginx/certs \
    && openssl req -x509 -nodes -days 3650 -newkey rsa:2048 \
        -keyout /etc/nginx/certs/key.pem \
        -out /etc/nginx/certs/cert.pem \
        -subj "/CN=tai-lieu-odoo17/O=Edupath"

COPY nginx.conf /etc/nginx/conf.d/default.conf

WORKDIR /build
COPY scripts/generate_htpasswd.py ./scripts/
RUN python3 scripts/generate_htpasswd.py -u technical -p "${TECH_PASSWORD}" \
    && cp config/htpasswd /etc/nginx/htpasswd

COPY --from=builder /build/site /usr/share/nginx/html

EXPOSE 4546 4547
