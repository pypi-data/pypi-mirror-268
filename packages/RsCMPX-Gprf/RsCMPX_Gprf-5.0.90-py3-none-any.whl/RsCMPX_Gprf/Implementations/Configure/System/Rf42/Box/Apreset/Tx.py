from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TxCls:
	"""Tx commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tx", core, parent)

	def set(self, amplification: enums.LowHigh, box=repcap.Box.Default) -> None:
		"""SCPI: [CONFigure]:SYSTem:RF42:BOX<BoxNo>:APReset:TX \n
		Snippet: driver.configure.system.rf42.box.apreset.tx.set(amplification = enums.LowHigh.HIGH, box = repcap.Box.Default) \n
		No command help available \n
			:param amplification: No help available
			:param box: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Box')
		"""
		param = Conversions.enum_scalar_to_str(amplification, enums.LowHigh)
		box_cmd_val = self._cmd_group.get_repcap_cmd_value(box, repcap.Box)
		self._core.io.write(f'CONFigure:SYSTem:RF42:BOX{box_cmd_val}:APReset:TX {param}')

	# noinspection PyTypeChecker
	def get(self, box=repcap.Box.Default) -> enums.LowHigh:
		"""SCPI: [CONFigure]:SYSTem:RF42:BOX<BoxNo>:APReset:TX \n
		Snippet: value: enums.LowHigh = driver.configure.system.rf42.box.apreset.tx.get(box = repcap.Box.Default) \n
		No command help available \n
			:param box: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Box')
			:return: amplification: No help available"""
		box_cmd_val = self._cmd_group.get_repcap_cmd_value(box, repcap.Box)
		response = self._core.io.query_str(f'CONFigure:SYSTem:RF42:BOX{box_cmd_val}:APReset:TX?')
		return Conversions.str_to_scalar_enum(response, enums.LowHigh)
