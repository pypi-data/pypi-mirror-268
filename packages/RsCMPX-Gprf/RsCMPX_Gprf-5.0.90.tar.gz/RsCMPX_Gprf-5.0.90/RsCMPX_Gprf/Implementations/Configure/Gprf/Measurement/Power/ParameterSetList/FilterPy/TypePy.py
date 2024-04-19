from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePyCls:
	"""TypePy commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, index: int, filter_py: enums.DigitalFilterType) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:TYPE \n
		Snippet: driver.configure.gprf.measurement.power.parameterSetList.filterPy.typePy.set(index = 1, filter_py = enums.DigitalFilterType.BANDpass) \n
		Selects the IF filter type for the parameter set <Index>. \n
			:param index: No help available
			:param filter_py: RF unit: BANDpass | GAUSs IF unit: BANDpass | GAUSs R&S CMW: BANDpass | GAUSs | WCDMa | CDMA | TDSCdma BANDpass: bandpass filter GAUSs: Gaussian filter WCDMA: 3.84-MHz RRC filter for WCDMA TX tests CDMA: 1.2288-MHz channel filter for CDMA 2000 TX tests TDSCdma: 1.28-MHz RRC filter for TD-SCDMA TX tests
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('filter_py', filter_py, DataType.Enum, enums.DigitalFilterType))
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:TYPE {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, index: int) -> enums.DigitalFilterType:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:TYPE \n
		Snippet: value: enums.DigitalFilterType = driver.configure.gprf.measurement.power.parameterSetList.filterPy.typePy.get(index = 1) \n
		Selects the IF filter type for the parameter set <Index>. \n
			:param index: No help available
			:return: filter_py: RF unit: BANDpass | GAUSs IF unit: BANDpass | GAUSs R&S CMW: BANDpass | GAUSs | WCDMa | CDMA | TDSCdma BANDpass: bandpass filter GAUSs: Gaussian filter WCDMA: 3.84-MHz RRC filter for WCDMA TX tests CDMA: 1.2288-MHz channel filter for CDMA 2000 TX tests TDSCdma: 1.28-MHz RRC filter for TD-SCDMA TX tests"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:TYPE? {param}')
		return Conversions.str_to_scalar_enum(response, enums.DigitalFilterType)

	# noinspection PyTypeChecker
	def get_all(self) -> List[enums.DigitalFilterType]:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:TYPE:ALL \n
		Snippet: value: List[enums.DigitalFilterType] = driver.configure.gprf.measurement.power.parameterSetList.filterPy.typePy.get_all() \n
		Selects the IF filter type for all parameter sets. \n
			:return: filter_py: RF unit: BANDpass | GAUSs IF unit: BANDpass | GAUSs R&S CMW: BANDpass | GAUSs | WCDMa | CDMA | TDSCdma Comma-separated list of 32 values, for parameter set 0 to 31. BANDpass: bandpass filter GAUSs: Gaussian filter WCDMA: 3.84-MHz RRC filter for WCDMA TX tests CDMA: 1.2288-MHz channel filter for CDMA 2000 TX tests TDSCdma: 1.28-MHz RRC filter for TD-SCDMA TX tests
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:TYPE:ALL?')
		return Conversions.str_to_list_enum(response, enums.DigitalFilterType)

	def set_all(self, filter_py: List[enums.DigitalFilterType]) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:TYPE:ALL \n
		Snippet: driver.configure.gprf.measurement.power.parameterSetList.filterPy.typePy.set_all(filter_py = [DigitalFilterType.BANDpass, DigitalFilterType.WCDMa]) \n
		Selects the IF filter type for all parameter sets. \n
			:param filter_py: RF unit: BANDpass | GAUSs IF unit: BANDpass | GAUSs R&S CMW: BANDpass | GAUSs | WCDMa | CDMA | TDSCdma Comma-separated list of 32 values, for parameter set 0 to 31. BANDpass: bandpass filter GAUSs: Gaussian filter WCDMA: 3.84-MHz RRC filter for WCDMA TX tests CDMA: 1.2288-MHz channel filter for CDMA 2000 TX tests TDSCdma: 1.28-MHz RRC filter for TD-SCDMA TX tests
		"""
		param = Conversions.enum_list_to_str(filter_py, enums.DigitalFilterType)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:TYPE:ALL {param}')
