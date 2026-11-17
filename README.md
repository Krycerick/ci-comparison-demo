# ci-comparison-demo

The same small FastAPI app run through three CI/CD tools: GitHub Actions, GitLab CI and CircleCI.

Each pipeline does two things:
1. Runs the pytest tests on every push
2. Builds the Docker image, only if the tests passed

| Tool | Config file |
|---|---|
| GitHub Actions | `.github/workflows/ci.yml` |
| GitLab CI | `.gitlab-ci.yml` |
| CircleCI | `.circleci/config.yml` |

## Run it locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -v
uvicorn app.main:app --reload   # then open http://127.0.0.1:8000/docs
```

## Docker

```bash
docker build -t ci-demo .
docker run -p 8000:8000 ci-demo
```
