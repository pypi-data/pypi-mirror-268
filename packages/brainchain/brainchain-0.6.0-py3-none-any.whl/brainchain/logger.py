import asyncio
import functools
import logging
import os
import time

import datadog
import watchtower

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure AWS credentials
aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
aws_region = os.environ.get("AWS_REGION")

# Configure CloudWatch logging default log group is watchtower
log_group_name = os.environ.get("LOG_GROUP_NAME")
log_stream_name = os.environ.get("LOG_STREAM_NAME")

try:
    # Check if Datadog environment variables are present
    datadog_api_key = os.environ.get("DATADOG_API_KEY")
    datadog_app_key = os.environ.get("DATADOG_APP_KEY")
    datadog_enabled = datadog_api_key is not None and datadog_app_key is not None
    # Initialize Datadog if the environment variables are present
    if datadog_enabled:
        datadog.initialize(api_key=datadog_api_key, app_key=datadog_app_key)
except:
    pass

# Initialize Datadog if the environment variables are present
if datadog_enabled:
    datadog.initialize(api_key=datadog_api_key, app_key=datadog_app_key)

# Set up the logger to send logs to CloudWatch
handler = watchtower.CloudWatchLogHandler(
    log_group=log_group_name, stream_name=log_stream_name
)
handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)

logger.addHandler(handler)

def log_function_info(func):
    if asyncio.iscoroutinefunction(func):

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            # Log function name and parameters at the beginning
            logger.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")

            # Increment a counter in Datadog if enabled
            if datadog_enabled:
                datadog.statsd.increment(f"{func.__name__}.calls")

            start_time = time.time()

            try:
                result = await func(*args, **kwargs)
            except Exception as e:
                logger.exception(f"Exception in {func.__name__}: {e}")
                raise
            finally:
                end_time = time.time()
                elapsed_time = end_time - start_time
                logger.info(f"{func.__name__} completed in {elapsed_time:.4f} seconds")

                # Send the timing to Datadog if enabled
                if datadog_enabled:
                    datadog.statsd.timing(f"{func.__name__}.time", elapsed_time)

            return result

        return async_wrapper
    else:

        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            logger.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")

            if datadog_enabled:
                datadog.statsd.increment(f"{func.__name__}.calls")

            start_time = time.time()

            try:
                result = func(*args, **kwargs)
            except Exception as e:
                logger.exception(f"Exception in {func.__name__}: {e}")
                raise
            finally:
                end_time = time.time()
                elapsed_time = end_time - start_time
                logger.info(f"{func.__name__} completed in {elapsed_time:.4f} seconds")

                if datadog_enabled:
                    datadog.statsd.timing(f"{func.__name__}.time", elapsed_time)

            return result

        return sync_wrapper
