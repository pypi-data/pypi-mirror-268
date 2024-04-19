from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RxCls:
	"""Rx commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rx", core, parent)

	def set(self, name_signal_path: str, value: float) -> None:
		"""SCPI: [CONFigure]:TENVironment:SPATh:ATTenuation:RX \n
		Snippet: driver.configure.tenvironment.spath.attenuation.rx.set(name_signal_path = 'abc', value = 1.0) \n
		No command help available \n
			:param name_signal_path: No help available
			:param value: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_signal_path', name_signal_path, DataType.String), ArgSingle('value', value, DataType.Float))
		self._core.io.write(f'CONFigure:TENVironment:SPATh:ATTenuation:RX {param}'.rstrip())

	def get(self, name_signal_path: str) -> float:
		"""SCPI: [CONFigure]:TENVironment:SPATh:ATTenuation:RX \n
		Snippet: value: float = driver.configure.tenvironment.spath.attenuation.rx.get(name_signal_path = 'abc') \n
		No command help available \n
			:param name_signal_path: No help available
			:return: value: No help available"""
		param = Conversions.value_to_quoted_str(name_signal_path)
		response = self._core.io.query_str(f'CONFigure:TENVironment:SPATh:ATTenuation:RX? {param}')
		return Conversions.str_to_float(response)
