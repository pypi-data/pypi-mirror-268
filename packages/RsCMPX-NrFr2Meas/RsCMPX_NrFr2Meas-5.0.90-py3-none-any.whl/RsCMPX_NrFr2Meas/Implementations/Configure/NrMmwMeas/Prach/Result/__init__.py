from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	def get_modulation(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:MODulation \n
		Snippet: value: bool = driver.configure.nrMmwMeas.prach.result.get_modulation() \n
		Enables or disables the evaluation of modulation results in the PRACH measurement. \n
			:return: enable: OFF: Do not evaluate the results. ON: Evaluate the results.
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:MODulation?')
		return Conversions.str_to_bool(response)

	def set_modulation(self, enable: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:MODulation \n
		Snippet: driver.configure.nrMmwMeas.prach.result.set_modulation(enable = False) \n
		Enables or disables the evaluation of modulation results in the PRACH measurement. \n
			:param enable: OFF: Do not evaluate the results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:MODulation {param}')

	def get_pdynamics(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:PDYNamics \n
		Snippet: value: bool = driver.configure.nrMmwMeas.prach.result.get_pdynamics() \n
		Enables or disables the evaluation of power dynamics results in the PRACH measurement. \n
			:return: enable: OFF: Do not evaluate the results. ON: Evaluate the results.
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:PDYNamics?')
		return Conversions.str_to_bool(response)

	def set_pdynamics(self, enable: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:PDYNamics \n
		Snippet: driver.configure.nrMmwMeas.prach.result.set_pdynamics(enable = False) \n
		Enables or disables the evaluation of power dynamics results in the PRACH measurement. \n
			:param enable: OFF: Do not evaluate the results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:PDYNamics {param}')

	def clone(self) -> 'ResultCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ResultCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
