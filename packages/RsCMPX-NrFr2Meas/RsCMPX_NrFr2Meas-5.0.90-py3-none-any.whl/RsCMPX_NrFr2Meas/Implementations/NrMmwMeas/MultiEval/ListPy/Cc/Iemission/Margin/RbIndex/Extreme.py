from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .........Internal.Types import DataType
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExtremeCls:
	"""Extreme commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("extreme", core, parent)

	def fetch(self, carrierComponentExt=repcap.CarrierComponentExt.Default) -> List[int]:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST[:CC<carrier>]:IEMission:MARGin:RBINdex:EXTReme \n
		Snippet: value: List[int] = driver.nrMmwMeas.multiEval.listPy.cc.iemission.margin.rbIndex.extreme.fetch(carrierComponentExt = repcap.CarrierComponentExt.Default) \n
		Return resource block indices of the in-band emission measurement for all measured list mode segments, for carrier <c>.
		At these RB indices, the CURRent and EXTReme margins have been detected. The results are returned as triplets per
		segment: <Reliability>, {<RBindex>, <IQImage>, <CarrLeakage>}seg 1, {<RBindex>, <IQImage>, <CarrLeakage>}seg 2, ... \n
		Suppressed linked return values: reliability \n
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: rb_index: Resource block index for the general margin (at non-allocated RBs)"""
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:CC{carrierComponentExt_cmd_val}:IEMission:MARGin:RBINdex:EXTReme?', suppressed)
		return response
