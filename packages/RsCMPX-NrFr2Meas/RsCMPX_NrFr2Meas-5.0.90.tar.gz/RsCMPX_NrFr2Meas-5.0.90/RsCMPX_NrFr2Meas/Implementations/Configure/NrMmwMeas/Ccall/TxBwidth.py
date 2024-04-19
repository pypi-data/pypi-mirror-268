from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TxBwidthCls:
	"""TxBwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("txBwidth", core, parent)

	# noinspection PyTypeChecker
	def get_sc_spacing(self) -> enums.ScSpacing:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:CCALl:TXBWidth:SCSPacing \n
		Snippet: value: enums.ScSpacing = driver.configure.nrMmwMeas.ccall.txBwidth.get_sc_spacing() \n
		Selects the subcarrier spacing for all carriers.
		For Signal Path = Network, use[CONFigure:]SIGNaling:NRADio:CELL:RFSettings:SSPacing. \n
			:return: scs: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:CCALl:TXBWidth:SCSPacing?')
		return Conversions.str_to_scalar_enum(response, enums.ScSpacing)

	def set_sc_spacing(self, scs: enums.ScSpacing) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:CCALl:TXBWidth:SCSPacing \n
		Snippet: driver.configure.nrMmwMeas.ccall.txBwidth.set_sc_spacing(scs = enums.ScSpacing.S120k) \n
		Selects the subcarrier spacing for all carriers.
		For Signal Path = Network, use[CONFigure:]SIGNaling:NRADio:CELL:RFSettings:SSPacing. \n
			:param scs: No help available
		"""
		param = Conversions.enum_scalar_to_str(scs, enums.ScSpacing)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:CCALl:TXBWidth:SCSPacing {param}')
