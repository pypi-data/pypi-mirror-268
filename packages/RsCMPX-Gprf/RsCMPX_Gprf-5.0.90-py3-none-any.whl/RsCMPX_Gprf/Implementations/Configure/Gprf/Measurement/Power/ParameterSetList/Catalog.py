from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CatalogCls:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get_pdef_set(self) -> List[str]:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:CATalog:PDEFset \n
		Snippet: value: List[str] = driver.configure.gprf.measurement.power.parameterSetList.catalog.get_pdef_set() \n
		Returns a comma-separated list of predefined parameter sets that can be loaded using method RsCMPX_Gprf.Configure.Gprf.
		Measurement.Power.ParameterSetList.PdefSet.set. See also 'Predefined parameter sets'. \n
			:return: predefined_set: Comma-separated list of strings
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:CATalog:PDEFset?')
		return Conversions.str_to_str_list(response)
