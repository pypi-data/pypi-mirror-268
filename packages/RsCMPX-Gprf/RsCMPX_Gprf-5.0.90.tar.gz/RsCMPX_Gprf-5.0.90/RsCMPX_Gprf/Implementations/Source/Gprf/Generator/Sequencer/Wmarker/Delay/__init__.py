from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DelayCls:
	"""Delay commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("delay", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	def set(self, waveform_marker: float, marker=repcap.Marker.Default) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:WMARker<no>:DELay \n
		Snippet: driver.source.gprf.generator.sequencer.wmarker.delay.set(waveform_marker = 1.0, marker = repcap.Marker.Default) \n
		No command help available \n
			:param waveform_marker: No help available
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Wmarker')
		"""
		param = Conversions.decimal_value_to_str(waveform_marker)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:WMARker{marker_cmd_val}:DELay {param}')

	def get(self, marker=repcap.Marker.Default) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:WMARker<no>:DELay \n
		Snippet: value: float = driver.source.gprf.generator.sequencer.wmarker.delay.get(marker = repcap.Marker.Default) \n
		No command help available \n
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Wmarker')
			:return: waveform_marker: No help available"""
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:WMARker{marker_cmd_val}:DELay?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'DelayCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DelayCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
