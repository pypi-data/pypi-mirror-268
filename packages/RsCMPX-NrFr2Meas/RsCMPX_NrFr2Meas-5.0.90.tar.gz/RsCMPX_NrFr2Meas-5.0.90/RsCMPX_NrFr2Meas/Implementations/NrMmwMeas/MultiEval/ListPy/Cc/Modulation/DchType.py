from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DchTypeCls:
	"""DchType commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dchType", core, parent)

	# noinspection PyTypeChecker
	def fetch(self, carrierComponentExt=repcap.CarrierComponentExt.Default) -> List[enums.ChannelTypeA]:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST[:CC<carrier>]:MODulation:DCHType \n
		Snippet: value: List[enums.ChannelTypeA] = driver.nrMmwMeas.multiEval.listPy.cc.modulation.dchType.fetch(carrierComponentExt = repcap.CarrierComponentExt.Default) \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: channel_type: No help available"""
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:CC{carrierComponentExt_cmd_val}:MODulation:DCHType?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ChannelTypeA)
