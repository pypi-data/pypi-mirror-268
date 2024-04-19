import argparse
import glob
import multiprocessing as mp
import os
import re

import numpy as np
import pandas as pd
from pyhdf.SD import SD, SDC

from mtmaod.products.modis import MXD04L2Reader

parser = argparse.ArgumentParser(description="Get Ging Coordinates From MODIS HDF Files")
parser.add_argument("--path", help="Pathname pattern string of MODIS HDF Files")
parser.add_argument("--out", help="Path of Output File")


def get_gring_from_modis_hdf(path):
    # 使用pyhdf读取hdf文件
    Reader = MXD04L2Reader
    fp = Reader.open(path)
    # 获取文件中的属性信息
    infos = fp.attributes()["ArchiveMetadata.0"]
    # 从属性信息中提取坐标信息
    lontitude_pattern = "GRINGPOINTLONGITUDE.*?\((.*?), (.*?), (.*?), (.*?)\).*?GRINGPOINTLONGITUDE"
    latitude_pattern = "GRINGPOINTLATITUDE.*?\((.*?), (.*?), (.*?), (.*?)\).*?GRINGPOINTLATITUDE"
    longitude_gring = re.findall(lontitude_pattern, infos, re.S)[0]
    latitude_gring = re.findall(latitude_pattern, infos, re.S)[0]
    # 将坐标信息转换为浮点数
    longitude_gring = [float(i) for i in longitude_gring]
    latitude_gring = [float(i) for i in latitude_gring]
    # 读取经纬度波段
    data_longitude = Reader.read(fp, Reader.Band_Longitude)[:]
    data_latitude = Reader.read(fp, Reader.Band_Latitude)[:]
    # 获取经纬度的最大最小值
    longitude_min = np.nanmin(np.array(data_longitude).flatten())
    longitude_max = np.nanmax(np.array(data_longitude).flatten())
    latitude_min = np.nanmin(np.array(data_latitude).flatten())
    latitude_max = np.nanmax(np.array(data_latitude).flatten())
    return longitude_gring + latitude_gring + [longitude_min, longitude_max, latitude_min, latitude_max]


def read_hdf_to_generate_hv_csv(path: str):
    print(path)
    # 获取文件名称
    filename = os.path.basename(path)
    coordinates = get_gring_from_modis_hdf(path)
    return [filename] + coordinates


if __name__ == "__main__":
    args = parser.parse_args()
    # 获取文件列表
    path_re_str = args.path
    out_path = args.out
    paths = list(glob.glob(path_re_str, recursive=True))
    paths = sorted(paths)
    print(f"文件数量: {len(paths)}")  # 输出文件数量
    # 读取文件，生成out文件
    pool = mp.Pool(processes=os.cpu_count())
    results = pool.map(read_hdf_to_generate_hv_csv, paths)
    pool.close()
    columns = (
        ["filename", "lon1", "lon2", "lon3", "lon4"]
        + ["lat1", "lat2", "lat3", "lat4"]
        + ["lon_min", "lon_max", "lat_min", "lat_max"]
    )
    df = pd.DataFrame.from_records(
        results,
        columns=columns,
    ).sort_values(by="filename")
    df.to_csv(out_path, index=False)
