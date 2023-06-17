Project Title : 
    Extract_my_Tweets

Description
This project uses Apache Airflow running on an EC2 instance to extract data from the Twitter API using Python. The extracted data is then stored in an Amazon S3 bucket, and subsequently loaded into Amazon Redshift using Amazon Glue.

Getting Started
    Prerequisites

        An AWS account
        An EC2 instance with Apache Airflow installed
        Access to the Twitter API
        An Amazon S3 bucket
        An Amazon Redshift cluster
        An AWS Glue job

    Installing

        Clone the repository to your local machine.
        Create a virtual environment and activate it.
        Configuration
        Configure your Twitter API credentials in config.py.
        

    Usage

        Start the Apache Airflow webserver and scheduler.
        Access the Apache Airflow UI and trigger the DAG.

    Authors
        Tawanda Charuka
    Acknowledgments
        https://www.youtube.com/watch?v=q8q3OFFfY6c 
        Apache Airflow Documentation
        Twitter API Documentation
        Amazon S3 Documentation
        Amazon Redshift Documentation
        AWS Glue Documentation
        



