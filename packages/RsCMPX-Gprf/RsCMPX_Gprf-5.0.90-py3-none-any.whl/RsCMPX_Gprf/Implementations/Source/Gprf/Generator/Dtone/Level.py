from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LevelCls:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: LevelSource, default value after init: LevelSource.Src1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_levelSource_get', 'repcap_levelSource_set', repcap.LevelSource.Src1)

	def repcap_levelSource_set(self, levelSource: repcap.LevelSource) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to LevelSource.Default
		Default value after init: LevelSource.Src1"""
		self._cmd_group.set_repcap_enum_value(levelSource)

	def repcap_levelSource_get(self) -> repcap.LevelSource:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def get(self, levelSource=repcap.LevelSource.Default) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:DTONe:LEVel<source> \n
		Snippet: value: float = driver.source.gprf.generator.dtone.level.get(levelSource = repcap.LevelSource.Default) \n
		Queries the output level of a source signal. The output level is a function of the generator output level and the ratio,
		see method RsCMPX_Gprf.Source.Gprf.Generator.RfSettings.level and method RsCMPX_Gprf.Source.Gprf.Generator.Dtone.ratio. \n
			:param levelSource: optional repeated capability selector. Default value: Src1 (settable in the interface 'Level')
			:return: level: No help available"""
		levelSource_cmd_val = self._cmd_group.get_repcap_cmd_value(levelSource, repcap.LevelSource)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:DTONe:LEVel{levelSource_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'LevelCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LevelCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
