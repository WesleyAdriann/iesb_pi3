IESB - PI3
===

## Description
Optimization project to create study groups in virtual learning environments using genetic algorithms developed in PI3 from IESB

## Chromosomes structure
![](./assets/chromosome.png)

## Prerequisites

- [Python 3.8](https://www.python.org/)

## Usage
### Python CLI
Inside the */code* directory execute
```bash
python3 Tests.py
```

### Docker
In project root builds the Dockerfile
```bash
# docker image build -t <IMAGE_NAME> <DOCKERFILE_DIRECTORY>
docker image build -t <IMAGE_NAME> .
```
Run the container using generated image
```bash
#  docker run <IMAGE_NAME>
docker run <IMAGE_NAME>
```

### Docker Compose
In project root execute
```
docker-compose up
```
or
```
docker-compose up --build
```

## Authors
- Bruno Teodoro
  - Github: [brunoteodoromota](https://github.com/brunoteodoromota)
- Lucas Simplicio
  - Github: [lucas0806](https://github.com/lucas0806)
- Médard TOSSOU
  - Github: [YanisToss](https://github.com/YanisToss)
- Wesley Adriann
  - Github: [WesleyAdriann](https://github.com/WesleyAdriann)

## Project Status

- **[Finalized](https://github.com/WesleyAdriann/iesb_pi3/releases/tag/v1.0.2)**

## URL Project Reference

- [https://github.com/WesleyAdriann/iesb_pi3](https://github.com/WesleyAdriann/iesb_pi3)
