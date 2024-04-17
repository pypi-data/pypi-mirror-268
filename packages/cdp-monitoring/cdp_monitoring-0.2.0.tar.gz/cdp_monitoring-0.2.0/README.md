# cdp-monitoring

fastapi prometheus + opentelemetry sdk 

## Install package
```shell  
VERSION=0.1.0
pip install git+https://github.daumkakao.com/cdpdev/cdp-monitoring.git#${VERSION}
```

## Usage  
### 1. Tempo url 을 환경변수로 설정  
설정되어 있지 않은 경우 모니터링도 비활성화  
```shell
export TEMPO_URL=""
```

### 2. 모니터링 대상 FastAPI 앱을 init_monitoring 함수의 인자로 전달
```python
# app 생성
from fastapi import FastAPI
app = FastAPI(title="My FastAPI App")

# 모니터링 설정 적용
from cdp_monitoring import init_monitoring
init_monitoring(app)
```

## Uninstall package  
```shell
pip uninstall cdp-monitoring
```