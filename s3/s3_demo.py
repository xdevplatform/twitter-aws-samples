import gzip
import shutil
import sys
from datetime import datetime
from time import sleep
import os
import boto3
import requests
from botocore.exceptions import ClientError

global count
global time_stamp

# Replace with the number of Tweets you want in a file
file_size = 1000
# Replace the AWS Bucket name below
aws_bucket_name = "your_s3_bucket_name"

url = "https://api.twitter.com/2/tweets/sample/stream"


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def stream_connect(headers):
    global count, time_stamp
    response = requests.request("GET", url, headers=headers, stream=True)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    for response_line in response.iter_lines():
        if response_line:
            tweet = response_line.decode("utf-8")
            if count == file_size:
                upload_file("data-{}.txt".format(time_stamp), aws_bucket_name,
                            "{}/data-{}.txt.gz".format(get_date(), time_stamp))
                time_stamp = int(datetime.utcnow().timestamp() * 1e3)
                count = 0
            count += 1
            append_new_line("data-{}.txt".format(time_stamp), tweet)


def upload_file(file_name, bucket, object_name):
    # Compress file
    print("Created new file with name {}".format(file_name))
    with open(file_name, 'rb') as f_in, gzip.open('{}.gz'.format(file_name), 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

    aws_access_key_id = os.environ.get("aws_access_key_id"),
    aws_secret_access_key = os.environ.get("aws_secret_access_key")

    if aws_access_key_id is not None and aws_secret_access_key is not None:
        # Upload the file
        s3_client = boto3.client('s3', aws_access_key_id, aws_secret_access_key)
        try:
            s3_client.upload_file('{}.gz'.format(file_name), bucket, object_name)
            print("Wrote file {}.gz to S3 bucket {}".format(file_name, bucket))
        except ClientError as e:
            print(e, file=sys.stderr)


def get_date():
    x = datetime.now()
    return x.strftime('%Y-%m-%d')


def append_new_line(file_name, text_to_append):
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)


def main():
    bearer_token = os.environ.get("bearer_token")
    if bearer_token is not None:
        headers = create_headers(bearer_token)
        global time_stamp, count
        count = 0
        time_stamp = int(datetime.utcnow().timestamp() * 1e3)
        retry = 0
        while True:
            stream_connect(headers)
            wait_seconds = 2 ** retry
            sleep(wait_seconds if wait_seconds < 900 else 900)
            retry += 1
    else:
        print(
            "Error obtaining the bearer token. Please make sure you have added a valid bearer token to the config file")


if __name__ == '__main__':
    main()
