from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqOffsetCls:
	"""IqOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqOffset", core, parent)

	def set(self, offset_0: float, offset_1: float, offset_2: float, offset_3: float) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:IBE:IQOFfset \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.bpwShaping.ibe.iqOffset.set(offset_0 = 1.0, offset_1 = 1.0, offset_2 = 1.0, offset_3 = 1.0) \n
		Defines I/Q origin offset values used for calculation of an upper limit for the in-band emission, for π/2-BPSK modulation
		with shaping. Four different values can be set for four TX power ranges. \n
			:param offset_0: I/Q origin offset limit for TX power 10 dBm
			:param offset_1: I/Q origin offset limit for TX power 0 dBm
			:param offset_2: I/Q origin offset limit for TX power -30 dBm
			:param offset_3: I/Q origin offset limit for TX power -40 dBm
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('offset_0', offset_0, DataType.Float), ArgSingle('offset_1', offset_1, DataType.Float), ArgSingle('offset_2', offset_2, DataType.Float), ArgSingle('offset_3', offset_3, DataType.Float))
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:IBE:IQOFfset {param}'.rstrip())

	# noinspection PyTypeChecker
	class IqOffsetStruct(StructBase):
		"""Response structure. Fields: \n
			- Offset_0: float: I/Q origin offset limit for TX power 10 dBm
			- Offset_1: float: I/Q origin offset limit for TX power 0 dBm
			- Offset_2: float: I/Q origin offset limit for TX power -30 dBm
			- Offset_3: float: I/Q origin offset limit for TX power -40 dBm"""
		__meta_args_list = [
			ArgStruct.scalar_float('Offset_0'),
			ArgStruct.scalar_float('Offset_1'),
			ArgStruct.scalar_float('Offset_2'),
			ArgStruct.scalar_float('Offset_3')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Offset_0: float = None
			self.Offset_1: float = None
			self.Offset_2: float = None
			self.Offset_3: float = None

	def get(self) -> IqOffsetStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:IBE:IQOFfset \n
		Snippet: value: IqOffsetStruct = driver.configure.nrSubMeas.multiEval.limit.bpwShaping.ibe.iqOffset.get() \n
		Defines I/Q origin offset values used for calculation of an upper limit for the in-band emission, for π/2-BPSK modulation
		with shaping. Four different values can be set for four TX power ranges. \n
			:return: structure: for return value, see the help for IqOffsetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:IBE:IQOFfset?', self.__class__.IqOffsetStruct())
