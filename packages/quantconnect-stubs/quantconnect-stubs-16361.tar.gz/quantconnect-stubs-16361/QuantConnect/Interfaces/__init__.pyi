from typing import overload
import abc
import typing

import QuantConnect.Api
import QuantConnect.Interfaces
import QuantConnect.Optimizer.Objectives
import QuantConnect.Optimizer.Parameters
import System
import System.Collections.Generic

QuantConnect_Interfaces_IBusyCollection_T = typing.TypeVar("QuantConnect_Interfaces_IBusyCollection_T")
QuantConnect_Interfaces_IExtendedDictionary_TKey = typing.TypeVar("QuantConnect_Interfaces_IExtendedDictionary_TKey")
QuantConnect_Interfaces_IExtendedDictionary_TValue = typing.TypeVar("QuantConnect_Interfaces_IExtendedDictionary_TValue")
QuantConnect_Interfaces__EventContainer_Callable = typing.TypeVar("QuantConnect_Interfaces__EventContainer_Callable")
QuantConnect_Interfaces__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Interfaces__EventContainer_ReturnType")


class ISecurityService(metaclass=abc.ABCMeta):
    """This interface exposes methods for creating a new Security"""


class IAccountCurrencyProvider(metaclass=abc.ABCMeta):
    """A reduced interface for an account currency provider"""


class IDataProviderEvents(metaclass=abc.ABCMeta):
    """Events related to data providers"""


class IRegressionAlgorithmDefinition(metaclass=abc.ABCMeta):
    """
    Defines a C# algorithm as a regression algorithm to be run as part of the test suite.
    This interface also allows the algorithm to declare that it has versions in other languages
    that should yield identical results.
    """


class ISubscriptionDataConfigProvider(metaclass=abc.ABCMeta):
    """Reduced interface which provides access to registered SubscriptionDataConfig"""


class ISubscriptionDataConfigService(QuantConnect.Interfaces.ISubscriptionDataConfigProvider, metaclass=abc.ABCMeta):
    """
    This interface exposes methods for creating a list of SubscriptionDataConfig for a given
    configuration
    """


class IAlgorithmSubscriptionManager(QuantConnect.Interfaces.ISubscriptionDataConfigService, metaclass=abc.ABCMeta):
    """AlgorithmSubscriptionManager interface will manage the subscriptions for the SubscriptionManager"""


class DataProviderNewDataRequestEventArgs(System.EventArgs):
    """Event arguments for the IDataProvider.NewDataRequest event"""

    @property
    def path(self) -> str:
        """Path to the fetched data"""
        ...

    @property
    def succeded(self) -> bool:
        """Whether the data was fetched successfully"""
        ...

    def __init__(self, path: str, succeded: bool) -> None:
        """
        Initializes a new instance of the DataProviderNewDataRequestEventArgs class
        
        :param path: The path to the fetched data
        :param succeded: Whether the data was fetched successfully
        """
        ...


class IBusyCollection(typing.Generic[QuantConnect_Interfaces_IBusyCollection_T], System.IDisposable, metaclass=abc.ABCMeta):
    """Interface used to handle items being processed and communicate busy state"""


class IMapFileProvider(metaclass=abc.ABCMeta):
    """Provides instances of MapFileResolver at run time"""


class IPrimaryExchangeProvider(metaclass=abc.ABCMeta):
    """Primary Exchange Provider interface"""


class IExtendedDictionary(typing.Generic[QuantConnect_Interfaces_IExtendedDictionary_TKey, QuantConnect_Interfaces_IExtendedDictionary_TValue], metaclass=abc.ABCMeta):
    """Represents a generic collection of key/value pairs that implements python dictionary methods."""


class ObjectStoreErrorRaisedEventArgs(System.EventArgs):
    """Event arguments for the IObjectStore.ErrorRaised event"""

    @property
    def error(self) -> System.Exception:
        """Gets the Exception that was raised"""
        ...

    def __init__(self, error: System.Exception) -> None:
        """
        Initializes a new instance of the ObjectStoreErrorRaisedEventArgs class
        
        :param error: The error that was raised
        """
        ...


class IAlgorithmSettings(metaclass=abc.ABCMeta):
    """User settings for the algorithm which can be changed in the IAlgorithm.Initialize method"""


class ISecurityPrice(metaclass=abc.ABCMeta):
    """
    Reduced interface which allows setting and accessing
    price properties for a Security
    """


class IOptionPrice(QuantConnect.Interfaces.ISecurityPrice, metaclass=abc.ABCMeta):
    """
    Reduced interface for accessing Option
    specific price properties and methods
    """


class IDataProvider(metaclass=abc.ABCMeta):
    """
    Fetches a remote file for a security.
    Must save the file to Globals.DataFolder.
    """


class IDataPermissionManager(metaclass=abc.ABCMeta):
    """Entity in charge of handling data permissions"""


class IDataMonitor(System.IDisposable, metaclass=abc.ABCMeta):
    """Monitors data requests and reports on missing data"""


class IDataChannelProvider(metaclass=abc.ABCMeta):
    """Specifies data channel settings"""


class IMessagingHandler(System.IDisposable, metaclass=abc.ABCMeta):
    """
    Messaging System Plugin Interface.
    Provides a common messaging pattern between desktop and cloud implementations of QuantConnect.
    """


class IFutureChainProvider(metaclass=abc.ABCMeta):
    """Provides the full future chain for a given underlying."""


class IRegressionResearchDefinition(metaclass=abc.ABCMeta):
    """Defines interface for research notebooks to be run as part of the research test suite."""


class IApi(System.IDisposable, metaclass=abc.ABCMeta):
    """API for QuantConnect.com"""

    def abort_optimization(self, optimization_id: str) -> QuantConnect.Api.RestResponse:
        """
        Abort an optimization
        
        :param optimization_id: Optimization id for the optimization we want to abort
        :returns: RestResponse.
        """
        ...

    def create_optimization(self, project_id: int, name: str, target: str, target_to: str, target_value: typing.Optional[float], strategy: str, compile_id: str, parameters: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter], constraints: System.Collections.Generic.IReadOnlyList[QuantConnect.Optimizer.Objectives.Constraint], estimated_cost: float, node_type: str, parallel_nodes: int) -> QuantConnect.Api.BaseOptimization:
        """
        Create an optimization with the specified parameters via QuantConnect.com API
        
        :param project_id: Project ID of the project the optimization belongs to
        :param name: Name of the optimization
        :param target: Target of the optimization, see examples in PortfolioStatistics
        :param target_to: Target extremum of the optimization, for example "max" or "min"
        :param target_value: Optimization target value
        :param strategy: Optimization strategy, GridSearchOptimizationStrategy
        :param compile_id: Optimization compile ID
        :param parameters: Optimization parameters
        :param constraints: Optimization constraints
        :param estimated_cost: Estimated cost for optimization
        :param node_type: Optimization node type
        :param parallel_nodes: Number of parallel nodes for optimization
        :returns: BaseOptimization object from the API.
        """
        ...

    def delete_object_store(self, organization_id: str, key: str) -> QuantConnect.Api.RestResponse:
        """
        Request to delete Object Store metadata of a specific organization and key
        
        :param organization_id: Organization ID we would like to delete the Object Store file from
        :param key: Key to the Object Store file
        :returns: RestResponse.
        """
        ...

    def delete_optimization(self, optimization_id: str) -> QuantConnect.Api.RestResponse:
        """
        Delete an optimization
        
        :param optimization_id: Optimization id for the optimization we want to delete
        :returns: RestResponse.
        """
        ...

    def estimate_optimization(self, project_id: int, name: str, target: str, target_to: str, target_value: typing.Optional[float], strategy: str, compile_id: str, parameters: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter], constraints: System.Collections.Generic.IReadOnlyList[QuantConnect.Optimizer.Objectives.Constraint]) -> QuantConnect.Api.Estimate:
        """
        Estimate optimization with the specified parameters via QuantConnect.com API
        
        :param project_id: Project ID of the project the optimization belongs to
        :param name: Name of the optimization
        :param target: Target of the optimization, see examples in PortfolioStatistics
        :param target_to: Target extremum of the optimization, for example "max" or "min"
        :param target_value: Optimization target value
        :param strategy: Optimization strategy, GridSearchOptimizationStrategy
        :param compile_id: Optimization compile ID
        :param parameters: Optimization parameters
        :param constraints: Optimization constraints
        :returns: Estimate object from the API.
        """
        ...

    def get_object_store(self, organization_id: str, keys: System.Collections.Generic.List[str], destination_folder: str = None) -> bool:
        """
        Download the object store associated with the given organization ID and key
        
        :param organization_id: Organization ID we would like to get the Object Store from
        :param keys: Keys for the Object Store files
        :param destination_folder: Folder in which the object will be stored
        :returns: True if the object was retrieved correctly, false otherwise.
        """
        ...

    def get_object_store_properties(self, organization_id: str, key: str) -> QuantConnect.Api.PropertiesObjectStoreResponse:
        """
        Get Object Store properties given the organization ID and the Object Store key
        
        :param organization_id: Organization ID we would like to get the Object Store from
        :param key: Key for the Object Store file
        :returns: PropertiesObjectStoreResponse.
        """
        ...

    def list_optimizations(self, project_id: int) -> System.Collections.Generic.List[QuantConnect.Api.BaseOptimization]:
        """
        List all the optimizations for a project
        
        :param project_id: Project id we'd like to get a list of optimizations for
        :returns: A list of BaseOptimization objects, BaseOptimization.
        """
        ...

    def list_organizations(self) -> System.Collections.Generic.List[QuantConnect.Api.Organization]:
        """Get a list of organizations tied to this account"""
        ...

    def read_account(self, organization_id: str = None) -> QuantConnect.Api.Account:
        """
        Will read the organization account status
        
        :param organization_id: The target organization id, if null will return default organization
        """
        ...

    def read_backtest_report(self, project_id: int, backtest_id: str) -> QuantConnect.Api.BacktestReport:
        """
        Read out the report of a backtest in the project id specified.
        
        :param project_id: Project id to read
        :param backtest_id: Specific backtest id to read
        :returns: BacktestReport.
        """
        ...

    def read_data_prices(self, organization_id: str) -> QuantConnect.Api.DataPricesList:
        """Gets data prices from data/prices"""
        ...

    def read_lean_versions(self) -> QuantConnect.Api.VersionsResponse:
        """Gets a list of LEAN versions with their corresponding basic descriptions"""
        ...

    def read_optimization(self, optimization_id: str) -> QuantConnect.Api.Optimization:
        """
        Read an optimization
        
        :param optimization_id: Optimization id for the optimization we want to read
        :returns: Optimization.
        """
        ...

    def read_organization(self, organization_id: str = None) -> QuantConnect.Api.Organization:
        """Fetch organization data from web API"""
        ...

    def set_object_store(self, organization_id: str, key: str, object_data: typing.List[int]) -> QuantConnect.Api.RestResponse:
        """
        Upload files to the Object Store
        
        :param organization_id: Organization ID we would like to upload the file to
        :param key: Key to the Object Store file
        :param object_data: File to be uploaded
        :returns: RestResponse.
        """
        ...

    def update_optimization(self, optimization_id: str, name: str = None) -> QuantConnect.Api.RestResponse:
        """
        Update an optimization
        
        :param optimization_id: Optimization id we want to update
        :param name: Name we'd like to assign to the optimization
        :returns: RestResponse.
        """
        ...


class IStreamReader(System.IDisposable, metaclass=abc.ABCMeta):
    """Defines a transport mechanism for data from its source into various reader methods"""


class IHistoryProvider(QuantConnect.Interfaces.IDataProviderEvents, metaclass=abc.ABCMeta):
    """Provides historical data to an algorithm at runtime"""


class MessagingHandlerInitializeParameters(System.Object):
    """Parameters required to initialize a IMessagingHandler instance"""

    @property
    def api(self) -> QuantConnect.Interfaces.IApi:
        """The api instance to use"""
        ...

    def __init__(self, api: QuantConnect.Interfaces.IApi) -> None:
        """
        Creates a new instance
        
        :param api: The api instance to use
        """
        ...


class IShortableProvider(metaclass=abc.ABCMeta):
    """Defines a short list/easy-to-borrow provider"""


class IFactorFileProvider(metaclass=abc.ABCMeta):
    """Provides instances of FactorFile at run time"""


class ITimeKeeper(metaclass=abc.ABCMeta):
    """Interface implemented by TimeKeeper"""


class ITradeBuilder(metaclass=abc.ABCMeta):
    """Generates trades from executions and market price updates"""


class IDownloadProvider(metaclass=abc.ABCMeta):
    """Wrapper on the API for downloading data for an algorithm."""


class ISecurityInitializerProvider(metaclass=abc.ABCMeta):
    """Reduced interface which provides an instance which implements ISecurityInitializer"""


class IAlgorithm(QuantConnect.Interfaces.ISecurityInitializerProvider, QuantConnect.Interfaces.IAccountCurrencyProvider, metaclass=abc.ABCMeta):
    """
    Interface for QuantConnect algorithm implementations. All algorithms must implement these
    basic members to allow interaction with the Lean Backtesting Engine.
    """


class IBrokerageCashSynchronizer(metaclass=abc.ABCMeta):
    """Defines live brokerage cash synchronization operations."""


class IBrokerage(QuantConnect.Interfaces.IBrokerageCashSynchronizer, System.IDisposable, metaclass=abc.ABCMeta):
    """
    Brokerage interface that defines the operations all brokerages must implement. The IBrokerage implementation
    must have a matching IBrokerageFactory implementation.
    """


class IObjectStore(System.IDisposable, metaclass=abc.ABCMeta):
    """Provides object storage for data persistence."""


class IJobQueueHandler(metaclass=abc.ABCMeta):
    """Task requestor interface with cloud system"""


class IDataQueueHandler(System.IDisposable, metaclass=abc.ABCMeta):
    """Task requestor interface with cloud system"""


class IOrderProperties(metaclass=abc.ABCMeta):
    """Contains additional properties and settings for an order"""


class ITimeInForceHandler(metaclass=abc.ABCMeta):
    """Handles the time in force for an order"""


class IDataCacheProvider(System.IDisposable, metaclass=abc.ABCMeta):
    """Defines a cache for data"""


class IDataQueueUniverseProvider(metaclass=abc.ABCMeta):
    """
    This interface allows interested parties to lookup or enumerate the available symbols. Data source exposes it if this feature is available.
    Availability of a symbol doesn't imply that it is possible to trade it. This is a data source specific interface, not broker specific.
    """


class IBrokerageFactory(System.IDisposable, metaclass=abc.ABCMeta):
    """Defines factory types for brokerages. Every IBrokerage is expected to also implement an IBrokerageFactory."""


class ISignalExportTarget(System.IDisposable, metaclass=abc.ABCMeta):
    """Interface to send positions holdings to different 3rd party API's"""


class IOptionChainProvider(metaclass=abc.ABCMeta):
    """Provides the full option chain for a given underlying."""


class _EventContainer(typing.Generic[QuantConnect_Interfaces__EventContainer_Callable, QuantConnect_Interfaces__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Interfaces__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Interfaces__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Interfaces__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


