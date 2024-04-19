from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqDataCls:
	"""IqData commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqData", core, parent)

	def get_capture(self) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:IQData:CAPTure \n
		Snippet: value: bool = driver.configure.gprf.measurement.power.listPy.iqData.get_capture() \n
		No command help available \n
			:return: capture_iq_data: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:IQData:CAPTure?')
		return Conversions.str_to_bool(response)

	def set_capture(self, capture_iq_data: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:IQData:CAPTure \n
		Snippet: driver.configure.gprf.measurement.power.listPy.iqData.set_capture(capture_iq_data = False) \n
		No command help available \n
			:param capture_iq_data: No help available
		"""
		param = Conversions.bool_to_str(capture_iq_data)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:IQData:CAPTure {param}')

	def set(self, index: int, iq_data: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:IQData \n
		Snippet: driver.configure.gprf.measurement.power.listPy.iqData.set(index = 1, iq_data = False) \n
		No command help available \n
			:param index: No help available
			:param iq_data: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('iq_data', iq_data, DataType.Boolean))
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:IQData {param}'.rstrip())

	def get(self, index: int) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:IQData \n
		Snippet: value: bool = driver.configure.gprf.measurement.power.listPy.iqData.get(index = 1) \n
		No command help available \n
			:param index: No help available
			:return: iq_data: No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:IQData? {param}')
		return Conversions.str_to_bool(response)

	def get_all(self) -> List[bool]:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:IQData:ALL \n
		Snippet: value: List[bool] = driver.configure.gprf.measurement.power.listPy.iqData.get_all() \n
		No command help available \n
			:return: iq_data: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:IQData:ALL?')
		return Conversions.str_to_bool_list(response)

	def set_all(self, iq_data: List[bool]) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:IQData:ALL \n
		Snippet: driver.configure.gprf.measurement.power.listPy.iqData.set_all(iq_data = [True, False, True]) \n
		No command help available \n
			:param iq_data: No help available
		"""
		param = Conversions.list_to_csv_str(iq_data)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:IQData:ALL {param}')
