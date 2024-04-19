from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnableCls:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, enable: bool, carrierComponent=repcap.CarrierComponent.Default, allocationMore=repcap.AllocationMore.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUSCh:ENABle \n
		Snippet: driver.configure.nrMmwMeas.cc.allocation.pusch.enable.set(enable = False, carrierComponent = repcap.CarrierComponent.Default, allocationMore = repcap.AllocationMore.Default) \n
		No command help available \n
			:param enable: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocationMore: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
		"""
		param = Conversions.bool_to_str(enable)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocationMore_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationMore, repcap.AllocationMore)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocationMore_cmd_val}:PUSCh:ENABle {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, allocationMore=repcap.AllocationMore.Default) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUSCh:ENABle \n
		Snippet: value: bool = driver.configure.nrMmwMeas.cc.allocation.pusch.enable.get(carrierComponent = repcap.CarrierComponent.Default, allocationMore = repcap.AllocationMore.Default) \n
		No command help available \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocationMore: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
			:return: enable: No help available"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocationMore_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationMore, repcap.AllocationMore)
		response = self._core.io.query_str(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocationMore_cmd_val}:PUSCh:ENABle?')
		return Conversions.str_to_bool(response)
