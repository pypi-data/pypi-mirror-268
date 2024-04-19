from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DmodulationCls:
	"""Dmodulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dmodulation", core, parent)

	# noinspection PyTypeChecker
	def fetch(self, carrierComponentExt=repcap.CarrierComponentExt.Default) -> List[enums.ModScheme]:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST[:CC<carrier>]:MODulation:DMODulation \n
		Snippet: value: List[enums.ModScheme] = driver.nrMmwMeas.multiEval.listPy.cc.modulation.dmodulation.fetch(carrierComponentExt = repcap.CarrierComponentExt.Default) \n
		Returns the modulation scheme for all measured list mode segments, for carrier <c>. The value applies to the last
		measured slot of the statistical length of a segment. \n
		Suppressed linked return values: reliability \n
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: modulation: Comma-separated list of values, one per measured segment π/2-BPSK, BPSK, QPSK, 16QAM, 64QAM, 256QAM"""
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:CC{carrierComponentExt_cmd_val}:MODulation:DMODulation?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ModScheme)
