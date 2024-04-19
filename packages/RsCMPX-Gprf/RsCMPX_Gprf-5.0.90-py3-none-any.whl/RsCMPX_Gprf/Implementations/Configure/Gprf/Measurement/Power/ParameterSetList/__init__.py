from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ParameterSetListCls:
	"""ParameterSetList commands group definition. 15 total commands, 5 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("parameterSetList", core, parent)

	@property
	def slength(self):
		"""slength commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_slength'):
			from .Slength import SlengthCls
			self._slength = SlengthCls(self._core, self._cmd_group)
		return self._slength

	@property
	def mlength(self):
		"""mlength commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_mlength'):
			from .Mlength import MlengthCls
			self._mlength = MlengthCls(self._core, self._cmd_group)
		return self._mlength

	@property
	def filterPy(self):
		"""filterPy commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPyCls
			self._filterPy = FilterPyCls(self._core, self._cmd_group)
		return self._filterPy

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import CatalogCls
			self._catalog = CatalogCls(self._core, self._cmd_group)
		return self._catalog

	@property
	def pdefSet(self):
		"""pdefSet commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdefSet'):
			from .PdefSet import PdefSetCls
			self._pdefSet = PdefSetCls(self._core, self._cmd_group)
		return self._pdefSet

	# noinspection PyTypeChecker
	def get_value(self) -> enums.ParameterSetMode:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET \n
		Snippet: value: enums.ParameterSetMode = driver.configure.gprf.measurement.power.parameterSetList.get_value() \n
		Selects whether all segments use the same measurement control settings. \n
			:return: parameter_set_mode: GLOBal: Use global settings for all segments. LIST: Use segment-specific settings.
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:PSET?')
		return Conversions.str_to_scalar_enum(response, enums.ParameterSetMode)

	def set_value(self, parameter_set_mode: enums.ParameterSetMode) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET \n
		Snippet: driver.configure.gprf.measurement.power.parameterSetList.set_value(parameter_set_mode = enums.ParameterSetMode.GLOBal) \n
		Selects whether all segments use the same measurement control settings. \n
			:param parameter_set_mode: GLOBal: Use global settings for all segments. LIST: Use segment-specific settings.
		"""
		param = Conversions.enum_scalar_to_str(parameter_set_mode, enums.ParameterSetMode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:PSET {param}')

	def clone(self) -> 'ParameterSetListCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ParameterSetListCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
