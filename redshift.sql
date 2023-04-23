#redshift table to store our tweets from S3 bucket

 CREATE TABLE public.tweets (
    user character varying(256) ENCODE lzo,
    text character varying(256) ENCODE lzo,
    favorite_count integer ENCODE az64,
    retweet_count integer ENCODE az64,
    created_at date ENCODE az64,
) DISTSTYLE AUTO;