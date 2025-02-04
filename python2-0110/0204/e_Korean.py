# e_Korean.py

### matplotlib 라이브러리의 한글 처리 ###

# font-manager & rc 모듈을 사용
# : 한글 폰트 등록

# C:\\Windows\\Fonts\\HMFMPYUN.TTF
# > 문자열 내에 저장해서 라이브러리에 제공
# > \가 이스케이프 문자로 취급

from matplotlib import font_manager, rc

import matplotlib.pyplot as plt
import matplotlib

font_path = 'C:\\Windows\\Fonts\\HMFMPYUN.TTF'

font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc('font', family=font_name)

# 데이터와 함꼐 한글 라벨 지정
plt.plot(['봄', '여름', '가을', '겨울'], [20, 30, 15, 10])
plt.title('한글 깨짐 방지')
plt.show()