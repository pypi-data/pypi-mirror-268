from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ........Internal.Types import DataType
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def fetch(self, carrierComponentExt=repcap.CarrierComponentExt.Default, difference=repcap.Difference.Default) -> List[float]:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST[:CC<carrier>]:ESFLatness:DIFFerence<nr>:AVERage \n
		Snippet: value: List[float] = driver.nrMmwMeas.multiEval.listPy.cc.esFlatness.difference.average.fetch(carrierComponentExt = repcap.CarrierComponentExt.Default, difference = repcap.Difference.Default) \n
		Return equalizer spectrum flatness single value results (differences between ranges) for all measured list mode segments,
		for carrier <c>. The values described below are returned by FETCh commands. CALCulate commands return limit check results
		instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param difference: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Difference')
			:return: difference: Comma-separated list of values, one per measured segment"""
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		difference_cmd_val = self._cmd_group.get_repcap_cmd_value(difference, repcap.Difference)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:CC{carrierComponentExt_cmd_val}:ESFLatness:DIFFerence{difference_cmd_val}:AVERage?', suppressed)
		return response

	def calculate(self, carrierComponentExt=repcap.CarrierComponentExt.Default, difference=repcap.Difference.Default) -> List[float or bool]:
		"""SCPI: CALCulate:NRMMw:MEASurement<Instance>:MEValuation:LIST[:CC<carrier>]:ESFLatness:DIFFerence<nr>:AVERage \n
		Snippet: value: List[float or bool] = driver.nrMmwMeas.multiEval.listPy.cc.esFlatness.difference.average.calculate(carrierComponentExt = repcap.CarrierComponentExt.Default, difference = repcap.Difference.Default) \n
		Return equalizer spectrum flatness single value results (differences between ranges) for all measured list mode segments,
		for carrier <c>. The values described below are returned by FETCh commands. CALCulate commands return limit check results
		instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param difference: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Difference')
			:return: difference: (float or boolean items) Comma-separated list of values, one per measured segment"""
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		difference_cmd_val = self._cmd_group.get_repcap_cmd_value(difference, repcap.Difference)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:NRMMw:MEASurement<Instance>:MEValuation:LIST:CC{carrierComponentExt_cmd_val}:ESFLatness:DIFFerence{difference_cmd_val}:AVERage?', suppressed)
		return Conversions.str_to_float_or_bool_list(response)
