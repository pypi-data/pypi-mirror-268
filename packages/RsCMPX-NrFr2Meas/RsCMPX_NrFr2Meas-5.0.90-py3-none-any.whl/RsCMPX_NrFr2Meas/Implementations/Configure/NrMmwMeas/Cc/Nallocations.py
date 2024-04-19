from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NallocationsCls:
	"""Nallocations commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nallocations", core, parent)

	def set(self, number: int, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:NALLocations \n
		Snippet: driver.configure.nrMmwMeas.cc.nallocations.set(number = 1, carrierComponent = repcap.CarrierComponent.Default) \n
		Number of allocations to be configured, for carrier <no>. \n
			:param number: For the measured carrier, 0 is not allowed.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(number)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:NALLocations {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> int:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:NALLocations \n
		Snippet: value: int = driver.configure.nrMmwMeas.cc.nallocations.get(carrierComponent = repcap.CarrierComponent.Default) \n
		Number of allocations to be configured, for carrier <no>. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: number: For the measured carrier, 0 is not allowed."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:NALLocations?')
		return Conversions.str_to_int(response)
