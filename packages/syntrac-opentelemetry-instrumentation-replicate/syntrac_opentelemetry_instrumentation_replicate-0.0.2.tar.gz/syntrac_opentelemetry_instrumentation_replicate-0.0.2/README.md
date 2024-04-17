# OpenTelemetry Replicate Instrumentation

<a href="https://pypi.org/project/syntrac-opentelemetry-instrumentation-replicate/">
    <img src="https://badge.fury.io/py/syntrac-opentelemetry-instrumentation-replicate.svg">
</a>

This library allows tracing Replicate prompts and image generation sent with the official [replicate library](https://github.com/replicate/replicate-python).

## Installation

```bash
pip install syntrac-opentelemetry-instrumentation-replicate
```

## Example usage

```python
from syntrac_opentelemetry.instrumentation.replicate import ReplicateInstrumentor

ReplicateInstrumentor().instrument()
```

## Privacy

**By default, this instrumentation logs prompts, completions, and embeddings to span attributes**. This gives you a clear visibility into how your LLM application is working, and can make it easy to debug and evaluate the quality of the outputs.

However, you may want to disable this logging for privacy reasons, as they may contain highly sensitive data from your users. You may also simply want to reduce the size of your traces.

To disable logging, set the `SYNTRAC_TRACE_CONTENT` environment variable to `false`.

```bash
SYNTRAC_TRACE_CONTENT=false
```
