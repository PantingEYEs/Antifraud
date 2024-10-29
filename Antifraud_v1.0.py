from PIL import Image

base = Image.open('Antifraud/Antifraud_base.png').convert('RGBA')
tl = Image.open('Fraud/Fraud_tl.png').convert('RGBA')
hp = Image.open('Fraud/Fraud_hp.png').convert('RGBA')
qq = Image.open('Fraud/Fraud_qq.png').convert('RGBA')
tl = tl.resize((647, 1370))
hp = hp.resize((647, 1370))
qq = qq.resize((427, 903))
qq = qq.crop((0, 0, 427, 703))
base.paste(tl, (297, 490, 944, 1860))
base.paste(hp, (1104, 490, 1751, 1860))
base.paste(qq, (1982, 1220, 2409, 1923))



qq_l = Image.open('Fraud/Fraud_qq.png').convert('RGBA')
pp = Image.open('Fraud/Fraud_pp.jpg').convert('RGBA')
qq_l = qq_l.resize((681, 1440))
pp = pp.resize((643, 642))
qq_l = qq_l.crop((0, 0, 681, 525))
base.paste(qq_l, (1219, 1370, 1900, 1895))
base.paste(pp, (168, 1206, 811, 1848))



qqf = Image.open('Antifraud/Antifraud_qqf.png').convert('RGBA')
ppf = Image.open('Antifraud/Antifraud_ppf.png').convert('RGBA')
base = Image.alpha_composite(base, qqf)
base = Image.alpha_composite(base, ppf)



base.save('Antifraud_op.png')