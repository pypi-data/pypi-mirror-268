from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ........Internal.Types import DataType
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExtremeCls:
	"""Extreme commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("extreme", core, parent)

	def fetch(self, carrierComponentExt=repcap.CarrierComponentExt.Default) -> List[float]:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST[:CC<carrier>]:IEMission:MARGin:EXTReme \n
		Snippet: value: List[float] = driver.nrMmwMeas.multiEval.listPy.cc.iemission.margin.extreme.fetch(carrierComponentExt = repcap.CarrierComponentExt.Default) \n
		Return the in-band emission limit line margin results for all measured list mode segments, for carrier <c>. The CURRent
		margins indicate the minimum (vertical) distance between the limit line and the current trace. A negative result
		indicates that the limit is exceeded. The AVERage, EXTReme and SDEViation values are calculated from the current margins.
		The results are returned as triplets per segment: <Reliability>, {<Margin>, <IQImage>, <CarrLeakage>}seg 1, {<Margin>,
		<IQImage>, <CarrLeakage>}seg 2, ... \n
		Suppressed linked return values: reliability \n
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: margin: Margin over all non-allocated RBs (scope of general limit component)"""
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:CC{carrierComponentExt_cmd_val}:IEMission:MARGin:EXTReme?', suppressed)
		return response
