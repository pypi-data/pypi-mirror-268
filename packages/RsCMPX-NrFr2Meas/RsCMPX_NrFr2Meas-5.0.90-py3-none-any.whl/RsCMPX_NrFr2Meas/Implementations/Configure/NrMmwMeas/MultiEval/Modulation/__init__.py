from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModulationCls:
	"""Modulation commands group definition. 11 total commands, 4 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	@property
	def ewLength(self):
		"""ewLength commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ewLength'):
			from .EwLength import EwLengthCls
			self._ewLength = EwLengthCls(self._core, self._cmd_group)
		return self._ewLength

	@property
	def evmSymbol(self):
		"""evmSymbol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_evmSymbol'):
			from .EvmSymbol import EvmSymbolCls
			self._evmSymbol = EvmSymbolCls(self._core, self._cmd_group)
		return self._evmSymbol

	@property
	def eePeriods(self):
		"""eePeriods commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_eePeriods'):
			from .EePeriods import EePeriodsCls
			self._eePeriods = EePeriodsCls(self._core, self._cmd_group)
		return self._eePeriods

	@property
	def tracking(self):
		"""tracking commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_tracking'):
			from .Tracking import TrackingCls
			self._tracking = TrackingCls(self._core, self._cmd_group)
		return self._tracking

	def get_tdl_offset(self) -> int:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TDLoffset \n
		Snippet: value: int = driver.configure.nrMmwMeas.multiEval.modulation.get_tdl_offset() \n
		Specifies the offset of the UL DC subcarrier from the center frequency (number of subcarriers) . \n
			:return: offset: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TDLoffset?')
		return Conversions.str_to_int(response)

	def set_tdl_offset(self, offset: int) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TDLoffset \n
		Snippet: driver.configure.nrMmwMeas.multiEval.modulation.set_tdl_offset(offset = 1) \n
		Specifies the offset of the UL DC subcarrier from the center frequency (number of subcarriers) . \n
			:param offset: No help available
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TDLoffset {param}')

	def get_dp_receiver(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:DPReceiver \n
		Snippet: value: bool = driver.configure.nrMmwMeas.multiEval.modulation.get_dp_receiver() \n
		Enables maximum ratio combining for modulation measurements with two RX antennas plus one transmission layer. \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:DPReceiver?')
		return Conversions.str_to_bool(response)

	def set_dp_receiver(self, enable: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:DPReceiver \n
		Snippet: driver.configure.nrMmwMeas.multiEval.modulation.set_dp_receiver(enable = False) \n
		Enables maximum ratio combining for modulation measurements with two RX antennas plus one transmission layer. \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:DPReceiver {param}')

	def clone(self) -> 'ModulationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ModulationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
