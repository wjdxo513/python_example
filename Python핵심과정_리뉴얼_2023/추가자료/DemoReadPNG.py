# byte 구조를 변환하는 모듈
import struct
# 파일 IO
import io

# 이미지 파일을 읽어온다.
with open("c:\\temp\\demo.png", "rb") as handle:
  data = handle.read()

# 처음은 \x89PNG\r\n\x1a\n로 시작하는지 확인한다.
if data[:8] == b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A':
  # struct.unpack의 결과는 무조건 튜플로 값이 온다. data[8:12]는 data[8], data[9], data[10], data[11]의 의미다.
  junk, = struct.unpack('>L', data[8:12])
  # junk 값은 13이다.
  print(junk)
  # IHDR를 받는다.
  ihdr, = struct.unpack('>4s', data[12:16])
  # IHDR를 확인한다.
  print(ihdr.decode('utf-8'))
  # 순서대로 너비, 높이 비트 깊이, 컬러 타입, 압축 메소드, 필터 메소드등을 취득ㅎ나다.
  width, height, bit, type1, type2, type3, type4, pnumber = struct.unpack('>2L5b4xL',data[16:37]);
  print('width :', width, 
        'height :', height, 
        'bit depth', bit, 
        'color type', type1,
        'compression method', type2, 
        'filter method', type3, 
        'interlace method', type4, 
        'palette number', pnumber);

