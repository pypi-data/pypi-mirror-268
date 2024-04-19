from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PvPreambleCls:
	"""PvPreamble commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pvPreamble", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:NRMMw:MEASurement<Instance>:PRACh:TRACe:PVPReamble \n
		Snippet: value: List[float] = driver.nrMmwMeas.prach.trace.pvPreamble.read() \n
		Return the values of the power vs preamble traces. See also 'Squares EVM vs Preamble, Power vs Preamble'. \n
		Suppressed linked return values: reliability \n
			:return: results: Comma-separated list of power values, for preamble 1 to n of the measurement interval."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:NRMMw:MEASurement<Instance>:PRACh:TRACe:PVPReamble?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:PRACh:TRACe:PVPReamble \n
		Snippet: value: List[float] = driver.nrMmwMeas.prach.trace.pvPreamble.fetch() \n
		Return the values of the power vs preamble traces. See also 'Squares EVM vs Preamble, Power vs Preamble'. \n
		Suppressed linked return values: reliability \n
			:return: results: Comma-separated list of power values, for preamble 1 to n of the measurement interval."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:NRMMw:MEASurement<Instance>:PRACh:TRACe:PVPReamble?', suppressed)
		return response
