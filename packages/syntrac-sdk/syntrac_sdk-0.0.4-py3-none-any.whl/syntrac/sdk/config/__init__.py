import os


def is_tracing_enabled() -> bool:
    return (os.getenv("SYNTRAC_TRACING_ENABLED") or "true").lower() == "true"


def is_content_tracing_enabled() -> bool:
    return (os.getenv("SYNTRAC_TRACE_CONTENT") or "true").lower() == "true"


def is_metrics_enabled() -> bool:
    return (os.getenv("SYNTRAC_METRICS_ENABLED") or "true").lower() == "true"
