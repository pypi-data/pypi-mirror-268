from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TimeCls:
	"""Time commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	@property
	def local(self):
		"""local commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_local'):
			from .Local import LocalCls
			self._local = LocalCls(self._core, self._cmd_group)
		return self._local

	# noinspection PyTypeChecker
	def get_source(self) -> enums.TimeSource:
		"""SCPI: SYSTem:TIME:SOURce \n
		Snippet: value: enums.TimeSource = driver.system.time.get_source() \n
		No command help available \n
			:return: time_source: No help available
		"""
		response = self._core.io.query_str('SYSTem:TIME:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.TimeSource)

	def set_source(self, time_source: enums.TimeSource) -> None:
		"""SCPI: SYSTem:TIME:SOURce \n
		Snippet: driver.system.time.set_source(time_source = enums.TimeSource.MANual) \n
		No command help available \n
			:param time_source: No help available
		"""
		param = Conversions.enum_scalar_to_str(time_source, enums.TimeSource)
		self._core.io.write(f'SYSTem:TIME:SOURce {param}')

	def get_ntp(self) -> str:
		"""SCPI: SYSTem:TIME:NTP \n
		Snippet: value: str = driver.system.time.get_ntp() \n
		No command help available \n
			:return: time_server: No help available
		"""
		response = self._core.io.query_str('SYSTem:TIME:NTP?')
		return trim_str_response(response)

	def set_ntp(self, time_server: str) -> None:
		"""SCPI: SYSTem:TIME:NTP \n
		Snippet: driver.system.time.set_ntp(time_server = 'abc') \n
		No command help available \n
			:param time_server: No help available
		"""
		param = Conversions.value_to_quoted_str(time_server)
		self._core.io.write(f'SYSTem:TIME:NTP {param}')

	def clone(self) -> 'TimeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TimeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
