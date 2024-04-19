class MappingTable:

    @staticmethod
    def get_kline_map():
        return {'HTSCSecurityID': 'htsc_code', 'OpenPx': 'open', 'ClosePx': 'close', 'HighPx': 'high', 'LowPx': 'low',
                'NumTrades': 'num_trades', 'TotalVolumeTrade': 'volume', 'TotalValueTrade': 'value',
                'OpenInterest': 'open_interest', 'SettlePrice': 'settle'}

    @staticmethod
    def get_htsc_margin_map():
        return {'HTSCSecurityID': 'htsc_code', 'TradingPhaseCode': 'trading_phase', 'securityIDSource': 'exchange',
                'securityType': 'security_type', 'PreWeightedRate': 'pre_weighted_rate', 'PreHighRate': 'pre_high_rate',
                'PreLowRate': 'pre_low_rate', 'PreHtscVolume': 'pre_htsc_volume',
                'PreMarketVolume': 'pre_market_volume', 'WeightedRate': 'weighted_rate', 'HighRate': 'high_rate',
                'LowRate': 'low_rate', 'HtscVolume': 'htsc_volume', 'MarketVolume': 'market_volume',
                'BestBorrowRate': 'best_borrow_rate', 'BestLendRate': 'best_lend_rate', 'ValidBorrows': 'valid_borrows',
                'ValidALends': 'valid_a_lends', 'ValidBLends': 'valid_b_lends', 'ValidCLends': 'valid_c_lends',
                'ALends': 'a_lends', 'BLends': 'b_lends', 'CLends': 'c_lends',
                'ValidReservationBorrows': 'valid_reservation_borrows',
                'ValidReservationLends': 'valid_reservation_lends', 'ReservationBorrows': 'reservation_borrows',
                'ReservationLends': 'reservation_lends', 'ValidOtcLends': 'valid_otc_lends',
                'BestReservationBorrowRate': 'best_reservationborrow_rate',
                'BestReservationLendRate': 'best_reservation_lend_rate', 'ValidLendAmount': 'valid_lend_amount',
                'ValidALendAmount': 'valid_a_lend_amount', 'ValidBLendAmount': 'valid_b_lend_amount',
                'HtscBorrowAmount': 'htsc_borrow_amount', 'HtscBorrowRate': 'htsc_borrow_rate',
                'BestLoanRate': 'best_loan_rate', 'HtscBorrowTradeVolume': 'htsc_borrow_trade_volume',
                'HtscBorrowWeightedRate': 'htsc_borrow_weighted_rate',
                'PreHtscBorrowTradeVolume': 'pre_htsc_borrow_trade_volume',
                'PreHtscBorrowWeightedRate': 'pre_htsc_borrow_weighted_rate', 'HtscBorrows': 'htsc_borrows',
                'Loans': 'loans', 'ExternalLends': 'external_lends', 'LongTermLends': 'long_term_lends',
                'LastPx': 'last', 'PreClosePx': 'pre_close', 'Borrows': 'borrows',
                'HtscLendTradeVolume': 'htsc_lend_trade_volume', 'MarketTradeVolume': 'market_trade_volume',
                'TradeDate': 'trade_date', 'HtscLendAmount': 'htsc_lend_amount', 'HtscLendTerms': 'htsc_lend_terms',
                'HtscBestLendRate': 'htsc_best_lend_rate', 'HtscBorrowTerms': 'htsc_borrow_terms',
                'TradeVolume': 'trade_volume', 'TradeMoney': 'trade_money', 'PreTradeVolume': 'pre_trade_volume',
                'PreTradeMoney': 'pre_trade_money', 'HtscBorrowTerm': 'htsc_borrow_term', 'LoanAmount': 'loan_amount',
                'MarketBorrows': 'market_borrows', 'ValidLendTerm': 'valid_lend_term',
                'ValidBorrowAmount': 'valid_borrow_amount', 'MarketLends': 'market_lends'}

    @staticmethod
    def get_derived_map():
        return {'HTSCSecurityID': 'htsc_code', 'securityIDSource': 'exchange', 'securityType': 'security_type',
                'TotalValueTrade': 'value', 'TotalBidValueTrade': 'total_buy_value_trade',
                'TotalOfferValueTrade': 'total_sell_value_trade', }

    @staticmethod
    def find_edb_index_map():
        return {'ModifyFrequency': 'modify_frequency', 'IndexId': 'index_id', 'Unit': 'unit',
                'IndexCodeSource': 'index_code_source', 'PathSource': 'path_source', 'IndustryCode': 'industry_code',
                'AccessId': 'access_id', 'IndexName': 'name', 'AccessName': 'access_name',
                'ResourceId': 'resource_id', 'IndexStatus': 'index_status', 'Refenence3': 'refenence3',
                'IS_COMPLIANCE': 'is_compliance'}

    @staticmethod
    def edb_map():
        return {'IndexValue': 'index_value', 'IndexId': 'index_id', 'AccessId': 'access_id', 'PubDate': 'pub_date',
                'AccessName': 'access_name'}

    @staticmethod
    def get_rpt_basicinfo_ht_map():
        return {'UpdateTime': 'update_time', 'AgencyName': 'agency_name', 'AbstractText': 'abstract_text',
                'EntryTime': 'entry_time', 'SubTitle': 'sub_title', 'Abstract': 'abstract', 'Url': 'url',
                'AgencyEngName': 'agency_eng_name', 'IsValid': 'is_valid', 'IssuePlace': 'issue_place',
                'Category': 'category', 'Id': 'id', 'CategoryName': 'category_name', 'Scale': 'scale',
                'ResourceId': 'resource_id', 'UpdateId': 'update_id', 'AgencyCode': 'agency_code',
                'Language': 'language', 'WriteDate': 'time', 'Pages': 'pages', 'GroundTime': 'ground_time',
                'LabelCode': 'label_code', 'LabelValue': 'label_value', 'ReportCode': 'report_code',
                'RecordId': 'record_id', 'IsOrg': 'is_org', 'DeptName': 'dept_name', 'Title': 'title',
                'KeyWords': 'key_words'}

    @staticmethod
    def get_rpt_stk_ht_map():
        return {'SecuCode': 'secu_code', 'InvratingDescLast': 'invrating_desc_last',
                'UpdateTime': 'update_time', 'SecuAbbr': 'secu_abbr', 'InvratingCodeLast': 'invrating_code_last',
                'PredictPrice': 'predict_price', 'ExchangeName': 'exchange_name', 'EntryTime': 'entry_time',
                'ExchangeCode': 'exchange_code', 'Forecastdate': 'forecast_date', 'IsValid': 'is_valid',
                'IsFirstRating': 'is_first_rating', 'PriceCurrency': 'price_currency', 'Id': 'id',
                'RatingChangeName': 'rating_change_name', 'PreDictpriceLast': 'predict_price_last',
                'InvratingDesc': 'invrating_desc', 'ResourceId': 'resource_id', 'UpdateId': 'update_id',
                'GroundTime': 'ground_time', 'TradingCode': 'trading_code', 'ReportCode': 'report_code',
                'RecordId': 'record_id', 'PriceChange': 'price_change', 'IDSOURCE': 'exchange',
                'InvratingCode': 'invrating_code', 'RatingChange': 'rating_change',
                'HTSCSECURITYID': 'htsc_code'}

    @staticmethod
    def get_rpt_industry_ht_map():
        return {'FInduCode': 'l1_code', 'InvratingDescLast': 'invrating_desc_last', 'UpdateTime': 'update_time',
                'GroundTime': 'ground_time', 'InvratingCodeLast': 'invrating_code_last', 'FInduName': 'l1_name',
                'InduLevel': 'industry_level', 'EntryTime': 'entry_time', 'ForecastDate': 'forecast_date',
                'ReportCode': 'report_code', 'RecordId': 'record_id', 'InduCode': 'industry_code',
                'IsValid': 'is_valid', 'SInduName': 'l2_name', 'IsFirstRating': 'is_first_rating',
                'SInduCode': 'l2_code', 'InduName': 'industry_name', 'InvratingCode': 'invrating_code',
                'RatingChange': 'rating_change', 'Id': 'id', 'RatingChangeName': 'rating_change_name',
                'InvratingDesc': 'invrating_desc', 'ResourceId': 'resource_id', 'UpdateId': 'update_id'}

    @staticmethod
    def get_rpt_author_ht_map():
        return {'AuthorWeight': 'author_weight', 'UpdateTime': 'update_time', 'GroundTime': 'ground_time',
                'CertiCode': 'certi_code', 'Rank': 'rank', 'AuthorCode': 'author_code',
                'CertiTypeCode': 'certi_type_code', 'EntryTime': 'entry_time', 'ReportCode': 'report_code',
                'AuthorName': 'author_name', 'RecordId': 'record_id', 'IsValid': 'is_valid', 'Id': 'id',
                'ResourceId': 'resource_id', 'AuthorType': 'author_type', 'UpdateId': 'update_id'}

    @staticmethod
    def get_rpt_annex_ht_map():
        return {'S3ContentUrl': 's3_content_url', 'S3AnnexUpdateTime': 's3_annex_update_time',
                'UpdateTime': 'update_time', 'AnnexName': 'annex_name', 'GroundTime': 'ground_time',
                'S3AnnexUrl': 's3_annex_url', 'AnnexSize': 'annex_size', 'EntryTime': 'entry_time',
                'ReportCode': 'report_code', 'RecordId': 'record_id', 'IsValid': 'is_valid',
                'S3ContentUpdateTime': 's3_content_update_time', 'AnnexUrl': 'annex_url', 'Id': 'id',
                'ResourceId': 'resource_id', 'AnnexFormat': 'annex_format', 'UpdateId': 'update_id',
                'StoreFileId': 'store_file_id'}

    @staticmethod
    def get_rpt_stkpredict_ht_map():
        return {'SecuCode': 'secu_code', 'UpdateTime': 'update_time', 'GroundTime': 'ground_time',
                'TradingCode': 'trading_code', 'SecuAbbr': 'name', 'EntryTime': 'entry_time',
                'ExchangeCode': 'exchange_code', 'ForecastDate': 'forecast_date', 'ReportCode': 'report_code',
                'RecordId': 'record_id', 'IndexValue': 'index_value', 'IsValid': 'is_valid',
                'PredictYear': 'predict_year', 'IDSOURCE': 'exchange', 'HTSCSECURITYID': 'htsc_code', 'Id': 'id',
                'IndexName': 'index_name', 'ResourceId': 'resource_id', 'UpdateId': 'update_id'}



    @classmethod
    def perform_operation(cls, method_name):
        method = getattr(cls, method_name)
        return method()


if __name__ == '__main__':
    n = MappingTable.perform_operation("get_kline_map")
    print(n)
