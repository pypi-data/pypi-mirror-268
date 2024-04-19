from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdynamicsCls:
	"""Pdynamics commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdynamics", core, parent)

	@property
	def aeoPower(self):
		"""aeoPower commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_aeoPower'):
			from .AeoPower import AeoPowerCls
			self._aeoPower = AeoPowerCls(self._core, self._cmd_group)
		return self._aeoPower

	# noinspection PyTypeChecker
	def get_tmask(self) -> enums.TimeMask:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:PDYNamics:TMASk \n
		Snippet: value: enums.TimeMask = driver.configure.nrMmwMeas.multiEval.pdynamics.get_tmask() \n
		No command help available \n
			:return: time_mask: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:PDYNamics:TMASk?')
		return Conversions.str_to_scalar_enum(response, enums.TimeMask)

	def set_tmask(self, time_mask: enums.TimeMask) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:PDYNamics:TMASk \n
		Snippet: driver.configure.nrMmwMeas.multiEval.pdynamics.set_tmask(time_mask = enums.TimeMask.GOO) \n
		No command help available \n
			:param time_mask: No help available
		"""
		param = Conversions.enum_scalar_to_str(time_mask, enums.TimeMask)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:PDYNamics:TMASk {param}')

	def clone(self) -> 'PdynamicsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PdynamicsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
