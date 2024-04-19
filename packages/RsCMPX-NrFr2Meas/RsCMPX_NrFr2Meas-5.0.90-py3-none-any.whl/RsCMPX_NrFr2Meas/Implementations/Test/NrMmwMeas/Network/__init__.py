from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NetworkCls:
	"""Network commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("network", core, parent)

	@property
	def cc(self):
		"""cc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cc'):
			from .Cc import CcCls
			self._cc = CcCls(self._core, self._cmd_group)
		return self._cc

	@property
	def caggregation(self):
		"""caggregation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_caggregation'):
			from .Caggregation import CaggregationCls
			self._caggregation = CaggregationCls(self._core, self._cmd_group)
		return self._caggregation

	def get_ncarrier(self) -> int:
		"""SCPI: TEST:NRMMw:MEASurement<Instance>:NETWork:NCARrier \n
		Snippet: value: int = driver.test.nrMmwMeas.network.get_ncarrier() \n
		No command help available \n
			:return: number: No help available
		"""
		response = self._core.io.query_str('TEST:NRMMw:MEASurement<Instance>:NETWork:NCARrier?')
		return Conversions.str_to_int(response)

	def set_ncarrier(self, number: int) -> None:
		"""SCPI: TEST:NRMMw:MEASurement<Instance>:NETWork:NCARrier \n
		Snippet: driver.test.nrMmwMeas.network.set_ncarrier(number = 1) \n
		No command help available \n
			:param number: No help available
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'TEST:NRMMw:MEASurement<Instance>:NETWork:NCARrier {param}')

	def clone(self) -> 'NetworkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NetworkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
