from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PsubCls:
	"""Psub commands group definition. 4 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("psub", core, parent)

	@property
	def filterPy(self):
		"""filterPy commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPyCls
			self._filterPy = FilterPyCls(self._core, self._cmd_group)
		return self._filterPy

	def get_payload(self) -> bool:
		"""SCPI: DIAGnostic[:CONFigure]:SYSTem:DAPI:LOGGing:FILE:PSUB:PAYLoad \n
		Snippet: value: bool = driver.diagnostic.configure.system.dapi.logging.file.psub.get_payload() \n
		No command help available \n
			:return: payload: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:CONFigure:SYSTem:DAPI:LOGGing:FILE:PSUB:PAYLoad?')
		return Conversions.str_to_bool(response)

	def set_payload(self, payload: bool) -> None:
		"""SCPI: DIAGnostic[:CONFigure]:SYSTem:DAPI:LOGGing:FILE:PSUB:PAYLoad \n
		Snippet: driver.diagnostic.configure.system.dapi.logging.file.psub.set_payload(payload = False) \n
		No command help available \n
			:param payload: No help available
		"""
		param = Conversions.bool_to_str(payload)
		self._core.io.write(f'DIAGnostic:CONFigure:SYSTem:DAPI:LOGGing:FILE:PSUB:PAYLoad {param}')

	def get_value(self) -> bool:
		"""SCPI: DIAGnostic[:CONFigure]:SYSTem:DAPI:LOGGing:FILE:PSUB \n
		Snippet: value: bool = driver.diagnostic.configure.system.dapi.logging.file.psub.get_value() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:CONFigure:SYSTem:DAPI:LOGGing:FILE:PSUB?')
		return Conversions.str_to_bool(response)

	def set_value(self, enable: bool) -> None:
		"""SCPI: DIAGnostic[:CONFigure]:SYSTem:DAPI:LOGGing:FILE:PSUB \n
		Snippet: driver.diagnostic.configure.system.dapi.logging.file.psub.set_value(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'DIAGnostic:CONFigure:SYSTem:DAPI:LOGGing:FILE:PSUB {param}')

	def clone(self) -> 'PsubCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PsubCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
