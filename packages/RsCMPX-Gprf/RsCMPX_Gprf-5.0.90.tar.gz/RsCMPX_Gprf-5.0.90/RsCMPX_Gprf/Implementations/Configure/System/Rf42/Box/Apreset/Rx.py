from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RxCls:
	"""Rx commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rx", core, parent)

	def set(self, amplification: enums.Amplification, box=repcap.Box.Default) -> None:
		"""SCPI: [CONFigure]:SYSTem:RF42:BOX<BoxNo>:APReset:RX \n
		Snippet: driver.configure.system.rf42.box.apreset.rx.set(amplification = enums.Amplification.HIGH, box = repcap.Box.Default) \n
		No command help available \n
			:param amplification: No help available
			:param box: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Box')
		"""
		param = Conversions.enum_scalar_to_str(amplification, enums.Amplification)
		box_cmd_val = self._cmd_group.get_repcap_cmd_value(box, repcap.Box)
		self._core.io.write(f'CONFigure:SYSTem:RF42:BOX{box_cmd_val}:APReset:RX {param}')

	# noinspection PyTypeChecker
	def get(self, box=repcap.Box.Default) -> enums.Amplification:
		"""SCPI: [CONFigure]:SYSTem:RF42:BOX<BoxNo>:APReset:RX \n
		Snippet: value: enums.Amplification = driver.configure.system.rf42.box.apreset.rx.get(box = repcap.Box.Default) \n
		No command help available \n
			:param box: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Box')
			:return: amplification: No help available"""
		box_cmd_val = self._cmd_group.get_repcap_cmd_value(box, repcap.Box)
		response = self._core.io.query_str(f'CONFigure:SYSTem:RF42:BOX{box_cmd_val}:APReset:RX?')
		return Conversions.str_to_scalar_enum(response, enums.Amplification)
