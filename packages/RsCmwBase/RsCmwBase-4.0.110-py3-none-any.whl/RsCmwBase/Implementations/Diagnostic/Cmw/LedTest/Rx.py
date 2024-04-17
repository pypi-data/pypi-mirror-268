from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RxCls:
	"""Rx commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rx", core, parent)

	def set(self, test: bool, cmwVariant=repcap.CmwVariant.Default) -> None:
		"""SCPI: DIAGnostic:CMW<variant>:LEDTest:RX \n
		Snippet: driver.diagnostic.cmw.ledTest.rx.set(test = False, cmwVariant = repcap.CmwVariant.Default) \n
		No command help available \n
			:param test: No help available
			:param cmwVariant: optional repeated capability selector. Default value: Cmw1 (settable in the interface 'Cmw')
		"""
		param = Conversions.bool_to_str(test)
		cmwVariant_cmd_val = self._cmd_group.get_repcap_cmd_value(cmwVariant, repcap.CmwVariant)
		self._core.io.write(f'DIAGnostic:CMW{cmwVariant_cmd_val}:LEDTest:RX {param}')
