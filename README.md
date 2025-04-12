# Observability Pipelines in Kubernetes using OpenTelemetry #

This GitHub repository serves as a hands-on playground for exploring the OpenTelemetry ecosystem. It provides practical examples and experiments related to Telemetry, Metrics, Logs, Traces, Monitoring, and Observability, showcasing integrations with various tools and vendors commonly used in observability stacks to build a modern Observability Pipelines.

## Why building it yourself? ##

I'm very well aware of the [OpenTelemetry Demo Application Helm Chart](https://opentelemetry.io/docs/demo/) but I found it overwhelming when starting my journey with Observability using OpenTelemetry.

The Demo app consists of over 10+ different services, which together are very fine representation of an actual real life solution using microservices architecture. But I wanted to start small and first make the collector scrape the metrics already available in my Kubernetes cluster, and then learn more about available SDK which could be used to instrument custom application. After that, I already had a simple setup of scraping metrics from a custom app, therefore I could proceed with learning more about logs and finally, traces, one step at a time.

The base otel stack is the result of this journey, with a very simple "microservice architecture" app (2 services) and auto-instrumentation.

In the future I plan to add more sophisticated/advanced setups, but this was enough for me to get a grasp of what the Observability Pipeline is and how to build one.

## Directory structure ##

- [`1-base-otel-stack`](/1-base-otel-stack/README.md) - starting point for understanding the OpenTelemetry using basic example app and simple observability pipeline using otel collector for metrics, traces and logs

## TBA ##

- Full OpenTelemetry example using Grafana Stack (Grafana - visualization, Loki - logs, Mimir - metrics, Tempo - traces, Pyroscope - profiling)
- Observability Pipeline using [Datadog's vector](https://vector.dev/)
- OpenTelemetry Collector HA/Scaling/Prometheus Receiver decoupling using [Target Allocators](https://opentelemetry.io/docs/platforms/kubernetes/operator/target-allocator/)
