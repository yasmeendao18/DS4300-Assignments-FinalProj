import pandas as pd


def sample_spotify_songs(csv_path, album="Is This It", sample_size=1000, random_state=42):
    """
    Sample approximately `sample_size` songs from a Spotify dataset CSV,
    ensuring that most or all songs from a specific album are included.

    Parameters:
    - csv_path: path to the spotify csv file
    - album: name of any album that should be included in the sample
    - sample_size: total number of songs in the sample
    - random_state: seed for random number generator (for reproducibility)

    Returns:
    - saves a CSV file with the sampled songs
    """
    spotify_df = pd.read_csv(csv_path)

    # filter for songs from the specified album
    album_songs = spotify_df[spotify_df['album_name'].str.contains(album, case=False, na=False)]
    additional_songs_needed = sample_size - len(album_songs)

    # sample additional songs, excluding those from the specified album
    additional_songs = spotify_df[~spotify_df['track_id'].isin(album_songs['track_id'])].sample(
        n=additional_songs_needed, random_state=random_state)

    sampled_songs = pd.concat([album_songs, additional_songs])

    output_path = "sampled_spotify_songs.csv"
    sampled_songs.to_csv(output_path, index=False)

    return output_path

if __name__ == '__main__':
    # Using the function to sample songs from the 'spotify.csv' file
    sampled_csv_path = sample_spotify_songs('spotify.csv')
    print("CSV file path:", sampled_csv_path)  # Print the sampled CSV file path
