import os
from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor, as_completed

import pandas as pd
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from moisesdb.dataset import MoisesDB
from moisesdb.track import MoisesDBTrack
from moisesdb.defaults import all_stems, default_sample_rate

import svc_toolkit.separation.audio as audio
from svc_toolkit.separation.constants import CSVColumns

def mix_track(track: MoisesDBTrack, stem: str, save_dir: str) -> None:
    if stem in track.stems:
        track_dir = f'{track.artist} - {track.name}'.strip().replace('ö', 'o')

        output_stems = {
            "mixture": all_stems,
            stem: [stem],
        }
        waves = track.mix_stems(output_stems)

        if waves['mixture'].shape != waves[stem].shape:
            min_len = min(waves['mixture'].shape[1], waves[stem].shape[1])
            waves['mixture'] = waves['mixture'][:, :min_len]
            waves[stem] = waves[stem][:, :min_len]

        os.makedirs(os.path.join(save_dir, track_dir), exist_ok=True)
        mixture_path = os.path.join(save_dir, track_dir, 'mixture.wav')
        stem_path = os.path.join(save_dir, track_dir, f'{stem}.wav')

        audio.save(mixture_path, waves['mixture'].T, default_sample_rate)
        audio.save(stem_path, waves[stem].T, default_sample_rate)

def moisesdb_mix(root: str, save_dir: str, stem: str) -> None:
    db = MoisesDB(root)
    os.makedirs(save_dir, exist_ok=True)

    with ThreadPoolExecutor(max_workers=cpu_count()) as executor:
        futures = {executor.submit(mix_track, track, stem, save_dir): track for track in db}
        for future in tqdm(as_completed(futures), total=len(db), desc="Processing tracks"):
            pass

def get_df(root: str, stem: str) -> pd.DataFrame:
    df = pd.DataFrame(columns=[CSVColumns.SONG, CSVColumns.MIXTURE_PATH, CSVColumns.STEM_PATH])

    for dir in sorted(os.listdir(root)):
        mixture_path = os.path.join(root, dir, 'mixture.wav')
        stem_path = os.path.join(root, dir, f'{stem}.wav')

        df.loc[len(df)] = [dir, mixture_path, stem_path]
    
    return df

def preprocess(musdb_dir: str, moisesdb_wav_dir: str, val_size: float, csv_dir: str, stem: str, seed: int) -> None:
    df_musdb = get_df(os.path.join(musdb_dir, 'train'), stem)
    df_musdb_train, df_musdb_val = train_test_split(df_musdb, test_size=val_size, random_state=seed)
    df_musdb_train.to_csv(os.path.join(csv_dir, 'musdb_train.csv'), index=False)
    df_musdb_val.to_csv(os.path.join(csv_dir, 'musdb_val.csv'), index=False)
    df_musdb_test = get_df(os.path.join(musdb_dir, 'test'), stem)
    df_musdb_test.to_csv(os.path.join(csv_dir, 'musdb_test.csv'), index=False)

    df_moisesdb = get_df(moisesdb_wav_dir, stem)
    df_moisesdb_train, df_moisesdb_val = train_test_split(df_moisesdb, test_size=val_size, random_state=seed)
    df_moisesdb_train.to_csv(os.path.join(csv_dir, 'moisesdb_train.csv'), index=False)
    df_moisesdb_val.to_csv(os.path.join(csv_dir, 'moisesdb_val.csv'), index=False)

    df_train = pd.concat([df_musdb_train, df_moisesdb_train])
    df_train.to_csv(os.path.join(csv_dir, 'train.csv'), index=False)
    df_val = pd.concat([df_musdb_val, df_moisesdb_val])
    df_val.to_csv(os.path.join(csv_dir, 'val.csv'), index=False)
