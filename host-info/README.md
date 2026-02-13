This is meant to be hosted on quay as an image. It's an exercise to learn how to upload a simple image to quay.io.

Steps

1. ```docker build --platform linux/amd64 -t quay.io/wingcheungma/2026-host-info:latest .```
2. ```docker tag host-info-script quay.io/wingcheungma/2026-host-info:latest```
3. ```docker push quay.io/wingcheungma/2026-host-info:latest```

On env

```docker pull quay.io/wingcheungma/2026-host-info:latest```

To run

```docker run --rm quay.io/wingcheungma/2026-host-info:latest```
