#!/usr/bin/env python
# -*- coding: latin-1 -*-
# :Copyright: 2007 Guenter Milde.
#             Released under the terms of the GNU General Public License 
#             (v. 2 or later)
 
# thermisch0d_symbolic.py: Kompaktes Modell eines Pyroelements 
# ============================================================
# mit sybolic computing (swiginac)
# --------------------------------
# 
# Imports
# =======
# 
# Import this module with
# 
# >>> from T0d import *
# 
# Python standard modules and established extensions::

import sys, os
from pprint import pprint

import Gnuplot

# The swiginac module for symbolic algebra with GiNaC:: 

from swiginac import *   # symbolic algebra (CAS)
# from Symbolic import *     # 

# and private extensions::

# from gm_tools import sgn
# from Sensor_analytisch import *
import LyX

# Ausgabe
# =======
# ::
# 
# 
# ::

if __name__ == '__main__':
    output_format = "text"
    # output_format = "lyx"
    # output_format = "tex"
else:
    output_format = ""     # keine Ausgabe

# Load the LyX client and open a new LyX buffer for the output::

if output_format == "lyx":
    from LyX import lfuns
    lfuns.buffer_new()

def heading(text, level=1, output_format=output_format):
    """print a heading (TODO: of level `level`)
    suited for `output_format`
    """
    if output_format == "lyx":
        lfuns.break_paragraph()
        lfuns.layout("Section")
        lfuns.self_insert(text)
        lfuns.break_paragraph()
        lfuns.layout("Standard")
    elif output_format == "tex":
        print "\n\\section{%s}"%text
    elif output_format == "text":
        print "\n" + text
        print "-" * len(text)

def printlatex(obj):
    try:
        return obj.printlatex()
    except AttributeError:
        return str(obj)

def printout(*args):
    if output_format == "lyx":
        lfuns.break_paragraph()
        args = [printlatex(arg) for arg in args]
        lfuns.math_insert(*args)
        lfuns.char_forward()
    elif output_format == "tex":
        print " ".join([printlatex(arg) for arg in args])
    elif output_format == "text":
        print " ".join([str(arg) for arg in args])
        

# Real und Imaginärteil sind (noch) nicht von Python aus zugänglich
def real(z):
    """z = real(z) + I * imag(z)"""
    try:
        return z.real()
    except AttributeError:
        return (z + conjugate(z))/2

def imag(z):
    """z = real(z) + I * imag(z)"""
    try:
        return z.imag()
    except AttributeError:
        return (z - conjugate(z))/(2*I)


# >>> conjugate(3+ 2*I)                  # complex conjugation
# 3-2*I
# >>> real(3 + 2*I)
# 3
# >>> print imag(3 + 2*I), imag(3), imag(2*I)
# 2 0 2
# >>> abs(3 + 2*I)
# 3.6055512754639892931
# 
# Noch nicht implementiert ist arg() für das Argument in Euler-Notation
# 
# #>>> arg(3 + 2*I)
# #>>> arg(3), arg(3 + 3*I), arg(3*I), arg(-3 + 3*I), arg(-3), arg(-3 + -3*I), arg(-3*I), arg(3 + -3*I)
# 
# 
# Einheiten
# =========
# 
# ::

W = symbol("W", "\\textrm{W}")
mm = symbol("mm", "\\textrm{mm}")
m = 1000*mm
mum = mm/1000
s = symbol("s", "\\textrm{s}")
K = symbol("K", "\\textrm{K}")
kg = symbol("kg", "\\textrm{kg}")
J = W*s
C = symbol("C", "\\textrm{C}")


# Größensymbole
# =============
# ::

# Geometrie
t = symbol('t'); t.unit = s                 # Zeit
l = symbol("l"); l.unit = m                 # Länge
A = symbol("A"); A.unit = m**2              # Fläche, Querschnitt
V = symbol("V"); V.unit = m**3              # Volumen

# Eingangsstrahlung
E = symbol("E"); E.unit = W/m**2            # IR-Strahlungsdichte
Phi = E*A; Phi.unit = W                     # Wärmestrom, Strahlungsleistung
omega = symbol("omega"); omega.unit = 1/s   # Kreisfrequenz

# Materialgrößen
lambda_T = symbol("lambda_T", r"\lambda_T")  # Wärmeleitfähighkeit
lambda_T.unit = W/(m*K)
c_T = symbol("c_T"); c_T.unit = J/(kg*K)    # spezifische Wärmekapazität
rho = symbol("rho"); rho.unit =  kg/m**3    # Dichte
cv_T = c_T * rho                            # volumenspez. Wärmekapazität 
cv_T.unit =  J/(m**3*K)
a_T = lambda_T/cv_T                        # Thermische Diffusionskonstante
a_T.unit = lambda_T.unit/cv_T.unit          # m²/s
p   = symbol("p"); p.unit = C/(m**2*K)      # pyroelektrischer Koeffizient



# Modell: Chip mit umgebender Luftschicht
# =======================================
# 
# ::

heading("Modellwerte")

# Geometrie
# ---------
# ::

# Pixel (Sensorelemente)
a_pix     = 90 * mum            # Pixelbreite [µm])
b_pix     = 100 * mum           # Pixelhöhe (x-Richtung) [µm]
c_pix     = 100 * mum           # Pitch (y-Richtung) [µm]
d_pix     = 20 * mum            # Dicke (z-Richtung) [µm]
# L_y     = 1200 * mum          # Länge des Modells in y-Richtung

A_pix     = a_pix * b_pix       # Pixelfläche
V_pix     = A_pix * d_pix       # Pixelvolumen

# Luftschicht
d_Luft = symbol("d_Luft")
d_Luft.oben  = 350 * mum        # Luftschicht oben
d_Luft.unten = 250 * mum        # Luftschicht unten

heading("Geometrie")
printout("A_\mathrm{pix} = ", A_pix.evalf())
printout("V_\mathrm{pix} =", V_pix.evalf())

# IR-Strahlung
# ------------
# ::

E_in      = 200 * W/m**2       # Strahlungsdichte
f_ch      = 128 * 1/s          # Chopperfrequenz
T_ch      = 1/f_ch             # Chopperperiode   (0.0078125 s)
omega.ch  = 2*Pi*f_ch          # Chopperkreisfrequenz
Phi_in = E_in * A_pix          # unmoduliert
Phi_quer = Phi_in/2            # mittlere Strahlungsdichte
Phi_0 = Phi_in/2               # Amplitude der Wechselgröße

heading("Eingangstrahlung")
printout(r"\Phi_\mathrm{in} =", Phi_in.evalf())
printout(r"<\Phi> = \Phi_0 = \Phi_\mathrm{in}/2 =", Phi_0.evalf())

# Materialkonstanten
# ------------------
# ::

# Wärmeleitfähigkeit
lambda_T.Lita = 4.2 * W/(m*K)
lambda_T.Luft = 0.026 * W/(m*K)

c_T.Lita  = 429.53 * J/(kg*K)    # spezifische Wärmekapazität
rho.Lita  = 7450 * kg/m**3       # Dichte
p.Lita    = -1.7e-4 * C/(m**2*K) # pyroelektrischer Koeffizient
#
cv_T.Lita = c_T.Lita * rho.Lita      # volumenspez. Wärmekapazität 'Ws/m³K'
a_T.Lita = lambda_T.Lita/cv_T.Lita  # Thermische Diffusionskonstante ,'m²/s')

heading("Materialkonstanten")
printout("cv_T(\LiTa) =", cv_T.Lita)
printout("a_T(\LiTa) =", a_T, "=", a_T.Lita)


# Zwischengrößen
# ==============
# Wärmeleitwert
# -------------
# ::
# 
# 
# ::

G_T = lambda_T * A / l

G_T.Luft_oben = G_T.subs([lambda_T == lambda_T.Luft, 
                          A == A_pix, l == d_Luft.oben ])
G_T.Luft_unten = G_T.subs([lambda_T == lambda_T.Luft,
                           A == A_pix, l == d_Luft.unten ])
G_T.Luft = G_T.Luft_oben + G_T.Luft_unten

heading("Wärmeleitwert")
printout("G_T =", G_T)
printout("G_T(Luft oben) =", G_T.Luft_oben)
printout("G_T(Luft unten) =", G_T.Luft_unten)
printout("G_T(Luft) =", G_T.Luft)

# Wärmekapazität
# --------------
# ::

C_T = cv_T * V
C_T.pix = V_pix * cv_T.Lita

heading("Wärmekapazität")
printout("C_T =", C_T)
printout("C_T(pix) =", C_T.pix)

# Wärmeleitwert der Kapazität
G_T.C = I * omega * C_T
G_T.C.pix = I * omega * C_T.pix
G_T.C.pix.omega_ch = G_T.C.pix.subs(omega == omega.ch.evalf())

heading("kapazitiver Wärmeleitwert")
printout("G_T(C) =", G_T.C)
printout("G_T(C_{pix}) =", G_T.C.pix)
printout("G_T(C_{pix}, \wch) =", G_T.C.pix.omega_ch)


# Lösung
# ======
# ::

heading("Lösungen")

# mittlere Temperaturdifferenz
# ----------------------------
# ::

T_quer = Phi / G_T
T_quer.pix = Phi_quer / G_T.Luft

heading("mittlere Temperatur")
printout("<T>=", T_quer)
printout("<T>(pix)=", T_quer.pix)

# Temperaturdifferenz bei sinusförmiger Zeitabhängigkeit
# ------------------------------------------------------
# 
# ::

heading("sinusförmige Zeitabhängigkeit mit omega_ch")

heading("Wärmeleitwerte")

printout("G_T(Luft) =", G_T.Luft)
printout("G_T(C_{pix}) =", G_T.C.pix)

G_T.omega = G_T.Luft + G_T.C.pix 

# Zusammenfassen der Einheiten
#G_T.omega = G_T.omega.collect(W).collect(K)
G_T.omega.ch = G_T.omega.subs(omega==omega.ch)
printout("G^~(\omega) =", G_T.omega)
printout("G^~(\omega=\omega_{ch}) =", G_T.omega.ch)

T_0 = Phi_0.evalf() / G_T.omega
T_0.ch = T_0.subs(omega == omega.ch.evalf())
T_sin = T_0 * exp(I*omega*t)
T_sin.ch = T_sin.subs(omega == omega.ch.evalf())

heading("Temperatur")

heading("Temperaturamplitude")
printout("komplexe Temperatuamplitude")
printout("T_0 =", T_0)
printout("reelle Temperatuamplitude")
printout("|T_0(\omega)| =", abs(T_0.subs([W==1, s==1, K==1]))*K)   # abs(K) == K
printout("für f_ch = 128 Hz")
printout("T_0(\omega_{ch}) =", T_0.ch)
printout("|T_0(\omega_{ch})| =", abs(T_0.ch/K)*K)   # abs(K) == K

heading("Zeitverlauf Sinus")
printout("T^~(\omega_{ch}) =", T_sin.ch)
printout("|T^~(\omega_{ch})| =", abs(T_sin.ch))

# printout("T^~ =", real(T_sin))
# 
# ::

printout("T_0 =")
printout(T_0.expand())
printout(T_0.collect(K))
printout(T_0.collect(I))
printout(T_0.simplify_indexed())
# printout(type(T_0)
# pprint( dir(T_0))

# Plotting
# --------
# 
# ::

# open a gnuplot session
gp =  Gnuplot.Gnuplot(persist=True)
# gp("set size 0.8,0.5")
# gp.xlabel('x [cm]')
# gp("set xtics 0.25");
# gp("set ytics 1");
# gp.ylabel('s(x) [beliebige Einheiten]')

gp("I = {0,1}")

funs = [Gnuplot.Func('x**2', title='calculated by gnuplot'),
        Gnuplot.Func('real(exp(I*x))', title='Re(e^Ix)')
       ]
# gp.plot(*funs)
# gp.hardcopy(filename="T_0d.eps", mode="eps", fontsize=14)
# os.system("gv T_0d.eps")

