from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TdoIndexCls:
	"""TdoIndex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tdoIndex", core, parent)

	def set(self, value: int, carrierComponent=repcap.CarrierComponent.Default, allocationMore=repcap.AllocationMore.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUCCh:TDOindex \n
		Snippet: driver.configure.nrMmwMeas.cc.allocation.pucch.tdoIndex.set(value = 1, carrierComponent = repcap.CarrierComponent.Default, allocationMore = repcap.AllocationMore.Default) \n
		Specifies the time domain OCC index for PUCCH format F1, for carrier <no>, allocation <a>. \n
			:param value: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocationMore: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
		"""
		param = Conversions.decimal_value_to_str(value)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocationMore_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationMore, repcap.AllocationMore)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocationMore_cmd_val}:PUCCh:TDOindex {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, allocationMore=repcap.AllocationMore.Default) -> int:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUCCh:TDOindex \n
		Snippet: value: int = driver.configure.nrMmwMeas.cc.allocation.pucch.tdoIndex.get(carrierComponent = repcap.CarrierComponent.Default, allocationMore = repcap.AllocationMore.Default) \n
		Specifies the time domain OCC index for PUCCH format F1, for carrier <no>, allocation <a>. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocationMore: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
			:return: value: No help available"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocationMore_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationMore, repcap.AllocationMore)
		response = self._core.io.query_str(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocationMore_cmd_val}:PUCCh:TDOindex?')
		return Conversions.str_to_int(response)
