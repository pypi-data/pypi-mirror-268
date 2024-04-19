from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NrMmwMeasCls:
	"""NrMmwMeas commands group definition. 195 total commands, 10 Subgroups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nrMmwMeas", core, parent)

	@property
	def multiEval(self):
		"""multiEval commands group. 9 Sub-classes, 10 commands."""
		if not hasattr(self, '_multiEval'):
			from .MultiEval import MultiEvalCls
			self._multiEval = MultiEvalCls(self._core, self._cmd_group)
		return self._multiEval

	@property
	def rfSettings(self):
		"""rfSettings commands group. 2 Sub-classes, 8 commands."""
		if not hasattr(self, '_rfSettings'):
			from .RfSettings import RfSettingsCls
			self._rfSettings = RfSettingsCls(self._core, self._cmd_group)
		return self._rfSettings

	@property
	def network(self):
		"""network commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_network'):
			from .Network import NetworkCls
			self._network = NetworkCls(self._core, self._cmd_group)
		return self._network

	@property
	def susage(self):
		"""susage commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_susage'):
			from .Susage import SusageCls
			self._susage = SusageCls(self._core, self._cmd_group)
		return self._susage

	@property
	def ulDl(self):
		"""ulDl commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ulDl'):
			from .UlDl import UlDlCls
			self._ulDl = UlDlCls(self._core, self._cmd_group)
		return self._ulDl

	@property
	def cc(self):
		"""cc commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_cc'):
			from .Cc import CcCls
			self._cc = CcCls(self._core, self._cmd_group)
		return self._cc

	@property
	def ccall(self):
		"""ccall commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccall'):
			from .Ccall import CcallCls
			self._ccall = CcallCls(self._core, self._cmd_group)
		return self._ccall

	@property
	def caggregation(self):
		"""caggregation commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_caggregation'):
			from .Caggregation import CaggregationCls
			self._caggregation = CaggregationCls(self._core, self._cmd_group)
		return self._caggregation

	@property
	def listPy(self):
		"""listPy commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPyCls
			self._listPy = ListPyCls(self._core, self._cmd_group)
		return self._listPy

	@property
	def prach(self):
		"""prach commands group. 7 Sub-classes, 12 commands."""
		if not hasattr(self, '_prach'):
			from .Prach import PrachCls
			self._prach = PrachCls(self._core, self._cmd_group)
		return self._prach

	# noinspection PyTypeChecker
	def get_spath(self) -> enums.Path:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:SPATh \n
		Snippet: value: enums.Path = driver.configure.nrMmwMeas.get_spath() \n
		Selects between a standalone measurement and a measurement with coupling to signaling settings (cell settings of the
		network configuration) . \n
			:return: path: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:SPATh?')
		return Conversions.str_to_scalar_enum(response, enums.Path)

	def set_spath(self, path: enums.Path) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:SPATh \n
		Snippet: driver.configure.nrMmwMeas.set_spath(path = enums.Path.NETWork) \n
		Selects between a standalone measurement and a measurement with coupling to signaling settings (cell settings of the
		network configuration) . \n
			:param path: No help available
		"""
		param = Conversions.enum_scalar_to_str(path, enums.Path)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:SPATh {param}')

	def get_nantenna(self) -> int:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:NANTenna \n
		Snippet: value: int = driver.configure.nrMmwMeas.get_nantenna() \n
		Selects the number of RX antennas used by the measurement. \n
			:return: number: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:NANTenna?')
		return Conversions.str_to_int(response)

	def set_nantenna(self, number: int) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:NANTenna \n
		Snippet: driver.configure.nrMmwMeas.set_nantenna(number = 1) \n
		Selects the number of RX antennas used by the measurement. \n
			:param number: No help available
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:NANTenna {param}')

	# noinspection PyTypeChecker
	def get_band(self) -> enums.Band:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:BAND \n
		Snippet: value: enums.Band = driver.configure.nrMmwMeas.get_band() \n
		Selects the frequency band. For Signal Path = Network, use[CONFigure:]SIGNaling:NRADio:CELL:RFSettings:FBINdicator. \n
			:return: band: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:BAND?')
		return Conversions.str_to_scalar_enum(response, enums.Band)

	def set_band(self, band: enums.Band) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:BAND \n
		Snippet: driver.configure.nrMmwMeas.set_band(band = enums.Band.B257) \n
		Selects the frequency band. For Signal Path = Network, use[CONFigure:]SIGNaling:NRADio:CELL:RFSettings:FBINdicator. \n
			:param band: No help available
		"""
		param = Conversions.enum_scalar_to_str(band, enums.Band)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:BAND {param}')

	# noinspection PyTypeChecker
	def get_ns_value(self) -> enums.NsValue:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:NSValue \n
		Snippet: value: enums.NsValue = driver.configure.nrMmwMeas.get_ns_value() \n
		No command help available \n
			:return: value: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:NSValue?')
		return Conversions.str_to_scalar_enum(response, enums.NsValue)

	def set_ns_value(self, value: enums.NsValue) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:NSValue \n
		Snippet: driver.configure.nrMmwMeas.set_ns_value(value = enums.NsValue.NS01) \n
		No command help available \n
			:param value: No help available
		"""
		param = Conversions.enum_scalar_to_str(value, enums.NsValue)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:NSValue {param}')

	def get_ncarrier(self) -> int:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:NCARrier \n
		Snippet: value: int = driver.configure.nrMmwMeas.get_ncarrier() \n
		Configures the number of contiguously aggregated UL carriers in the measured signal. For Signal Path = Network, use the
		signaling commands configuring contiguous UL CA. \n
			:return: number: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:NCARrier?')
		return Conversions.str_to_int(response)

	def set_ncarrier(self, number: int) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:NCARrier \n
		Snippet: driver.configure.nrMmwMeas.set_ncarrier(number = 1) \n
		Configures the number of contiguously aggregated UL carriers in the measured signal. For Signal Path = Network, use the
		signaling commands configuring contiguous UL CA. \n
			:param number: No help available
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:NCARrier {param}')

	def get_iqswap(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:IQSWap \n
		Snippet: value: bool = driver.configure.nrMmwMeas.get_iqswap() \n
		Enables or disables I/Q swapping (mapping the I values to the Q channel and vice versa) . \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:IQSWap?')
		return Conversions.str_to_bool(response)

	def set_iqswap(self, enable: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:IQSWap \n
		Snippet: driver.configure.nrMmwMeas.set_iqswap(enable = False) \n
		Enables or disables I/Q swapping (mapping the I values to the Q channel and vice versa) . \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:IQSWap {param}')

	def get_do_signaling(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:DOSignaling \n
		Snippet: value: bool = driver.configure.nrMmwMeas.get_do_signaling() \n
		No command help available \n
			:return: path: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:DOSignaling?')
		return Conversions.str_to_bool(response)

	def set_do_signaling(self, path: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:DOSignaling \n
		Snippet: driver.configure.nrMmwMeas.set_do_signaling(path = False) \n
		No command help available \n
			:param path: No help available
		"""
		param = Conversions.bool_to_str(path)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:DOSignaling {param}')

	# noinspection PyTypeChecker
	def get_pclass(self) -> enums.PowerClass:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PCLass \n
		Snippet: value: enums.PowerClass = driver.configure.nrMmwMeas.get_pclass() \n
		Selects the power class of the UE. The setting influences modulation limits. \n
			:return: power_class: Power class 1 to 4
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PCLass?')
		return Conversions.str_to_scalar_enum(response, enums.PowerClass)

	def set_pclass(self, power_class: enums.PowerClass) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PCLass \n
		Snippet: driver.configure.nrMmwMeas.set_pclass(power_class = enums.PowerClass.PC1) \n
		Selects the power class of the UE. The setting influences modulation limits. \n
			:param power_class: Power class 1 to 4
		"""
		param = Conversions.enum_scalar_to_str(power_class, enums.PowerClass)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PCLass {param}')

	def clone(self) -> 'NrMmwMeasCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NrMmwMeasCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
