from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, frequency: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: TEST:NRMMw:MEASurement<Instance>:NETWork[:CC<no>]:FREQuency \n
		Snippet: driver.test.nrMmwMeas.network.cc.frequency.set(frequency = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		No command help available \n
			:param frequency: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'TEST:NRMMw:MEASurement<Instance>:NETWork:CC{carrierComponent_cmd_val}:FREQuency {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: TEST:NRMMw:MEASurement<Instance>:NETWork[:CC<no>]:FREQuency \n
		Snippet: value: float = driver.test.nrMmwMeas.network.cc.frequency.get(carrierComponent = repcap.CarrierComponent.Default) \n
		No command help available \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: frequency: No help available"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'TEST:NRMMw:MEASurement<Instance>:NETWork:CC{carrierComponent_cmd_val}:FREQuency?')
		return Conversions.str_to_float(response)
