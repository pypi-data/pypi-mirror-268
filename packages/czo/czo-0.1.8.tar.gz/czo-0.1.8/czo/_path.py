import os
import shutil
import sys
from pathlib import Path


class PathLib:
    """
    处理文件相关的功能
    """

    @staticmethod
    def clear_directory(path):
        """
        清空指定目录下的所有文件和子目录。

        Args:
            path:要清空的目录
        """
        if not os.path.exists(path):
            sys.exit("要清空的目录不存在")

        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

    @staticmethod
    def clear_key_file(dir_path, keyword) -> None:
        """
        删除一个目录下包含关键字的文件

        Args:
            dir_path: 要检索的目录
            keyword:文件名中包含的关键字
        """
        file_list = [os.path.join(dir_path, j) for dir_path, dirnames, filenames in
                     os.walk(dir_path) for j in filenames]
        for target_file in file_list:
            if keyword in target_file:
                os.remove(target_file)

    @staticmethod
    def del_key_row(file: str, key: str) -> None:
        """
        删除文件中和 key 相等的行

        Args:
            file : str
            key : str 
        """
        with open(file, 'r', encoding='utf8') as f:
            lines: list[str] = f.readlines()
        with open(file, 'w', encoding='utf8') as f:
            for line in lines:
                if line.strip('\n') != key:
                    f.write(line)

    @staticmethod
    def get_dir_file_list(path: str) -> list:
        """
        获取path下所有文件的路径，包括子目录。
        """
        return [
            os.path.join(root, fn)
            for root, dirs, files in os.walk(path)
            for fn in files
        ]

    @staticmethod
    def mkdir_dir(path) -> None:
        """
        如果目录不存在就创建

        Args:
            path:目录
        """
        if not os.path.exists(path):
            os.mkdir(path)

    @staticmethod
    def get_project_path(project_name: str) -> str:
        """
        根据项目名称获取项目根目录绝对路径
        """
        curPath: str = os.path.abspath(os.path.dirname(__file__))
        return curPath[:curPath.find(project_name) + len(project_name)]

    @staticmethod
    def is_none_then_mkdir(path: str | Path) -> Path:
        """
        如果指定的路径不存在，则创建该路径及其所有父路径。

        参数:
        - path: 字符串或Path类型，表示需要检查和可能创建的路径。

        返回值:
        - Path类型，表示处理后的路径对象。
        """

        if not isinstance(path, Path):
            path = Path(path)  # 将字符串类型的路径转换为Path对象

        if not path.exists():
            path.mkdir(parents=True)  # 如果路径不存在，则创建该路径及其所有父路径
        return path


class DirLib:
    """处理目录相关功能"""

    def __init__(self, directory_path: str | Path):
        # 创建 Path 对象
        self.directory: Path = Path(directory_path)

        # 使用 exists() 方法检查目录是否存在,不存在时新建
        if not self.directory.exists():
            self.directory.mkdir(parents=True)

    @property
    def is_directory_empty(self) -> bool:
        """
        检查目录是否为空。

        无需参数，方法内部会使用实例属性 `directory` 来代表需要检查的目录。
        目录下有空目录时也会判断为非空

        返回值:
            bool: 如果目录为空，则返回 True；否则返回 False。
        """

        # 使用 `any()` 函数和目录迭代器判断目录中是否至少有一个文件或子目录
        return not any(self.directory.iterdir())

    def rename_non_empty_directory(self, new_path: str | Path = None):
        """
        重命名非空目录。

        如果指定的目录不为空，则为其生成一个新的名称，如果指定新的路径，则将目录移动到该路径下，并在原路径上重命名。
        如果新的路径不存在，则会创建该路径。

        参数:
        - new_path: str | Path 类型，指定目录重命名后的新路径。如果为 None，则只重命名不移动目录。

        返回值:
        - Path 类型，表示重命名后的目录路径。如果目录为空，则返回 False。
        """
        # 检查目录是否为空，不为空则进行重命名
        if not self.is_directory_empty:

            serial_number: int = 1  # 初始化序列号，用于生成新的目录名称
            while True:
                # 生成新的目录名称，如果存在则递增序列号
                new_directory_name = f"{self.directory.stem}-{serial_number}"

                if new_path is None:
                    # 如果未指定新路径，则在原路径下重命名
                    new_directory_path = self.directory.parent / new_directory_name
                else:
                    # 如果指定了新路径，则在新路径下重命名
                    new_path = Path(new_path)
                    PathLib.is_none_then_mkdir(new_path)  # 确保新路径存在
                    new_directory_path: Path = new_path / new_directory_name

                if new_directory_path.exists():
                    serial_number += 1  # 如果新名称已存在，则递增序列号并重试
                    continue
                else:
                    break  # 找到可用的新名称，退出循环

            # 执行目录重命名操作
            self.directory.rename(new_directory_path)

            return new_directory_path
        else:
            # 目录为空，不进行重命名
            return False
