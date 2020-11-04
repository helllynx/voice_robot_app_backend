## Voice helper

For voice recognition i use ``alphacep/kaldi``.

Run from docker:

```shell script
docker run -d -p 2700:2700 alphacep/kaldi-en:latest 
```

## Python dependencies

Just run:

```shell script
poetry install
```