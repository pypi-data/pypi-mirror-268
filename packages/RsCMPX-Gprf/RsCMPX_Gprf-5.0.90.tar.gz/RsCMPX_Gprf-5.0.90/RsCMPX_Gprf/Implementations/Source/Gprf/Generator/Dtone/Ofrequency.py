from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OfrequencyCls:
	"""Ofrequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: FrequencySource, default value after init: FrequencySource.Src1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ofrequency", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_frequencySource_get', 'repcap_frequencySource_set', repcap.FrequencySource.Src1)

	def repcap_frequencySource_set(self, frequencySource: repcap.FrequencySource) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to FrequencySource.Default
		Default value after init: FrequencySource.Src1"""
		self._cmd_group.set_repcap_enum_value(frequencySource)

	def repcap_frequencySource_get(self) -> repcap.FrequencySource:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, frequency: float, frequencySource=repcap.FrequencySource.Default) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:DTONe:OFRequency<source> \n
		Snippet: driver.source.gprf.generator.dtone.ofrequency.set(frequency = 1.0, frequencySource = repcap.FrequencySource.Default) \n
		Selects an offset frequency. The frequency of the modulated signal is equal to the base frequency (see method RsCMPX_Gprf.
		Source.Gprf.Generator.RfSettings.frequency) plus the offset frequency. \n
			:param frequency: No help available
			:param frequencySource: optional repeated capability selector. Default value: Src1 (settable in the interface 'Ofrequency')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		frequencySource_cmd_val = self._cmd_group.get_repcap_cmd_value(frequencySource, repcap.FrequencySource)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:DTONe:OFRequency{frequencySource_cmd_val} {param}')

	def get(self, frequencySource=repcap.FrequencySource.Default) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:DTONe:OFRequency<source> \n
		Snippet: value: float = driver.source.gprf.generator.dtone.ofrequency.get(frequencySource = repcap.FrequencySource.Default) \n
		Selects an offset frequency. The frequency of the modulated signal is equal to the base frequency (see method RsCMPX_Gprf.
		Source.Gprf.Generator.RfSettings.frequency) plus the offset frequency. \n
			:param frequencySource: optional repeated capability selector. Default value: Src1 (settable in the interface 'Ofrequency')
			:return: frequency: No help available"""
		frequencySource_cmd_val = self._cmd_group.get_repcap_cmd_value(frequencySource, repcap.FrequencySource)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:DTONe:OFRequency{frequencySource_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'OfrequencyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OfrequencyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
