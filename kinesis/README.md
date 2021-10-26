# Streaming Tweets with AWS Kinesis

The code sample (in Python) demonstrates how you can deliver Tweets to S3 in [Amazon Web Services (AWS) S3](https://aws.amazon.com) using the [sampled stream endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/introduction) that is part of the new Twitter API.

## Demo Features

This code sample demonstrates:

- Use of the Twitter API v2
- Use of [AWS Kinesis Data Firehose delivery streams](https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html)

## How does it work

When you add the appropriate keys as your environment variables (steps shown in sections below) and run the `kinesis_demo.py` script, you will connect to the [sampled stream endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/introduction) in the new Twitter API, receive Tweets which you can deliver to S3 buckets using Amazon Kinesis Data Firehose delivery streams.

## Setting up a Twitter App

- You must have an approved developer account, and have activated the [new developer portal experience](https://developer.twitter.com/en/portal/opt-in.html). Access is available with active keys and tokens for a developer App that is attached to a [Project](https://developer.twitter.com/en/docs/projects.html) created in the [developer portal](https://developer.twitter.com/en/docs/developer-portal.html).
- A bearer token from your App in the [Twitter developer portal](https://developer.twitter.com/en/docs/developer-portal/overview).
- Copy the bearer token from your app as shown above and export it as an environment variable as shown below:

```sh
export 'bearer_token'='<your_bearer_token>'
```

Be sure to replace `<your_bearer_token>` with your own bearer token without the `< >`

## Obtaining your AWS keys

- In order to write the file with Tweets to AWS, you will need a valid [Amazon developer account](https://aws.amazon.com/free).
- You will need to sign in to your [AWS developer console](https://console.aws.amazon.com/) and obtain your AWS access key ID and secret access key. Copy these and set them as environment variables by running the following in a terminal:

```sh
export 'aws_access_key_id'='<your_aws_access_key_id>'
export 'aws_secret_access_key'='<your_aws_secret_access_key>'
```

Be sure to replace `<your_aws_access_key_id>` and `<your_aws_secret_access_key>` with your own credentials without the `< >`

- Remember to set the AWS region name as an environment variable by running:

```sh
export 'aws_region'='<your_aws_region>'
```

Be sure to replace `<your_aws_region>` with your own AWS region value without the `< >`

## Setting up an Amazon Kinesis Data Firehose delivery stream

- In order to create a Kinesis delivery stream, go to the [AWS developer console](https://console.aws.amazon.com) and click on 'Services' and select Kinesis.
- Next Click on Create delivery stream
- Give your delivery stream a name
- Under Choose a source, select the Direct PUT or other sources and click next
- Select the default values (disabled on this screen, unless you wish to convert record format, transform source records etc.) and click next
- Next, for 'Choose a destination', select 'Amazon S3'. Then, next to S3 bucket, click create new and create a new S3 bucket in which you want the Tweets to be sent to, and click next.
- Then, in the Configure settings window, under S3 buffer conditions, select the conditions on which you want the Tweets to be written to the S3 bucket. You can either choose the buffer size or interval for this.
- Finally, click next and on the next screen Review your configurations and click 'Create delivery stream'
- Make sure to add the name of this delivery stream to the [kinesis_demo.py](kniesis_demo.py) file.

## Running this script

- Download this project
- Make sure that you have added the correct Twitter bearer token and the AWS keys and region as environment variables, as shown in the steps above.
- Install dependencies specified in the [requirements.txt](https://github.com/twitterdev/twitter-aws-samples/blob/master/requirements.txt) file by running:

```sh
pip3 install -r requirements.txt
```

- Run the `kinesis_demo.py` file by running the following command in the terminal:

```sh
python3 kinesis_demo.py
```
