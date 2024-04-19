from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEvalCls:
	"""MultiEval commands group definition. 79 total commands, 9 Subgroups, 10 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multiEval", core, parent)

	@property
	def pcomp(self):
		"""pcomp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcomp'):
			from .Pcomp import PcompCls
			self._pcomp = PcompCls(self._core, self._cmd_group)
		return self._pcomp

	@property
	def mslot(self):
		"""mslot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mslot'):
			from .Mslot import MslotCls
			self._mslot = MslotCls(self._core, self._cmd_group)
		return self._mslot

	@property
	def spectrum(self):
		"""spectrum commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_spectrum'):
			from .Spectrum import SpectrumCls
			self._spectrum = SpectrumCls(self._core, self._cmd_group)
		return self._spectrum

	@property
	def modulation(self):
		"""modulation commands group. 4 Sub-classes, 2 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import ModulationCls
			self._modulation = ModulationCls(self._core, self._cmd_group)
		return self._modulation

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def pdynamics(self):
		"""pdynamics commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdynamics'):
			from .Pdynamics import PdynamicsCls
			self._pdynamics = PdynamicsCls(self._core, self._cmd_group)
		return self._pdynamics

	@property
	def scount(self):
		"""scount commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_scount'):
			from .Scount import ScountCls
			self._scount = ScountCls(self._core, self._cmd_group)
		return self._scount

	@property
	def result(self):
		"""result commands group. 1 Sub-classes, 13 commands."""
		if not hasattr(self, '_result'):
			from .Result import ResultCls
			self._result = ResultCls(self._core, self._cmd_group)
		return self._result

	@property
	def limit(self):
		"""limit commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import LimitCls
			self._limit = LimitCls(self._core, self._cmd_group)
		return self._limit

	# noinspection PyTypeChecker
	def get_pformat(self) -> enums.PucchFormat:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:PFORmat \n
		Snippet: value: enums.PucchFormat = driver.configure.nrMmwMeas.multiEval.get_pformat() \n
		No command help available \n
			:return: pucch_format: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:PFORmat?')
		return Conversions.str_to_scalar_enum(response, enums.PucchFormat)

	def set_pformat(self, pucch_format: enums.PucchFormat) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:PFORmat \n
		Snippet: driver.configure.nrMmwMeas.multiEval.set_pformat(pucch_format = enums.PucchFormat.F0) \n
		No command help available \n
			:param pucch_format: No help available
		"""
		param = Conversions.enum_scalar_to_str(pucch_format, enums.PucchFormat)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:PFORmat {param}')

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:TOUT \n
		Snippet: value: float = driver.configure.nrMmwMeas.multiEval.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually. When the measurement has completed the first measurement
		cycle (first single shot) , the statistical depth is reached and the timer is reset. If the first measurement cycle has
		not been completed when the timer expires, the measurement is stopped. The measurement state changes to RDY.
		The reliability indicator is set to 1, indicating that a measurement timeout occurred. Still running READ, FETCh or
		CALCulate commands are completed, returning the available results. At least for some results, there are no values at all
		or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite measurement timeout. \n
			:return: timeout: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:TOUT \n
		Snippet: driver.configure.nrMmwMeas.multiEval.set_timeout(timeout = 1.0) \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually. When the measurement has completed the first measurement
		cycle (first single shot) , the statistical depth is reached and the timer is reset. If the first measurement cycle has
		not been completed when the timer expires, the measurement is stopped. The measurement state changes to RDY.
		The reliability indicator is set to 1, indicating that a measurement timeout occurred. Still running READ, FETCh or
		CALCulate commands are completed, returning the available results. At least for some results, there are no values at all
		or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite measurement timeout. \n
			:param timeout: No help available
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:TOUT {param}')

	# noinspection PyTypeChecker
	def get_dmode(self) -> enums.DuplexModeB:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:DMODe \n
		Snippet: value: enums.DuplexModeB = driver.configure.nrMmwMeas.multiEval.get_dmode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:DMODe?')
		return Conversions.str_to_scalar_enum(response, enums.DuplexModeB)

	def set_dmode(self, mode: enums.DuplexModeB) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:DMODe \n
		Snippet: driver.configure.nrMmwMeas.multiEval.set_dmode(mode = enums.DuplexModeB.FDD) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.DuplexModeB)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:DMODe {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.nrMmwMeas.multiEval.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:return: repetition: SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:REPetition \n
		Snippet: driver.configure.nrMmwMeas.multiEval.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:param repetition: SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:REPetition {param}')

	# noinspection PyTypeChecker
	def get_scondition(self) -> enums.StopCondition:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:SCONdition \n
		Snippet: value: enums.StopCondition = driver.configure.nrMmwMeas.multiEval.get_scondition() \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:return: stop_condition: NONE: Continue measurement irrespective of the limit check. SLFail: Stop measurement on limit failure.
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:SCONdition?')
		return Conversions.str_to_scalar_enum(response, enums.StopCondition)

	def set_scondition(self, stop_condition: enums.StopCondition) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:SCONdition \n
		Snippet: driver.configure.nrMmwMeas.multiEval.set_scondition(stop_condition = enums.StopCondition.NONE) \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:param stop_condition: NONE: Continue measurement irrespective of the limit check. SLFail: Stop measurement on limit failure.
		"""
		param = Conversions.enum_scalar_to_str(stop_condition, enums.StopCondition)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:SCONdition {param}')

	# noinspection PyTypeChecker
	def get_mmode(self) -> enums.MeasurementMode:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MMODe \n
		Snippet: value: enums.MeasurementMode = driver.configure.nrMmwMeas.multiEval.get_mmode() \n
		Selects the measurement mode. \n
			:return: measurement_mode: NORMal: normal mode MELMode: multi-evaluation list mode For a setting command, only NORMal is allowed (disables the list mode) . A query can also return MELM.
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MMODe?')
		return Conversions.str_to_scalar_enum(response, enums.MeasurementMode)

	def set_mmode(self, measurement_mode: enums.MeasurementMode) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MMODe \n
		Snippet: driver.configure.nrMmwMeas.multiEval.set_mmode(measurement_mode = enums.MeasurementMode.MELMode) \n
		Selects the measurement mode. \n
			:param measurement_mode: NORMal: normal mode MELMode: multi-evaluation list mode For a setting command, only NORMal is allowed (disables the list mode) . A query can also return MELM.
		"""
		param = Conversions.enum_scalar_to_str(measurement_mode, enums.MeasurementMode)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MMODe {param}')

	def get_mo_exception(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MOEXception \n
		Snippet: value: bool = driver.configure.nrMmwMeas.multiEval.get_mo_exception() \n
		Specifies whether measurement results identified as faulty or inaccurate are rejected. \n
			:return: meas_on_exception: OFF: Faulty results are rejected. ON: Results are never rejected.
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MOEXception?')
		return Conversions.str_to_bool(response)

	def set_mo_exception(self, meas_on_exception: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MOEXception \n
		Snippet: driver.configure.nrMmwMeas.multiEval.set_mo_exception(meas_on_exception = False) \n
		Specifies whether measurement results identified as faulty or inaccurate are rejected. \n
			:param meas_on_exception: OFF: Faulty results are rejected. ON: Results are never rejected.
		"""
		param = Conversions.bool_to_str(meas_on_exception)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MOEXception {param}')

	def get_nsub_frames(self) -> int:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:NSUBframes \n
		Snippet: value: int = driver.configure.nrMmwMeas.multiEval.get_nsub_frames() \n
		Specifies the number of subframes to be evaluated. If you use two RX antennas, the maximum allowed value is reduced to 10. \n
			:return: no_subframe: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:NSUBframes?')
		return Conversions.str_to_int(response)

	def set_nsub_frames(self, no_subframe: int) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:NSUBframes \n
		Snippet: driver.configure.nrMmwMeas.multiEval.set_nsub_frames(no_subframe = 1) \n
		Specifies the number of subframes to be evaluated. If you use two RX antennas, the maximum allowed value is reduced to 10. \n
			:param no_subframe: No help available
		"""
		param = Conversions.decimal_value_to_str(no_subframe)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:NSUBframes {param}')

	# noinspection PyTypeChecker
	def get_fstructure(self) -> enums.ConfigType:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:FSTRucture \n
		Snippet: value: enums.ConfigType = driver.configure.nrMmwMeas.multiEval.get_fstructure() \n
		No command help available \n
			:return: frame_structure: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:FSTRucture?')
		return Conversions.str_to_scalar_enum(response, enums.ConfigType)

	def get_ghopping(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:GHOPping \n
		Snippet: value: bool = driver.configure.nrMmwMeas.multiEval.get_ghopping() \n
		No command help available \n
			:return: value: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:GHOPping?')
		return Conversions.str_to_bool(response)

	def set_ghopping(self, value: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:GHOPping \n
		Snippet: driver.configure.nrMmwMeas.multiEval.set_ghopping(value = False) \n
		No command help available \n
			:param value: No help available
		"""
		param = Conversions.bool_to_str(value)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:GHOPping {param}')

	def clone(self) -> 'MultiEvalCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiEvalCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
