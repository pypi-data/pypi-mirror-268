from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TrackingCls:
	"""Tracking commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tracking", core, parent)

	def get_timing(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TRACking:TIMing \n
		Snippet: value: bool = driver.configure.nrMmwMeas.multiEval.modulation.tracking.get_timing() \n
		Activate or deactivate timing tracking. With enabled tracking, fluctuations are compensated. \n
			:return: tracking: OFF: Tracking disabled ON: Tracking enabled
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TRACking:TIMing?')
		return Conversions.str_to_bool(response)

	def set_timing(self, tracking: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TRACking:TIMing \n
		Snippet: driver.configure.nrMmwMeas.multiEval.modulation.tracking.set_timing(tracking = False) \n
		Activate or deactivate timing tracking. With enabled tracking, fluctuations are compensated. \n
			:param tracking: OFF: Tracking disabled ON: Tracking enabled
		"""
		param = Conversions.bool_to_str(tracking)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TRACking:TIMing {param}')

	def get_phase(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TRACking:PHASe \n
		Snippet: value: bool = driver.configure.nrMmwMeas.multiEval.modulation.tracking.get_phase() \n
		Activate or deactivate phase tracking. With enabled tracking, fluctuations are compensated. \n
			:return: tracking: OFF: Tracking disabled ON: Tracking enabled
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TRACking:PHASe?')
		return Conversions.str_to_bool(response)

	def set_phase(self, tracking: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TRACking:PHASe \n
		Snippet: driver.configure.nrMmwMeas.multiEval.modulation.tracking.set_phase(tracking = False) \n
		Activate or deactivate phase tracking. With enabled tracking, fluctuations are compensated. \n
			:param tracking: OFF: Tracking disabled ON: Tracking enabled
		"""
		param = Conversions.bool_to_str(tracking)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TRACking:PHASe {param}')

	def get_level(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TRACking:LEVel \n
		Snippet: value: bool = driver.configure.nrMmwMeas.multiEval.modulation.tracking.get_level() \n
		Activate or deactivate level tracking. With enabled tracking, fluctuations are compensated. \n
			:return: tracking: OFF: Tracking disabled ON: Tracking enabled
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TRACking:LEVel?')
		return Conversions.str_to_bool(response)

	def set_level(self, tracking: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TRACking:LEVel \n
		Snippet: driver.configure.nrMmwMeas.multiEval.modulation.tracking.set_level(tracking = False) \n
		Activate or deactivate level tracking. With enabled tracking, fluctuations are compensated. \n
			:param tracking: OFF: Tracking disabled ON: Tracking enabled
		"""
		param = Conversions.bool_to_str(tracking)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TRACking:LEVel {param}')
