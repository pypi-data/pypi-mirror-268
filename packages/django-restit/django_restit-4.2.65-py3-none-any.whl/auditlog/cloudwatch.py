import boto3
import datetime
import time
import json
from objict import objict
from rest import settings
from concurrent.futures import ThreadPoolExecutor


LOG_CACHE = objict()


def getClient():
    if LOG_CACHE.client is None:
        key = settings.AWS_KEY
        secret = settings.AWS_SECRET
        region = settings.AWS_REGION
        LOG_CACHE.client = boto3.client("logs", aws_access_key_id=key, aws_secret_access_key=secret, region_name=region)
    return LOG_CACHE.client


def log(data, log_group, log_stream):
    if LOG_CACHE.pool is None:
        LOG_CACHE.pool = ThreadPoolExecutor(max_workers=1)
    LOG_CACHE.pool.submit(logToCloudWatch, data, log_group, log_stream)
    return True


def logToCloudWatch(data, log_group, log_stream):
    message = data
    if isinstance(message, dict):
        message = json.dumps(message)
    return logBatchToCloudWatch([
            dict(
                timestamp=int(datetime.datetime.utcnow().timestamp() * 1000),
                message=message)
        ], log_group, log_stream)


def logBatchToCloudWatch(batch, log_group, log_stream):
    return getClient().put_log_events(
        logGroupName=log_group,
        logStreamName=log_stream,
        logEvents=batch
    )


def getLogGroups():
    response = getClient().describe_log_groups()
    return response.get('logGroups', [])


def createLogStream(log_group, log_stream):
    try:
        getClient().create_log_stream(logGroupName=log_group, logStreamName=log_stream)
    except Exception:
        pass  # Log stream already exists, no need to create it


def getInsights(log_group, start_time, end_time, query_string):
    """
    Executes a CloudWatch Logs Insights query and returns the results.

    :param log_group: The name of the log group to query.
    :param start_time: The start time of the query (epoch time in seconds).
    :param end_time: The end time of the query (epoch time in seconds).
    :param query_string: The query string to use.
    :param region_name: AWS region name.
    :return: The query results.
    """
    # Create a CloudWatch Logs client
    client = getClient()
    
    # Start the query
    start_query_response = client.start_query(
        logGroupName=log_group,
        startTime=start_time,
        endTime=end_time,
        queryString=query_string,
    )
    
    query_id = start_query_response['queryId']
    
    # Wait for the query to complete
    response = None
    while response is None or response['status'] == 'Running':
        time.sleep(1)  # Sleep to rate limit the polling
        response = client.get_query_results(queryId=query_id)
    
    if response['status'] == 'Complete':
        return response['results']
    else:
        raise Exception(f"Query did not complete successfully. Status: {response['status']}")
