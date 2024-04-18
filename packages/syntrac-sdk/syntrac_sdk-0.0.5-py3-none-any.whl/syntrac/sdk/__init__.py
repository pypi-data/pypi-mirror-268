import os
import sys
from deprecated import deprecated
import requests
from pathlib import Path

from typing import Optional, Set
from colorama import Fore
from opentelemetry.sdk.trace import SpanProcessor
from opentelemetry.sdk.trace.export import SpanExporter
from opentelemetry.sdk.metrics.export import MetricExporter
from opentelemetry.sdk.resources import SERVICE_NAME
from opentelemetry.propagators.textmap import TextMapPropagator
from opentelemetry.util.re import parse_env_headers

from syntrac.sdk.metrics.metrics import MetricsWrapper
from syntrac.sdk.telemetry import Telemetry
from syntrac.sdk.instruments import Instruments
from syntrac.sdk.config import (
    is_content_tracing_enabled,
    is_tracing_enabled,
    is_metrics_enabled,
)
from syntrac.sdk.fetcher import Fetcher
from syntrac.sdk.tracing.tracing import (
    TracerWrapper,
    set_association_properties,
    set_correlation_id,
)
from typing import Dict


class Syntrac:
    AUTO_CREATED_KEY_PATH = str(
        Path.home() / ".cache" / "syntrac" / "auto_created_key"
    )
    AUTO_CREATED_URL = str(Path.home() / ".cache" / "syntrac" / "auto_created_url")

    __tracer_wrapper: TracerWrapper
    __fetcher: Fetcher

    @staticmethod
    def init(
        app_name: Optional[str] = sys.argv[0],
        api_endpoint: str = "https://analytics-api.syntrac.dev",
        api_key: str = None,
        headers: Dict[str, str] = {},
        disable_batch=False,
        exporter: SpanExporter = None,
        metrics_exporter: MetricExporter = None,
        metrics_headers: Dict[str, str] = {},
        processor: SpanProcessor = None,
        propagator: TextMapPropagator = None,
        syntrac_sync_enabled: bool = True,
        resource_attributes: dict = {},
        instruments: Optional[Set[Instruments]] = None,
    ) -> None:
        Telemetry()

        api_endpoint = os.getenv("SYNTRAC_BASE_URL") or api_endpoint
        api_key = os.getenv("SYNTRAC_API_KEY") or api_key

        if (
            syntrac_sync_enabled
            and api_endpoint.find("syntrac.com") != -1
            and api_key
            and not exporter
            and not processor
        ):
            Syntrac.__fetcher = Fetcher(base_url=api_endpoint, api_key=api_key)
            Syntrac.__fetcher.run()
            print(
                Fore.GREEN + "Syntrac syncing configuration and prompts" + Fore.RESET
            )

        if not is_tracing_enabled():
            print(Fore.YELLOW + "Tracing is disabled" + Fore.RESET)
            return

        enable_content_tracing = is_content_tracing_enabled()

        if exporter or processor:
            print(Fore.GREEN + "Syntrac exporting traces to a custom exporter")

        headers = os.getenv("SYNTRAC_HEADERS") or headers

        if isinstance(headers, str):
            headers = parse_env_headers(headers)

        # auto-create a dashboard on Syntrac if no export endpoint is provided
        if (
            not exporter
            and not processor
            and api_endpoint == "https://analytics-api.syntrac.dev"
            and not api_key
        ):
            if not Telemetry().feature_enabled("auto_create_dashboard"):
                print(
                    Fore.RED
                    + "Error: Missing Syntrac API key,"
                    + " go to https://analytics-api.syntrac.dev/settings/api-keys to create one"
                )
                print("Set the SYNTRAC_API_KEY environment variable to the key")
                print(Fore.RESET)
                return

            headers = None  # disable headers if we're auto-creating a dashboard
            if not os.path.exists(
                Syntrac.AUTO_CREATED_KEY_PATH
            ) or not os.path.exists(Syntrac.AUTO_CREATED_URL):
                os.makedirs(
                    os.path.dirname(Syntrac.AUTO_CREATED_KEY_PATH), exist_ok=True
                )
                os.makedirs(os.path.dirname(Syntrac.AUTO_CREATED_URL), exist_ok=True)

                print(
                    Fore.YELLOW
                    + "No Syntrac API key provided, auto-creating a dashboard on Syntrac",
                )
                res = requests.post(
                    "https://analytics-api.syntrac.dev/api/registration/auto-create"
                ).json()
                access_url = f"https://analytics-api.syntrac.dev/trace?skt={res['uiAccessKey']}"
                api_key = res["apiKey"]

                print(Fore.YELLOW + "SYNTRAC_API_KEY=", api_key)

                open(Syntrac.AUTO_CREATED_KEY_PATH, "w").write(api_key)
                open(Syntrac.AUTO_CREATED_URL, "w").write(access_url)
            else:
                api_key = open("/tmp/syntrac_key.txt").read()
                access_url = open("/tmp/syntrac_url.txt").read()

            print(
                Fore.GREEN + f"\nGo to {access_url} to see a live dashboard\n",
            )

        if not exporter and not processor and headers:
            print(
                Fore.GREEN
                + f"Syntrac exporting traces to {api_endpoint}, authenticating with custom headers"
            )

        if api_key and not exporter and not processor and not headers:
            print(
                Fore.GREEN
                + f"Syntrac exporting traces to {api_endpoint} authenticating with bearer token"
            )
            headers = {
                "Authorization": f"Bearer {api_key}",
            }

        print(Fore.RESET)

        # Tracer init
        resource_attributes.update({SERVICE_NAME: app_name})
        TracerWrapper.set_static_params(
            resource_attributes, enable_content_tracing, api_endpoint, headers
        )
        Syntrac.__tracer_wrapper = TracerWrapper(
            disable_batch=disable_batch,
            processor=processor,
            propagator=propagator,
            exporter=exporter,
            instruments=instruments,
        )

        # Metrics init: disabled for Syntrac as we don't have a metrics endpoint (yet)
        if api_endpoint.find("syntrac.dev") != -1 or not is_metrics_enabled():
            if not is_metrics_enabled():
                print(Fore.YELLOW + "OpenTelemetry metrics are disabled" + Fore.RESET)
            return

        if metrics_exporter:
            print(Fore.GREEN + "Syntrac exporting metrics to a custom exporter")

        metrics_endpoint = os.getenv("SYNTRAC_METRICS_ENDPOINT")
        metrics_headers = os.getenv("SYNTRAC_METRICS_HEADERS") or metrics_headers

        MetricsWrapper.set_static_params(
            resource_attributes, metrics_endpoint, metrics_headers
        )
        Syntrac.__metrics_wrapper = MetricsWrapper(exporter=metrics_exporter)

    @staticmethod
    @deprecated(version="0.0.62", reason="Use set_association_properties instead")
    def set_correlation_id(correlation_id: str) -> None:
        set_correlation_id(correlation_id)

    def set_association_properties(properties: dict) -> None:
        set_association_properties(properties)

    def report_score(
        association_property_name: str,
        association_property_id: str,
        score: float,
    ):
        if not Syntrac.__fetcher:
            print(
                Fore.RED
                + "Error: Cannot report score. Missing Syntrac API key,"
                + " go to https://app.syntrac.com/settings/api-keys to create one"
            )
            print("Set the SYNTRAC_API_KEY environment variable to the key")
            print(Fore.RESET)
            return

        Syntrac.__fetcher.post(
            "score",
            {
                "entity_name": f"syntrac.association.properties.{association_property_name}",
                "entity_id": association_property_id,
                "score": score,
            },
        )
