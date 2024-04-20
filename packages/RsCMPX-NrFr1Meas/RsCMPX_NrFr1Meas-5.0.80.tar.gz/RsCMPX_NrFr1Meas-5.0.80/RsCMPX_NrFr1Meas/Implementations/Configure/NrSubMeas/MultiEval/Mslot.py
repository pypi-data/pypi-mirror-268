from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MslotCls:
	"""Mslot commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mslot", core, parent)

	def set(self, measure_slot: enums.MeasureSlot, meas_slot_no: int = None) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:MSLot \n
		Snippet: driver.configure.nrSubMeas.multiEval.mslot.set(measure_slot = enums.MeasureSlot.ALL, meas_slot_no = 1) \n
		Selects which slots within the first 10 captured subframes are evaluated. \n
			:param measure_slot: ALL: all slots UDEF: single slot selected via MeasSlotNo
			:param meas_slot_no: Slot number for MeasureSlot=UDEF The number of slots per subframe depends on the SCS. The slot must be within the captured number of subframes, limited to 10 subframes, see method RsCMPX_NrFr1Meas.Configure.NrSubMeas.MultiEval.nsubFrames.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('measure_slot', measure_slot, DataType.Enum, enums.MeasureSlot), ArgSingle('meas_slot_no', meas_slot_no, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:MSLot {param}'.rstrip())

	# noinspection PyTypeChecker
	class MslotStruct(StructBase):
		"""Response structure. Fields: \n
			- Measure_Slot: enums.MeasureSlot: ALL: all slots UDEF: single slot selected via MeasSlotNo
			- Meas_Slot_No: int: Slot number for MeasureSlot=UDEF The number of slots per subframe depends on the SCS. The slot must be within the captured number of subframes, limited to 10 subframes, see [CMDLINKRESOLVED Configure.NrSubMeas.MultiEval#NsubFrames CMDLINKRESOLVED]."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Measure_Slot', enums.MeasureSlot),
			ArgStruct.scalar_int('Meas_Slot_No')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Measure_Slot: enums.MeasureSlot = None
			self.Meas_Slot_No: int = None

	def get(self) -> MslotStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:MSLot \n
		Snippet: value: MslotStruct = driver.configure.nrSubMeas.multiEval.mslot.get() \n
		Selects which slots within the first 10 captured subframes are evaluated. \n
			:return: structure: for return value, see the help for MslotStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:MSLot?', self.__class__.MslotStruct())
