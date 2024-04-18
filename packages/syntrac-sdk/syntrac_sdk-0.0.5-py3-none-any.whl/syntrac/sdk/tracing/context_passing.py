from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator


def get_carrier_from_trace_context():
    carrier = {}
    TraceContextTextMapPropagator().inject(carrier)
    return carrier


def get_trace_context_from_carrier(carrier):
    return TraceContextTextMapPropagator().extract(carrier)
