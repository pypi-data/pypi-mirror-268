from finazon_grpc_python.time_series_service import TimeSeriesService, GetTimeSeriesRequest
from finazon_grpc_python.common.errors import FinazonGrpcRequestError


service = TimeSeriesService('your_api_key')

try:
    request = GetTimeSeriesRequest(ticker='AAPL', dataset='sip_non_pro', interval='1h', page_size=10)
    response = service.get_time_series(request)
    print('Last OHLCV data\n')
    for item in response.result:
        print(f'{item.timestamp} - {item.open}, {item.high}, {item.low}, {item.close}, {item.volume}')
except FinazonGrpcRequestError as e:
    print(f'Received error, code: {e.code}, message: {e.message}')
