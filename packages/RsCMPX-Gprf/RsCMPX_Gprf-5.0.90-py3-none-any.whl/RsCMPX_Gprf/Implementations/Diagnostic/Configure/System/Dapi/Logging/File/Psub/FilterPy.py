from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPyCls:
	"""FilterPy commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("filterPy", core, parent)

	def get_mname(self) -> str:
		"""SCPI: DIAGnostic[:CONFigure]:SYSTem:DAPI:LOGGing:FILE:PSUB:FILTer:MNAMe \n
		Snippet: value: str = driver.diagnostic.configure.system.dapi.logging.file.psub.filterPy.get_mname() \n
		No command help available \n
			:return: filter_mname: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:CONFigure:SYSTem:DAPI:LOGGing:FILE:PSUB:FILTer:MNAMe?')
		return trim_str_response(response)

	def set_mname(self, filter_mname: str) -> None:
		"""SCPI: DIAGnostic[:CONFigure]:SYSTem:DAPI:LOGGing:FILE:PSUB:FILTer:MNAMe \n
		Snippet: driver.diagnostic.configure.system.dapi.logging.file.psub.filterPy.set_mname(filter_mname = 'abc') \n
		No command help available \n
			:param filter_mname: No help available
		"""
		param = Conversions.value_to_quoted_str(filter_mname)
		self._core.io.write(f'DIAGnostic:CONFigure:SYSTem:DAPI:LOGGing:FILE:PSUB:FILTer:MNAMe {param}')

	def get_rname(self) -> str:
		"""SCPI: DIAGnostic[:CONFigure]:SYSTem:DAPI:LOGGing:FILE:PSUB:FILTer:RNAMe \n
		Snippet: value: str = driver.diagnostic.configure.system.dapi.logging.file.psub.filterPy.get_rname() \n
		No command help available \n
			:return: filter_rname: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:CONFigure:SYSTem:DAPI:LOGGing:FILE:PSUB:FILTer:RNAMe?')
		return trim_str_response(response)

	def set_rname(self, filter_rname: str) -> None:
		"""SCPI: DIAGnostic[:CONFigure]:SYSTem:DAPI:LOGGing:FILE:PSUB:FILTer:RNAMe \n
		Snippet: driver.diagnostic.configure.system.dapi.logging.file.psub.filterPy.set_rname(filter_rname = 'abc') \n
		No command help available \n
			:param filter_rname: No help available
		"""
		param = Conversions.value_to_quoted_str(filter_rname)
		self._core.io.write(f'DIAGnostic:CONFigure:SYSTem:DAPI:LOGGing:FILE:PSUB:FILTer:RNAMe {param}')
