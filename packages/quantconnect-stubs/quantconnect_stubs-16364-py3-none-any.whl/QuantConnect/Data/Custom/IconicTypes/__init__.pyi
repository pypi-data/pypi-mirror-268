from typing import overload
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Custom.IconicTypes
import QuantConnect.Data.Market
import System.Collections.Generic


class IndexedLinkedData2(QuantConnect.Data.IndexedBaseData):
    """
    Data type that is indexed, i.e. a file that points to another file containing the contents
    we're looking for in a Symbol.
    """

    @property
    def count(self) -> int:
        """Example data property"""
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Set the data time zone to UTC
        
        :returns: Time zone as UTC.
        """
        ...

    def default_resolution(self) -> int:
        """
        Sets the default resolution to Second
        
        :returns: Resolution.Second. This method returns the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Gets the source of the index file
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: Is live mode
        :returns: SubscriptionDataSource indicating where data is located and how it's stored.
        """
        ...

    def get_source_for_an_index(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], index: str, is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Determines the actual source from an index contained within a ticker folder
        
        :param config: Subscription configuration
        :param date: Date
        :param index: File to load data from
        :param is_live_mode: Is live mode
        :returns: SubscriptionDataSource pointing to the article.
        """
        ...

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data source is sparse.
        If false, it will disable missing file logging.
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Creates an instance from a line of JSON containing article information read from the `content` directory
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source can undergo
        rename events/is tied to equities.
        
        :returns: true.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """
        Gets a list of all the supported Resolutions
        
        :returns: All resolutions.
        """
        ...


class IndexedLinkedData(QuantConnect.Data.IndexedBaseData):
    """
    Data type that is indexed, i.e. a file that points to another file containing the contents
    we're looking for in a Symbol.
    """

    @property
    def count(self) -> int:
        """Example data property"""
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Set the data time zone to UTC
        
        :returns: Time zone as UTC.
        """
        ...

    def default_resolution(self) -> int:
        """
        Sets the default resolution to Second
        
        :returns: Resolution.Second. This method returns the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Gets the source of the index file
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: Is live mode
        :returns: SubscriptionDataSource indicating where data is located and how it's stored.
        """
        ...

    def get_source_for_an_index(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], index: str, is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Determines the actual source from an index contained within a ticker folder
        
        :param config: Subscription configuration
        :param date: Date
        :param index: File to load data from
        :param is_live_mode: Is live mode
        :returns: SubscriptionDataSource pointing to the article.
        """
        ...

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data source is sparse.
        If false, it will disable missing file logging.
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Creates an instance from a line of JSON containing article information read from the `content` directory
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param is_live_mode: Is live mode
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source can undergo
        rename events/is tied to equities.
        
        :returns: true.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """
        Gets a list of all the supported Resolutions
        
        :returns: All resolutions.
        """
        ...


class UnlinkedData(QuantConnect.Data.BaseData):
    """Data source that is unlinked (no mapping) and takes any ticker when calling AddData"""

    any_ticker: bool
    """If true, we accept any ticker from the AddData call"""

    @property
    def ticker(self) -> str:
        """Example data"""
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Set the data time zone to UTC
        
        :returns: Time zone as UTC.
        """
        ...

    def default_resolution(self) -> int:
        """
        Sets the default resolution to Second
        
        :returns: Resolution.Second. This method returns the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        ...

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data source is sparse.
        If false, it will disable missing file logging.
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source can undergo
        rename events/is tied to equities.
        
        :returns: true.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """
        Gets a list of all the supported Resolutions
        
        :returns: All resolutions.
        """
        ...


class UnlinkedDataTradeBar(QuantConnect.Data.Market.TradeBar):
    """Data source that is unlinked (no mapping) and takes any ticker when calling AddData"""

    any_ticker: bool
    """If true, we accept any ticker from the AddData call"""

    def __init__(self) -> None:
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Set the data time zone to UTC
        
        :returns: Time zone as UTC.
        """
        ...

    def default_resolution(self) -> int:
        """
        Sets the default resolution to Second
        
        :returns: Resolution.Second. This method returns the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        ...

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data source is sparse.
        If false, it will disable missing file logging.
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source can undergo
        rename events/is tied to equities.
        
        :returns: true.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """
        Gets a list of all the supported Resolutions
        
        :returns: All resolutions.
        """
        ...


class LinkedData(QuantConnect.Data.BaseData):
    """Data source that is linked (tickers that can have renames or be delisted)"""

    @property
    def count(self) -> int:
        """Example data"""
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Set the data time zone to UTC
        
        :returns: Time zone as UTC.
        """
        ...

    def default_resolution(self) -> int:
        """
        Sets the default resolution to Second
        
        :returns: Resolution.Second. This method returns the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        ...

    def is_sparse_data(self) -> bool:
        """
        Indicates whether the data source is sparse.
        If false, it will disable missing file logging.
        
        :returns: true.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> QuantConnect.Data.BaseData:
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates whether the data source can undergo
        rename events/is tied to equities.
        
        :returns: true.
        """
        ...

    def supported_resolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """
        Gets a list of all the supported Resolutions
        
        :returns: All resolutions.
        """
        ...


