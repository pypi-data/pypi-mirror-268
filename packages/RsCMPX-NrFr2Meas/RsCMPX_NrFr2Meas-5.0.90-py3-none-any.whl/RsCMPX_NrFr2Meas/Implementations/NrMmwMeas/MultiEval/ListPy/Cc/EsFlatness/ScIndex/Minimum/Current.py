from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .........Internal.Types import DataType
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def fetch(self, carrierComponentExt=repcap.CarrierComponentExt.Default, minimum=repcap.Minimum.Default) -> List[int]:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST[:CC<carrier>]:ESFLatness:SCINdex:MINimum<nr>:CURRent \n
		Snippet: value: List[int] = driver.nrMmwMeas.multiEval.listPy.cc.esFlatness.scIndex.minimum.current.fetch(carrierComponentExt = repcap.CarrierComponentExt.Default, minimum = repcap.Minimum.Default) \n
		Return subcarrier indices of the equalizer spectrum flatness measurement for all measured list mode segments, for carrier
		<c>. At these SC indices, the current MINimum or MAXimum power of the equalizer coefficients has been detected within the
		selected range. \n
		Suppressed linked return values: reliability \n
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param minimum: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Minimum')
			:return: minimum: Comma-separated list of values, one per measured segment"""
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		minimum_cmd_val = self._cmd_group.get_repcap_cmd_value(minimum, repcap.Minimum)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:CC{carrierComponentExt_cmd_val}:ESFLatness:SCINdex:MINimum{minimum_cmd_val}:CURRent?', suppressed)
		return response
