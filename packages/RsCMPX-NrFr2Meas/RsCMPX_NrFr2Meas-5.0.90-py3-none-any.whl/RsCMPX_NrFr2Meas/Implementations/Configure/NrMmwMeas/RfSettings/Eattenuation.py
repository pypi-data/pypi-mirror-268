from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EattenuationCls:
	"""Eattenuation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eattenuation", core, parent)

	def set(self, rf_input_ext_att: float, rf_input_ext_att_2: float = None) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:RFSettings:EATTenuation \n
		Snippet: driver.configure.nrMmwMeas.rfSettings.eattenuation.set(rf_input_ext_att = 1.0, rf_input_ext_att_2 = 1.0) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector.
		A query returns 1 or 2 values, depending on the number of RX antennas configured via method RsCMPX_NrFr2Meas.Configure.
		NrMmwMeas.nantenna. With full RF path sharing, this command is not applicable. \n
			:param rf_input_ext_att: For input path with antenna 1
			:param rf_input_ext_att_2: For input path with antenna 2
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('rf_input_ext_att', rf_input_ext_att, DataType.Float), ArgSingle('rf_input_ext_att_2', rf_input_ext_att_2, DataType.Float, None, is_optional=True))
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:RFSettings:EATTenuation {param}'.rstrip())

	# noinspection PyTypeChecker
	class EattenuationStruct(StructBase):
		"""Response structure. Fields: \n
			- Rf_Input_Ext_Att: float: For input path with antenna 1
			- Rf_Input_Ext_Att_2: float: For input path with antenna 2"""
		__meta_args_list = [
			ArgStruct.scalar_float('Rf_Input_Ext_Att'),
			ArgStruct.scalar_float('Rf_Input_Ext_Att_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rf_Input_Ext_Att: float = None
			self.Rf_Input_Ext_Att_2: float = None

	def get(self) -> EattenuationStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:RFSettings:EATTenuation \n
		Snippet: value: EattenuationStruct = driver.configure.nrMmwMeas.rfSettings.eattenuation.get() \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector.
		A query returns 1 or 2 values, depending on the number of RX antennas configured via method RsCMPX_NrFr2Meas.Configure.
		NrMmwMeas.nantenna. With full RF path sharing, this command is not applicable. \n
			:return: structure: for return value, see the help for EattenuationStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:RFSettings:EATTenuation?', self.__class__.EattenuationStruct())
