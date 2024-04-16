import os

import pandas as pd

from svc_toolkit.separation.constants import CSVColumns

def get_best_checkpoint_path(model_dir: str) -> str:
    return get_checkpoint_path(model_dir, 'best')

def get_last_checkpoint_path(model_dir: str) -> str:
    return get_checkpoint_path(model_dir, 'last')

def get_checkpoint_path(model_dir: str, prefix: str) -> str:
    for file in os.listdir(model_dir):
        if file.startswith(prefix) and file.endswith('.ckpt'):
            return os.path.join(model_dir, file)
    return None

def save_song_list(csv_path: str, model_dir: str, file_name: str) -> None:
    song_list_pd = pd.read_csv(csv_path)

    # Select only the song column
    song_list_pd = song_list_pd[[CSVColumns.SONG]]

    song_list_pd.to_csv(os.path.join(model_dir, file_name), index=False)