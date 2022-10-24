# https://github.com/financedata-org/FinanceDataReader

import FinanceDataReader as fdr

# 삼성전자(005930) 전체 (1996-11-05 ~ 현재)
df = fdr.DataReader('005930', '2021')
print(df)

# Apple (AAPL), 2017-01-01 ~ Now
#df = fdr.DataReader('AAPL', '2017')

# 캔들차트 그리기
fdr.chart.plot(df, title='삼성전자(005930)', save='./result/test.png')