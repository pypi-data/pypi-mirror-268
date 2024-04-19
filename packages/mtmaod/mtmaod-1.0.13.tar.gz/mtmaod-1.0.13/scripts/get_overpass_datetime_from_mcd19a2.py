import os
import glob
import argparse
import multiprocessing as mp

import pandas as pd
from mtmaod.products.modis import MCD19A2Reader
from mtmaod.path import Extractor


parser = argparse.ArgumentParser(description="Get Overpass Datetime From MCD19A2 HDF Files")
parser.add_argument("--path", help="Pathname pattern string of MCD19A2 HDF Files")
parser.add_argument("--out", help="Path of Output File")


def get_overpass_datetime_from_mcd19a2(path) -> pd.DataFrame:
    fp = MCD19A2Reader.open(path)
    datetimes = MCD19A2Reader.list_orbit_times(fp)
    get_hv = Extractor.file_hv()
    records = [
        {
            "filename": os.path.basename(path),
            "hv": get_hv(i),
            "timestr": i[:-1],
            "satellite": i[-1],
            "band_idx": idx,
        }
        for idx, i in enumerate(datetimes)
    ]
    df = pd.DataFrame.from_records(records)
    df = df.assign(h=df["hv"].str[1:3].astype(int), v=df["hv"].str[4:6].astype(int))
    return df


if __name__ == "__main__":
    args = parser.parse_args()
    path_re_str = args.path
    out_path = args.out
    # 获取文件列表
    paths = list(glob.glob(path_re_str, recursive=True))

    # 并行处理
    pool = mp.Pool(processes=47)
    df_result = pd.concat(pool.map(get_overpass_datetime_from_mcd19a2, paths))
    pool.close()
    # 保存结果
    df_result = df_result.sort_values(by=["filename", "timestr", "satellite", "band_idx"])
    if "filepath" in df_result.columns:
        df_result.drop(columns=["filepath"], inplace=True)
    df_result.to_csv(out_path, index=False)
