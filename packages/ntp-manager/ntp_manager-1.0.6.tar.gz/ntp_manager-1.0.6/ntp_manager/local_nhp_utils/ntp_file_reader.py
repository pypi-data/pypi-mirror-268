from functools import wraps
from pathlib import Path
from typing import Literal
import numpy as np
import os
import h5py
import logging

from ntp_manager.models import Cells, Gains


def get_item(ele: h5py.Dataset | str | int | float | list | tuple | np.ndarray):
    if (shape := getattr(ele, 'shape', None)) is not None:
        if shape == (1, 1):
            return ele[0, 0]    # type: ignore
        elif shape == (1,):
            return ele[0]       # type: ignore
    return ele

gi = get_item

def wrapper_bin_and_center(func):
    """
    用于自动把默认的bin和center参数塞进去
    """
    @wraps(func)
    def wrapper(
        self, 
        bin_size: float | None=None, image_center: np.ndarray | None=None,
        *args, **kwargs
    ):
        if bin_size is None:
            bin_size = self.default_bin
        if image_center is None:
            image_center = self.default_image_center

        return func(self, bin_size, image_center, *args, **kwargs)
    return wrapper

T_LIST_STR = list['T_LIST_STR'] | str | None
T_COLOR_SOURCE = Literal['green', 'red', 'blue', 'yellow']

def matlab_str_helper(x) -> T_LIST_STR:
    if isinstance(x, np.ndarray) or isinstance(x, list):
        res = [matlab_str_helper(i) for i in x]
        if len(res) == 1:
            return res[0]
        if len(res) == 0:
            return None
        else:
            return [matlab_str_helper(i) for i in x]
    else:
        return x

class NTPFileReader:

    def __init__(
        self, 
        ntp_path: str | Path, default_bin: float=1, 
        default_image_center: np.ndarray | tuple[float, float] | tuple[int, int] | None=None, 
        resolution=None, transpose=False, 
    ) -> None:
        """_summary_

        Args:
            file_path (str | Path): _description_

            default_bin (float, optional): _description_. Defaults to 1.

            default_image_center (np.ndarray, optional): (x, y) 顺序. 不填则使用 ntp 中的默认值, 
                                  此中默认值有时与图像中心并未对齐, 不指定是危险的. 指定时，应当与 binsize 同等次.  

            resolution (float, optional): Defaults from umPerPixel, 华大的测序小球为0.5μm, 
                                  自有的荧光图像通常为0.65μm/0.89μm.
        """
        ntp_path = str(ntp_path)
        self.file_path = ntp_path
        try:
            self.ntp = h5py.File(ntp_path)
            self.ntp_version = '7.3'

            self.image_meta = self.ntp["cf"]["biggestImage"] # 这个数据的 xy 是正确的
            self.ntp_wh: tuple[float, float] = self.image_meta['xSize'][0, 0], self.image_meta['ySize'][0, 0]
            self.ntp_center = self.image_meta['xCenter'][0, 0], self.image_meta['yCenter'][0, 0]
        except OSError:
            import scipy.io as scio

            self.ntp = scio.loadmat(ntp_path, simplify_cells=True)
            self.ntp_version = '5'

            self.image_meta = self.ntp["cf"]["biggestImage"] # 这个数据的 xy 是正确的
            self.ntp_wh: tuple[float, float] = self.image_meta['xSize'], self.image_meta['ySize']
            self.ntp_center = self.image_meta['xCenter'], self.image_meta['yCenter']
        except Exception:
            print('ntp file error', ntp_path)
            raise
        self.default_bin = default_bin
        self.ntp_resolution: float = float(get_item(self.ntp['cf']['umPerPixel']))

        if resolution is None:
            resolution = self.ntp_resolution

        if default_image_center is None:
            self.ntp_center = np.array(self.ntp_center).astype(int)
            logging.debug(f"default_image_center is None, use default center: {self.ntp_center}")
            default_image_center = self.ntp_center # type: ignore

        self.default_image_center = np.array(default_image_center)
        self.default_image_center = self.default_image_center.astype(int)
        self.default_resolution = resolution
        self.transpose = transpose

    def read_ntp_region_mark(self, bin_size: float | None=None, image_center: np.ndarray | None=None):
        """
        读取ntp文件的区域(region)或标记(mark)，由于ntp文件中坐标按(6cm, 6cm)为中心，因此需要转换. 
        一个华大测序小球是0.5μm，一个荧光图像像素是0.65μm. 
        因此转换为bin n像素坐标系数为1000*10/resolution/n=10000/resolution/n
            bin_size: 关乎如何转换为像素点坐标
            image_center: 目标图像中心
        这里出的数据完全矫正过
        """
        if self.ntp_version == '5':
            return self.read_ntp_region_mark_5(bin_size, image_center)
        else:
            return self.read_ntp_region_mark_73(bin_size, image_center)

    @wrapper_bin_and_center
    def read_ntp_region_mark_5(self, bin_size: float | None=None, image_center: np.ndarray | None=None):
        """
        读取ntp文件的区域(region)或标记(mark)，由于ntp文件中坐标按(6cm, 6cm)为中心，因此需要转换. 
        一个华大测序小球是0.5μm，一个荧光图像像素是0.65μm. 
        因此转换为bin n像素坐标系数为1000*10/resolution/n=10000/resolution/n
            bin_size: 关乎如何转换为像素点坐标
            image_center: 目标图像中心
        这里出的数据完全矫正过
        """

        assert bin_size is not None and image_center is not None
        res: dict[str, list[tuple[int, np.ndarray]]] = {"region": [], "mark": []}

        for data_type in ["region", "mark"]:
            data = self.ntp["cf"][data_type]
            length = int(data["n"])
            points = np.array(data["data"][:, :, :length])
            point_type = np.array(data["type"][:, :length])

            for i in range(length):
                current_type, current_point_num = point_type[:, i]
                current_point_num = int(current_point_num)
                current_type = int(current_type)

                current_data = points[:, :current_point_num, i]
                current_data = np.transpose(current_data) # 形 (n, 2), 序 (y, x)
                current_data = (current_data - 6) * (10000 / self.default_resolution / bin_size)
                if os.environ.get('CURRENT_SPECIES') != 'monkey':
                    # 常规情况
                    current_data[:, 1] = -current_data[:, 1]
                else:
                    # 旧版本的猴子底图有加过一个转置, 因此先临时用这份代码处理掉
                    current_data[:, [0,1]] = current_data[:, [1,0]]
                    current_data[:, 0] = -current_data[:, 0]

                if self.transpose:
                    current_data[:, [0,1]] = current_data[:, [1,0]]
                current_data += image_center

                # current_data = current_data.astype("int32")
                res[data_type].append((current_type, current_data))
        return res

    @wrapper_bin_and_center
    def read_ntp_region_mark_73(self, bin_size: float | None=None, image_center: np.ndarray | None=None):
        assert bin_size is not None and image_center is not None
        res: dict[str, list[tuple[int, np.ndarray]]] = {"region": [], "mark": []}

        for data_type in ["region", "mark"]:
            data = self.ntp['cf'][data_type]
            length = int(data['n'][0, 0]) # 总共有多少个标记

            point_type = data['type'][:length, :].astype(int)
            '''
            结果类似于：
            array([[ 2, 36],
                [ 8, 20],
                [ 8, 19],
                [ 6, 21],
                [ 8,  2],
                [ 8, 36]]
            第一项是线形，第二项是点数
            '''

            for i in range(length):
                current_type, current_point_num = point_type[i]
                current_type = int(current_type)
                current_data = data['data'][i, :current_point_num, :] - 6
                '''
                结果类似于：
                [[-0.01238006 -0.27584566]
                [-0.00353852 -0.27133467]
                [ 0.00151379 -0.26880851]
                [ 0.01342281 -0.26321488]
                [ 0.01991863 -0.25888433]
                [ 0.02280567 -0.25220807]
                [ 0.02424918 -0.23470542]
                [ 0.02623402 -0.2099852 ]
                [ 0.02839929 -0.18562585]
                [ 0.02948193 -0.17389728]

                第一项是x，第二项是y，但是向上y是增加的
                '''
                current_data[:, 1] = -current_data[:, 1] # 转换为向下y增
                current_data = current_data * (10000 / self.default_resolution / bin_size)
                if self.transpose:
                    current_data[:, [0,1]] = current_data[:, [1,0]]
                current_data += image_center
                res[data_type].append((current_type, current_data))
        return res


    def read_cells(
        self, bin_size: float | None=None, image_center: np.ndarray | None=None
    ) -> Cells:
        if self.ntp_version == '5':
            return self.read_cells_5(bin_size, image_center)
        elif self.ntp_version == '7.3':
            return self.read_cells_73(bin_size, image_center)
        else:
            raise Exception(f'Unknown ntp version: {self.ntp_version}')

    @wrapper_bin_and_center
    def read_cells_5(
        self, bin_size: float | None=None, image_center: np.ndarray | None=None
    ) -> Cells:
        assert bin_size is not None and image_center is not None
        cells = Cells()
        for cell_name in cells.colors:
            cell_n = self.ntp['cf'][f'{cell_name}N']
            cell_nd = self.ntp['cf'][f'{cell_name}Cells'][:, :cell_n]
            cell_nd = (cell_nd.T - 6) * (10000.0 / self.default_resolution / bin_size)
            cell_nd[:, 1] = -cell_nd[:, 1]
            if self.transpose:
                cell_nd[:, [0,1]] = cell_nd[:, [1,0]]
            cell_nd += image_center

            cells[cell_name] = cell_nd

        return cells


    def read_labels(self, bin_size: float | None=None, image_center: np.ndarray | None=None):
        if self.ntp_version == '5':
            return self.read_labels_5(bin_size, image_center)
        else:
            return self.read_labels_73(bin_size, image_center)


    @wrapper_bin_and_center
    def read_labels_5(self, bin_size: float | None=None, image_center: np.ndarray | None=None):
        assert bin_size is not None and image_center is not None

        label_count = int(self.ntp['cf']['cat9N'])
        label_postions = self.ntp['cf']['cat9'][:, :label_count].T
        label_postions = (label_postions - 6) * (10000 / self.default_resolution / bin_size)
        label_postions[:, 1] = -label_postions[:, 1]
        if self.transpose:
            label_postions[:, [0,1]] = label_postions[:, [1,0]]
        label_postions += image_center

        labels: list[tuple[str, tuple[float, float]]] = []
        for i in range(label_count):
            label = matlab_str_helper(self.ntp['cf']['textinfo'][i])
            if label is None:
                continue
            assert isinstance(label, str)
            pos = tuple(label_postions[i])

            labels.append((label, pos))
        return labels

    @wrapper_bin_and_center
    def read_cells_73(
        self, bin_size: float | None=None, image_center: np.ndarray | None=None
    ) -> Cells:
        assert bin_size is not None and image_center is not None
        cells = Cells()
        for cell_name in cells.colors:
            cell_n = int(self.ntp['cf'][f'{cell_name}N'][0, 0])
            cell_nd = self.ntp['cf'][f'{cell_name}Cells'][:cell_n, :] - 6
            cell_nd = cell_nd * (10000.0 / self.default_resolution / bin_size)
            cell_nd[:, 1] = -cell_nd[:, 1]

            if self.transpose:
                cell_nd[:, [0,1]] = cell_nd[:, [1,0]]
            cell_nd += image_center

            cells[cell_name] = cell_nd
        return cells


    @wrapper_bin_and_center
    def read_labels_73(self, bin_size: float | None=None, image_center: np.ndarray | None=None):
        assert bin_size is not None and image_center is not None

        label_count = int(self.ntp['cf']['cat9N'][0, 0])
        label_postions = self.ntp['cf']['cat9'][:label_count, :] - 6
        label_postions[:, 1] = -label_postions[:, 1]

        label_postions = label_postions * (10000 / self.default_resolution / bin_size)
        if self.transpose:
            label_postions[:, [0,1]] = label_postions[:, [1,0]]
        label_postions += image_center

        labels: list[tuple[str, tuple[float, float]]] = []
        textinfo = self.ntp['cf']['textinfo']

        for i in range(label_count):
            label = ''
            for j in self.ntp[self.ntp[textinfo[i, 0]][0, 0]]:
                if hasattr(j, '__len__'):
                    label += chr(j[0])

            if label == '':
                continue

            pos = tuple(label_postions[i])

            labels.append((label, pos))
        return labels

    @property
    def gains(self) -> Gains:
        return Gains((
            float(gi(self.ntp['cf']['gain_blue'])),   # type: ignore
            float(gi(self.ntp['cf']['gain_yellow'])), # type: ignore
            float(gi(self.ntp['cf']['gain_red'])),    # type: ignore
            float(gi(self.ntp['cf']['gain_green'])),  # type: ignore
        ))
