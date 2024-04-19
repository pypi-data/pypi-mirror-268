from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ........Internal.Types import DataType
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExtremeCls:
	"""Extreme commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("extreme", core, parent)

	def fetch(self, carrierComponentExt=repcap.CarrierComponentExt.Default, ripple=repcap.Ripple.Default) -> List[float]:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST[:CC<carrier>]:ESFLatness:RIPPle<nr>:EXTReme \n
		Snippet: value: List[float] = driver.nrMmwMeas.multiEval.listPy.cc.esFlatness.ripple.extreme.fetch(carrierComponentExt = repcap.CarrierComponentExt.Default, ripple = repcap.Ripple.Default) \n
		Return equalizer spectrum flatness single value results (ripple 1 or ripple 2) for all measured list mode segments, for
		carrier <c>. The values described below are returned by FETCh commands. CALCulate commands return limit check results
		instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param ripple: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ripple')
			:return: ripple: Comma-separated list of values, one per measured segment"""
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		ripple_cmd_val = self._cmd_group.get_repcap_cmd_value(ripple, repcap.Ripple)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:CC{carrierComponentExt_cmd_val}:ESFLatness:RIPPle{ripple_cmd_val}:EXTReme?', suppressed)
		return response

	def calculate(self, carrierComponentExt=repcap.CarrierComponentExt.Default, ripple=repcap.Ripple.Default) -> List[float or bool]:
		"""SCPI: CALCulate:NRMMw:MEASurement<Instance>:MEValuation:LIST[:CC<carrier>]:ESFLatness:RIPPle<nr>:EXTReme \n
		Snippet: value: List[float or bool] = driver.nrMmwMeas.multiEval.listPy.cc.esFlatness.ripple.extreme.calculate(carrierComponentExt = repcap.CarrierComponentExt.Default, ripple = repcap.Ripple.Default) \n
		Return equalizer spectrum flatness single value results (ripple 1 or ripple 2) for all measured list mode segments, for
		carrier <c>. The values described below are returned by FETCh commands. CALCulate commands return limit check results
		instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param ripple: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ripple')
			:return: ripple: (float or boolean items) Comma-separated list of values, one per measured segment"""
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		ripple_cmd_val = self._cmd_group.get_repcap_cmd_value(ripple, repcap.Ripple)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:NRMMw:MEASurement<Instance>:MEValuation:LIST:CC{carrierComponentExt_cmd_val}:ESFLatness:RIPPle{ripple_cmd_val}:EXTReme?', suppressed)
		return Conversions.str_to_float_or_bool_list(response)
