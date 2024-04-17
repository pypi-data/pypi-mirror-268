# OpenTelemetry Weaviate Instrumentation

<a href="https://pypi.org/project/syntrac-opentelemetry-instrumentation-weaviate/">
    <img src="https://badge.fury.io/py/syntrac-opentelemetry-instrumentation-weaviate.svg">
</a>

This library allows tracing client-side calls to Weaviate vector DB sent with the official [Weaviate library](https://github.com/weaviate/weaviate-python-client).

## Installation

```bash
pip install syntrac-opentelemetry-instrumentation-weaviate
```

## Example usage

```python
from syntrac_opentelemetry.instrumentation.weaviate import WeaviateInstrumentor

WeaviateInstrumentor().instrument()
```
