from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CaggregationCls:
	"""Caggregation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("caggregation", core, parent)

	def set(self) -> None:
		"""SCPI: TEST:NRMMw:MEASurement<Instance>:NETWork:CAGGregation \n
		Snippet: driver.test.nrMmwMeas.network.caggregation.set() \n
		No command help available \n
		"""
		self._core.io.write(f'TEST:NRMMw:MEASurement<Instance>:NETWork:CAGGregation')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: TEST:NRMMw:MEASurement<Instance>:NETWork:CAGGregation \n
		Snippet: driver.test.nrMmwMeas.network.caggregation.set_with_opc() \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCMPX_NrFr2Meas.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'TEST:NRMMw:MEASurement<Instance>:NETWork:CAGGregation', opc_timeout_ms)
