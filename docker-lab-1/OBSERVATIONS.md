# Docker Lab 1 Observations

Assigned image: `nginx:alpine`

1. The image was listed as `93.5MB` disk usage, with `26.9MB` content size in my Docker output. I consider it small for a web server image because it uses Alpine Linux as the base instead of a larger full Linux distribution, and it only includes the files needed to run nginx and its startup scripts.

2. `docker image history nginx:alpine` showed 20 history entries/layers. The major pieces are the Alpine miniroot filesystem layer (`9.11MB`), an nginx setup/package layer (`5.59MB`), a larger package/module layer (`51.8MB`), several tiny copied entrypoint scripts, and metadata-only layers such as `ENV`, `EXPOSE`, `ENTRYPOINT`, and `CMD` that add `0B`. The largest layer was the `51.8MB` `RUN` layer, which contains the main nginx runtime packages/modules installed into the Alpine image.

3. From `docker inspect`, the image uses `linux` as the operating system and `amd64` as the architecture. The environment variables included `PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin`, `NGINX_VERSION=1.29.8`, `PKG_RELEASE=1`, `DYNPKG_RELEASE=1`, `NJS_VERSION=0.9.6`, `NJS_RELEASE=1`, and `ACME_VERSION=0.3.1`.

4. For nginx, the port mapping `-p 8080:80` means port `8080` on my computer is forwarded to port `80` inside the container. Nginx still listens on port `80` in the container, but I reach it from Windows at `http://localhost:8080`. If I used `-p 9090:80` instead, I would open `http://localhost:9090` on my computer, while the container side would still be port `80`.

5. What surprised me most was that the same nginx container could be checked from several angles: `docker ps` showed the port mapping, `curl` showed the HTML page, the browser showed the same welcome page, and `docker logs` showed both requests. It made the connection between the host port and the container port much clearer than just reading the command.
