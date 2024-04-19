from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OffsetCls:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, offset: int, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:TXBWidth:OFFSet \n
		Snippet: driver.configure.nrMmwMeas.cc.txBwidth.offset.set(offset = 1, carrierComponent = repcap.CarrierComponent.Default) \n
		Specifies the offset to carrier (TxBW offset) of carrier <no>.
		For Signal Path = Network, use[CONFigure:]SIGNaling:NRADio:CELL:RFSettings:UL:OCARrier. \n
			:param offset: Number of RBs
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(offset)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:TXBWidth:OFFSet {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> int:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:TXBWidth:OFFSet \n
		Snippet: value: int = driver.configure.nrMmwMeas.cc.txBwidth.offset.get(carrierComponent = repcap.CarrierComponent.Default) \n
		Specifies the offset to carrier (TxBW offset) of carrier <no>.
		For Signal Path = Network, use[CONFigure:]SIGNaling:NRADio:CELL:RFSettings:UL:OCARrier. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: offset: Number of RBs"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:TXBWidth:OFFSet?')
		return Conversions.str_to_int(response)
