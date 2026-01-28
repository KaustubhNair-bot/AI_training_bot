from data_loader import CityDataLoader

if __name__ == "__main__":
    loader = CityDataLoader("data/raw/worldcities.csv")

    df = loader.load_data()
    print(f"Total rows: {len(df)}")

    filtered_df = loader.filter_by_country_and_population(
        df,
        country="United Kingdom",
        min_population=1_000_000
    )

    print(filtered_df[["city", "country", "population"]])
