from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LowCls:
	"""Low commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("low", core, parent)

	def get(self, sEGMent=repcap.SEGMent.Default) -> float:
		"""SCPI: SENSe:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>:CAGGregation:FREQuency:AGGRegated:LOW \n
		Snippet: value: float = driver.sense.nrMmwMeas.listPy.segment.caggregation.frequency.aggregated.low.get(sEGMent = repcap.SEGMent.Default) \n
		No command help available \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: frequency: No help available"""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		response = self._core.io.query_str(f'SENSe:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:CAGGregation:FREQuency:AGGRegated:LOW?')
		return Conversions.str_to_float(response)
