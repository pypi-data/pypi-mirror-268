# OpenTelemetry Chroma Instrumentation

<a href="https://pypi.org/project/syntrac-opentelemetry-instrumentation-chromadb/">
    <img src="https://badge.fury.io/py/syntrac-opentelemetry-instrumentation-chromadb.svg">
</a>

This library allows tracing client-side calls to Chroma vector DB sent with the official [Chroma library](https://github.com/chroma-core/chroma).

## Installation

```bash
pip install syntrac-opentelemetry-instrumentation-chromadb
```

## Example usage

```python
from syntrac_opentelemetry.instrumentation.chromadb import ChromaInstrumentor

ChromaInstrumentor().instrument()
```
