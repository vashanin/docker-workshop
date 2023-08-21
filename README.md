# docker-workshop

```bash
docker build . --tag demo:0.1
docker run -p 8402:8402 -v $(pwd):/app -d -it demo:0.1
```