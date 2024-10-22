import os
import json
import boto3

def handler(event, context):
    # Create a Comprehend client
    client = boto3.client('comprehend')

    try:
        # Extract the body from the event
        body = event["body"]

        # Detect sentiment using AWS Comprehend
        sentiment_response = client.detect_sentiment(LanguageCode="en", Text=body)

        # Simplify the response to return just the sentiment and scores
        sentiment = sentiment_response['Sentiment']
        sentiment_score = sentiment_response['SentimentScore']

        # Log the input and sentiment for debugging
        print(f"Input: {body}")
        print(f"Sentiment: {sentiment}, Score: {sentiment_score}")

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "sentiment": sentiment,
                "sentiment_score": sentiment_score
            })
        }
    except Exception as e:
        # Handle errors and return a meaningful message
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "error": "Unable to process the request."
            })
        }