# Storing Twitter data in S3

The code sample (in Python) demonstrates how you can store Tweets in [Amazon Web Services (AWS) S3](https://aws.amazon.com) using the [sampled stream endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/introduction) that is part of the new Twitter API.

## Demo Features

This code sample demonstrates:

- Use of the Twitter API v2
- Use of AWS S3 to store Tweets

## How does it work

When you add the appropriate keys as your environment variables (steps shown in sections below) and run the `s3_demo.py` script, you will connect to the [sampled stream endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/introduction) in the new Twitter API, receive Tweets which will be written to a text file which is zipped and uploaded to AWS S3.

Setting up a Twitter App

- You must have an approved developer account, and have activated the [new developer portal experience](https://developer.twitter.com/en/portal/opt-in.html). Access is available with active keys and tokens for a developer App that is attached to a [Project](https://developer.twitter.com/en/docs/projects.html) created in the [developer portal](https://developer.twitter.com/en/docs/developer-portal.html).
- A bearer token from your App in the [Twitter developer portal](https://developer.twitter.com/en/docs/developer-portal/overview).
- Copy the bearer token from your app as shown above and export it as an environment variable as shown below:

```sh
export 'bearer_token'='<your_bearer_token>'
```

Be sure to replace `<your_bearer_token>` with your own bearer token without the `< >`

## Obtaining your AWS keys

- In order to write the file with Tweets to AWS S3, you will need a valid [Amazon developer account](https://aws.amazon.com/free).
- You will need to sign in to your [AWS developer console](https://console.aws.amazon.com/) and obtain your AWS access key ID and secret access key. Copy these and set them as environment variables by running the following in a terminal:

```sh
export 'aws_access_key_id'='<your_aws_access_key_id>'
export 'aws_secret_access_key'='<your_aws_secret_access_key>'
```

Be sure to replace `<your_aws_access_key_id>` and `<your_aws_secret_access_key>` with your own credentials without the `< >`

## Setting up an AWS bucket

- In order to store data on S3, you will first need to create a bucket. In order to do so, go to the [AWS developer console](https://console.aws.amazon.com) and click on 'Services' and select S3.
- Next, Click on 'Create bucket'
- Provide a unique name for the bucket.
- Then click next and select defaults (or customize as needed) and on the final screen click on create bucket. Remember the name of this bucket and add it to the [s3_demo.py](s3_demo.py) file. This bucket is where the files with Tweets will be added to.

## Running this script

- Download this project
- Make sure that you have added the right Twitter bearer token and the AWS keys as environment variables as shown in the steps above. __Note:__ If you do not have an AWS account, or if your AWS keys and bucket name are not setup correctly, then the file with Tweets will be written to your local machine only.
- Install dependencies specified in the [requirements.txt](https://github.com/twitterdev/twitter-aws-samples/blob/master/requirements.txt) file by running:

```sh
pip3 install -r requirements.txt
```

- Run the `s3_demo.py` file by running the following command in the terminal:

```sh
python3 s3_demo.py
``
