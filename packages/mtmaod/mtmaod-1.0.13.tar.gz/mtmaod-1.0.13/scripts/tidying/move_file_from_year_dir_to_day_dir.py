import argparse
import glob
import os
import shutil

# 移动数据文件从年目录到日目录
parser = argparse.ArgumentParser(description="Move files from year directory to day directory")
parser.add_argument("--data_re_path", type=str, help="The directory where the data is stored")
args = parser.parse_args()


def move_file_from_year_dir_to_day_dir(data_re_path: str):
    """移动数据文件从年目录到日目录

    Parameters
    ----------
    data_re_path : str
        数据文件的路径, 可以使用通配符, 例如"data/**/*.hdf"

    Examples
    --------
    >>> move_file_from_year_dir_to_day_dir("data/**/*.hdf")
    """
    for filepath in sorted(list(glob.glob(data_re_path, recursive=True))):
        filename = os.path.basename(filepath)
        dirname = os.path.dirname(filepath)
        # 判断父目录是否为年目录
        try:
            year = int(os.path.basename(dirname))
        except Exception as e:
            raise ValueError(f"父目录{dirname}不是一个有效的年目录")
        if year > 2100 or year < 366:
            raise ValueError(f"父目录{dirname}不是一个有效的年目录")
        # 创建日目录
        day = filename.split(".")[1][-3:]
        objdir = os.path.join(dirname, day)
        if not os.path.exists(objdir):
            os.mkdir(objdir)
        # 移动文件
        shutil.move(filepath, os.path.join(objdir, filename))
        print(filename, day)
    print(f"Done! {data_re_path}")


if __name__ == "__main__":
    move_file_from_year_dir_to_day_dir(args.data_re_path)

    # Command line Example:
    # python move_file_from_year_dir_to_day_dir.py --data_re_path "data/61/MCD19A2/**/*.hdf"
