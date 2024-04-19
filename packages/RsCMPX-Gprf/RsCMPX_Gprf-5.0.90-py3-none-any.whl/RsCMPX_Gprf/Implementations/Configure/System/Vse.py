from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VseCls:
	"""Vse commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vse", core, parent)

	def get_connect(self) -> str:
		"""SCPI: [CONFigure]:SYSTem:VSE:CONNect \n
		Snippet: value: str = driver.configure.system.vse.get_connect() \n
		No command help available \n
			:return: address: No help available
		"""
		response = self._core.io.query_str('CONFigure:SYSTem:VSE:CONNect?')
		return trim_str_response(response)

	def set_connect(self, address: str) -> None:
		"""SCPI: [CONFigure]:SYSTem:VSE:CONNect \n
		Snippet: driver.configure.system.vse.set_connect(address = 'abc') \n
		No command help available \n
			:param address: No help available
		"""
		param = Conversions.value_to_quoted_str(address)
		self._core.io.write(f'CONFigure:SYSTem:VSE:CONNect {param}')

	def get_disconnect(self) -> str:
		"""SCPI: [CONFigure]:SYSTem:VSE:DISConnect \n
		Snippet: value: str = driver.configure.system.vse.get_disconnect() \n
		No command help available \n
			:return: address: No help available
		"""
		response = self._core.io.query_str('CONFigure:SYSTem:VSE:DISConnect?')
		return trim_str_response(response)

	def set_disconnect(self, address: str) -> None:
		"""SCPI: [CONFigure]:SYSTem:VSE:DISConnect \n
		Snippet: driver.configure.system.vse.set_disconnect(address = 'abc') \n
		No command help available \n
			:param address: No help available
		"""
		param = Conversions.value_to_quoted_str(address)
		self._core.io.write(f'CONFigure:SYSTem:VSE:DISConnect {param}')
