from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CorrectionCls:
	"""Correction commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("correction", core, parent)

	def set(self, corr_cmd: str) -> None:
		"""SCPI: DIAGnostic:GPRF:GENerator<Instance>:CORR \n
		Snippet: driver.diagnostic.gprf.generator.correction.set(corr_cmd = 'abc') \n
		No command help available \n
			:param corr_cmd: No help available
		"""
		param = Conversions.value_to_quoted_str(corr_cmd)
		self._core.io.write(f'DIAGnostic:GPRF:GENerator<Instance>:CORR {param}')

	def get(self) -> str:
		"""SCPI: DIAGnostic:GPRF:GENerator<Instance>:CORR \n
		Snippet: value: str = driver.diagnostic.gprf.generator.correction.get() \n
		No command help available \n
			:return: corr_cmd_result: No help available"""
		response = self._core.io.query_str(f'DIAGnostic:GPRF:GENerator<Instance>:CORR?')
		return trim_str_response(response)
