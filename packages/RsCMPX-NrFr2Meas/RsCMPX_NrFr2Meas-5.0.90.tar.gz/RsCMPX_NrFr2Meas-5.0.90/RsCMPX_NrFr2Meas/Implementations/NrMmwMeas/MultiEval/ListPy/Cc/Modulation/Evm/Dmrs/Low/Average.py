from typing import List

from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ..........Internal.Types import DataType
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def fetch(self, carrierComponentExt=repcap.CarrierComponentExt.Default) -> List[float]:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST[:CC<carrier>]:MODulation:EVM:DMRS:LOW:AVERage \n
		Snippet: value: List[float] = driver.nrMmwMeas.multiEval.listPy.cc.modulation.evm.dmrs.low.average.fetch(carrierComponentExt = repcap.CarrierComponentExt.Default) \n
		Return error vector magnitude DMRS values for low and high EVM window position, for all measured list mode segments, for
		carrier <c>. The values described below are returned by FETCh commands. CALCulate commands return limit check results
		instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: evm_dmrs_low: Comma-separated list of values, one per measured segment"""
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:CC{carrierComponentExt_cmd_val}:MODulation:EVM:DMRS:LOW:AVERage?', suppressed)
		return response

	def calculate(self, carrierComponentExt=repcap.CarrierComponentExt.Default) -> List[float or bool]:
		"""SCPI: CALCulate:NRMMw:MEASurement<Instance>:MEValuation:LIST[:CC<carrier>]:MODulation:EVM:DMRS:LOW:AVERage \n
		Snippet: value: List[float or bool] = driver.nrMmwMeas.multiEval.listPy.cc.modulation.evm.dmrs.low.average.calculate(carrierComponentExt = repcap.CarrierComponentExt.Default) \n
		Return error vector magnitude DMRS values for low and high EVM window position, for all measured list mode segments, for
		carrier <c>. The values described below are returned by FETCh commands. CALCulate commands return limit check results
		instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: evm_dmrs_low: (float or boolean items) Comma-separated list of values, one per measured segment"""
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:NRMMw:MEASurement<Instance>:MEValuation:LIST:CC{carrierComponentExt_cmd_val}:MODulation:EVM:DMRS:LOW:AVERage?', suppressed)
		return Conversions.str_to_float_or_bool_list(response)
