def ingest_data(file_path):
    # Update to absolute path inside the container
    df = pd.read_csv('/app/data/Britney_Spears_tweets_500MB.tsv', sep='\t')
    actions = [
        {
            "_index": "tweets",
            "_source": tweet.to_dict()
        }
        for _, tweet in df.iterrows()
    ]
    helpers.bulk(es, actions)
