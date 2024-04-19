from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LoggingCls:
	"""Logging commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("logging", core, parent)

	def get_file(self) -> bool:
		"""SCPI: DIAGnostic[:CONFigure]:SYSTem:SCPI:LOGGing:FILE \n
		Snippet: value: bool = driver.diagnostic.configure.system.scpi.logging.get_file() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:CONFigure:SYSTem:SCPI:LOGGing:FILE?')
		return Conversions.str_to_bool(response)

	def set_file(self, enable: bool) -> None:
		"""SCPI: DIAGnostic[:CONFigure]:SYSTem:SCPI:LOGGing:FILE \n
		Snippet: driver.diagnostic.configure.system.scpi.logging.set_file(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'DIAGnostic:CONFigure:SYSTem:SCPI:LOGGing:FILE {param}')

	def get_mars(self) -> bool:
		"""SCPI: DIAGnostic[:CONFigure]:SYSTem:SCPI:LOGGing:MARS \n
		Snippet: value: bool = driver.diagnostic.configure.system.scpi.logging.get_mars() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:CONFigure:SYSTem:SCPI:LOGGing:MARS?')
		return Conversions.str_to_bool(response)

	def set_mars(self, enable: bool) -> None:
		"""SCPI: DIAGnostic[:CONFigure]:SYSTem:SCPI:LOGGing:MARS \n
		Snippet: driver.diagnostic.configure.system.scpi.logging.set_mars(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'DIAGnostic:CONFigure:SYSTem:SCPI:LOGGing:MARS {param}')
