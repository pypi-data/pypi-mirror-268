from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CaggregationCls:
	"""Caggregation commands group definition. 7 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("caggregation", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def cbandwidth(self):
		"""cbandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbandwidth'):
			from .Cbandwidth import CbandwidthCls
			self._cbandwidth = CbandwidthCls(self._core, self._cmd_group)
		return self._cbandwidth

	@property
	def acSpacing(self):
		"""acSpacing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_acSpacing'):
			from .AcSpacing import AcSpacingCls
			self._acSpacing = AcSpacingCls(self._core, self._cmd_group)
		return self._acSpacing

	@property
	def ngBandwidth(self):
		"""ngBandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ngBandwidth'):
			from .NgBandwidth import NgBandwidthCls
			self._ngBandwidth = NgBandwidthCls(self._core, self._cmd_group)
		return self._ngBandwidth

	# noinspection PyTypeChecker
	def get_mcarrier(self) -> enums.MeasCarrier:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:CAGGregation:MCARrier \n
		Snippet: value: enums.MeasCarrier = driver.configure.nrMmwMeas.caggregation.get_mcarrier() \n
		Selects a component carrier for synchronization and single carrier measurements (power dynamics) . \n
			:return: meas_carrier: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:CAGGregation:MCARrier?')
		return Conversions.str_to_scalar_enum(response, enums.MeasCarrier)

	def set_mcarrier(self, meas_carrier: enums.MeasCarrier) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:CAGGregation:MCARrier \n
		Snippet: driver.configure.nrMmwMeas.caggregation.set_mcarrier(meas_carrier = enums.MeasCarrier.CC1) \n
		Selects a component carrier for synchronization and single carrier measurements (power dynamics) . \n
			:param meas_carrier: No help available
		"""
		param = Conversions.enum_scalar_to_str(meas_carrier, enums.MeasCarrier)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:CAGGregation:MCARrier {param}')

	def clone(self) -> 'CaggregationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CaggregationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
