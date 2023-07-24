import matplotlib.font_manager as fm

for i, x in enumerate(fm.fontManager.ttflist):
    print i, x, type(x) , x.name , x.fname   # x.name  == font name (family name)

    fp1=fm.FontProperties(fname= x.fname).get_name()  # font famiily name
    print fp1
    
    if i == 10: break   # 10개만 출력하기
