# OpenTelemetry Qdrant Instrumentation

<a href="https://pypi.org/project/syntrac-opentelemetry-instrumentation-qdrant/">
    <img src="https://badge.fury.io/py/syntrac-opentelemetry-instrumentation-qdrant.svg">
</a>

This library allows tracing client-side calls to Qdrant vector DB sent with the official [Qdrant client library](https://github.com/qdrant/qdrant-client).

## Installation

```bash
pip install syntrac-opentelemetry-instrumentation-qdrant
```

## Example usage

```python
from syntrac_opentelemetry.instrumentation.qdrant import QdrantInstrumentor

QdrantInstrumentor().instrument()
```
