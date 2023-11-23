from prometheus_client import start_http_server, Gauge
import time

# Create a Prometheus Gauge metric
predictions_metric = Gauge('release_date_predictions', 'Predicted release dates')

# Expose predictions as metrics
def expose_predictions(predictions):
    predictions_metric.set(predictions)

# Start a simple HTTP server to expose the metrics
start_http_server(8000)

# Expose predictions periodically (adjust as needed)
while True:
    expose_predictions(predictions)
    time.sleep(60)  # Update every 60 seconds
