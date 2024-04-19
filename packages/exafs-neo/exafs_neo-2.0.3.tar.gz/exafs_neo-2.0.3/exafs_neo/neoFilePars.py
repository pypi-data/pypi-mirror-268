# from dataclasses import dataclass, field
from attrs import define, field

from pathlib import Path

from exafs_neo.utils import checkKey


@define
class NeoFilePars:
    base: str = Path.cwd()
    data_file: str = ''
    output_file: str = ''
    feff_file: list = field(factory=list)
    log_file: str = 'test.csv'

    firstPass: bool = False
    multi_data_toggle: bool = False
    multi_data: list = field(factory=list)
    nComp: int = 1

    front: list = field(factory=list)

    data_path: Path = None
    output_path: Path = None
    log_path: Path = None

    pathOptimize: bool = False
    end: str = ".dat"

    def read_inputs(self, input_dicts):
        self.nComp = checkKey('nComp', input_dicts, 1)
        if self.nComp > 1:
            try:
                self.feff_file = list(input_dicts['feff_file'].split(","))
            except FileNotFoundError:
                print("Feff folder is not correct")
        else:
            self.feff_file = input_dicts['feff_file']

        self.data_file = checkKey('data_file', input_dicts, '')
        self.output_file = checkKey('output_file', input_dicts, '')
        self.log_file = checkKey('log_file', input_dicts, 'test_log.log')
        self.pathOptimize = checkKey('pathOptimize', input_dicts, False)

    def initialize_filepath(self, cycles=0):
        """
        Initialize File Path
        @param int cycles: the cycles of multiple run
        @return:
        """

        if self.nComp > 1:
            for i in range(self.nComp):
                self.front.append(self.base / self.feff_file[i])
        else:
            self.front = self.base / self.feff_file

        if self.multi_data_toggle:
            self.data_path = self.base / self.multi_data[cycles]
            # self.output_path = os.path.splitext(os.path.join(self.base, output_file))[
            #                        0] + "_" + str(i) + ".csv"
            self.output_path = Path(str((self.base / self.output_file).with_suffix('')) + f"_{cycles}.csv")
            # self.log_path = os.path.splitext(
            #     copy.deepcopy(self.output_path))[0] + ".log"
            self.log_path = Path(str(self.output_path.with_suffix('')) + ".log")
        else:
            # self.data_path = os.path.join(self.base, csv_file)
            self.data_path = self.base / self.data_file
            self.output_path = self.base / self.output_file
            self.log_path = Path(str(self.output_path.with_suffix('')) + ".log")
            # self.log_path = os.path.splitext(
            #     copy.deepcopy(self.output_path))[0] + ".log"
        if self.pathOptimize:
            self.output_path = Path(str((self.base / self.output_file).with_suffix('')) + f"_optimizes.csv")
        #     self.output_path = os.path.splitext(os.path.join(self.base, output_file))[
        #                            0] + "_optimized.csv"


if __name__ == "__main__":
    # exafs_pars = EXAFSPars()
    inputs_pars = {'data_file': 'path_files/Cu/cu_10k.xmu', 'output_file': '', 'feff_file': 'test/feff', 'kmin': 0.95,
                   'kmax': 9.775,
                   'kweight': 3.0,
                   'deltak': 0.05, 'rbkg': 1.1, 'bkgkw': 1.0, 'bkgkmax': 15.0, 'pathOptimize': True}

    exafs_NeoPars = NeoFilePars()

    exafs_NeoPars.read_inputs(inputs_pars)
    exafs_NeoPars.initialize_filepath()
    print(exafs_NeoPars)
