# Generator path SVG aliran energi di hero. Jalankan: python3 energy-paths.py out.json
# lalu salin nilai d ke <g class="line" data-line="..."> di landing-plts-hybrid.html.
import math, json
def rounded(pts, r=10):
    d=f"M{pts[0][0]} {pts[0][1]}"
    for i in range(1,len(pts)-1):
        (x0,y0),(x1,y1),(x2,y2)=pts[i-1],pts[i],pts[i+1]
        def toward(ax,ay,bx,by,dist):
            L=math.hypot(bx-ax,by-ay); k=min(dist,L/2)/L; return (round(ax+(bx-ax)*k,1),round(ay+(by-ay)*k,1))
        a=toward(x1,y1,x0,y0,r); b=toward(x1,y1,x2,y2,r)
        d+=f" L{a[0]} {a[1]} Q{x1} {y1} {b[0]} {b[1]}"
    return d+f" L{pts[-1][0]} {pts[-1][1]}"
# Semua titik = koordinat foto 1920x1072, ditempel ke pipa/tepi yang terlihat di foto.
SURYA = [(1077,353),(1157,470),(1581,451),(1581,610),(1680,631),(1679,708),(1658,712)]
RUMAH = [(1622,704),(1541,716),(1541,694),(1476,662),(1290,735),(1284,632)]
PLN_CURVE = "M1838 552 C1800 730 1625 902 1372 886"
PLN_FENCE = [(1372,886),(1358,880),(1357,856),(1570,785),(1612,771)]
d = {
 'surya': rounded(SURYA, 10),
 'rumah': rounded(RUMAH, 14),
 'pln':   PLN_CURVE + rounded(PLN_FENCE, 8)[len("M1372 886"):],
}
json.dump(d, open(__import__('sys').argv[1],'w'), indent=1)
