### NumPy Mathematische Funktionen (https://numpy.org/doc/stable/reference/routines.math.html)

## Trigonometrische Funktionen:
# numpy.sin(x): Trigonometrischer Sinus, elementweise.
# numpy.cos(x): Kosinus, elementweise.
# numpy.tan(x): Tangens, elementweise.
# numpy.arcsin(x) / numpy.asin(x): Inverser Sinus, elementweise.
# numpy.arccos(x) / numpy.acos(x): Inverser Kosinus, elementweise.
# numpy.arctan(x) / numpy.atan(x): Inverser Tangens, elementweise.
# numpy.hypot(x1, x2): Gibt die Hypotenuse eines rechtwinkligen Dreiecks zurück.
# numpy.arctan2(x1, x2) / numpy.atan2(x1, x2): Elementweiser Arkustangens von x1/x2 unter Berücksichtigung des Quadranten.
# numpy.degrees(x): Konvertiert Winkel von Radiant in Grad.
# numpy.radians(x): Konvertiert Winkel von Grad in Radiant.
# numpy.unwrap(p): Entpackt durch Komplement großer Deltas bezüglich der Periode.
# numpy.deg2rad(x): Konvertiert Winkel von Grad in Radiant.
# numpy.rad2deg(x): Konvertiert Winkel von Grad in Radiant.

## Hyperbolische Funktionen:
# numpy.sinh(x): Hyperbolischer Sinus, elementweise.
# numpy.cosh(x): Hyperbolischer Kosinus, elementweise.
# numpy.tanh(x): Hyperbolischer Tangens, elementweise.
# numpy.arcsinh(x) / numpy.asinh(x): Inverser hyperbolischer Sinus, elementweise.
# numpy.arccosh(x) / numpy.acosh(x): Inverser hyperbolischer Kosinus, elementweise.
# numpy.arctanh(x) / numpy.atanh(x): Inverser hyperbolischer Tangens, elementweise.

## Runden:
# numpy.round(a) / numpy.around(a): Rundet auf die nächste ganze Zahl oder auf eine bestimmte Anzahl von Dezimalstellen.
# numpy.rint(x): Rundet die Elemente eines Arrays auf die nächste ganze Zahl.
# numpy.fix(x): Rundet auf die nächste ganze Zahl in Richtung Null.
# numpy.floor(x): Gibt den Bodenwert (kleinste ganze Zahl <= x) des Inputs zurück, elementweise.
# numpy.ceil(x): Gibt den Deckenwert (größte ganze Zahl >= x) des Inputs zurück, elementweise.
# numpy.trunc(x): Gibt den abgeschnittenen Wert (ganzzahliger Teil) des Inputs zurück, elementweise.

## Summen, Produkte, Differenzen:
# numpy.prod(a): Gibt das Produkt der Array-Elemente über eine gegebene Achse zurück.
# numpy.sum(a): Gibt die Summe der Array-Elemente über eine gegebene Achse zurück.
# numpy.nanprod(a): Gibt das Produkt der Array-Elemente über eine gegebene Achse zurück, wobei NaN-Werte als Einsen behandelt werden.
# numpy.nansum(a): Gibt die Summe der Array-Elemente über eine gegebene Achse zurück, wobei NaN-Werte als Null behandelt werden.
# numpy.cumsum(a): Gibt die kumulative Summe der Elemente entlang einer gegebenen Achse zurück.
# numpy.cumprod(a): Gibt das kumulative Produkt der Elemente entlang einer gegebenen Achse zurück.
# numpy.nancumprod(a): Gibt das kumulative Produkt der Array-Elemente über eine gegebene Achse zurück, wobei NaN-Werte als Einsen behandelt werden.
# numpy.nancumsum(a): Gibt die kumulative Summe der Array-Elemente über eine gegebene Achse zurück, wobei NaN-Werte als Null behandelt werden.
# numpy.diff(a): Berechnet die n-te diskrete Differenz entlang der gegebenen Achse.
# numpy.ediff1d(ary): Die Differenzen zwischen aufeinanderfolgenden Elementen eines Arrays.
# numpy.gradient(f): Gibt den Gradienten eines N-dimensionalen Arrays zurück.
# numpy.cross(a, b): Gibt das Kreuzprodukt zweier (Arrays von) Vektoren zurück.
# numpy.trapezoid(y): Integriert entlang der gegebenen Achse unter Verwendung der zusammengesetzten Trapezregel.

## Exponenten und Logarithmen:
# numpy.exp(x): Berechnet die Exponentialfunktion für alle Elemente im Eingabe-Array.
# numpy.expm1(x): Berechnet exp(x) - 1 für alle Elemente im Array.
# numpy.exp2(x): Berechnet 2**p für alle p im Eingabe-Array.
# numpy.log(x): Natürlicher Logarithmus, elementweise.
# numpy.log10(x): Zehnerlogarithmus, elementweise.
# numpy.log2(x): Zweierlogarithmus.
# numpy.log1p(x): Gibt den natürlichen Logarithmus von eins plus dem Eingabe-Array zurück, elementweise.
# numpy.logaddexp(x1, x2): Logarithmus der Summe der Exponentiationen der Eingaben.
# numpy.logaddexp2(x1, x2): Logarithmus der Summe der Exponentiationen der Eingaben zur Basis 2.

## Andere spezielle Funktionen:
# numpy.i0(x): Modifizierte Bessel-Funktion erster Art, Ordnung 0.
# numpy.sinc(x): Gibt die normalisierte Sinc-Funktion zurück.

## Gleitkommaroutinen:
# numpy.signbit(x): Gibt elementweise True zurück, wenn das Vorzeichenbit gesetzt ist (kleiner als Null).
# numpy.copysign(x1, x2): Ändert das Vorzeichen von x1 auf das von x2, elementweise.
# numpy.frexp(x): Zerlegt die Elemente von x in Mantisse und Zweierpotenz.
# numpy.ldexp(x1, x2): Gibt x1 * 2**x2 zurück, elementweise.
# numpy.nextafter(x1, x2): Gibt den nächsten Gleitkommawert nach x1 in Richtung x2 zurück, elementweise.
# numpy.spacing(x): Gibt den Abstand zwischen x und der nächsten benachbarten Zahl zurück.

## Rationale Routinen:
# numpy.lcm(x1, x2): Gibt das kleinste gemeinsame Vielfache von |x1| und |x2| zurück.
# numpy.gcd(x1, x2): Gibt den größten gemeinsamen Teiler von |x1| und |x2| zurück.

## Arithmetische Operationen:
# numpy.add(x1, x2): Addiert Argumente elementweise.
# numpy.reciprocal(x): Gibt den Kehrwert des Arguments zurück, elementweise.
# numpy.positive(x): Numerisch positiv, elementweise.
# numpy.negative(x): Numerisch negativ, elementweise.
# numpy.multiply(x1, x2): Multipliziert Argumente elementweise.
# numpy.divide(x1, x2): Dividiert Argumente elementweise.
# numpy.power(x1, x2) / numpy.pow(x1, x2): Erste Array-Elemente potenziert mit Potenzen aus dem zweiten Array, elementweise.
# numpy.subtract(x1, x2): Subtrahiert Argumente, elementweise.
# numpy.true_divide(x1, x2): Dividiert Argumente elementweise.
# numpy.floor_divide(x1, x2): Gibt die größte ganze Zahl kleiner oder gleich der Division der Eingaben zurück.
# numpy.float_power(x1, x2): Erste Array-Elemente potenziert mit Potenzen aus dem zweiten Array, elementweise.
# numpy.fmod(x1, x2) / numpy.mod(x1, x2) / numpy.remainder(x1, x2): Gibt den elementweisen Rest der Division zurück.
# numpy.modf(x): Gibt den gebrochenen und ganzzahligen Teil eines Arrays zurück, elementweise.
# numpy.divmod(x1, x2): Gibt elementweisen Quotienten und Rest gleichzeitig zurück.

## Umgang mit komplexen Zahlen:
# numpy.angle(z): Gibt den Winkel des komplexen Arguments zurück.
# numpy.real(val): Gibt den Realteil des komplexen Arguments zurück.
# numpy.imag(val): Gibt den Imaginärteil des komplexen Arguments zurück.
# numpy.conj(x) / numpy.conjugate(x): Gibt das komplex Konjugierte zurück, elementweise.

## Extrema finden:
# numpy.maximum(x1, x2) / numpy.max(a) / numpy.amax(a): Elementweises Maximum von Array-Elementen.
# numpy.fmax(x1, x2): Elementweises Maximum von Array-Elementen.
# numpy.nanmax(a): Gibt das Maximum eines Arrays oder das Maximum entlang einer Achse zurück, wobei NaN-Werte ignoriert werden.
# numpy.minimum(x1, x2) / numpy.min(a) / numpy.amin(a): Elementweises Minimum von Array-Elementen.
# numpy.fmin(x1, x2): Elementweises Minimum von Array-Elementen.
# numpy.nanmin(a): Gibt das Minimum eines Arrays oder das Minimum entlang einer Achse zurück, wobei NaN-Werte ignoriert werden.

## Sonstiges:
# numpy.convolve(a, v): Gibt die diskrete, lineare Faltung zweier eindimensionaler Sequenzen zurück.
# numpy.clip(a): Beschneidet (begrenzt) die Werte in einem Array.
# numpy.sqrt(x): Gibt die nicht-negative Quadratwurzel eines Arrays zurück, elementweise.
# numpy.cbrt(x): Gibt die Kubikwurzel eines Arrays zurück, elementweise.
# numpy.square(x): Gibt das elementweise Quadrat des Inputs zurück.
# numpy.absolute(x) / numpy.fabs(x): Berechnet den Absolutwert elementweise.
# numpy.sign(x): Gibt eine elementweise Angabe des Vorzeichens einer Zahl zurück.
# numpy.heaviside(x1, x2): Berechnet die Heaviside-Sprungfunktion.
# numpy.nan_to_num(x): Ersetzt NaN durch Null und Unendlich durch große endliche Zahlen.
# numpy.real_if_close(a): Wenn der Input komplex ist und alle Imaginärteile nahe Null liegen, werden die Realteile zurückgegeben.
# numpy.interp(x, xp, fp): Eindimensionale lineare Interpolation für monoton steigende Abtastpunkte.
# numpy.bitwise_count(x): Berechnet die Anzahl der 1-Bits im Absolutwert von x.


### Informationen zu Farben, Markern und Linienstilen in Matplotlib ---
## Farben für den 'plot'-Befehl:
# 'b': Blau
# 'g': Grün
# 'r': Rot
# 'c': Cyan
# 'm': Magenta
# 'y': Gelb
# 'k': Schwarz
# 'w': Weiß

## Marker für die Datenpunkte im 'plot'-Befehl:
# '.': Punkt
# ',': Pixel
# 'o': Kreis
# 'v': Dreieck nach unten
# '^': Dreieck nach oben
# '<': Dreieck nach links
# '>': Dreieck nach rechts
# 's': Quadrat
# 'p': Fünfeck
# '*': Stern
# 'h': Sechseck 1
# 'H': Sechseck 2
# '+': Pluszeichen
# 'x': Kreuz
# 'D': Raute
# 'd': dünne Raute
# '|': senkrechte Linie
# '_': waagerechte Linie

## Linienstile für den 'plot'-Befehl:
# '-' : durchgezogen (solid line)
# '--' : gestrichelt (dashed line)
# '-.' : punktiert-gestrichelt (dash-dot line)
# ':' : gepunktet (dotted line)


## NumPy - enthält Arrays und Matrizen
# Jede Matrix ist ein Array, aber nicht jedes Array eine Matrix!
import numpy as np

# 1. Erstellen der Arrays
# -----------------------
array_plot = np.array([2, 1, 5, 7, 4, 6, 8, 14, 10, 9, 18, 20, 22])
array_2d = np.array([[1, 2, 3],
                    [4, 5, 6]])

array_3d = np.array([[[1, 2], [3, 4]],
                    [[5, 6], [7, 8]]])

# 2. Anwendung der mathematischen Funktionen auf das 2D Array
# ----------------------------------------------------------
sin_2d = np.sin(array_2d)
sqrt_2d = np.sqrt(array_2d)
sum_2d = np.sum(array_2d)
mean_2d = np.mean(array_2d)
exp_2d = np.exp(array_2d)

# 3. Anwendung der mathematischen Funktionen auf das 3D Array
# ----------------------------------------------------------
cos_3d = np.cos(array_3d)
cbrt_3d = np.cbrt(array_3d)
prod_3d = np.prod(array_3d)
max_3d = np.max(array_3d)
log_3d = np.log(array_3d)

# 4. Ouput zum 2D Array
# -----------------------------
print(array_2d)
print(sin_2d)
print(sqrt_2d)
print(sum_2d)
print(mean_2d)
print(exp_2d)
print (array_2d.shape)
print (array_2d.size)
print (array_2d.T)

# 5. Output zum 3D Array
# -----------------------------
print(array_3d)
print(cos_3d)
print(cbrt_3d)
print(prod_3d)
print(max_3d)
print(log_3d)

# 6. Ploting der Arrays
# -----------------------------
import matplotlib.pyplot as plt
plt.plot(array_plot, 'r-')   # 'r-' für rote, durchgezogene Linie
plt.plot(array_plot, 'k.')   # 'k.' für schwarze Punkte
# plt.show() wäre hier nur nötig, wenn ich unten keinen Befehl dafür hätte

# 7. Erstellen einer 3D-Figur
# -----------------------------
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
X = np.arange(-5, 5, 0.15)
Y = np.arange(-5, 5, 0.15)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
plt.show()