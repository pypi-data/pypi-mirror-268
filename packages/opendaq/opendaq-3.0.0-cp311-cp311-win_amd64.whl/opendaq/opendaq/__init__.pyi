"""
openDAQ python bindings
"""
from __future__ import annotations
import numpy
import typing
__all__ = ['AndSearchFilter', 'AnySearchFilter', 'ArgumentInfo', 'BaseObject', 'BasicFileLoggerSink', 'BlockReader', 'BlockReaderFromExisting', 'BlockReaderStatus', 'BoolProperty', 'BoolPropertyBuilder', 'Boolean', 'CallableInfo', 'Client', 'CmdLineArgsConfigProvider', 'Coercer', 'ComplexNumber', 'Component', 'ComponentStatusContainer', 'Connection', 'ConstantDataRule', 'Context', 'CoreType', 'CustomSearchFilter', 'DataDescriptorBuilder', 'DataDescriptorBuilderFromExisting', 'DataDescriptorChangedEventPacket', 'DataDescriptorFromBuilder', 'DataPacket', 'DataPacketWithDomain', 'DataRule', 'DataRuleBuilder', 'DataRuleBuilderFromExisting', 'DataRuleFromBuilder', 'DataRuleType', 'DeviceDomain', 'DeviceInfoConfig', 'DeviceInfoConfigWithCustomSdkVersion', 'DeviceType', 'Dict', 'DictProperty', 'DictPropertyBuilder', 'Dimension', 'DimensionBuilder', 'DimensionBuilderFromExisting', 'DimensionFromBuilder', 'DimensionRule', 'DimensionRuleBuilder', 'DimensionRuleBuilderFromExisting', 'DimensionRuleFromBuilder', 'DimensionRuleType', 'Enumeration', 'EnumerationProperty', 'EnumerationPropertyBuilder', 'EnumerationType', 'EnumerationTypeWithValues', 'EnumerationWithType', 'EnvConfigProvider', 'EvalValue', 'EvalValueArgs', 'EvalValueFunc', 'EventArgs', 'EventPacket', 'ExcludedTagsSearchFilter', 'ExplicitDataRule', 'ExplicitDomainDataRule', 'ExternalAllocator', 'Float', 'FloatProperty', 'FloatPropertyBuilder', 'Folder', 'FolderWithItemType', 'Function', 'FunctionBlockType', 'FunctionProperty', 'FunctionPropertyBuilder', 'IAllocator', 'IArgumentInfo', 'IAwaitable', 'IBaseObject', 'IBlockReader', 'IBlockReaderStatus', 'IBoolean', 'ICallableInfo', 'IChannel', 'ICoercer', 'IComplexNumber', 'IComponent', 'IComponentPrivate', 'IComponentStatusContainer', 'IComponentStatusContainerPrivate', 'IComponentType', 'IConfigProvider', 'IConnection', 'IContext', 'IDataDescriptor', 'IDataDescriptorBuilder', 'IDataPacket', 'IDataRule', 'IDataRuleBuilder', 'IDevice', 'IDeviceDomain', 'IDeviceInfo', 'IDeviceInfoConfig', 'IDeviceType', 'IDict', 'IDimension', 'IDimensionBuilder', 'IDimensionRule', 'IDimensionRuleBuilder', 'IEnumeration', 'IEnumerationType', 'IEvalValue', 'IEventArgs', 'IEventPacket', 'IFloat', 'IFolder', 'IFolderConfig', 'IFunction', 'IFunctionBlock', 'IFunctionBlockType', 'IGraphVisualization', 'IInputPort', 'IInputPortConfig', 'IInputPortNotifications', 'IInstance', 'IInstanceBuilder', 'IInteger', 'IIterable', 'IIterator', 'IList', 'ILogger', 'ILoggerComponent', 'ILoggerSink', 'ILoggerThreadPool', 'IMirroredSignalConfig', 'IMirroredSignalPrivate', 'IModule', 'IModuleManager', 'INumber', 'IOwnable', 'IPacket', 'IPacketDestructCallback', 'IPacketReader', 'IProcedure', 'IProperty', 'IPropertyBuilder', 'IPropertyObject', 'IPropertyObjectClass', 'IPropertyObjectClassBuilder', 'IPropertyObjectProtected', 'IPropertyValueEventArgs', 'IRange', 'IRatio', 'IReader', 'IReaderStatus', 'IRemovable', 'ISampleReader', 'IScaling', 'IScalingBuilder', 'IScheduler', 'ISearchFilter', 'IServer', 'IServerCapability', 'IServerType', 'ISignal', 'ISignalConfig', 'ISignalEvents', 'ISimpleType', 'IStreamReader', 'IStreaming', 'IString', 'IStruct', 'IStructBuilder', 'IStructType', 'ISubscriptionEventArgs', 'ITags', 'ITagsPrivate', 'ITailReader', 'ITask', 'ITaskGraph', 'IType', 'ITypeManager', 'IUnit', 'IUnitBuilder', 'IValidator', 'InputPort', 'Instance', 'InstanceBuilder', 'InstanceFromBuilder', 'IntProperty', 'IntPropertyBuilder', 'Integer', 'InterfaceIdSearchFilter', 'IoFolder', 'JsonConfigProvider', 'LinearDataRule', 'LinearDimensionRule', 'LinearScaling', 'List', 'ListDimensionRule', 'ListProperty', 'ListPropertyBuilder', 'LocalIdSearchFilter', 'LogLevel', 'LogarithmicDimensionRule', 'Logger', 'LoggerComponent', 'LoggerThreadPool', 'MallocAllocator', 'MockSignal', 'ModuleManager', 'ModuleManagerMultiplePaths', 'NotSearchFilter', 'ObjectProperty', 'ObjectPropertyBuilder', 'OrSearchFilter', 'PacketReader', 'PacketReaderFromPort', 'PacketReadyNotification', 'PacketType', 'Procedure', 'PropertyBuilder', 'PropertyEventType', 'PropertyObject', 'PropertyObjectClassBuilder', 'PropertyObjectClassBuilderWithManager', 'PropertyObjectClassFromBuilder', 'PropertyObjectWithClassAndManager', 'PropertyValueEventArgs', 'ProtocolType', 'Range', 'Ratio', 'RatioProperty', 'RatioPropertyBuilder', 'ReadMode', 'ReadStatus', 'ReadTimeoutType', 'ReaderStatus', 'RecursiveSearchFilter', 'ReferenceProperty', 'ReferencePropertyBuilder', 'RequiredTagsSearchFilter', 'RotatingFileLoggerSink', 'SampleType', 'ScaledSampleType', 'Scaling', 'ScalingBuilder', 'ScalingBuilderFromExisting', 'ScalingFromBuilder', 'ScalingType', 'Scheduler', 'SelectionProperty', 'SelectionPropertyBuilder', 'ServerType', 'Signal', 'SignalWithDescriptor', 'SimpleType', 'SparseSelectionProperty', 'SparseSelectionPropertyBuilder', 'StdErrLoggerSink', 'StdOutLoggerSink', 'StreamReader', 'StreamReaderFromExisting', 'String', 'StringProperty', 'StringPropertyBuilder', 'Struct', 'StructBuilder', 'StructBuilderFromStruct', 'StructFromBuilder', 'StructProperty', 'StructPropertyBuilder', 'StructType', 'StructTypeNoDefaults', 'SubscriptionEventArgs', 'SubscriptionEventType', 'Tags', 'TailReader', 'TailReaderFromExisting', 'Task', 'TaskGraph', 'TimeBlockReader', 'TimeStreamReader', 'TimeTailReader', 'TypeManager', 'Unit', 'UnitBuilder', 'UnitBuilderFromExisting', 'Validator', 'VisibleSearchFilter', 'WinDebugLoggerSink', 'clear_error_info', 'get_tracked_object_count', 'print_tracked_objects']
class CoreType:
    """
    Members:
    
      ctBool
    
      ctInt
    
      ctFloat
    
      ctString
    
      ctList
    
      ctDict
    
      ctRatio
    
      ctProc
    
      ctObject
    
      ctBinaryData
    
      ctFunc
    
      ctComplexNumber
    
      ctStruct
    
      ctEnumeration
    
      ctUndefined
    """
    __members__: typing.ClassVar[dict[str, CoreType]]  # value = {'ctBool': <CoreType.ctBool: 0>, 'ctInt': <CoreType.ctInt: 1>, 'ctFloat': <CoreType.ctFloat: 2>, 'ctString': <CoreType.ctString: 3>, 'ctList': <CoreType.ctList: 4>, 'ctDict': <CoreType.ctDict: 5>, 'ctRatio': <CoreType.ctRatio: 6>, 'ctProc': <CoreType.ctProc: 7>, 'ctObject': <CoreType.ctObject: 8>, 'ctBinaryData': <CoreType.ctBinaryData: 9>, 'ctFunc': <CoreType.ctFunc: 10>, 'ctComplexNumber': <CoreType.ctComplexNumber: 11>, 'ctStruct': <CoreType.ctStruct: 12>, 'ctEnumeration': <CoreType.ctEnumeration: 13>, 'ctUndefined': <CoreType.ctUndefined: 65535>}
    ctBinaryData: typing.ClassVar[CoreType]  # value = <CoreType.ctBinaryData: 9>
    ctBool: typing.ClassVar[CoreType]  # value = <CoreType.ctBool: 0>
    ctComplexNumber: typing.ClassVar[CoreType]  # value = <CoreType.ctComplexNumber: 11>
    ctDict: typing.ClassVar[CoreType]  # value = <CoreType.ctDict: 5>
    ctEnumeration: typing.ClassVar[CoreType]  # value = <CoreType.ctEnumeration: 13>
    ctFloat: typing.ClassVar[CoreType]  # value = <CoreType.ctFloat: 2>
    ctFunc: typing.ClassVar[CoreType]  # value = <CoreType.ctFunc: 10>
    ctInt: typing.ClassVar[CoreType]  # value = <CoreType.ctInt: 1>
    ctList: typing.ClassVar[CoreType]  # value = <CoreType.ctList: 4>
    ctObject: typing.ClassVar[CoreType]  # value = <CoreType.ctObject: 8>
    ctProc: typing.ClassVar[CoreType]  # value = <CoreType.ctProc: 7>
    ctRatio: typing.ClassVar[CoreType]  # value = <CoreType.ctRatio: 6>
    ctString: typing.ClassVar[CoreType]  # value = <CoreType.ctString: 3>
    ctStruct: typing.ClassVar[CoreType]  # value = <CoreType.ctStruct: 12>
    ctUndefined: typing.ClassVar[CoreType]  # value = <CoreType.ctUndefined: 65535>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class DataRuleType:
    """
    Members:
    
      Other
    
      Linear
    
      Constant
    
      Explicit
    """
    Constant: typing.ClassVar[DataRuleType]  # value = <DataRuleType.Constant: 2>
    Explicit: typing.ClassVar[DataRuleType]  # value = <DataRuleType.Explicit: 3>
    Linear: typing.ClassVar[DataRuleType]  # value = <DataRuleType.Linear: 1>
    Other: typing.ClassVar[DataRuleType]  # value = <DataRuleType.Other: 0>
    __members__: typing.ClassVar[dict[str, DataRuleType]]  # value = {'Other': <DataRuleType.Other: 0>, 'Linear': <DataRuleType.Linear: 1>, 'Constant': <DataRuleType.Constant: 2>, 'Explicit': <DataRuleType.Explicit: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class DimensionRuleType:
    """
    Members:
    
      Other
    
      Linear
    
      Logarithmic
    
      List
    """
    Linear: typing.ClassVar[DimensionRuleType]  # value = <DimensionRuleType.Linear: 1>
    List: typing.ClassVar[DimensionRuleType]  # value = <DimensionRuleType.List: 3>
    Logarithmic: typing.ClassVar[DimensionRuleType]  # value = <DimensionRuleType.Logarithmic: 2>
    Other: typing.ClassVar[DimensionRuleType]  # value = <DimensionRuleType.Other: 0>
    __members__: typing.ClassVar[dict[str, DimensionRuleType]]  # value = {'Other': <DimensionRuleType.Other: 0>, 'Linear': <DimensionRuleType.Linear: 1>, 'Logarithmic': <DimensionRuleType.Logarithmic: 2>, 'List': <DimensionRuleType.List: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class IAllocator(IBaseObject):
    """
    An allocator used to allocate memory.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IAllocator:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IAllocator:
        ...
    def allocate(self, descriptor: IDataDescriptor, bytes: int, align: int) -> capsule:
        """
        Allocates a chunk of memory for a packet.
        """
    def free(self, address: capsule) -> None:
        """
        Releases a chunk of memory allocated by allocate().
        """
class IArgumentInfo(IBaseObject):
    """
    Provides the name and type of a single function/procedure argument
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IArgumentInfo:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IArgumentInfo:
        ...
    @property
    def name(self) -> str:
        """
        Gets the name of the argument.
        """
    @property
    def type(self) -> CoreType:
        """
        Gets the core type of the argument.
        """
class IAwaitable(IBaseObject):
    """
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IAwaitable:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IAwaitable:
        ...
    def cancel(self) -> int:
        """
        Cancels the outstanding work if it has not already started.
        """
    def has_completed(self) -> int:
        """
        Checks if the execution has already finished.
        """
    def wait(self) -> None:
        ...
    @property
    def result(self) -> typing.Any:
        """
        Waits until the awaitable has a valid result and retrieves it or re-throws the exception that occurred during the execution.
        """
class IBaseObject:
    """
    Extends `IUnknown` by providing additional methods for borrowing interfaces, hashing, and equality comparison. All openDAQ objects implement `IBaseObject` interface or its descendants. Hashing and equality comparison provides the ability to use the object as an element in dictionaries and lists. Classes that implement any interface derived from `IBaseObject` should be derived from `ImplementationOf` class, which provides the default implementation of `IBaseObject` interface methods.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IBaseObject:
        ...
    def __eq__(self, arg0: typing.Any) -> bool:
        ...
    def __float__(self) -> float:
        ...
    def __hash__(self) -> int:
        ...
    def __init__(self, arg0: IBaseObject) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __str__(self) -> str:
        ...
    @property
    def core_type(self) -> CoreType:
        ...
class IBlockReader(ISampleReader):
    """
    A signal data reader that abstracts away reading of signal packets by keeping an internal read-position and automatically advances it on subsequent reads. The difference to a StreamReader is that instead of reading on per sample basis it always returns only a full block of samples. This means that even if more samples are available they will not be read until there is enough of them to fill at least one block.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IBlockReader:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IBlockReader:
        ...
    def read(self, count: int, timeout_ms: int = 0) -> numpy.ndarray[numpy.float32] | numpy.ndarray[numpy.float64] | numpy.ndarray[numpy.uint32] | numpy.ndarray[numpy.int32] | numpy.ndarray[numpy.uint64] | numpy.ndarray[numpy.int64] | numpy.ndarray[numpy.uint8] | numpy.ndarray[numpy.int8] | numpy.ndarray[numpy.uint16] | numpy.ndarray[numpy.int16]:
        """
        Copies at maximum the next `count` blocks of unread samples to the values buffer.The amount actually read is returned through the `count` parameter
        """
    def read_with_domain(self, count: int, timeout_ms: int = 0) -> tuple[numpy.ndarray[numpy.float32] | numpy.ndarray[numpy.float64] | numpy.ndarray[numpy.uint32] | numpy.ndarray[numpy.int32] | numpy.ndarray[numpy.uint64] | numpy.ndarray[numpy.int64] | numpy.ndarray[numpy.uint8] | numpy.ndarray[numpy.int8] | numpy.ndarray[numpy.uint16] | numpy.ndarray[numpy.int16], numpy.ndarray[numpy.float32] | numpy.ndarray[numpy.float64] | numpy.ndarray[numpy.uint32] | numpy.ndarray[numpy.int32] | numpy.ndarray[numpy.uint64] | numpy.ndarray[numpy.int64] | numpy.ndarray[numpy.uint8] | numpy.ndarray[numpy.int8] | numpy.ndarray[numpy.uint16] | numpy.ndarray[numpy.int16]]:
        """
        Copies at maximum the next `count` blocks of unread samples and clock-stamps to the `dataBlocks` and `domainBlocks` buffers.The amount actually read is returned through the `count` parameter.
        """
    @property
    def block_size(self) -> int:
        """
        The amount of samples the reader considers as one block.
        """
class IBlockReaderStatus(IReaderStatus):
    """
    IBlockReaderStatus inherits from IReaderStatus to expand information returned read function
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IBlockReaderStatus:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IBlockReaderStatus:
        ...
    @property
    def read_samples(self) -> int:
        """
        Returns the number of samples that were read. Sometimes, during the process of reading, an event packet may occur that stops the reading of remaining samples. Developers can use this function to determine how many samples were actually read.
        """
class IBoolean(IBaseObject):
    """
    Represents boolean variable as `IBoolean` interface. Use this interface to wrap boolean variable when you need to add the variable to lists, dictionaries and other containers which accept `IBaseObject` interface.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IBoolean:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IBoolean:
        ...
    def __bool__(self) -> bool:
        ...
    @property
    def value(self) -> bool:
        """
        Gets a boolean value stored in the object.
        """
class ICallableInfo(IBaseObject):
    """
    Provides information about the argument count and types, as well as the return type of Function/Procedure-type properties.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> ICallableInfo:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> ICallableInfo:
        ...
    @property
    def arguments(self) -> IList:
        """
        Gets the list of arguments the callable function/procedure expects.
        """
    @property
    def return_type(self) -> CoreType:
        """
        Gets the return type of the callable function.
        """
class IChannel(IFunctionBlock):
    """
    Channels represent physical sensors of openDAQ devices. Internally they are standard function blocks with an additional option to provide a list of tags.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IChannel:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IChannel:
        ...
class ICoercer(IBaseObject):
    """
    Used by openDAQ properties to coerce a value to match the restrictions imposed by the Property.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> ICoercer:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> ICoercer:
        ...
    def coerce(self, prop_obj: typing.Any, value: typing.Any) -> typing.Any:
        """
        Coerces `value` to match the coercion restrictions and outputs the result.
        """
    @property
    def eval(self) -> str:
        """
        Gets the string expression used when creating the coercer.
        """
class IComplexNumber(IBaseObject):
    """
    Represents a complex number as `IComplexNumber` interface. Use this interface to wrap complex number when you need to add the number to lists, dictionaries and other containers which accept `IBaseObject` and derived interfaces. Complex numbers have two components: real and imaginary. Both of them are of Float type.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IComplexNumber:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IComplexNumber:
        ...
    def __complex__(self) -> complex:
        ...
    def equals_value(self, value: ...) -> bool:
        """
        Compares stored complex value to the complex number parameter.
        """
    @property
    def imaginary(self) -> float:
        """
        Gets the imaginary part of the complex number value.
        """
    @property
    def real(self) -> float:
        """
        Gets the real part of the complex number value.
        """
    @property
    def value(self) -> complex:
        """
        Gets a complex value stored in the object.
        """
class IComponent(IPropertyObject):
    """
    Acts as a base interface for components, such as device, function block, channel and signal.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IComponent:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IComponent:
        ...
    def find_component(self, id: str) -> IComponent:
        """
        Finds the component (signal/device/function block) with the specified (global) id.
        """
    @property
    def active(self) -> int:
        """
        Returns true if the component is active; false otherwise. / Sets the component to be either active or inactive. Also recursively sets the `active` field of all child components if component is a folder.
        """
    @active.setter
    def active(self, arg1: bool) -> None:
        ...
    @property
    def context(self) -> IContext:
        """
        Gets the context object.
        """
    @property
    def description(self) -> str:
        """
        Gets the description of the component. / Sets the description of the component.
        """
    @description.setter
    def description(self, arg1: str) -> None:
        ...
    @property
    def global_id(self) -> str:
        """
        Gets the global ID of the component.
        """
    @property
    def local_id(self) -> str:
        """
        Gets the local ID of the component.
        """
    @property
    def locked_attributes(self) -> IList:
        """
        Gets a list of the component's locked attributes. The locked attributes cannot be modified via their respective setters.
        """
    @property
    def name(self) -> str:
        """
        Gets the name of the component. / Sets the name of the component.
        """
    @name.setter
    def name(self, arg1: str) -> None:
        ...
    @property
    def parent(self) -> IComponent:
        """
        Gets the parent of the component.
        """
    @property
    def status_container(self) -> IComponentStatusContainer:
        """
        Gets the container of Component statuses.
        """
    @property
    def tags(self) -> ITags:
        """
        Gets the tags of the component.
        """
    @property
    def visible(self) -> int:
        """
        Gets `visible` metadata state of the component / Sets `visible` attribute state of the component
        """
    @visible.setter
    def visible(self, arg1: bool) -> None:
        ...
class IComponentPrivate(IBaseObject):
    """
    Provides access to private methods of the component.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IComponentPrivate:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IComponentPrivate:
        ...
    def lock_all_attributes(self) -> None:
        """
        Locks all attributes of the component.
        """
    def lock_attributes(self, attributes: IList) -> None:
        """
        Locks the attributes contained in the provided list.
        """
    def trigger_component_core_event(self, args: ...) -> None:
        """
        Triggers the component-specific core event with the provided arguments.
        """
    def unlock_all_attributes(self) -> None:
        """
        Unlocks all attributes of the component.
        """
    def unlock_attributes(self, attributes: IList) -> None:
        """
        Unlocks the attributes contained in the provided list.
        """
class IComponentStatusContainer(IBaseObject):
    """
    A container of Component Statuses and their corresponding values.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IComponentStatusContainer:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IComponentStatusContainer:
        ...
    def get_status(self, name: str) -> IEnumeration:
        """
        Gets the the current value of Component status with a given name.
        """
    @property
    def statuses(self) -> IDict:
        """
        Gets the current values of all Component statuses.
        """
class IComponentStatusContainerPrivate(IBaseObject):
    """
    Provides access to private methods of the Component status container.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IComponentStatusContainerPrivate:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IComponentStatusContainerPrivate:
        ...
    def add_status(self, name: str, initial_value: IEnumeration) -> None:
        """
        Adds the new status with given name and initial value.
        """
    def set_status(self, name: str, value: IEnumeration) -> None:
        """
        Sets the value for the existing component status.
        """
class IComponentType(IBaseObject):
    """
    Provides information about the component types.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IComponentType:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IComponentType:
        ...
    def create_default_config(self) -> IPropertyObject:
        """
        The function creates and returns default configuration. On each call, we need to create new object, because we want that each instance of the component has its own configuration object.
        """
    @property
    def description(self) -> str:
        """
        Gets the description of a component.
        """
    @property
    def id(self) -> str:
        """
        Gets the unique component type id.
        """
    @property
    def name(self) -> str:
        """
        Gets the user-friendly name of a component.
        """
class IConfigProvider(IBaseObject):
    """
    Config provider is an interface that was made for populating an options dictionary of an instance builder from external sources like a config file, environment variables, or command line arguments. The process of population of the dictionary have to be alligned with rules: - all keys are set in lowercase. Values are set without case changes. - if a provider is trying to override an existing value, it has to have the same type. For example provider can not replace integer value with string or object with list - if a provider is overriding a list, it replaces old list items with a new one.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IConfigProvider:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IConfigProvider:
        ...
    def populate_options(self, options: IDict) -> None:
        """
        Populate the existing options dictionary with variables from config provider
        """
class IConnection(IBaseObject):
    """
    Represents a connection between an Input port and Signal. Acts as a queue for packets sent by the signal, which can be read by the input port and the input port's owner.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IConnection:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IConnection:
        ...
    def dequeue(self) -> IPacket:
        """
        Removes the packet at the front of the queue and returns it.
        """
    def enqueue(self, packet: IPacket) -> None:
        """
        Places a packet at the back of the queue.
        """
    def enqueue_on_this_thread(self, packet: IPacket) -> None:
        """
        Places a packet at the back of the queue.
        """
    def peek(self) -> IPacket:
        """
        Returns the packet at the front of the queue without removing it.
        """
    @property
    def available_samples(self) -> int:
        """
        Gets the number of samples available in the queued packets. The returned value ignores any Sample-Descriptor changes.
        """
    @property
    def input_port(self) -> IInputPort:
        """
        Gets the Input port to which packets are being sent.
        """
    @property
    def packet_count(self) -> int:
        """
        Gets the number of queued packets.
        """
    @property
    def remote(self) -> int:
        """
        Returns true if the type of connection is remote.
        """
    @property
    def samples_until_next_descriptor(self) -> int:
        """
        Gets the number of same-type samples available in the queued packets. The returned value is up-to the next Sample-Descriptor-Changed packet if any.
        """
    @property
    def signal(self) -> ISignal:
        """
        Gets the Signal that is sending packets through the Connection.
        """
class IContext(IBaseObject):
    """
    The Context serves as a container for the Scheduler and Logger. It originates at the instance, and is passed to the root device, which forwards it to components such as function blocks and signals.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IContext:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IContext:
        ...
    def get_module_options(self, module_id: str) -> IDict:
        """
        Retrieves the options associated with the specified module ID.
        """
    @property
    def logger(self) -> ILogger:
        """
        Gets the logger.
        """
    @property
    def module_manager(self) -> typing.Any:
        """
        Gets the Module Manager as a Base Object.
        """
    @property
    def options(self) -> IDict:
        """
        Gets the dictionary of options
        """
    @property
    def scheduler(self) -> IScheduler:
        """
        Gets the scheduler.
        """
    @property
    def type_manager(self) -> ITypeManager:
        """
        Gets the Type Manager.
        """
class IDataDescriptor(IBaseObject):
    """
    Describes the data sent by a signal, defining how they are to be interpreted by anyone receiving the signal's packets.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IDataDescriptor:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IDataDescriptor:
        ...
    @property
    def dimensions(self) -> IList:
        """
        Gets the list of the descriptor's dimension's.
        """
    @property
    def metadata(self) -> IDict:
        """
        Gets any extra metadata defined by the data descriptor.
        """
    @property
    def name(self) -> str:
        """
        Gets a descriptive name of the signal value.
        """
    @property
    def origin(self) -> str:
        """
        Gets the absolute origin of a signal value component.
        """
    @property
    def post_scaling(self) -> IScaling:
        ...
    @property
    def raw_sample_size(self) -> int:
        """
        Gets the actual sample size in buffer of one sample in bytes.
        """
    @property
    def rule(self) -> IDataRule:
        """
        Gets the value Data rule.
        """
    @property
    def sample_size(self) -> int:
        """
        Gets the size of one sample in bytes.
        """
    @property
    def sample_type(self) -> SampleType:
        """
        Gets the descriptor's sample type.
        """
    @property
    def struct_fields(self) -> IList:
        """
        Gets the fields of the struct, forming a recursive value descriptor definition.
        """
    @property
    def tick_resolution(self) -> IRatio:
        """
        Gets the Resolution which scales the explicit or implicit value to the physical unit defined in `unit`. It is defined as domain (usually time) between two consecutive ticks.
        """
    @property
    def unit(self) -> IUnit:
        """
        Gets the unit of the data in a signal's packets.
        """
    @property
    def value_range(self) -> IRange:
        """
        Gets the value range of the data in a signal's packets defining the lowest and highest expected values.
        """
class IDataDescriptorBuilder(IBaseObject):
    """
    Builder component of Data descriptor objects. Contains setter methods that allow for Data descriptor parameter configuration, and a `build` method that builds the Data descriptor.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IDataDescriptorBuilder:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IDataDescriptorBuilder:
        ...
    def build(self) -> IDataDescriptor:
        """
        Builds and returns a Data descriptor object using the currently set values of the Builder.
        """
    @property
    def dimensions(self) -> IList:
        """
        Gets the list of the descriptor's dimension's. / Sets the list of the descriptor's dimension's.
        """
    @dimensions.setter
    def dimensions(self, arg1: IList) -> None:
        ...
    @property
    def metadata(self) -> IDict:
        """
        Gets any extra metadata defined by the data descriptor. / Sets any extra metadata defined by the data descriptor.
        """
    @metadata.setter
    def metadata(self, arg1: IDict) -> None:
        ...
    @property
    def name(self) -> str:
        """
        Gets a descriptive name for the signal's value. / Sets a descriptive name for the signal's value.
        """
    @name.setter
    def name(self, arg1: str) -> None:
        ...
    @property
    def origin(self) -> str:
        """
        Gets the absolute origin of a signal value component. / Sets the absolute origin of a signal value component.
        """
    @origin.setter
    def origin(self, arg1: str) -> None:
        ...
    @property
    def post_scaling(self) -> IScaling:
        """
        Gets the scaling rule that needs to be applied to explicit/implicit data by readers. / Sets the scaling rule that needs to be applied to explicit/implicit data by readers.
        """
    @post_scaling.setter
    def post_scaling(self, arg1: IScaling) -> None:
        ...
    @property
    def rule(self) -> IDataRule:
        """
        Gets the value Data rule. / Sets the value Data rule.
        """
    @rule.setter
    def rule(self, arg1: IDataRule) -> None:
        ...
    @property
    def sample_type(self) -> SampleType:
        """
        Gets the descriptor's sample type. / Sets the descriptor's sample type.
        """
    @sample_type.setter
    def sample_type(self, arg1: SampleType) -> None:
        ...
    @property
    def struct_fields(self) -> IList:
        """
        Gets the fields of the struct, forming a recursive value descriptor definition. / Sets the fields of the struct, forming a recursive value descriptor definition.
        """
    @struct_fields.setter
    def struct_fields(self, arg1: IList) -> None:
        ...
    @property
    def tick_resolution(self) -> IRatio:
        """
        Gets the Resolution which scales the an explicit or implicit value to the physical unit defined in `unit`. / Sets the Resolution which scales the an explicit or implicit value to the physical unit defined in `unit`.
        """
    @tick_resolution.setter
    def tick_resolution(self, arg1: IRatio) -> None:
        ...
    @property
    def unit(self) -> IUnit:
        """
        Gets the unit of the data in a signal's packets. / Sets the unit of the data in a signal's packets.
        """
    @unit.setter
    def unit(self, arg1: IUnit) -> None:
        ...
    @property
    def value_range(self) -> IRange:
        """
        Gets the value range of the data in a signal's packets defining the lowest and highest expected values. / Sets the value range of the data in a signal's packets defining the lowest and highest expected values.
        """
    @value_range.setter
    def value_range(self, arg1: IRange) -> None:
        ...
class IDataPacket(IPacket):
    """
    Packet that contains data sent by a signal. The data can be either explicit, or implicit.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IDataPacket:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IDataPacket:
        ...
    def get_last_value(self, type_manager: ITypeManager = None) -> typing.Any:
        """
        Gets the data packet last value
        """
    @property
    def data_descriptor(self) -> IDataDescriptor:
        """
        Gets the signal descriptor of the signal that sent the packet at the time of sending.
        """
    @property
    def data_size(self) -> int:
        """
        Gets size of data buffer in bytes.
        """
    @property
    def domain_packet(self) -> IDataPacket:
        """
        Gets the associated domain Data packet.
        """
    @property
    def last_value(self) -> typing.Any:
        """
        Gets the data packet last value
        """
    @property
    def offset(self) -> INumber:
        """
        Gets current packet offset. This offset is later applied to the data rule used by a signal to calculate actual data value. This value is usually a time or other domain value. Packet offset is particularly useful when one wants to transfer a gap in otherwise equidistant samples. If we have a linear data rule, defined by equation f(x) = k*x + n, then the data value will be calculated by the equation g(x) = offset + f(x).
        """
    @property
    def packet_id(self) -> int:
        """
        Gets the unique packet id.
        """
    @property
    def raw_data_size(self) -> int:
        """
        Gets size of raw data buffer in bytes.
        """
    @property
    def sample_count(self) -> int:
        """
        Gets the number of samples in the packet.
        """
class IDataRule(IBaseObject):
    """
    Rule that defines how a signal value is calculated from an implicit initialization value when the rule type is not `Explicit`.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IDataRule:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IDataRule:
        ...
    @property
    def parameters(self) -> IDict:
        """
        Gets a dictionary of string-object key-value pairs representing the parameters used to evaluate the rule.
        """
    @property
    def type(self) -> DataRuleType:
        """
        Gets the type of the data rule.
        """
class IDataRuleBuilder(IBaseObject):
    """
    Configuration component of Data rule objects. Contains setter methods that allow for Data rule parameter configuration, and a `build` method that builds the Data rule.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IDataRuleBuilder:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IDataRuleBuilder:
        ...
    def add_parameter(self, name: str, parameter: typing.Any) -> None:
        """
        Adds a string-object pair parameter to the Dictionary of Data rule parameters.
        """
    def build(self) -> IDataRule:
        """
        Builds and returns a Data rule object using the currently set values of the Builder.
        """
    def remove_parameter(self, name: str) -> None:
        """
        Removes the parameter with the given name from the Dictionary of Data rule parameters.
        """
    @property
    def parameters(self) -> IDict:
        """
        Gets a dictionary of string-object key-value pairs representing the parameters used to evaluate the rule. / Sets a dictionary of string-object key-value pairs representing the parameters used to evaluate the rule.
        """
    @parameters.setter
    def parameters(self, arg1: IDict) -> None:
        ...
    @property
    def type(self) -> DataRuleType:
        """
        Gets the type of the data rule. / Sets the type of the data rule.
        """
    @type.setter
    def type(self, arg1: DataRuleType) -> None:
        ...
class IDevice(IFolder):
    """
    Represents an openDAQ device. The device contains a list of signals and physical channels. Some devices support adding function blocks, or connecting to devices. The list of available function blocks/devices can be obtained via the `getAvailable` functions, and added via the `add` functions.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IDevice:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IDevice:
        ...
    def add_device(self, connection_string: str, config: IPropertyObject = None) -> IDevice:
        """
        Connects to a device at the given connection string and returns it.
        """
    def add_function_block(self, type_id: str, config: IPropertyObject = None) -> IFunctionBlock:
        """
        Creates and adds a function block to the device with the provided unique ID and returns it.
        """
    def get_channels(self, search_filter: ISearchFilter = None) -> IList:
        """
        Gets a flat list of the device's physical channels.
        """
    def get_channels_recursive(self, search_filter: ISearchFilter = None) -> IList:
        """
        Gets a flat list of the device's physical channels. Also finds all visible channels of visible child devices
        """
    def get_devices(self, search_filter: ISearchFilter = None) -> IList:
        """
        Gets a list of child devices that the device is connected to.
        """
    def get_function_blocks(self, search_filter: ISearchFilter = None) -> IList:
        """
        Gets the list of added function blocks.
        """
    def get_signals(self, search_filter: ISearchFilter = None) -> IList:
        """
        Gets a list of the device's signals.
        """
    def get_signals_recursive(self, search_filter: ISearchFilter = None) -> IList:
        """
        Gets a list of the signals that belong to the device.
        """
    def load_configuration(self, configuration: str) -> None:
        """
        Loads the configuration of the device from string.
        """
    def remove_device(self, device: IDevice) -> None:
        """
        Disconnects from the device provided as argument and removes it from the internal list of devices.
        """
    def remove_function_block(self, function_block: IFunctionBlock) -> None:
        """
        Removes the function block provided as argument, disconnecting its signals and input ports.
        """
    def save_configuration(self) -> str:
        """
        Saves the configuration of the device to string.
        """
    @property
    def available_device_types(self) -> IDict:
        """
        Get a dictionary of available device types as <IString, IDeviceType> pairs
        """
    @property
    def available_devices(self) -> IList:
        """
        Gets a list of available devices, containing their Device Info.
        """
    @property
    def available_function_block_types(self) -> IDict:
        """
        Gets all function block types that are supported by the device, containing their description.
        """
    @property
    def channels(self) -> IList:
        """
        Gets a flat list of the device's physical channels.
        """
    @property
    def channels_recursive(self) -> IList:
        """
        Gets a flat list of the device's physical channels. Also finds all visible channels of visible child devices
        """
    @property
    def custom_components(self) -> IList:
        """
        Gets a list of all components/folders in a device that are not titled 'io', 'sig', 'dev' or 'fb'
        """
    @property
    def devices(self) -> IList:
        """
        Gets a list of child devices that the device is connected to.
        """
    @property
    def domain(self) -> IDeviceDomain:
        """
        Gets the device's domain data. It allows for querying the device for its domain (time) values.
        """
    @property
    def function_blocks(self) -> IList:
        """
        Gets the list of added function blocks.
        """
    @property
    def info(self) -> IDeviceInfo:
        """
        Gets the device info. It contains data about the device such as the device's serial number, location, and connection string.
        """
    @property
    def inputs_outputs_folder(self) -> IFolder:
        """
        Gets a folder containing channels.
        """
    @property
    def signals(self) -> IList:
        """
        Gets a list of the device's signals.
        """
    @property
    def signals_recursive(self) -> IList:
        """
        Gets a list of the signals that belong to the device.
        """
    @property
    def ticks_since_origin(self) -> int:
        """
        Gets the number of ticks passed since the device's absolute origin.
        """
class IDeviceDomain(IBaseObject):
    """
    Contains information about the domain of the device.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IDeviceDomain:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IDeviceDomain:
        ...
    @property
    def origin(self) -> str:
        """
        Gets the device's absolute origin. Most often this is a time epoch in the ISO 8601 format.
        """
    @property
    def tick_resolution(self) -> IRatio:
        """
        Gets domain (usually time) between two consecutive ticks. Resolution is provided in a domain unit.
        """
    @property
    def unit(self) -> IUnit:
        """
        Gets the domain unit (eg. seconds, hours, degrees...)
        """
class IDeviceInfo(IPropertyObject):
    """
    Contains standard information about an openDAQ device and device type. The Device Info object is a Property Object, allowing for custom String, Int, Bool, or Float-type properties to be added.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IDeviceInfo:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IDeviceInfo:
        ...
    @property
    def asset_id(self) -> str:
        """
        Gets the asset ID of the device. Represents a user writable alphanumeric character sequence uniquely identifying a component.
        """
    @property
    def connection_string(self) -> str:
        """
        Gets the string representation of a connection address used to connect to the device.
        """
    @property
    def custom_info_property_names(self) -> IList:
        """
        Gets the list of property names that are not in the default set of Device info properties. Default properties are all info properties that have a corresponding getter method.
        """
    @property
    def device_class(self) -> str:
        """
        Gets the purpose of the device. For example "TestMeasurementDevice".
        """
    @property
    def device_manual(self) -> str:
        """
        Gets the address of the user manual. It may be a pathname in the file system or a URL (Web address)
        """
    @property
    def device_revision(self) -> str:
        """
        Gets the revision level of the device.
        """
    @property
    def device_type(self) -> IDeviceType:
        """
        Gets a device type as an object providing type id, name, short description and default device configuration. By using default config object as a starting point, users can easily modify the preset properties to tailor the configuration of the client device accordingly.
        """
    @property
    def hardware_revision(self) -> str:
        """
        Gets the revision level of the hardware.
        """
    @property
    def mac_address(self) -> str:
        """
        Gets the Mac address of the device.
        """
    @property
    def manufacturer(self) -> str:
        """
        Gets the company that manufactured the device
        """
    @property
    def manufacturer_uri(self) -> str:
        """
        Gets the unique identifier of the company that manufactured the device This identifier should be a fully qualified domain name; however, it may be a GUID or similar construct that ensures global uniqueness.
        """
    @property
    def model(self) -> str:
        """
        Gets the model of the device
        """
    @property
    def name(self) -> str:
        """
        Gets the name of the device
        """
    @property
    def parent_mac_address(self) -> str:
        """
        Gets the Mac address of the device's parent.
        """
    @property
    def platform(self) -> str:
        """
        Gets the platform of the device. The platform specifies whether real hardware is used or if the device is simulated.
        """
    @property
    def position(self) -> int:
        """
        Gets the position of the device. The position specifies the position within a given system. For example in which slot or slice the device is in.
        """
    @property
    def product_code(self) -> str:
        """
        Gets the unique combination of numbers and letters used to identify the device.
        """
    @property
    def product_instance_uri(self) -> str:
        """
        Gets the globally unique resource identifier provided by the manufacturer. The recommended syntax of the ProductInstanceUri is: <ManufacturerUri>/<any string> where <any string> is unique among all instances using the same ManufacturerUri.
        """
    @property
    def revision_counter(self) -> int:
        """
        Gets the incremental counter indicating the number of times the configuration data has been modified.
        """
    @property
    def sdk_version(self) -> str:
        """
        Gets the version of the SDK used to build said device. Can be empty if the device does not use the SDK as its firmware/is implemented at a protocol-level.
        """
    @property
    def serial_number(self) -> str:
        """
        Gets the unique production number provided by the manufacturer
        """
    @property
    def server_capabilities(self) -> IList:
        """
        Gets the list of server capabilities stored in device info.
        """
    @property
    def software_revision(self) -> str:
        """
        Gets the revision level of the software component.
        """
    @property
    def system_type(self) -> str:
        """
        Gets the system type. The system type can, for example, be LayeredSystem, StandaloneSystem, or RackSystem.
        """
    @property
    def system_uuid(self) -> str:
        """
        Gets the system UUID that represents a unique ID of a system. All devices in a system share this UUID.
        """
class IDeviceInfoConfig(IDeviceInfo):
    """
    Configuration component of Device info objects. Contains setter methods that are available until the object is frozen.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IDeviceInfoConfig:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IDeviceInfoConfig:
        ...
class IDeviceType(IComponentType):
    """
    Provides information about the device type.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IDeviceType:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IDeviceType:
        ...
class IDict(IBaseObject):
    """
    Represents a heterogeneous dictionary of objects.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IDict:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IDict:
        ...
    def __delitem__(self, arg0: typing.Any) -> None:
        ...
    def __getitem__(self, arg0: typing.Any) -> typing.Any:
        ...
    def __iter__(self) -> typing.Any:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: typing.Any, arg1: typing.Any) -> None:
        ...
    def clear(self) -> None:
        ...
    def items(self) -> list:
        ...
    def keys(self) -> IIterable:
        ...
    def pop(self, arg0: typing.Any) -> IBaseObject:
        ...
    def values(self) -> IIterable:
        ...
class IDimension(IBaseObject):
    """
    Describes a dimension of the signal's data. Eg. a column/row in a matrix.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IDimension:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IDimension:
        ...
    @property
    def labels(self) -> IList:
        """
        Gets a list of labels that defines the dimension.
        """
    @property
    def name(self) -> str:
        """
        Gets the name of the dimension.
        """
    @property
    def rule(self) -> IDimensionRule:
        """
        Gets the rule that defines the labels and size of the dimension.
        """
    @property
    def size(self) -> int:
        """
        Gets the size of the dimension.
        """
    @property
    def unit(self) -> IUnit:
        """
        Gets the unit of the dimension's labels.
        """
class IDimensionBuilder(IBaseObject):
    """
    Configuration component of Dimension objects. Contains setter methods that allow for Dimension parameter configuration, and a `build` method that builds the Dimension.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IDimensionBuilder:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IDimensionBuilder:
        ...
    def build(self) -> IDimension:
        """
        Builds and returns a Dimension object using the currently set values of the Builder.
        """
    @property
    def name(self) -> str:
        """
        Gets the name of the dimension. / Sets the name of the dimension.
        """
    @name.setter
    def name(self, arg1: str) -> None:
        ...
    @property
    def rule(self) -> IDimensionRule:
        """
        Gets the rule that defines the labels and size of the dimension. / Sets the rule that defines the labels and size of the dimension.
        """
    @rule.setter
    def rule(self, arg1: IDimensionRule) -> None:
        ...
    @property
    def unit(self) -> IUnit:
        """
        Gets the unit of the dimension's labels. / Sets the unit of the dimension's labels.
        """
    @unit.setter
    def unit(self, arg1: IUnit) -> None:
        ...
class IDimensionRule(IBaseObject):
    """
    Rule that defines the labels (alternatively called bins, ticks) of a dimension.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IDimensionRule:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IDimensionRule:
        ...
    @property
    def parameters(self) -> IDict:
        """
        Gets a dictionary of string-object key-value pairs representing the parameters used to evaluate the rule.
        """
    @property
    def type(self) -> DimensionRuleType:
        """
        Gets the type of the dimension rule.
        """
class IDimensionRuleBuilder(IBaseObject):
    """
    Configuration component of Dimension rule objects. Contains setter methods that allow for Dimension rule parameter configuration, and a `build` method that builds the Dimension rule.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IDimensionRuleBuilder:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IDimensionRuleBuilder:
        ...
    def add_parameter(self, name: str, parameter: typing.Any) -> None:
        """
        Adds a string-object pair parameter to the Dictionary of Dimension rule parameters.
        """
    def build(self) -> IDimensionRule:
        """
        Builds and returns a Dimension rule object using the currently set values of the Builder.
        """
    def remove_parameter(self, name: str) -> None:
        """
        Removes the parameter with the given name from the Dictionary of Dimension rule parameters.
        """
    @property
    def parameters(self) -> IDict:
        """
        Gets a dictionary of string-object key-value pairs representing the parameters used to evaluate the rule. / Sets a dictionary of string-object key-value pairs representing the parameters used to evaluate the rule.
        """
    @parameters.setter
    def parameters(self, arg1: IDict) -> None:
        ...
    @property
    def type(self) -> DimensionRuleType:
        """
        Gets the type of the dimension rule. / Sets the type of the dimension rule. Rule parameters must be configured to match the requirements of the rule type.
        """
    @type.setter
    def type(self, arg1: DimensionRuleType) -> None:
        ...
class IEnumeration(IBaseObject):
    """
    Enumerations are immutable objects that encapsulate a value within a predefined set of named integral constants. These constants are predefined in an Enumeration type with the same name as the Enumeration.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IEnumeration:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IEnumeration:
        ...
    def __str__(self) -> typing.Any:
        ...
    @property
    def enumeration_type(self) -> IEnumerationType:
        """
        Gets the Enumeration's type.
        """
    @property
    def name(self) -> str:
        """
        Gets the Enumeration value as String containing the name of the enumerator constant.
        """
    @property
    def value(self) -> int:
        """
        Gets the Enumeration value as Integer enumerator constant.
        """
class IEnumerationType(IType):
    """
    Enumeration types define the enumerator names and values of Enumerations with a name matching that of the Enumeration type.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IEnumerationType:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IEnumerationType:
        ...
    def __call__(self, arg0: int) -> IEnumeration:
        ...
    def __getattr__(self, arg0: str) -> IEnumeration:
        ...
    def __getitem__(self, arg0: str) -> IEnumeration:
        ...
    def get_enumerator_int_value(self, name: str) -> int:
        """
        Gets the value of enumerator with the specified name.
        """
    @property
    def as_dictionary(self) -> IDict:
        """
        Gets the enumerator names and values as a Dictionary.
        """
    @property
    def count(self) -> int:
        """
        Gets the number of enumerators within the Enumeration Type.
        """
    @property
    def enumerator_names(self) -> IList:
        """
        Gets the list of enumerator names.
        """
class IEvalValue(IBaseObject):
    """
    Dynamic expression evaluator
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IEvalValue:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IEvalValue:
        ...
    def clone_with_owner(self, owner: IPropertyObject) -> IEvalValue:
        """
        Clones the object and attaches an owner.
        """
    def get_parse_error_code(self) -> None:
        """
        Returns the parse error code.
        """
    @property
    def eval(self) -> str:
        """
        Gets the expression.
        """
    @property
    def property_references(self) -> IList:
        """
        Returns the names of all properties referenced by the eval value.
        """
    @property
    def result(self) -> typing.Any:
        """
        Gets the result of the expression.
        """
class IEventArgs(IBaseObject):
    """
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IEventArgs:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IEventArgs:
        ...
    @property
    def event_id(self) -> int:
        ...
    @property
    def event_name(self) -> str:
        ...
class IEventPacket(IPacket):
    """
    As with Data packets, Event packets travel along the signal paths. They are used to notify recipients of any relevant changes to the signal sending the packet.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IEventPacket:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IEventPacket:
        ...
    @property
    def event_id(self) -> str:
        """
        Gets the ID of the event as a string. In example "DATA_DESCRIPTOR_CHANGED".
        """
    @property
    def parameters(self) -> IDict:
        """
        Dictionary containing parameters as <String, BaseObject> pairs relevant to the event signalized by the Event packet.
        """
class IFloat(IBaseObject):
    """
    Represents float number as `IFloat` interface. Use this interface to wrap float variable when you need to add the number to lists, dictionaries and other containers which accept `IBaseObject` and derived interfaces. Float type is defined as double-precision IEEE 754 value.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IFloat:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IFloat:
        ...
    @property
    def value(self) -> float:
        """
        Gets a float value stored in the object.
        """
class IFolder(IComponent):
    """
    Acts as a container for other components
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IFolder:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IFolder:
        ...
    def get_item(self, local_id: str) -> IComponent:
        """
        Gets the item component with the specified localId.
        """
    def get_items(self, search_filter: ISearchFilter = None) -> IList:
        """
        Gets the list of the items in the folder.
        """
    def has_item(self, local_id: str) -> int:
        """
        Returns True if the folder has an item with local ID.
        """
    @property
    def empty(self) -> int:
        """
        Returns True if the folder is empty.
        """
    @property
    def items(self) -> IList:
        """
        Gets the list of the items in the folder.
        """
class IFolderConfig(IFolder):
    """
    Allows write access to folder.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IFolderConfig:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IFolderConfig:
        ...
    def add_item(self, item: IComponent) -> None:
        """
        Adds a component to the folder.
        """
    def clear(self) -> None:
        """
        Removes all items from the folder.
        """
    def remove_item(self, item: IComponent) -> None:
        """
        Removes the item from the folder.
        """
    def remove_item_with_local_id(self, local_id: str) -> None:
        """
        Removes the item from the folder using local id of the component.
        """
class IFunction(IBaseObject):
    """
    Holds a callback function with return value.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IFunction:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IFunction:
        ...
    def __call__(self, *args) -> typing.Any:
        ...
class IFunctionBlock(IFolder):
    """
    Function blocks perform calculations on inputs/generate data, outputting new data in its output signals as packets.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IFunctionBlock:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IFunctionBlock:
        ...
    def get_function_blocks(self, search_filter: ISearchFilter = None) -> IList:
        """
        Gets a list of sub-function blocks.
        """
    def get_input_ports(self, search_filter: ISearchFilter = None) -> IList:
        """
        Gets a list of the function block's input ports.
        """
    def get_signals(self, search_filter: ISearchFilter = None) -> IList:
        """
        Gets the list of the function block's output signals.
        """
    def get_signals_recursive(self, search_filter: ISearchFilter = None) -> IList:
        """
        Gets the list of the function block's visible output signals including signals from visible child function blocks.
        """
    @property
    def function_block_type(self) -> IFunctionBlockType:
        """
        Gets an information structure contain metadata of the function block type.
        """
    @property
    def function_blocks(self) -> IList:
        """
        Gets a list of sub-function blocks.
        """
    @property
    def input_ports(self) -> IList:
        """
        Gets a list of the function block's input ports.
        """
    @property
    def signals(self) -> IList:
        """
        Gets the list of the function block's output signals.
        """
    @property
    def signals_recursive(self) -> IList:
        """
        Gets the list of the function block's visible output signals including signals from visible child function blocks.
        """
    @property
    def status_signal(self) -> ISignal:
        """
        Gets the function block's status signal.
        """
class IFunctionBlockType(IComponentType):
    """
    Provides information about the function block.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IFunctionBlockType:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IFunctionBlockType:
        ...
class IGraphVisualization(IBaseObject):
    """
    Represents a way to get a string representation of a graph usually in some diagram description language like DOT, mermaid or D2.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IGraphVisualization:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IGraphVisualization:
        ...
    def dump(self) -> str:
        """
        Returns the graph representation as a string.
        """
class IInputPort(IComponent):
    """
    Signals accepted by input ports can be connected, forming a connection between the input port and signal, through which Packets can be sent.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IInputPort:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IInputPort:
        ...
    def accepts_signal(self, signal: ISignal) -> int:
        """
        Returns true if the signal can be connected to the input port; false otherwise.
        """
    def connect(self, signal: ISignal) -> None:
        """
        Connects the signal to the input port, forming a Connection.
        """
    def disconnect(self) -> None:
        """
        Disconnects the signal from the input port.
        """
    @property
    def connection(self) -> IConnection:
        """
        Gets the Connection object formed between the Signal and Input port.
        """
    @property
    def requires_signal(self) -> int:
        """
        Returns true if the input port requires a signal to be connected; false otherwise.
        """
    @property
    def signal(self) -> ISignal:
        """
        Gets the signal connected to the input port.
        """
class IInputPortConfig(IInputPort):
    """
    The configuration component of input ports. Provides access to Input port owners to internal components of the input port.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IInputPortConfig:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IInputPortConfig:
        ...
    def notify_packet_enqueued(self) -> None:
        """
        Gets called when a packet was enqueued in a connection.
        """
    def notify_packet_enqueued_on_this_thread(self) -> None:
        """
        Gets called when a packet was enqueued in a connection.
        """
    @property
    def custom_data(self) -> typing.Any:
        """
        Get a custom data attached to the object. / Set a custom data attached to the object.
        """
    @custom_data.setter
    def custom_data(self, arg1: typing.Any) -> None:
        ...
class IInputPortNotifications(IBaseObject):
    """
    Notifications object passed to the input port on construction by its owner (listener).
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IInputPortNotifications:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IInputPortNotifications:
        ...
    def accepts_signal(self, port: IInputPort, signal: ISignal) -> int:
        """
        Called when the Input port method `acceptsSignal` is called. Should return true if the signal is accepted; false otherwise.
        """
    def connected(self, port: IInputPort) -> None:
        """
        Called when a signal is connected to the input port.
        """
    def disconnected(self, port: IInputPort) -> None:
        """
        Called when a signal is disconnected from the input port.
        """
    def packet_received(self, port: IInputPort) -> None:
        """
        Notifies the listener of the newly received packet on the specified input-port.
        """
class IInstance(IDevice):
    """
    The top-level openDAQ object. It acts as container for the openDAQ context and the base module manager.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IInstance:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IInstance:
        ...
    def add_server(self, server_type_id: str, server_config: IPropertyObject) -> IServer:
        """
        Creates and adds a server with the provided serverType and configuration.
        """
    def add_standard_servers(self) -> IList:
        """
        Creates and adds streaming and "openDAQ OpcUa" servers with default configurations.
        """
    def remove_server(self, server: IServer) -> None:
        """
        Removes the server provided as argument.
        """
    def set_root_device(self, connection_string: str, config: IPropertyObject = None) -> None:
        """
        Adds a device with the connection string as root device.
        """
    @property
    def available_server_types(self) -> IDict:
        """
        Get a dictionary of available server types as <IString, IServerType> pairs
        """
    @property
    def module_manager(self) -> IModuleManager:
        """
        Gets the Module manager.
        """
    @property
    def root_device(self) -> IDevice:
        """
        Gets the current root device.
        """
    @property
    def servers(self) -> IList:
        """
        Get list of added servers.
        """
class IInstanceBuilder(IBaseObject):
    """
    Builder component of Instance objects. Contains setter methods to configure the Instance parameters, such as Context (Logger, Scheduler, ModuleManager) and RootDevice. Contains a  `build` method that builds the Instance object.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IInstanceBuilder:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IInstanceBuilder:
        ...
    def add_config_provider(self, config_provider: IConfigProvider) -> None:
        """
        Populates internal options dictionary with values from set config provider
        """
    def add_logger_sink(self, sink: ILoggerSink) -> None:
        """
        Adds the logger sink of the default Instance logger. If Logger has been set, configuring of the Logger sink has no effect in building Instance.
        """
    def add_module_path(self, path: str) -> None:
        """
        Add the path for the default ModuleManager of the Instance. If Module manager has been set, configuring of Module path has no effect in building Instance.
        """
    def build(self) -> IInstance:
        """
        Builds and returns an Instance object using the currently set values of the Builder.
        """
    def enable_standard_providers(self, flag: bool) -> None:
        """
        Allows enabling or disabling standard configuration providers, including JsonConfigProvider, based on the specified flag.
        """
    def set_component_log_level(self, component: str, log_level: LogLevel) -> None:
        """
        Sets The Logger level for a specific component of the Instance. Log messages related to that component will be processed according to the specified log level.
        """
    def set_sink_log_level(self, sink: ILoggerSink, log_level: LogLevel) -> None:
        """
        Sets the sink logger level of the default Instance logger. If Logger has been set, configuring of the Logger sink has no effect in building Instance.
        """
    @property
    def components_log_level(self) -> IDict:
        """
        Gets the dictionary of component names and log level which will be added to logger components
        """
    @property
    def default_root_device_info(self) -> IDeviceInfo:
        """
        Gets the default device info of Instance / Sets the default device info of Instance. If device info has been set, method getInfo of Instance will return set device info if Root Device has not been set
        """
    @default_root_device_info.setter
    def default_root_device_info(self, arg1: IDeviceInfo) -> None:
        ...
    @property
    def default_root_device_local_id(self) -> str:
        """
        Gets the default root device local id / Sets the local id for default device. Has no effect if `Root device` has been congigured.
        """
    @default_root_device_local_id.setter
    def default_root_device_local_id(self, arg1: str) -> None:
        ...
    @property
    def global_log_level(self) -> LogLevel:
        """
        Gets the default Logger global level of Instance / Sets the Logger global log level for the Instance. All log messages with a severity level equal to or higher than the specified level will be processed.
        """
    @global_log_level.setter
    def global_log_level(self, arg1: LogLevel) -> None:
        ...
    @property
    def logger(self) -> ILogger:
        """
        Gets the Logger of the Instance. Returns nullptr if custom logger has not been set / Sets the custom Logger for the Instance. This logger will be used for logging messages related to the Instance and its components. When configured, the `Logger sink` will be ignored, as it is in use only with the default Instance logger.
        """
    @logger.setter
    def logger(self, arg1: ILogger) -> None:
        ...
    @property
    def logger_sinks(self) -> IList:
        """
        Gets the list of logger sinks for the default Instance logger.
        """
    @property
    def module_manager(self) -> IModuleManager:
        """
        Gets the custom ModuleManager of Instance / Sets The custom ModuleManager for the Instance.
        """
    @module_manager.setter
    def module_manager(self, arg1: IModuleManager) -> None:
        ...
    @property
    def module_path(self) -> str:
        """
        Gets the path for the default ModuleManager of Instance. / Sets the path for the default ModuleManager of the Instance. If Module manager has been set, configuring of Module path has no effect in building Instance.
        """
    @module_path.setter
    def module_path(self, arg1: str) -> None:
        ...
    @property
    def module_paths_list(self) -> IList:
        """
        Get the list of paths for the default ModuleManager of the Instance. If Module manager has been set, configuring of Module path has no effect in building Instance.
        """
    @property
    def options(self) -> IDict:
        """
        Gets the dictionary of instance options
        """
    @property
    def root_device(self) -> str:
        """
        Gets the connection string for the default root device of Instance. / Sets the connection string for a device that replaces the default openDAQ root device. When the instance is created, a connection to the device with the given connection string will be established, and the device will be placed at the root of the component tree structure.
        """
    @root_device.setter
    def root_device(self, arg1: str) -> None:
        ...
    @property
    def scheduler(self) -> IScheduler:
        """
        Gets the custom scheduler of Instance / Sets the custom scheduler of Instance
        """
    @scheduler.setter
    def scheduler(self, arg1: IScheduler) -> None:
        ...
    @property
    def scheduler_worker_num(self) -> int:
        """
        Gets the amount of worker threads in the scheduler of Instance. / Sets the number of worker threads in the scheduler of the Instance. If Scheduler has been set, configuring of Scheduler worker num has no effect in building Instance.
        """
    @scheduler_worker_num.setter
    def scheduler_worker_num(self, arg1: int) -> None:
        ...
class IInteger(IBaseObject):
    """
    Represents int number as `IInteger` interface. Use this interface to wrap integer variable when you need to add the number to lists, dictionaries and other containers which accept `IBaseObject` and derived interfaces.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IInteger:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IInteger:
        ...
    @property
    def value(self) -> int:
        """
        Gets an int value stored in the object.
        """
class IIterable(IBaseObject):
    """
    An iterable object can construct iterators and use them to iterate through items.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IIterable:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IIterable:
        ...
    def __iter__(self) -> IIterator:
        """
        Creates and returns the object's start iterator.
        """
class IIterator(IBaseObject):
    """
    Interface to iterate through items of a container object.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IIterator:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IIterator:
        ...
    def __next__(self) -> typing.Any:
        ...
class IList(IBaseObject):
    """
    Represents a heterogeneous collection of objects that can be individually accessed by index.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IList:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IList:
        ...
    @typing.overload
    def __getitem__(self, arg0: int) -> typing.Any:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> IList:
        ...
    def __iter__(self) -> typing.Any:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        ...
    def __setitem__(self, arg0: int, arg1: typing.Any) -> None:
        ...
    def __str__(self) -> str:
        ...
    def append(self, arg0: typing.Any) -> None:
        ...
    def clear(self) -> None:
        """
        Removes all elements from the list.
        """
    def pop_back(self) -> typing.Any:
        ...
    def pop_front(self) -> typing.Any:
        ...
    def push_back(self, arg0: typing.Any) -> None:
        ...
    def push_front(self, arg0: typing.Any) -> None:
        ...
class ILogger(IBaseObject):
    """
    Represents a collection of @ref ILoggerComponent "Logger Components" with multiple
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> ILogger:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> ILogger:
        ...
    def add_component(self, name: str) -> ILoggerComponent:
        """
        Creates a component with a given name and adds it to the Logger object.
        """
    def flush(self) -> None:
        """
        Triggers writing out the messages stored in temporary buffers for added components and sinks associated with the Logger object.
        """
    def flush_on_level(self, level: LogLevel) -> None:
        """
        Sets the minimum severity level of messages to be automatically flushed by components of Logger object.
        """
    def get_component(self, name: str) -> ILoggerComponent:
        """
        Gets an added component by name.
        """
    def get_or_add_component(self, name: str) -> ILoggerComponent:
        """
        Gets an added component by name or creates a new one with a given name and adds it to the Logger object.
        """
    def remove_component(self, name: str) -> None:
        """
        Removes the component with a given name from the Logger object.
        """
    @property
    def components(self) -> IList:
        """
        Gets a list of added components.
        """
    @property
    def level(self) -> LogLevel:
        """
        Gets the default log severity level. / Sets the default log severity level.
        """
    @level.setter
    def level(self, arg1: LogLevel) -> None:
        ...
class ILoggerComponent(IBaseObject):
    """
    Logs messages produced by a specific part of openDAC SDK. The messages are written into the @ref ILoggerSink "Logger Sinks" associated with the Logger Component object.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> ILoggerComponent:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> ILoggerComponent:
        ...
    def flush(self) -> None:
        """
        Triggers writing out the messages stored in temporary buffers.
        """
    def flush_on_level(self, level: LogLevel) -> None:
        """
        Sets the minimum severity level of messages to be automatically written to the associated sinks bypassing the temporary buffers.
        """
    def log_message(self, location: ..., msg: str, level: LogLevel) -> None:
        """
        Logs a message with the provided source location and severity level.
        """
    def should_log(self, level: LogLevel) -> int:
        """
        Checks whether the messages with given log severity level will be logged or not.
        """
    @property
    def level(self) -> LogLevel:
        """
        Gets the minimal severity level of messages to be logged by the component. / Sets the minimal severity level of messages to be logged by the component.
        """
    @level.setter
    def level(self, arg1: LogLevel) -> None:
        ...
    @property
    def name(self) -> str:
        """
        Gets the name of the component.
        """
class ILoggerSink(IBaseObject):
    """
    Represents the object that actually writes the log messages to the target. Each Logger Sink is responsible for only single target: file, console etc.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> ILoggerSink:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> ILoggerSink:
        ...
    def flush(self) -> None:
        """
        Triggers writing out the messages from temporary buffers to the target.
        """
    def should_log(self, level: LogLevel) -> int:
        """
        Checks whether the messages with given log severity level will be written to the target or not.
        """
    @property
    def level(self) -> LogLevel:
        """
        Gets the minimal severity level of messages to be written to the target. / Sets the minimal severity level of messages to be written to the target.
        """
    @level.setter
    def level(self, arg1: LogLevel) -> None:
        ...
class ILoggerThreadPool(IBaseObject):
    """
    Container for messages queue and backing threads used for asynchronous logging.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> ILoggerThreadPool:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> ILoggerThreadPool:
        ...
class IMirroredSignalConfig(ISignalConfig):
    """
    Represents configuration interface for mirrored signals. Allows selecting streaming data sources per signal.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IMirroredSignalConfig:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IMirroredSignalConfig:
        ...
    def deactivate_streaming(self) -> None:
        """
        Stops the streaming and clears the active streaming source of the signal.
        """
    @property
    def active_streaming_source(self) -> str:
        """
        Gets a connection strings of the active streaming source of the signal. / Sets the active streaming source of the signal.
        """
    @active_streaming_source.setter
    def active_streaming_source(self, arg1: str) -> None:
        ...
    @property
    def remote_id(self) -> str:
        """
        Gets the global ID of the signal as it appears on the remote device.
        """
    @property
    def streaming_sources(self) -> IList:
        """
        Gets a list of connection strings of all available streaming sources of the signal.
        """
class IMirroredSignalPrivate(IBaseObject):
    """
    Internal functions used by openDAQ core. This interface should never be used in client SDK or module code.
    """
    mirrored_data_descriptor: IDataDescriptor
    mirrored_domain_signal: IMirroredSignalConfig
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IMirroredSignalPrivate:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IMirroredSignalPrivate:
        ...
    def add_streaming_source(self, streaming: IStreaming) -> None:
        """
        Adds streaming source for signal.
        """
    def remove_streaming_source(self, streaming_connection_string: str) -> None:
        """
        Removes streaming source for signal.
        """
    def subscribe_completed(self, streaming_connection_string: str) -> None:
        """
        Handles the completion of subscription acknowledged by the specified streaming source.
        """
    def trigger_event(self, event_packet: IEventPacket) -> int:
        """
        Handles event packet e.g. packet with changes of the signals descriptors or signal properties
        """
    def unsubscribe_completed(self, streaming_connection_string: str) -> None:
        """
        Handles the completion of unsubscription acknowledged by the specified streaming source.
        """
class IModule(IBaseObject):
    """
    A module is an object that provides device and function block factories. The object is usually implemented in an external dynamic link / shared library. IModuleManager is responsible for loading all modules.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IModule:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IModule:
        ...
    def accepts_connection_parameters(self, connection_string: str, config: IPropertyObject = None) -> int:
        """
        Checks if connection string can be used to connect to devices supported by this module and if the configuration object provided to this module is valid.
        """
    def accepts_streaming_connection_parameters(self, connection_string: str, config: IPropertyObject = None) -> int:
        """
        Verifies whether the provided connection string or config object can be used to establish a streaming connection supported by this module. If the connection string is not assigned, it checks if the config object is valid and complete enough to generate a connection string.
        """
    def create_device(self, connection_string: str, parent: IComponent, config: IPropertyObject = None) -> IDevice:
        """
        Creates a device object that can communicate with the device described in the specified connection string. The device object is not automatically added as a sub-device of the caller, but only returned by reference.
        """
    def create_function_block(self, id: str, parent: IComponent, local_id: str, config: IPropertyObject = None) -> IFunctionBlock:
        """
        Creates and returns a function block with the specified id. The function block is not automatically added to the FB list of the caller.
        """
    def create_server(self, server_type_id: str, root_device: IDevice, config: IPropertyObject = None) -> IServer:
        """
        Creates and returns a server with the specified server type. To prevent cyclic reference, we should not use the Instance instead of rootDevice.
        """
    def create_streaming(self, connection_string: str, config: IPropertyObject) -> IStreaming:
        """
        Creates and returns a streaming object using the specified connection string or config info object.
        """
    @property
    def available_device_types(self) -> IDict:
        """
        Returns a dictionary of known and available device types this module can create.
        """
    @property
    def available_devices(self) -> IList:
        """
        Returns a list of known devices info. The implementation can start discovery in background and only return the results in this function.
        """
    @property
    def available_function_block_types(self) -> IDict:
        """
        Returns a dictionary of known and available function block types this module can create.
        """
    @property
    def available_server_types(self) -> IDict:
        """
        Returns a dictionary of known and available servers types that this module can create.
        """
    @property
    def id(self) -> str:
        """
        Gets the module id.
        """
    @property
    def name(self) -> str:
        """
        Gets the module name.
        """
    @property
    def version_info(self) -> ...:
        """
        Retrieves the module version information.
        """
class IModuleManager(IBaseObject):
    """
    Loads all available modules in a implementation-defined manner. User can also side-load custom modules via `addModule` call.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IModuleManager:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IModuleManager:
        ...
    def add_module(self, module: IModule) -> None:
        """
        Side-load a custom module in run-time from memory that was not found by default.
        """
    def load_modules(self, context: IContext) -> None:
        """
        Loads all modules from the directory path specified during manager construction. The Context is passed to all loaded modules for internal use.
        """
    @property
    def modules(self) -> IList:
        """
        Retrieves all modules known to the manager. Whether they were found or side-loaded.
        """
class INumber(IBaseObject):
    """
    Represents either a float or an int number.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> INumber:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> INumber:
        ...
    def __float__(self) -> float:
        ...
    def __int__(self) -> int:
        ...
    @property
    def float_value(self) -> float:
        """
        Gets a value stored in the object as a floating point value.
        """
    @property
    def int_value(self) -> int:
        """
        Gets a value stored in the object as an integer value.
        """
class IOwnable(IBaseObject):
    """
    An ownable object can have IPropertyObject as the owner.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IOwnable:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IOwnable:
        ...
class IPacket(IBaseObject):
    """
    Base packet type. Data, Value, and Event packets are all also packets. Provides the packet's unique ID that is unique to a given device, as well as the packet type.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IPacket:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IPacket:
        ...
    def subscribe_for_destruct_notification(self, packet_destruct_callback: IPacketDestructCallback) -> None:
        """
        Subscribes for notification when the packet is destroyed.
        """
    @property
    def ref_count(self) -> int:
        """
        Gets the reference count of the packet.
        """
    @property
    def type(self) -> PacketType:
        """
        Gets the packet's type.
        """
class IPacketDestructCallback(IBaseObject):
    """
    Used to subscribe to packet destruction
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IPacketDestructCallback:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IPacketDestructCallback:
        ...
    def on_packet_destroyed(self) -> None:
        """
        Called when packet is destroyed.
        """
class IPacketReader(IReader):
    """
    A signal reader reads packets from a signal data stream.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IPacketReader:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IPacketReader:
        ...
    def read(self) -> IPacket:
        """
        Retrieves the next available packet in the data-stream.
        """
    def read_all(self) -> IList:
        """
        Retrieves all the currently available packets in the data-stream.
        """
class IProcedure(IBaseObject):
    """
    Holds a callback function without return value.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IProcedure:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IProcedure:
        ...
    def __call__(self, *args) -> None:
        ...
class IProperty(IBaseObject):
    """
    Defines a set of metadata that describes the values held by a Property object stored under the key equal to the property's name.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IProperty:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IProperty:
        ...
    @property
    def callable_info(self) -> ICallableInfo:
        """
        Gets the Callable information objects of the Property that specifies the argument and return types of the callable object stored as the Property value.
        """
    @property
    def coercer(self) -> ICoercer:
        """
        Gets the coercer of the Property.
        """
    @property
    def default_value(self) -> typing.Any:
        """
        Gets the Default value of the Property. The Default value must always be configured for a Property to be in a valid state. Exceptions are Function/Procedure and Reference properties.
        """
    @property
    def description(self) -> str:
        """
        Gets the short string Description of the Property.
        """
    @property
    def is_referenced(self) -> int:
        """
        Used to determine whether the Property is referenced by another property.
        """
    @property
    def item_type(self) -> CoreType:
        """
        Gets the Item type of the Property. Configured only if the Value type is `ctDict` or `ctList`. If so, the item types of the list/dictionary must match the Property's Item type.
        """
    @property
    def key_type(self) -> CoreType:
        """
        Gets the Key type of the Property. Configured only if the Value type is `ctDict`. If so, the key type of the dictionary Property values must match the Property's Key type.
        """
    @property
    def max_value(self) -> INumber:
        """
        Gets the Maximum value of the Property. Available only if the Value type is `ctInt` or `ctFloat`.
        """
    @property
    def min_value(self) -> INumber:
        """
        Gets the Minimum value of the Property. Available only if the Value type is `ctInt` or `ctFloat`.
        """
    @property
    def name(self) -> str:
        """
        Gets the Name of the Property. The names of Properties in a Property object must be unique. The name is used as the key to the corresponding Property value when getting/setting the value.
        """
    @property
    def read_only(self) -> int:
        """
        Used to determine whether the Property is a read-only property or not.
        """
    @property
    def referenced_property(self) -> IProperty:
        """
        Gets the referenced property. If set, all getters except for the `Name`, `Referenced property`, and `Is referenced` getters will return the value of the `Referenced property`.
        """
    @property
    def selection_values(self) -> typing.Any:
        """
        Gets the list or dictionary of selection values. If the list/dictionary is not empty, the property is a Selection property, and must have the Value type `ctInt`.
        """
    @property
    def struct_type(self) -> IStructType:
        """
        Gets the Struct type object of the Property, if the Property is a Struct property.
        """
    @property
    def suggested_values(self) -> IList:
        """
        Gets the list of Suggested values. Contains values that are the optimal settings for the corresponding Property value. These values, however, are not enforced when setting a new Property value.
        """
    @property
    def unit(self) -> IUnit:
        """
        Gets the Unit of the Property.
        """
    @property
    def validator(self) -> IValidator:
        """
        Gets the validator of the Property.
        """
    @property
    def value_type(self) -> CoreType:
        """
        Gets the Value type of the Property. Values written to the corresponding Property value must be of the same type.
        """
    @property
    def visible(self) -> int:
        """
        Used to determine whether the property is visible or not.
        """
class IPropertyBuilder(IBaseObject):
    """
    The builder interface of Properties. Allows for construction of Properties through the `build` method.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IPropertyBuilder:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IPropertyBuilder:
        ...
    def build(self) -> IProperty:
        """
        Builds and returns a Property using the currently set values of the Builder.
        """
    @property
    def callable_info(self) -> ICallableInfo:
        """
        Gets the Callable information objects of the Property that specifies the argument and return types of the callable object stored as the Property value. / Sets the Callable information objects of the Property that specifies the argument and return types of the callable object stored as the Property value.
        """
    @callable_info.setter
    def callable_info(self, arg1: typing.Any) -> None:
        ...
    @property
    def coercer(self) -> ICoercer:
        """
        Gets the coercer of the Property. / Sets the coercer of the Property.
        """
    @coercer.setter
    def coercer(self, arg1: typing.Any) -> None:
        ...
    @property
    def default_value(self) -> typing.Any:
        """
        Gets the Default value of the Property. / Sets the Default value of the Property. The Default value must always be configured for a Property to be in a valid state. Exceptions are Function/Procedure and Reference properties. The function will freeze default value if it is freezable.
        """
    @default_value.setter
    def default_value(self, arg1: typing.Any) -> None:
        ...
    @property
    def description(self) -> str:
        """
        Gets the short string Description of the Property. / Sets the short string Description of the Property.
        """
    @description.setter
    def description(self, arg1: str) -> None:
        ...
    @property
    def max_value(self) -> INumber:
        """
        Gets the Maximum value of the Property. Available only if the Value type is `ctInt` or `ctFloat`. / Sets the Maximum value of the Property. Available only if the Value type is `ctInt` or `ctFloat`.
        """
    @max_value.setter
    def max_value(self, arg1: typing.Any) -> None:
        ...
    @property
    def min_value(self) -> INumber:
        """
        Gets the Minimum value of the Property. Available only if the Value type is `ctInt` or `ctFloat`. / Sets the Minimum value of the Property. Available only if the Value type is `ctInt` or `ctFloat`.
        """
    @min_value.setter
    def min_value(self, arg1: typing.Any) -> None:
        ...
    @property
    def name(self) -> str:
        """
        Gets the Name of the Property. / Sets the Name of the Property. The names of Properties in a Property object must be unique. The name is used as the key to the corresponding Property value when getting/setting the value.
        """
    @name.setter
    def name(self, arg1: str) -> None:
        ...
    @property
    def read_only(self) -> IBoolean:
        """
        Used to determine whether the Property is a read-only property or not. / Used to determine whether the Property is a read-only property or not.
        """
    @read_only.setter
    def read_only(self, arg1: typing.Any) -> None:
        ...
    @property
    def referenced_property(self) -> IEvalValue:
        """
        Gets the referenced property. / Sets the referenced property. If set, all getters except for the `Name`, `Referenced property`, and `Is referenced` getters will return the value of the `Referenced property`.
        """
    @referenced_property.setter
    def referenced_property(self, arg1: IEvalValue) -> None:
        ...
    @property
    def selection_values(self) -> typing.Any:
        """
        Gets the list or dictionary of selection values. / Sets the list or dictionary of selection values. If the list/dictionary is not empty, the property is a Selection property, and must have the Value type `ctInt`.
        """
    @selection_values.setter
    def selection_values(self, arg1: typing.Any) -> None:
        ...
    @property
    def suggested_values(self) -> IList:
        """
        Gets the list of Suggested values. Contains values that are the optimal gettings for the corresponding Property value. These values, however, are not enforced when getting a new Property value. / Sets the list of Suggested values. Contains values that are the optimal settings for the corresponding Property value. These values, however, are not enforced when setting a new Property value.
        """
    @suggested_values.setter
    def suggested_values(self, arg1: typing.Any) -> None:
        ...
    @property
    def unit(self) -> IUnit:
        """
        Gets the Unit of the Property. / Sets the Unit of the Property.
        """
    @unit.setter
    def unit(self, arg1: typing.Any) -> None:
        ...
    @property
    def validator(self) -> IValidator:
        """
        Gets the validator of the Property. / Sets the validator of the Property.
        """
    @validator.setter
    def validator(self, arg1: typing.Any) -> None:
        ...
    @property
    def value_type(self) -> CoreType:
        """
        Gets the Value type of the Property. / Sets the Value type of the Property. Values written to the corresponding Property value must be of the same type.
        """
    @value_type.setter
    def value_type(self, arg1: CoreType) -> None:
        ...
    @property
    def visible(self) -> IBoolean:
        """
        Used to determine whether the property is visible or not. / Used to determine whether the property is visible or not.
        """
    @visible.setter
    def visible(self, arg1: typing.Any) -> None:
        ...
class IPropertyObject(IBaseObject):
    """
    A container of Properties and their corresponding Property values.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IPropertyObject:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IPropertyObject:
        ...
    def add_property(self, property: IProperty) -> None:
        """
        Adds the property to the Property object.
        """
    def begin_update(self) -> None:
        """
        Begins batch configuration of the object.
        """
    def clear_property_value(self, property_name: str) -> None:
        """
        Clears the Property value from the Property object
        """
    def end_update(self) -> None:
        """
        Ends batch configuration of the object.
        """
    def get_property(self, property_name: str) -> IProperty:
        """
        Gets the Property with the given `propertyName`.
        """
    def get_property_selection_value(self, property_name: str) -> typing.Any:
        """
        Gets the selected value of the Property, if the Property is a Selection property.
        """
    def get_property_value(self, property_name: str) -> typing.Any:
        """
        Gets the value of the Property with the given name.
        """
    def has_property(self, property_name: str) -> int:
        """
        Checks if the Property object contains a property named `propertyName`.
        """
    def remove_property(self, property_name: str) -> None:
        """
        Removes the Property named `propertyName` from the Property object.
        """
    def set_property_value(self, property_name: str, value: typing.Any) -> None:
        """
        Sets the value of the Property with the given name.
        """
    @property
    def all_properties(self) -> IList:
        """
        Returns a list of all properties contained in the Property object.
        """
    @property
    def class_name(self) -> str:
        """
        Gets the name of the class the Property object was constructed with.
        """
    @property
    def visible_properties(self) -> IList:
        """
        Returns a list of visible properties contained in the Property object.
        """
class IPropertyObjectClass(IType):
    """
    Container of properties that can be used as a base class when instantiating a Property object.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IPropertyObjectClass:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IPropertyObjectClass:
        ...
    def get_properties(self, include_inherited: bool) -> IList:
        """
        Gets the list of properties added to the class.
        """
    def get_property(self, property_name: str) -> IProperty:
        """
        Gets the class's property with the given name.
        """
    def has_property(self, property_name: str) -> int:
        """
        Checks if the property is registered.
        """
    @property
    def parent_name(self) -> str:
        """
        Gets the name of the parent of the property class.
        """
class IPropertyObjectClassBuilder(IBaseObject):
    """
    The builder interface of Property object classes. Allows for their modification and building of Property object classes.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IPropertyObjectClassBuilder:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IPropertyObjectClassBuilder:
        ...
    def add_property(self, property: IProperty) -> None:
        """
        Adds a property to the class.
        """
    def build(self) -> IPropertyObjectClass:
        """
        Builds and returns a Property object class using the currently set values of the Builder.
        """
    def remove_property(self, property_name: str) -> None:
        """
        Removes a property with the given name from the class.
        """
    @property
    def manager(self) -> ITypeManager:
        """
        Gets a type manager
        """
    @property
    def name(self) -> str:
        """
        Gets the name of the property class. / Sets the name of the property class.
        """
    @name.setter
    def name(self, arg1: str) -> None:
        ...
    @property
    def parent_name(self) -> str:
        """
        Gets the name of the parent of the property class. / Gets the name of the parent of the property class.
        """
    @parent_name.setter
    def parent_name(self, arg1: str) -> None:
        ...
    @property
    def properties(self) -> IDict:
        """
        Gets the dictionary of properties
        """
    @property
    def property_order(self) -> IList:
        """
        Gets a custom order of properties as defined in the list of property names. / Sets a custom order of properties as defined in the list of property names.
        """
    @property_order.setter
    def property_order(self, arg1: IList) -> None:
        ...
class IPropertyObjectProtected(IBaseObject):
    """
    Provides protected access that allows changing read-only property values of a Property object.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IPropertyObjectProtected:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IPropertyObjectProtected:
        ...
    def clear_protected_property_value(self, property_name: str) -> None:
        """
        Clears a property value. Does not fail if the property is read-only.
        """
    def set_protected_property_value(self, property_name: str, value: typing.Any) -> None:
        """
        Sets a property value. Does not fail if the property is read-only.
        """
class IPropertyValueEventArgs(IEventArgs):
    """
    """
    value: typing.Any
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IPropertyValueEventArgs:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IPropertyValueEventArgs:
        ...
    @property
    def is_updating(self) -> int:
        ...
    @property
    def property(self) -> IProperty:
        ...
    @property
    def property_event_type(self) -> PropertyEventType:
        ...
class IRange(IBaseObject):
    """
    Describes a range of values between the `lowValue` and `highValue` boundaries.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IRange:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IRange:
        ...
    @property
    def high_value(self) -> INumber:
        """
        Gets the upper boundary value of the range.
        """
    @property
    def low_value(self) -> INumber:
        """
        Gets the lower boundary value of the range.
        """
class IRatio(IBaseObject):
    """
    Represents rational number as `IRatio` interface. Use this interface to wrap rational number when you need to add the number to lists, dictionaries and other containers which accept `IBaseObject` and derived interfaces. Rational numbers are defined as numerator / denominator.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IRatio:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IRatio:
        ...
    def simplify(self) -> typing.Any:
        """
        Simplifies rational number if possible and returns the simplified ratio as a new object.
        """
    @property
    def denominator(self) -> int:
        """
        Gets denominator part.
        """
    @property
    def numerator(self) -> int:
        """
        Gets numerator part.
        """
class IReader(IBaseObject):
    """
    A basic signal reader that simplifies accessing the signals's data stream.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IReader:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IReader:
        ...
    @property
    def available_count(self) -> int:
        """
        Gets the number of segments available to read
        """
class IReaderStatus(IBaseObject):
    """
    Represents the status of the reading process returned by the reader::read function.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IReaderStatus:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IReaderStatus:
        ...
    @property
    def event_packet(self) -> IEventPacket:
        """
        Retrieves the event packet from the reading process.
        """
    @property
    def read_status(self) -> ReadStatus:
        """
        Retrieves the current reading status, indicating whether the reading process is in an "Ok" state, has encountered an Event, has failed, or is in an Unknown state.
        """
    @property
    def valid(self) -> int:
        """
        Checks the validity of the reader.
        """
class IRemovable(IBaseObject):
    """
    Allows the component to be notified when it is removed.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IRemovable:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IRemovable:
        ...
    def remove(self) -> None:
        """
        Notifies the component that it is being removed.
        """
    @property
    def removed(self) -> int:
        """
        Returns True if component was removed.
        """
class ISampleReader(IReader):
    """
    A basic signal reader that simplifies reading the signals's samples.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> ISampleReader:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> ISampleReader:
        ...
    @property
    def domain_read_type(self) -> SampleType:
        """
        Gets the sample-type the signal domain samples will be converted to when read or @c SampleType::Invalid if read-type has not been determined yet.
        """
    @property
    def read_mode(self) -> ReadMode:
        """
        Gets the reader's read mode which determines if the reader will also scale the read data or not.
        """
    @property
    def value_read_type(self) -> SampleType:
        """
        Gets the sample-type the signal value samples will be converted to when read or @c SampleType::Invalid if read-type has not been determined yet.
        """
class IScaling(IBaseObject):
    """
    Signal descriptor field that defines a scaling transformation, which should be applied to data carried by the signal's packets when read.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IScaling:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IScaling:
        ...
    @property
    def input_sample_type(self) -> SampleType:
        """
        Gets the scaling's input data type.
        """
    @property
    def output_sample_type(self) -> ScaledSampleType:
        """
        Gets the scaling's output data type.
        """
    @property
    def parameters(self) -> IDict:
        """
        Gets the dictionary of parameters that are used to calculate the scaling in conjunction with the input data.
        """
    @property
    def type(self) -> ScalingType:
        """
        Gets the type of the scaling that determines how the scaling parameters should be interpreted and how the scaling should be calculated.
        """
class IScalingBuilder(IBaseObject):
    """
    Configuration component of Scaling objects. Contains setter methods that allow for Scaling parameter configuration, and a `build` method that builds the Scaling object.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IScalingBuilder:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IScalingBuilder:
        ...
    def add_parameter(self, name: str, parameter: typing.Any) -> None:
        """
        Adds a string-object pair parameter to the Dictionary of Scaling parameters.
        """
    def build(self) -> IScaling:
        """
        Builds and returns a Scaling object using the currently set values of the Builder.
        """
    def remove_parameter(self, name: str) -> None:
        """
        Removes the parameter with the given name from the Dictionary of Scaling parameters.
        """
    @property
    def input_data_type(self) -> SampleType:
        """
        Gets the scaling's input data type. / Sets the scaling's input data type.
        """
    @input_data_type.setter
    def input_data_type(self, arg1: SampleType) -> None:
        ...
    @property
    def output_data_type(self) -> ScaledSampleType:
        """
        Gets the scaling's output data type. / Sets the scaling's output data type.
        """
    @output_data_type.setter
    def output_data_type(self, arg1: ScaledSampleType) -> None:
        ...
    @property
    def parameters(self) -> IDict:
        """
        Gets the list of parameters that are used to calculate the scaling in conjunction with the input data. / Gets the list of parameters that are used to calculate the scaling in conjunction with the input data.
        """
    @parameters.setter
    def parameters(self, arg1: IDict) -> None:
        ...
    @property
    def scaling_type(self) -> ScalingType:
        """
        Gets the type of the scaling that determines how the scaling parameters should be interpreted and how the scaling should be calculated. / Sets the type of the scaling that determines how the scaling parameters should be interpreted and how the scaling should be calculated.
        """
    @scaling_type.setter
    def scaling_type(self, arg1: ScalingType) -> None:
        ...
class IScheduler(IBaseObject):
    """
    A thread-pool scheduler that supports scheduling one-off functions as well as dependency graphs.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IScheduler:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IScheduler:
        ...
    def schedule_graph(self, graph: ITaskGraph) -> IAwaitable:
        """
        Schedules the specified dependency @p graph to run on the thread-pool. The call does not block but immediately returns an @p awaitable that represents the asynchronous execution. It can be waited upon and queried for status and result. <b>Any exceptions that occur during the graph execution are silently ignored.</b>
        """
    def schedule_work(self, work: IFunction) -> IAwaitable:
        """
        Schedules the specified @p work function to run on the thread-pool. The call does not block but immediately returns an @p awaitable that represents the asynchronous execution. It can be waited upon and queried for status and result.
        """
    def stop(self) -> None:
        """
        Cancels all outstanding work and waits for the remaining to complete. After this point the scheduler does not allow any new work or graphs for scheduling.
        """
    def wait_all(self) -> None:
        """
        Waits fo all current scheduled work and tasks to complete.
        """
    @property
    def multi_threaded(self) -> int:
        """
        Returns whether more than one worker thread is used.
        """
class ISearchFilter(IBaseObject):
    """
    Search filter that can be passed as an optional parameter to openDAQ tree traversal functions to filter out unwanted results. Allows for recursive searches.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> ISearchFilter:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> ISearchFilter:
        ...
    def accepts_component(self, component: IComponent) -> int:
        """
        Defines whether or not the component should be included in the search results
        """
    def visit_children(self, component: IComponent) -> int:
        """
        Defines whether or not the children of said component should be traversed during a recursive search.
        """
class IServer(IBaseObject):
    """
    Represents a server. The server provides access to the openDAQ device. Depend of the implementation, it can support configuring the device, reading configuration, and data streaming.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IServer:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IServer:
        ...
    def stop(self) -> None:
        """
        Stops the server. This is called when we remove the server from the Instance or Instance is closing.
        """
class IServerCapability(IPropertyObject):
    """
    Represents standard information about a server's capability to support various protocols. The Server Capability object functions as a Property Object, facilitating the inclusion of custom properties of String, Int, Bool, or Float types. This interface serves to store essential details regarding the supported protocol by a device. It adheres to a standardized set of properties, including methods to retrieve information such as the connection string, protocol name, protocol type, connection type, and core events enabled.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IServerCapability:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IServerCapability:
        ...
    @property
    def connection_string(self) -> str:
        """
        Gets the connection string of the device with the current protocol.
        """
    @property
    def connection_strings(self) -> IList:
        """
        Gets the connection string of the device with the current protocol.
        """
    @property
    def connection_type(self) -> str:
        """
        Gets the type of connection supported by the device.
        """
    @property
    def core_events_enabled(self) -> int:
        """
        Gets the client update method supported by the device.
        """
    @property
    def prefix(self) -> str:
        """
        Gets the prefix of the connection string (eg. "daq.nd" or "daq.opcua")
        """
    @property
    def protocol_id(self) -> str:
        """
        Gets the id of the protocol supported by the device. Should not contain spaces or special characters except for '_' and '-'.
        """
    @property
    def protocol_name(self) -> str:
        """
        Gets the name of the protocol supported by the device.
        """
    @property
    def protocol_type(self) -> ProtocolType:
        """
        Gets the type of protocol supported by the device.
        """
class IServerType(IComponentType):
    """
    Provides information about the server.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IServerType:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IServerType:
        ...
class ISignal(IComponent):
    """
    A signal with an unique ID that sends event/data packets through connections to input ports the signal is connected to.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> ISignal:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> ISignal:
        ...
    @property
    def connections(self) -> IList:
        """
        Gets the list of connections to input ports formed by the signal.
        """
    @property
    def descriptor(self) -> IDataDescriptor:
        """
        Gets the signal's data descriptor.
        """
    @property
    def domain_signal(self) -> ISignal:
        """
        Gets the signal that carries its domain data.
        """
    @property
    def last_value(self) -> typing.Any:
        """
        Gets the signal last value
        """
    @property
    def public(self) -> int:
        """
        Returns true if the signal is public; false otherwise. / Sets the signal to be either public or private.
        """
    @public.setter
    def public(self, arg1: bool) -> None:
        ...
    @property
    def related_signals(self) -> IList:
        """
        Gets a list of related signals.
        """
    @property
    def streamed(self) -> int:
        """
        Returns true if the signal is streamed; false otherwise. / Sets the signal to be either streamed or not.
        """
    @streamed.setter
    def streamed(self, arg1: bool) -> None:
        ...
class ISignalConfig(ISignal):
    """
    The configuration component of a Signal. Allows for configuration of its properties, managing its streaming sources, and sending packets through its connections.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> ISignalConfig:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> ISignalConfig:
        ...
    def add_related_signal(self, signal: ISignal) -> None:
        """
        Adds a related signal to the list of related signals.
        """
    def clear_related_signals(self) -> None:
        """
        Clears the list of related signals.
        """
    def remove_related_signal(self, signal: ISignal) -> None:
        """
        Removes a signal from the list of related signal.
        """
    def send_packet(self, packet: IPacket) -> None:
        """
        Sends a packet through all connections of the signal.
        """
class ISignalEvents(IBaseObject):
    """
    Internal functions of a signal containing event methods that are called on certain events. Eg. when a signal is connected to an input port, or when a signal is used as a domain signal of another.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> ISignalEvents:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> ISignalEvents:
        ...
    def domain_signal_reference_removed(self, signal: ISignal) -> None:
        """
        Notifies the signal that it is no longer being used as a domain signal by the signal passed as the function argument.
        """
    def domain_signal_reference_set(self, signal: ISignal) -> None:
        """
        Notifies the signal that it is being used as a domain signal by the signal passed as the function argument.
        """
    def listener_connected(self, connection: IConnection) -> None:
        """
        Notifies the signal that it has been connected to an input port forming a new connection.
        """
    def listener_disconnected(self, connection: IConnection) -> None:
        """
        Notifies the signal that it has been disconnected from an input port with the given connection.
        """
class ISimpleType(IType):
    """
    Simple type created from a CoreType. The name of the type matches that of the CoreType used for its construction (eg. ctInt == "int"
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> ISimpleType:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> ISimpleType:
        ...
class IStreamReader(ISampleReader):
    """
    A signal data reader that abstracts away reading of signal packets by keeping an internal read-position and automatically advances it on subsequent reads.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IStreamReader:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IStreamReader:
        ...
    def read(self, count: int, timeout_ms: int = 0) -> numpy.ndarray[numpy.float32] | numpy.ndarray[numpy.float64] | numpy.ndarray[numpy.uint32] | numpy.ndarray[numpy.int32] | numpy.ndarray[numpy.uint64] | numpy.ndarray[numpy.int64] | numpy.ndarray[numpy.uint8] | numpy.ndarray[numpy.int8] | numpy.ndarray[numpy.uint16] | numpy.ndarray[numpy.int16]:
        """
        Copies at maximum the next `count` unread samples to the values buffer. The amount actually read is returned through the `count` parameter.
        """
    def read_with_domain(self, count: int, timeout_ms: int = 0) -> tuple[numpy.ndarray[numpy.float32] | numpy.ndarray[numpy.float64] | numpy.ndarray[numpy.uint32] | numpy.ndarray[numpy.int32] | numpy.ndarray[numpy.uint64] | numpy.ndarray[numpy.int64] | numpy.ndarray[numpy.uint8] | numpy.ndarray[numpy.int8] | numpy.ndarray[numpy.uint16] | numpy.ndarray[numpy.int16], numpy.ndarray[numpy.float32] | numpy.ndarray[numpy.float64] | numpy.ndarray[numpy.uint32] | numpy.ndarray[numpy.int32] | numpy.ndarray[numpy.uint64] | numpy.ndarray[numpy.int64] | numpy.ndarray[numpy.uint8] | numpy.ndarray[numpy.int8] | numpy.ndarray[numpy.uint16] | numpy.ndarray[numpy.int16]]:
        """
        Copies at maximum the next `count` unread samples and clock-stamps to the `values` and `stamps` buffers. The amount actually read is returned through the `count` parameter.
        """
class IStreaming(IBaseObject):
    """
    Represents the client-side part of a streaming service responsible for initiating communication with the openDAQ device streaming server and processing the received data. Wraps the client-side implementation details of the particular data transfer protocol used by openDAQ to send processed/acquired data from devices running an openDAQ Server to an openDAQ Client.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IStreaming:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IStreaming:
        ...
    def add_signals(self, signals: IList) -> None:
        """
        Adds signals to the Streaming.
        """
    def remove_all_signals(self) -> None:
        """
        Removes all added signals from the Streaming.
        """
    def remove_signals(self, signals: IList) -> None:
        """
        Removes signals from the Streaming.
        """
    @property
    def active(self) -> int:
        """
        Gets the active state of the Streaming. / Sets the Streaming to be either active or inactive.
        """
    @active.setter
    def active(self, arg1: bool) -> None:
        ...
    @property
    def connection_string(self) -> str:
        """
        Gets the string representation of a connection address used to connect to the streaming service of the device.
        """
class IString(IBaseObject):
    """
    Represents string variable as `IString` interface. Use this interface to wrap string variable when you need to add the variable to lists, dictionaries and other containers which accept `IBaseObject` and derived interfaces.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IString:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IString:
        ...
    @property
    def length(self) -> int:
        """
        Gets length of string.
        """
class IStruct(IBaseObject):
    """
    Structs are immutable objects that contain a set of key-value pairs. The key, as well as the types of each associated value for each struct are defined in advance within a Struct type that has the same name as the Struct.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IStruct:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IStruct:
        ...
    def __delattr__(self, name: str) -> None:
        """
        Deletes the field with the given name.
        """
    def __getattr__(self, name: str) -> typing.Any:
        """
        Gets the value of a field with the given name.
        """
    def __setattr__(self, name: str, value: typing.Any) -> None:
        """
        Sets the value of a field with the given name.
        """
    def get(self, name: str) -> typing.Any:
        """
        Gets the value of a field with the given name.
        """
    def has_field(self, name: str) -> int:
        """
        Checks whether a field with the given name exists in the Struct
        """
    @property
    def as_dictionary(self) -> IDict:
        """
        Gets the field names and values of the Struct as a Dictionary.
        """
    @property
    def field_names(self) -> IList:
        """
        Gets a list of all Struct field names.
        """
    @property
    def field_values(self) -> IList:
        """
        Gets a list of all Struct field values.
        """
    @property
    def struct_type(self) -> IStructType:
        """
        Gets the Struct's type.
        """
class IStructBuilder(IBaseObject):
    """
    Builder component of Struct objects. Contains setter methods to configure the Struct parameters, and a `build` method that builds the Struct object.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IStructBuilder:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IStructBuilder:
        ...
    def build(self) -> IStruct:
        """
        Builds and returns a Struct object using the currently set values of the Builder.
        """
    def get(self, name: str) -> typing.Any:
        """
        Gets the value of a field with the given name.
        """
    def has_field(self, name: str) -> int:
        """
        Checks whether a field with the given name exists in the Struct
        """
    def set(self, name: str, field: typing.Any) -> None:
        """
        Sets the value of a field with the given name.
        """
    @property
    def as_dictionary(self) -> IDict:
        """
        Gets the field names and values of the Struct as a Dictionary.
        """
    @property
    def field_names(self) -> IList:
        """
        Gets a list of all Struct field names.
        """
    @property
    def field_values(self) -> IList:
        """
        Gets a list of all Struct field values. / Gets a list of all Struct field values.
        """
    @field_values.setter
    def field_values(self, arg1: IList) -> None:
        ...
    @property
    def struct_type(self) -> IStructType:
        """
        Gets the Struct's type.
        """
class IStructType(IType):
    """
    Struct types define the fields (names and value types, as well as optional default values) of Structs with a name matching that of the Struct type.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IStructType:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IStructType:
        ...
    @property
    def field_default_values(self) -> IList:
        """
        Gets the list of field default values.
        """
    @property
    def field_names(self) -> IList:
        """
        Gets the list of field names.
        """
    @property
    def field_types(self) -> IList:
        """
        Gets the list of field types.
        """
class ISubscriptionEventArgs(IEventArgs):
    """
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> ISubscriptionEventArgs:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> ISubscriptionEventArgs:
        ...
    @property
    def streaming_connection_string(self) -> str:
        ...
    @property
    def subscription_event_type(self) -> SubscriptionEventType:
        ...
class ITags(IBaseObject):
    """
    List of string tags. Provides helpers to get and search the list of tags.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> ITags:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> ITags:
        ...
    def contains(self, name: str) -> int:
        """
        Checks whether a tag is present in the list of tags.
        """
    def query(self, query: str) -> int:
        """
        Queries the list of tags, creating an EvalValue expression from the `query` string. Returns true if the list of tags matches the query, false otherwise.
        """
    @property
    def list(self) -> IList:
        """
        Gets the list of all tags in the list.
        """
class ITagsPrivate(IBaseObject):
    """
    Private interface to component tags. Allows for adding/removing tags.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> ITagsPrivate:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> ITagsPrivate:
        ...
    def add(self, name: str) -> None:
        """
        Adds a new tag to the list.
        """
    def remove(self, name: str) -> None:
        """
        Removes a new tag from the list.
        """
    def replace(self, tags: IList) -> None:
        """
        Replaces all tags.
        """
class ITailReader(ISampleReader):
    """
    A reader that only ever reads the last N samples, subsequent calls may result in overlapping data.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> ITailReader:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> ITailReader:
        ...
    def read(self, count: int) -> numpy.ndarray[numpy.float32] | numpy.ndarray[numpy.float64] | numpy.ndarray[numpy.uint32] | numpy.ndarray[numpy.int32] | numpy.ndarray[numpy.uint64] | numpy.ndarray[numpy.int64] | numpy.ndarray[numpy.uint8] | numpy.ndarray[numpy.int8] | numpy.ndarray[numpy.uint16] | numpy.ndarray[numpy.int16]:
        """
        Copies at maximum the next `count` unread samples to the values buffer. The amount actually read is returned through the `count` parameter.
        """
    def read_with_domain(self, count: int) -> tuple[numpy.ndarray[numpy.float32] | numpy.ndarray[numpy.float64] | numpy.ndarray[numpy.uint32] | numpy.ndarray[numpy.int32] | numpy.ndarray[numpy.uint64] | numpy.ndarray[numpy.int64] | numpy.ndarray[numpy.uint8] | numpy.ndarray[numpy.int8] | numpy.ndarray[numpy.uint16] | numpy.ndarray[numpy.int16], numpy.ndarray[numpy.float32] | numpy.ndarray[numpy.float64] | numpy.ndarray[numpy.uint32] | numpy.ndarray[numpy.int32] | numpy.ndarray[numpy.uint64] | numpy.ndarray[numpy.int64] | numpy.ndarray[numpy.uint8] | numpy.ndarray[numpy.int8] | numpy.ndarray[numpy.uint16] | numpy.ndarray[numpy.int16]]:
        """
        Copies at maximum the next `count` unread samples and clock-stamps to the `values` and `stamps` buffers. The amount actually read is returned through the `count` parameter.
        """
    @property
    def history_size(self) -> int:
        """
        The maximum amount of samples in history to keep.
        """
class ITask(IBaseObject):
    """
    A packaged callback with possible continuations and dependencies that can be arranged in a dependency graph (directed acyclic graph). The task is not executed directly but only when the graph is scheduled for execution and all dependencies have been satisfied.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> ITask:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> ITask:
        ...
    def then(self, continuation: ITask) -> None:
        """
        Sets the continuation to only execute after this task completes. Be careful of forming cycles as tasks whose dependencies cannot be satisfied will never execute.
        """
    @property
    def name(self) -> str:
        """
        Gets the task name. / Sets the task name that is used in diagnostics.
        """
    @name.setter
    def name(self, arg1: str) -> None:
        ...
class ITaskGraph(ITask):
    """
    A dependency graph (directed acyclic graph) of tasks that can be scheduled for execution on a Scheduler.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> ITaskGraph:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> ITaskGraph:
        ...
class IType(IBaseObject):
    """
    The base object type that is inherited by all Types (eg. Struct type, Simple type, Property object class) in openDAQ.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IType:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IType:
        ...
    @property
    def name(self) -> str:
        """
        Gets the name of the Type
        """
class ITypeManager(IBaseObject):
    """
    Container for Type objects. The Type manager is used when creating certain types of objects (eg. Structs and Property object classes). The Types stored within the manager contain pre-defined fields, as well as constraints specifying how objects should look.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> ITypeManager:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> ITypeManager:
        ...
    def add_type(self, type: IType) -> None:
        """
        Adds a type to the manager.
        """
    def get_type(self, type_name: str) -> IType | IEnumerationType:
        """
        Gets an added Type by name.
        """
    def has_type(self, type_name: str) -> int:
        """
        Checks if a type with the specified name is already added.
        """
    def remove_type(self, type_name: str) -> None:
        """
        Removes the type from the manager.
        """
    @property
    def types(self) -> IList:
        """
        Gets a list of all added Types.
        """
class IUnit(IBaseObject):
    """
    Describes a measurement unit with IDs as defined in <a href="https://unece.org/trade/cefact/UNLOCODE-Download">Codes for Units of Measurement used in International Trade</a>.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IUnit:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IUnit:
        ...
    @property
    def id(self) -> int:
        """
        Gets the unit ID as defined in <a href="https://unece.org/trade/cefact/UNLOCODE-Download">Codes for Units of Measurement used in International Trade</a>.
        """
    @property
    def name(self) -> str:
        """
        Gets the full name of the unit, i.e. "meters per second".
        """
    @property
    def quantity(self) -> str:
        """
        Gets the quantity represented by the unit, i.e. "Velocity"
        """
    @property
    def symbol(self) -> str:
        """
        Gets the symbol of the unit, i.e. "m/s".
        """
class IUnitBuilder(IBaseObject):
    """
    Builder component of Unit objects. Contains setter methods to configure the Unit parameters, and a `build` method that builds the Unit object.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IUnitBuilder:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IUnitBuilder:
        ...
    def build(self) -> IUnit:
        """
        Builds and returns a Unit object using the currently set values of the Builder.
        """
    @property
    def id(self) -> int:
        """
        Gets the unit ID as defined in <a href="https://unece.org/trade/cefact/UNLOCODE-Download">Codes for Units of Measurement used in International Trade</a>. / Sets the unit ID as defined in <a href="https://unece.org/trade/cefact/UNLOCODE-Download">Codes for Units of Measurement used in International Trade</a>.
        """
    @id.setter
    def id(self, arg1: int) -> None:
        ...
    @property
    def name(self) -> str:
        """
        Gets the full name of the unit, i.e. "meters per second". / Sets the full name of the unit, i.e. "meters per second".
        """
    @name.setter
    def name(self, arg1: str) -> None:
        ...
    @property
    def quantity(self) -> str:
        """
        Gets the quantity represented by the unit, i.e. "Velocity" / Sets the quantity represented by the unit, i.e. "Velocity"
        """
    @quantity.setter
    def quantity(self, arg1: str) -> None:
        ...
    @property
    def symbol(self) -> str:
        """
        Gets the symbol of the unit, i.e. "m/s". / Sets the symbol of the unit, i.e. "m/s".
        """
    @symbol.setter
    def symbol(self, arg1: str) -> None:
        ...
class IValidator(IBaseObject):
    """
    Used by openDAQ properties to validate whether a value fits the value restrictions of the Property.
    """
    @staticmethod
    def can_cast_from(arg0: IBaseObject) -> bool:
        ...
    @staticmethod
    def cast_from(arg0: IBaseObject) -> IValidator:
        ...
    @staticmethod
    def convert_from(arg0: IBaseObject) -> IValidator:
        ...
    def validate(self, prop_obj: typing.Any, value: typing.Any) -> None:
        """
        Checks whether `value` adheres to the validity conditions of the validator.
        """
    @property
    def eval(self) -> str:
        """
        Gets the string expression used when creating the validator.
        """
class LogLevel:
    """
    Members:
    
      Trace
    
      Debug
    
      Info
    
      Warn
    
      Error
    
      Critical
    
      Off
    
      Default
    """
    Critical: typing.ClassVar[LogLevel]  # value = <LogLevel.Critical: 5>
    Debug: typing.ClassVar[LogLevel]  # value = <LogLevel.Debug: 1>
    Default: typing.ClassVar[LogLevel]  # value = <LogLevel.Default: 7>
    Error: typing.ClassVar[LogLevel]  # value = <LogLevel.Error: 4>
    Info: typing.ClassVar[LogLevel]  # value = <LogLevel.Info: 2>
    Off: typing.ClassVar[LogLevel]  # value = <LogLevel.Off: 6>
    Trace: typing.ClassVar[LogLevel]  # value = <LogLevel.Trace: 0>
    Warn: typing.ClassVar[LogLevel]  # value = <LogLevel.Warn: 3>
    __members__: typing.ClassVar[dict[str, LogLevel]]  # value = {'Trace': <LogLevel.Trace: 0>, 'Debug': <LogLevel.Debug: 1>, 'Info': <LogLevel.Info: 2>, 'Warn': <LogLevel.Warn: 3>, 'Error': <LogLevel.Error: 4>, 'Critical': <LogLevel.Critical: 5>, 'Off': <LogLevel.Off: 6>, 'Default': <LogLevel.Default: 7>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MockSignal:
    """
    A mock signal that can be used for testing purposes.
    """
    def __init__(self) -> None:
        """
        Constructs a mock signal.
        """
    def add_data(self, data: numpy.ndarray[numpy.float64]) -> None:
        """
        Adds the given data to the signal.
        """
    @property
    def domain_signal(self) -> ISignalConfig:
        """
        The domain signal.
        """
    @property
    def signal(self) -> ISignalConfig:
        """
        The value signal.
        """
class PacketReadyNotification:
    """
    Members:
    
      None
    
      SameThread
    
      Scheduler
    """
    None: typing.ClassVar[PacketReadyNotification]  # value = <PacketReadyNotification.None: 0>
    SameThread: typing.ClassVar[PacketReadyNotification]  # value = <PacketReadyNotification.SameThread: 1>
    Scheduler: typing.ClassVar[PacketReadyNotification]  # value = <PacketReadyNotification.Scheduler: 2>
    __members__: typing.ClassVar[dict[str, PacketReadyNotification]]  # value = {'None': <PacketReadyNotification.None: 0>, 'SameThread': <PacketReadyNotification.SameThread: 1>, 'Scheduler': <PacketReadyNotification.Scheduler: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class PacketType:
    """
    Members:
    
      None
    
      Data
    
      Event
    """
    Data: typing.ClassVar[PacketType]  # value = <PacketType.Data: 1>
    Event: typing.ClassVar[PacketType]  # value = <PacketType.Event: 2>
    None: typing.ClassVar[PacketType]  # value = <PacketType.None: 0>
    __members__: typing.ClassVar[dict[str, PacketType]]  # value = {'None': <PacketType.None: 0>, 'Data': <PacketType.Data: 1>, 'Event': <PacketType.Event: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class PropertyEventType:
    """
    Members:
    
      Update
    
      Clear
    
      Read
    """
    Clear: typing.ClassVar[PropertyEventType]  # value = <PropertyEventType.Clear: 1>
    Read: typing.ClassVar[PropertyEventType]  # value = <PropertyEventType.Read: 2>
    Update: typing.ClassVar[PropertyEventType]  # value = <PropertyEventType.Update: 0>
    __members__: typing.ClassVar[dict[str, PropertyEventType]]  # value = {'Update': <PropertyEventType.Update: 0>, 'Clear': <PropertyEventType.Clear: 1>, 'Read': <PropertyEventType.Read: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ProtocolType:
    """
    Members:
    
      Configuration
    
      Streaming
    
      ConfigurationAndStreaming
    
      Unknown
    """
    Configuration: typing.ClassVar[ProtocolType]  # value = <ProtocolType.Configuration: 1>
    ConfigurationAndStreaming: typing.ClassVar[ProtocolType]  # value = <ProtocolType.ConfigurationAndStreaming: 3>
    Streaming: typing.ClassVar[ProtocolType]  # value = <ProtocolType.Streaming: 2>
    Unknown: typing.ClassVar[ProtocolType]  # value = <ProtocolType.Unknown: 0>
    __members__: typing.ClassVar[dict[str, ProtocolType]]  # value = {'Configuration': <ProtocolType.Configuration: 1>, 'Streaming': <ProtocolType.Streaming: 2>, 'ConfigurationAndStreaming': <ProtocolType.ConfigurationAndStreaming: 3>, 'Unknown': <ProtocolType.Unknown: 0>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ReadMode:
    """
    Members:
    
      Unscaled
    
      Scaled
    
      RawValue
    """
    RawValue: typing.ClassVar[ReadMode]  # value = <ReadMode.RawValue: 2>
    Scaled: typing.ClassVar[ReadMode]  # value = <ReadMode.Scaled: 1>
    Unscaled: typing.ClassVar[ReadMode]  # value = <ReadMode.Unscaled: 0>
    __members__: typing.ClassVar[dict[str, ReadMode]]  # value = {'Unscaled': <ReadMode.Unscaled: 0>, 'Scaled': <ReadMode.Scaled: 1>, 'RawValue': <ReadMode.RawValue: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ReadStatus:
    """
    Members:
    
      Ok
    
      Event
    
      Fail
    
      Unknown
    """
    Event: typing.ClassVar[ReadStatus]  # value = <ReadStatus.Event: 1>
    Fail: typing.ClassVar[ReadStatus]  # value = <ReadStatus.Fail: 2>
    Ok: typing.ClassVar[ReadStatus]  # value = <ReadStatus.Ok: 0>
    Unknown: typing.ClassVar[ReadStatus]  # value = <ReadStatus.Unknown: 65535>
    __members__: typing.ClassVar[dict[str, ReadStatus]]  # value = {'Ok': <ReadStatus.Ok: 0>, 'Event': <ReadStatus.Event: 1>, 'Fail': <ReadStatus.Fail: 2>, 'Unknown': <ReadStatus.Unknown: 65535>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ReadTimeoutType:
    """
    Members:
    
      Any
    
      All
    """
    All: typing.ClassVar[ReadTimeoutType]  # value = <ReadTimeoutType.All: 1>
    Any: typing.ClassVar[ReadTimeoutType]  # value = <ReadTimeoutType.Any: 0>
    __members__: typing.ClassVar[dict[str, ReadTimeoutType]]  # value = {'Any': <ReadTimeoutType.Any: 0>, 'All': <ReadTimeoutType.All: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SampleType:
    """
    Members:
    
      Invalid
    
      Undefined
    
      Float32
    
      Float64
    
      UInt8
    
      Int8
    
      UInt16
    
      Int16
    
      UInt32
    
      Int32
    
      UInt64
    
      Int64
    
      RangeInt64
    
      ComplexFloat32
    
      ComplexFloat64
    
      Binary
    
      String
    """
    Binary: typing.ClassVar[SampleType]  # value = <SampleType.Binary: 14>
    ComplexFloat32: typing.ClassVar[SampleType]  # value = <SampleType.ComplexFloat32: 12>
    ComplexFloat64: typing.ClassVar[SampleType]  # value = <SampleType.ComplexFloat64: 13>
    Float32: typing.ClassVar[SampleType]  # value = <SampleType.Float32: 1>
    Float64: typing.ClassVar[SampleType]  # value = <SampleType.Float64: 2>
    Int16: typing.ClassVar[SampleType]  # value = <SampleType.Int16: 6>
    Int32: typing.ClassVar[SampleType]  # value = <SampleType.Int32: 8>
    Int64: typing.ClassVar[SampleType]  # value = <SampleType.Int64: 10>
    Int8: typing.ClassVar[SampleType]  # value = <SampleType.Int8: 4>
    Invalid: typing.ClassVar[SampleType]  # value = <SampleType.Invalid: 0>
    RangeInt64: typing.ClassVar[SampleType]  # value = <SampleType.RangeInt64: 11>
    String: typing.ClassVar[SampleType]  # value = <SampleType.String: 15>
    UInt16: typing.ClassVar[SampleType]  # value = <SampleType.UInt16: 5>
    UInt32: typing.ClassVar[SampleType]  # value = <SampleType.UInt32: 7>
    UInt64: typing.ClassVar[SampleType]  # value = <SampleType.UInt64: 9>
    UInt8: typing.ClassVar[SampleType]  # value = <SampleType.UInt8: 3>
    Undefined: typing.ClassVar[SampleType]  # value = <SampleType.Invalid: 0>
    __members__: typing.ClassVar[dict[str, SampleType]]  # value = {'Invalid': <SampleType.Invalid: 0>, 'Undefined': <SampleType.Invalid: 0>, 'Float32': <SampleType.Float32: 1>, 'Float64': <SampleType.Float64: 2>, 'UInt8': <SampleType.UInt8: 3>, 'Int8': <SampleType.Int8: 4>, 'UInt16': <SampleType.UInt16: 5>, 'Int16': <SampleType.Int16: 6>, 'UInt32': <SampleType.UInt32: 7>, 'Int32': <SampleType.Int32: 8>, 'UInt64': <SampleType.UInt64: 9>, 'Int64': <SampleType.Int64: 10>, 'RangeInt64': <SampleType.RangeInt64: 11>, 'ComplexFloat32': <SampleType.ComplexFloat32: 12>, 'ComplexFloat64': <SampleType.ComplexFloat64: 13>, 'Binary': <SampleType.Binary: 14>, 'String': <SampleType.String: 15>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ScaledSampleType:
    """
    Members:
    
      Invalid
    
      Float32
    
      Float64
    """
    Float32: typing.ClassVar[ScaledSampleType]  # value = <ScaledSampleType.Float32: 1>
    Float64: typing.ClassVar[ScaledSampleType]  # value = <ScaledSampleType.Float64: 2>
    Invalid: typing.ClassVar[ScaledSampleType]  # value = <ScaledSampleType.Invalid: 0>
    __members__: typing.ClassVar[dict[str, ScaledSampleType]]  # value = {'Invalid': <ScaledSampleType.Invalid: 0>, 'Float32': <ScaledSampleType.Float32: 1>, 'Float64': <ScaledSampleType.Float64: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ScalingType:
    """
    Members:
    
      Other
    
      Linear
    """
    Linear: typing.ClassVar[ScalingType]  # value = <ScalingType.Linear: 1>
    Other: typing.ClassVar[ScalingType]  # value = <ScalingType.Other: 0>
    __members__: typing.ClassVar[dict[str, ScalingType]]  # value = {'Other': <ScalingType.Other: 0>, 'Linear': <ScalingType.Linear: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SubscriptionEventType:
    """
    Members:
    
      Subscribed
    
      Unsubscribed
    """
    Subscribed: typing.ClassVar[SubscriptionEventType]  # value = <SubscriptionEventType.Subscribed: 0>
    Unsubscribed: typing.ClassVar[SubscriptionEventType]  # value = <SubscriptionEventType.Unsubscribed: 1>
    __members__: typing.ClassVar[dict[str, SubscriptionEventType]]  # value = {'Subscribed': <SubscriptionEventType.Subscribed: 0>, 'Unsubscribed': <SubscriptionEventType.Unsubscribed: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class TimeBlockReader:
    """
    A wrapper for block signal data reader that provides the ability to read samples with timestamps.
    """
    def __init__(self, arg0: IBlockReader) -> None:
        ...
    def read_with_timestamps(self, count: int, timeout_ms: int = 0) -> tuple[numpy.ndarray[numpy.float32] | numpy.ndarray[numpy.float64] | numpy.ndarray[numpy.uint32] | numpy.ndarray[numpy.int32] | numpy.ndarray[numpy.uint64] | numpy.ndarray[numpy.int64] | numpy.ndarray[numpy.uint8] | numpy.ndarray[numpy.int8] | numpy.ndarray[numpy.uint16] | numpy.ndarray[numpy.int16], numpy.ndarray[numpy.float32] | numpy.ndarray[numpy.float64] | numpy.ndarray[numpy.uint32] | numpy.ndarray[numpy.int32] | numpy.ndarray[numpy.uint64] | numpy.ndarray[numpy.int64] | numpy.ndarray[numpy.uint8] | numpy.ndarray[numpy.int8] | numpy.ndarray[numpy.uint16] | numpy.ndarray[numpy.int16]]:
        """
        Copies at maximum the next `count` unread samples and clock-stamps to the `values` and `stamps` buffers. The amount actually read is returned through the `count` parameter.
        """
class TimeStreamReader:
    """
    A wrapper for stream signal data reader that provides the ability to read samples with timestamps.
    """
    def __init__(self, arg0: IStreamReader) -> None:
        ...
    def read_with_timestamps(self, count: int, timeout_ms: int = 0) -> tuple[numpy.ndarray[numpy.float32] | numpy.ndarray[numpy.float64] | numpy.ndarray[numpy.uint32] | numpy.ndarray[numpy.int32] | numpy.ndarray[numpy.uint64] | numpy.ndarray[numpy.int64] | numpy.ndarray[numpy.uint8] | numpy.ndarray[numpy.int8] | numpy.ndarray[numpy.uint16] | numpy.ndarray[numpy.int16], numpy.ndarray[numpy.float32] | numpy.ndarray[numpy.float64] | numpy.ndarray[numpy.uint32] | numpy.ndarray[numpy.int32] | numpy.ndarray[numpy.uint64] | numpy.ndarray[numpy.int64] | numpy.ndarray[numpy.uint8] | numpy.ndarray[numpy.int8] | numpy.ndarray[numpy.uint16] | numpy.ndarray[numpy.int16]]:
        """
        Copies at maximum the next `count` unread samples and clock-stamps to the `values` and `stamps` buffers. The amount actually read is returned through the `count` parameter.
        """
class TimeTailReader:
    """
    A wrapper for tail signal data reader that provides the ability to read samples with timestamps.
    """
    def __init__(self, arg0: ITailReader) -> None:
        ...
    def read_with_timestamps(self, count: int, timeout_ms: int = 0) -> tuple[numpy.ndarray[numpy.float32] | numpy.ndarray[numpy.float64] | numpy.ndarray[numpy.uint32] | numpy.ndarray[numpy.int32] | numpy.ndarray[numpy.uint64] | numpy.ndarray[numpy.int64] | numpy.ndarray[numpy.uint8] | numpy.ndarray[numpy.int8] | numpy.ndarray[numpy.uint16] | numpy.ndarray[numpy.int16], numpy.ndarray[numpy.float32] | numpy.ndarray[numpy.float64] | numpy.ndarray[numpy.uint32] | numpy.ndarray[numpy.int32] | numpy.ndarray[numpy.uint64] | numpy.ndarray[numpy.int64] | numpy.ndarray[numpy.uint8] | numpy.ndarray[numpy.int8] | numpy.ndarray[numpy.uint16] | numpy.ndarray[numpy.int16]]:
        """
        Copies at maximum the next `count` unread samples and clock-stamps to the `values` and `stamps` buffers. The amount actually read is returned through the `count` parameter.
        """
def AndSearchFilter(arg0: ISearchFilter, arg1: ISearchFilter) -> ISearchFilter:
    ...
def AnySearchFilter() -> ISearchFilter:
    ...
def ArgumentInfo(arg0: IString, arg1: CoreType) -> IArgumentInfo:
    ...
def BaseObject() -> IBaseObject:
    ...
def BasicFileLoggerSink(arg0: IString) -> ILoggerSink:
    ...
def BlockReader(signal: ISignal, block_size: int, value_type: SampleType = ..., domain_type: SampleType = ...) -> IBlockReader:
    ...
def BlockReaderFromExisting(arg0: IBlockReader, arg1: SampleType, arg2: SampleType, arg3: int) -> IBlockReader:
    ...
def BlockReaderStatus(arg0: IEventPacket, arg1: int, arg2: int) -> IBlockReaderStatus:
    ...
def BoolProperty(arg0: IString, arg1: IBoolean, arg2: IBoolean) -> IProperty:
    ...
def BoolPropertyBuilder(arg0: IString, arg1: IBoolean) -> IPropertyBuilder:
    ...
def Boolean(value: bool) -> IBoolean:
    """
    Creates a new Boolean.
    """
def CallableInfo(arg0: IList, arg1: CoreType) -> ICallableInfo:
    ...
def Client(arg0: IContext, arg1: IString, arg2: IDeviceInfo, arg3: IComponent) -> IDevice:
    ...
def CmdLineArgsConfigProvider(arg0: IList) -> IConfigProvider:
    ...
def Coercer(arg0: IString) -> ICoercer:
    ...
@typing.overload
def ComplexNumber(real: float, imaginary: float) -> IComplexNumber:
    """
    Creates a new ComplexNumber object.
    """
@typing.overload
def ComplexNumber(value: complex) -> IComplexNumber:
    """
    Creates a new ComplexNumber object.
    """
def Component(arg0: IContext, arg1: IComponent, arg2: IString, arg3: IString) -> IComponent:
    ...
def ComponentStatusContainer() -> IComponentStatusContainer:
    ...
def Connection(arg0: IInputPort, arg1: ISignal, arg2: IContext) -> IConnection:
    ...
def ConstantDataRule() -> IDataRule:
    ...
def Context(arg0: IScheduler, arg1: ILogger, arg2: ITypeManager, arg3: IModuleManager, arg4: IDict) -> IContext:
    ...
def CustomSearchFilter(arg0: IFunction, arg1: IFunction) -> ISearchFilter:
    ...
def DataDescriptorBuilder() -> IDataDescriptorBuilder:
    ...
def DataDescriptorBuilderFromExisting(arg0: IDataDescriptor) -> IDataDescriptorBuilder:
    ...
def DataDescriptorChangedEventPacket(arg0: IDataDescriptor, arg1: IDataDescriptor) -> IEventPacket:
    ...
def DataDescriptorFromBuilder(arg0: IDataDescriptorBuilder) -> IDataDescriptor:
    ...
def DataPacket(arg0: IDataDescriptor, arg1: int, arg2: INumber) -> IDataPacket:
    ...
def DataPacketWithDomain(arg0: IDataPacket, arg1: IDataDescriptor, arg2: int, arg3: INumber) -> IDataPacket:
    ...
def DataRule(arg0: DataRuleType, arg1: IDict) -> IDataRule:
    ...
def DataRuleBuilder() -> IDataRuleBuilder:
    ...
def DataRuleBuilderFromExisting(arg0: IDataRule) -> IDataRuleBuilder:
    ...
def DataRuleFromBuilder(arg0: IDataRuleBuilder) -> IDataRule:
    ...
def DeviceDomain(arg0: IRatio, arg1: IString, arg2: IUnit) -> IDeviceDomain:
    ...
def DeviceInfoConfig(arg0: IString, arg1: IString) -> IDeviceInfoConfig:
    ...
def DeviceInfoConfigWithCustomSdkVersion(arg0: IString, arg1: IString, arg2: IString) -> IDeviceInfoConfig:
    ...
def DeviceType(arg0: IString, arg1: IString, arg2: IString, arg3: IFunction) -> IDeviceType:
    ...
def Dict() -> IDict:
    ...
def DictProperty(arg0: IString, arg1: IDict, arg2: IBoolean) -> IProperty:
    ...
def DictPropertyBuilder(arg0: IString, arg1: IDict) -> IPropertyBuilder:
    ...
def Dimension(arg0: IDimensionRule, arg1: IUnit, arg2: IString) -> IDimension:
    ...
def DimensionBuilder() -> IDimensionBuilder:
    ...
def DimensionBuilderFromExisting(arg0: IDimension) -> IDimensionBuilder:
    ...
def DimensionFromBuilder(arg0: IDimensionBuilder) -> IDimension:
    ...
def DimensionRule(arg0: DimensionRuleType, arg1: IDict) -> IDimensionRule:
    ...
def DimensionRuleBuilder() -> IDimensionRuleBuilder:
    ...
def DimensionRuleBuilderFromExisting(arg0: IDimensionRule) -> IDimensionRuleBuilder:
    ...
def DimensionRuleFromBuilder(arg0: IDimensionRuleBuilder) -> IDimensionRule:
    ...
def Enumeration(arg0: IString, arg1: IString, arg2: ITypeManager) -> IEnumeration:
    ...
def EnumerationProperty(arg0: IString, arg1: IEnumeration, arg2: IBoolean) -> IProperty:
    ...
def EnumerationPropertyBuilder(arg0: IString, arg1: IEnumeration) -> IPropertyBuilder:
    ...
def EnumerationType(arg0: IString, arg1: IList, arg2: int) -> IEnumerationType:
    ...
def EnumerationTypeWithValues(arg0: IString, arg1: IDict) -> IEnumerationType:
    ...
def EnumerationWithType(arg0: IEnumerationType, arg1: IString) -> IEnumeration:
    ...
def EnvConfigProvider() -> IConfigProvider:
    ...
def EvalValue(arg0: IString) -> IEvalValue:
    ...
def EvalValueArgs(arg0: IString, arg1: IList) -> IEvalValue:
    ...
def EvalValueFunc(arg0: IString, arg1: IFunction) -> IEvalValue:
    ...
def EventArgs(arg0: int, arg1: IString) -> IEventArgs:
    ...
def EventPacket(arg0: IString, arg1: IDict) -> IEventPacket:
    ...
def ExcludedTagsSearchFilter(arg0: IList) -> ISearchFilter:
    ...
def ExplicitDataRule() -> IDataRule:
    ...
def ExplicitDomainDataRule(arg0: INumber, arg1: INumber) -> IDataRule:
    ...
def ExternalAllocator(arg0: capsule, arg1: ...) -> IAllocator:
    ...
def Float(arg0: float) -> IFloat:
    ...
def FloatProperty(arg0: IString, arg1: IFloat, arg2: IBoolean) -> IProperty:
    ...
def FloatPropertyBuilder(arg0: IString, arg1: IFloat) -> IPropertyBuilder:
    ...
def Folder(arg0: IContext, arg1: IComponent, arg2: IString) -> IFolderConfig:
    ...
def FolderWithItemType(arg0: ..., arg1: IContext, arg2: IComponent, arg3: IString) -> IFolderConfig:
    ...
def Function(arg0: typing.Any) -> IFunction:
    ...
def FunctionBlockType(arg0: IString, arg1: IString, arg2: IString, arg3: IFunction) -> IFunctionBlockType:
    ...
def FunctionProperty(arg0: IString, arg1: ICallableInfo, arg2: IBoolean) -> IProperty:
    ...
def FunctionPropertyBuilder(arg0: IString, arg1: ICallableInfo) -> IPropertyBuilder:
    ...
def InputPort(arg0: IContext, arg1: IComponent, arg2: IString) -> IInputPortConfig:
    ...
@typing.overload
def Instance(arg0: IContext, arg1: IString) -> IInstance:
    ...
@typing.overload
def Instance() -> IInstance:
    ...
def InstanceBuilder() -> IInstanceBuilder:
    ...
def InstanceFromBuilder(arg0: IInstanceBuilder) -> IInstance:
    ...
def IntProperty(arg0: IString, arg1: IInteger, arg2: IBoolean) -> IProperty:
    ...
def IntPropertyBuilder(arg0: IString, arg1: IInteger) -> IPropertyBuilder:
    ...
def Integer(arg0: int) -> IInteger:
    ...
def InterfaceIdSearchFilter(arg0: ...) -> ISearchFilter:
    ...
def IoFolder(arg0: IContext, arg1: IComponent, arg2: IString) -> IFolderConfig:
    ...
def JsonConfigProvider(arg0: IString) -> IConfigProvider:
    ...
def LinearDataRule(arg0: INumber, arg1: INumber) -> IDataRule:
    ...
def LinearDimensionRule(arg0: INumber, arg1: INumber, arg2: int) -> IDimensionRule:
    ...
def LinearScaling(arg0: INumber, arg1: INumber, arg2: SampleType, arg3: ScaledSampleType) -> IScaling:
    ...
def List() -> IList:
    ...
def ListDimensionRule(arg0: IList) -> IDimensionRule:
    ...
def ListProperty(arg0: IString, arg1: IList, arg2: IBoolean) -> IProperty:
    ...
def ListPropertyBuilder(arg0: IString, arg1: IList) -> IPropertyBuilder:
    ...
def LocalIdSearchFilter(arg0: IString) -> ISearchFilter:
    ...
def LogarithmicDimensionRule(arg0: INumber, arg1: INumber, arg2: INumber, arg3: int) -> IDimensionRule:
    ...
def Logger(arg0: IList, arg1: LogLevel) -> ILogger:
    ...
def LoggerComponent(arg0: IString, arg1: IList, arg2: ILoggerThreadPool, arg3: LogLevel) -> ILoggerComponent:
    ...
def LoggerThreadPool() -> ILoggerThreadPool:
    ...
def MallocAllocator() -> IAllocator:
    ...
def ModuleManager(arg0: IString) -> IModuleManager:
    ...
def ModuleManagerMultiplePaths(arg0: IList) -> IModuleManager:
    ...
def NotSearchFilter(arg0: ISearchFilter) -> ISearchFilter:
    ...
def ObjectProperty(arg0: IString, arg1: IPropertyObject) -> IProperty:
    ...
def ObjectPropertyBuilder(arg0: IString, arg1: IPropertyObject) -> IPropertyBuilder:
    ...
def OrSearchFilter(arg0: ISearchFilter, arg1: ISearchFilter) -> ISearchFilter:
    ...
def PacketReader(arg0: ISignal) -> IPacketReader:
    ...
def PacketReaderFromPort(arg0: IInputPortConfig) -> IPacketReader:
    ...
def Procedure(arg0: typing.Any) -> IProcedure:
    ...
def PropertyBuilder(arg0: IString) -> IPropertyBuilder:
    ...
def PropertyObject() -> IPropertyObject:
    ...
def PropertyObjectClassBuilder(arg0: IString) -> IPropertyObjectClassBuilder:
    ...
def PropertyObjectClassBuilderWithManager(arg0: ITypeManager, arg1: IString) -> IPropertyObjectClassBuilder:
    ...
def PropertyObjectClassFromBuilder(arg0: IPropertyObjectClassBuilder) -> IPropertyObjectClass:
    ...
def PropertyObjectWithClassAndManager(arg0: ITypeManager, arg1: IString) -> IPropertyObject:
    ...
def PropertyValueEventArgs(arg0: IProperty, arg1: IBaseObject, arg2: PropertyEventType, arg3: int) -> IPropertyValueEventArgs:
    ...
def Range(arg0: INumber, arg1: INumber) -> IRange:
    ...
def Ratio(numerator: int, denominator: int) -> IRatio:
    """
    Creates a new Ratio object.
    """
def RatioProperty(arg0: IString, arg1: IRatio, arg2: IBoolean) -> IProperty:
    ...
def RatioPropertyBuilder(arg0: IString, arg1: IRatio) -> IPropertyBuilder:
    ...
def ReaderStatus(arg0: IEventPacket, arg1: int) -> IReaderStatus:
    ...
def RecursiveSearchFilter(arg0: ISearchFilter) -> ISearchFilter:
    ...
def ReferenceProperty(arg0: IString, arg1: IEvalValue) -> IProperty:
    ...
def ReferencePropertyBuilder(arg0: IString, arg1: IEvalValue) -> IPropertyBuilder:
    ...
def RequiredTagsSearchFilter(arg0: IList) -> ISearchFilter:
    ...
def RotatingFileLoggerSink(arg0: IString, arg1: int, arg2: int) -> ILoggerSink:
    ...
def Scaling(arg0: SampleType, arg1: ScaledSampleType, arg2: ScalingType, arg3: IDict) -> IScaling:
    ...
def ScalingBuilder() -> IScalingBuilder:
    ...
def ScalingBuilderFromExisting(arg0: IScaling) -> IScalingBuilder:
    ...
def ScalingFromBuilder(arg0: IScalingBuilder) -> IScaling:
    ...
def Scheduler(arg0: ILogger, arg1: int) -> IScheduler:
    ...
def SelectionProperty(arg0: IString, arg1: IList, arg2: IInteger, arg3: IBoolean) -> IProperty:
    ...
def SelectionPropertyBuilder(arg0: IString, arg1: IList, arg2: IInteger) -> IPropertyBuilder:
    ...
def ServerType(arg0: IString, arg1: IString, arg2: IString, arg3: IFunction) -> IServerType:
    ...
def Signal(arg0: IContext, arg1: IComponent, arg2: IString, arg3: IString) -> ISignalConfig:
    ...
def SignalWithDescriptor(arg0: IContext, arg1: IDataDescriptor, arg2: IComponent, arg3: IString, arg4: IString) -> ISignalConfig:
    ...
def SimpleType(arg0: CoreType) -> ISimpleType:
    ...
def SparseSelectionProperty(arg0: IString, arg1: IDict, arg2: IInteger, arg3: IBoolean) -> IProperty:
    ...
def SparseSelectionPropertyBuilder(arg0: IString, arg1: IDict, arg2: IInteger) -> IPropertyBuilder:
    ...
def StdErrLoggerSink() -> ILoggerSink:
    ...
def StdOutLoggerSink() -> ILoggerSink:
    ...
def StreamReader(signal: ISignal, value_type: SampleType = ..., domain_type: SampleType = ..., timeout_type: ReadTimeoutType = ...) -> IStreamReader:
    ...
def StreamReaderFromExisting(arg0: IStreamReader, arg1: SampleType, arg2: SampleType) -> IStreamReader:
    ...
def String(arg0: str) -> IString:
    ...
def StringProperty(arg0: IString, arg1: IString, arg2: IBoolean) -> IProperty:
    ...
def StringPropertyBuilder(arg0: IString, arg1: IString) -> IPropertyBuilder:
    ...
def Struct(arg0: IString, arg1: IDict, arg2: ITypeManager) -> IStruct:
    ...
def StructBuilder(arg0: IString, arg1: ITypeManager) -> IStructBuilder:
    ...
def StructBuilderFromStruct(arg0: IStruct) -> IStructBuilder:
    ...
def StructFromBuilder(arg0: IStructBuilder) -> IStruct:
    ...
def StructProperty(arg0: IString, arg1: IStruct, arg2: IBoolean) -> IProperty:
    ...
def StructPropertyBuilder(arg0: IString, arg1: IStruct) -> IPropertyBuilder:
    ...
def StructType(arg0: IString, arg1: IList, arg2: IList, arg3: IList) -> IStructType:
    ...
def StructTypeNoDefaults(arg0: IString, arg1: IList, arg2: IList) -> IStructType:
    ...
def SubscriptionEventArgs(arg0: IString, arg1: SubscriptionEventType) -> ISubscriptionEventArgs:
    ...
def Tags() -> ITags:
    ...
def TailReader(signal: ISignal, history_size: int, value_type: SampleType = ..., domain_type: SampleType = ...) -> ITailReader:
    """
    A reader that only ever reads the last N samples, subsequent calls may result in overlapping data.
    """
def TailReaderFromExisting(arg0: ITailReader, arg1: int, arg2: SampleType, arg3: SampleType) -> ITailReader:
    ...
def Task(arg0: IProcedure, arg1: IString) -> ITask:
    ...
def TaskGraph(arg0: IProcedure, arg1: IString) -> ITaskGraph:
    ...
def TypeManager() -> ITypeManager:
    ...
def Unit(arg0: int, arg1: IString, arg2: IString, arg3: IString) -> IUnit:
    ...
def UnitBuilder() -> IUnitBuilder:
    ...
def UnitBuilderFromExisting(arg0: IUnit) -> IUnitBuilder:
    ...
def Validator(arg0: IString) -> IValidator:
    ...
def VisibleSearchFilter() -> ISearchFilter:
    ...
def WinDebugLoggerSink() -> ILoggerSink:
    ...
def clear_error_info() -> None:
    ...
def get_tracked_object_count() -> int:
    ...
def print_tracked_objects() -> None:
    ...
