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
# Semua titik = koordinat foto 1920x1072, mengikuti coretan pengguna (sketsa 2000px x 0.96),
# lalu ditepatkan ke pipa/tepi bangunan terdekat.
SURYA = [(1072,354),(1152,482),(1546,441),(1578,468),(1578,610),(1694,636),(1693,669),(1676,670),(1676,712)]
RUMAH = [(1614,742),(1501,710),(1292,757),(1292,576)]
PLN   = [(1843,560),(1818,926),(1536,1056),(1360,956),(1360,856),(1614,771)]
d = {
 'surya': rounded(SURYA, 8),
 'rumah': rounded(RUMAH, 10),
 'pln':   rounded(PLN, 10),
}
json.dump(d, open(__import__('sys').argv[1],'w'), indent=1)
