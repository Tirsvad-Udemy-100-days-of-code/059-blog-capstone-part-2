# Headless browser for the lecture screenshots; not part of the Python project.
#
# Build and run from the repository root:
#   docker build -t blog-screenshots -f tests/e2e/Dockerfile .
#   docker run --rm --ipc=host -v "$(pwd)/docs/screenshots:/work/docs/screenshots" blog-screenshots
FROM mcr.microsoft.com/playwright/python:v1.49.1-noble@sha256:42e251ec3238672c931be6c3565ff279690ae072c3e22058128d0412494f6866

RUN pip install --no-cache-dir --break-system-packages playwright==1.49.1

WORKDIR /work
COPY pyproject.toml README.md LICENSE ./
COPY src ./src
# The pinned Playwright image ships Python 3.12, the project requires >= 3.13;
# the code runs on 3.12, so the check is skipped for this screenshot image only.
RUN pip install --no-cache-dir --break-system-packages --ignore-requires-python .
COPY tests/e2e/capture_screenshots.py ./capture_screenshots.py
RUN mkdir -p /work/docs/screenshots && chown -R pwuser:pwuser /work

USER pwuser

CMD ["python3", "capture_screenshots.py", "docs/screenshots"]
