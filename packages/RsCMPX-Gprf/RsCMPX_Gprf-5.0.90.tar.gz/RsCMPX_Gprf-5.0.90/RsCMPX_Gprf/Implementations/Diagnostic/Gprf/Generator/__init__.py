from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GeneratorCls:
	"""Generator commands group definition. 8 total commands, 6 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("generator", core, parent)

	@property
	def rfSetttings(self):
		"""rfSetttings commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfSetttings'):
			from .RfSetttings import RfSetttingsCls
			self._rfSetttings = RfSetttingsCls(self._core, self._cmd_group)
		return self._rfSetttings

	@property
	def rfSettings(self):
		"""rfSettings commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfSettings'):
			from .RfSettings import RfSettingsCls
			self._rfSettings = RfSettingsCls(self._core, self._cmd_group)
		return self._rfSettings

	@property
	def rfProperty(self):
		"""rfProperty commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfProperty'):
			from .RfProperty import RfPropertyCls
			self._rfProperty = RfPropertyCls(self._core, self._cmd_group)
		return self._rfProperty

	@property
	def rms(self):
		"""rms commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rms'):
			from .Rms import RmsCls
			self._rms = RmsCls(self._core, self._cmd_group)
		return self._rms

	@property
	def snumber(self):
		"""snumber commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_snumber'):
			from .Snumber import SnumberCls
			self._snumber = SnumberCls(self._core, self._cmd_group)
		return self._snumber

	@property
	def correction(self):
		"""correction commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_correction'):
			from .Correction import CorrectionCls
			self._correction = CorrectionCls(self._core, self._cmd_group)
		return self._correction

	def get_pn_mode(self) -> bool:
		"""SCPI: DIAGnostic:GPRF:GENerator<Instance>:PNMode \n
		Snippet: value: bool = driver.diagnostic.gprf.generator.get_pn_mode() \n
		No command help available \n
			:return: pn_mode: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:GPRF:GENerator<Instance>:PNMode?')
		return Conversions.str_to_bool(response)

	def set_pn_mode(self, pn_mode: bool) -> None:
		"""SCPI: DIAGnostic:GPRF:GENerator<Instance>:PNMode \n
		Snippet: driver.diagnostic.gprf.generator.set_pn_mode(pn_mode = False) \n
		No command help available \n
			:param pn_mode: No help available
		"""
		param = Conversions.bool_to_str(pn_mode)
		self._core.io.write(f'DIAGnostic:GPRF:GENerator<Instance>:PNMode {param}')

	def clone(self) -> 'GeneratorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = GeneratorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
