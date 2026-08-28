# Roadmap riguroso para leer *The Economics of Bicycles for the Mind*

Este mapa organiza el paper por dependencia lógica, no por número de página. La
regla de lectura es simple: no se debe interpretar una proposición hasta haber
identificado qué objeto varía, qué elige el agente y en qué región del problema
se está trabajando.

## 1. El mapa completo

```text
Bloque A. Primitivas y secuencia temporal
  s, alpha, gamma(t), Delta, theta, e_t
  p(s e_t; theta), c(e_t; theta)
          |
          v
Bloque B. Problema estático por oportunidad
  M(e; s, alpha, Delta, theta)
  existencia / interioridad / condición de primer orden
          |
          +---------------------> Proposición 1
          |
          v
Bloque C. Llegada de oportunidades
  Pr(llegar a t) = producto de gamma(i)
  descuento delta^t
  Gamma = gamma0 / (1 - delta gamma)
          |
          +---------------------> Proposición 2
          |
          v
Bloque D. Especialización de la Sección 4
  p = sqrt(s e + theta), c = e
  e* interior y condición e* > 0
  V = Gamma[alpha^2 Delta^2 s/4 + theta/s]
          |
          v
Bloque E. Heterogeneidad y momentos
  independencia de alpha, Gamma y s
  media, varianza, covarianza
  derivada afín a0 + 2 theta Var(Gamma/s)
          |
          +---------------------> Proposición 3
          |                         |-- caída inicial: condición (H)
          |                         |-- giro: Var(Gamma/s) > 0
          |                         |-- giro antes de 1: theta* < 1
          |                         `-- dominio: e*(theta) > 0
          v
Bloques F y G. Extensiones del mecanismo
  automatización y organización en equipos
          |
          +---------------------> Proposiciones 4 y 5
```

Para entender la Proposición 3 no basta con leer su enunciado. Se necesitan,
en este orden, los Bloques A, B, C, la solución interior del Bloque D y las
identidades de momentos del Bloque E.

## 2. Diccionario: qué es primitivo, qué se elige y qué se deriva

| Símbolo | Naturaleza | Quién lo determina | Interpretación |
|---|---|---|---|
| `s` | parámetro individual | dado para el agente; heterogéneo en la población | habilidad de implementar |
| `alpha` | parámetro individual | dado para el agente | probabilidad de elegir la acción con payoff |
| `gamma(t)` | parámetro individual y temporal | dado para el agente | probabilidad de reconocer la oportunidad de la ronda `t` |
| `Delta` | parámetro tecnológico | dado | valor creado por una implementación correcta |
| `theta` | calidad de la herramienta | exógena en el problema individual | capacidad de la herramienta cognitiva |
| `e_t` | variable de decisión | elegida por el agente | esfuerzo de implementación en la ronda `t` |
| `p(s e_t; theta)` | resultado tecnológico | función primitiva | probabilidad de implementación exitosa |
| `c(e_t; theta)` | costo | función primitiva | costo de esfuerzo |
| `M` | objetivo derivado | se evalúa y luego maximiza | retorno neto condicional a haber visto una oportunidad |
| `Gamma` | multiplicador derivado | resulta de `gamma0`, `gamma` y `delta` | número esperado descontado de oportunidades aprovechables |
| `V` | resultado derivado | valor optimizado total | valor presente esperado de la secuencia de mejoras |

La distinción decisiva es esta:

```text
Para un individuo: s, alpha y gamma están dados; e se elige.
Para el análisis transversal: s, alpha y gamma varían entre individuos.
```

Por eso `s` puede ser simultáneamente “dado” en la optimización y “aleatorio” en
la varianza poblacional. No hay contradicción: son dos niveles de análisis.

## 3. Por qué aparece el producto `s e`

`s` no es un conjunto; es un escalar positivo. El producto `s e` representa
**input efectivo de implementación**. Dos personas pueden gastar el mismo
esfuerzo `e`, pero quien tiene mayor `s` transforma ese esfuerzo en más capacidad
efectiva.

La probabilidad se escribe

```text
p(s e; theta)
```

porque depende de dos canales distintos:

1. `s e`: capacidad humana efectiva, que combina habilidad y esfuerzo;
2. `theta`: contribución directa o cambio tecnológico producido por la
   herramienta.

En la forma funcional de la Sección 4,

```text
p(s e; theta) = sqrt(s e + theta).
```

Aquí una unidad adicional de `theta` sustituye input efectivo humano. Esta forma
es útil porque genera una solución cerrada, pero no es inocua: si `p` se lee
literalmente como probabilidad, el dominio debe garantizar `p <= 1` o la función
debe normalizarse. Esa restricción no es necesaria para comprobar la identidad
algebraica de la Proposición 3, pero sí para una interpretación probabilística
global.

## 4. Qué es realmente `M`

La notación abreviada del paper,

```text
M(e; theta) = p(s e; theta) alpha Delta - c(e; theta),
```

oculta parámetros. Una notación completamente explícita sería

```text
M(e; s, alpha, Delta, theta)
  = p(s e; theta) alpha Delta - c(e; theta).
```

Sí depende de `s`, aunque el paper no lo muestre después del punto y coma. `s`
no se elige: el agente conoce su tipo y elige `e` condicionado en él.

`M` tampoco es el valor de toda la vida del problema. Es el retorno neto
esperado **de una oportunidad que ya fue reconocida**:

- `p`: probabilidad de implementar bien;
- `alpha`: probabilidad de haber elegido la acción que crea valor;
- `Delta`: valor si ambas cosas salen bien;
- `c`: costo pagado por el esfuerzo.

El problema estático correcto es

```text
e*(s, alpha, theta) in argmax_{e >= 0} M(e; s, alpha, Delta, theta).
```

## 5. ¿Hace falta especificar `c(e; theta)`?

La respuesta depende de la pregunta.

### Modelo general

No hace falta una forma cerrada para obtener comparativas cualitativas. Bastan
hipótesis como crecimiento y convexidad de `c`, concavidad de `p`, existencia
del máximo y una condición de *single crossing* o razón marginal que ordene el
efecto de `theta` sobre el esfuerzo.

Estas hipótesis permiten afirmar direcciones, no números. Una prueba rigurosa
debe mencionar además si el máximo es único y cómo se tratan las esquinas.

### Proposición 3

Sí hace falta. La Sección 4 fija

```text
c(e) = e
```

y hace entrar la herramienta por `p`, no directamente por el costo. Sin esa
linealidad no se obtienen exactamente

```text
e* = alpha^2 Delta^2 s / 4 - theta/s
V  = Gamma[alpha^2 Delta^2 s/4 + theta/s].
```

Otra función de costo puede preservar la intuición y cambiar por completo la
curvatura, el punto de giro y la solución de esquina. Por eso no se debe usar la
Proposición 3 como si fuera un teorema para cualquier `c`.

## 6. Por qué el valor esperado contiene productos de `gamma`

Sea `R_t` el indicador de que el agente llega a la oportunidad `t`. Para llegar
a ella debe reconocer la inicial y cada oportunidad intermedia. Bajo la
estructura secuencial del modelo,

```text
E[R_t] = Pr(R_t = 1) = producto desde i=0 hasta t de gamma(i).
```

Si el retorno neto optimizado de cada oportunidad es `M(e*; theta)`, el valor
presente esperado es

```text
V(theta)
  = sumatoria sobre t de
      delta^t [producto de gamma(i), i=0,...,t] M(e*; theta).
```

La igualdad usa linealidad de la esperanza. El producto de `gamma` no es un
factor de éxito técnico: es la probabilidad de que la cadena de reconocimiento
permanezca viva hasta esa ronda. El éxito técnico ya está dentro de `p` y, por
lo tanto, dentro de `M`.

Cuando

```text
gamma(0) = gamma0,
gamma(t) = gamma para t > 0,
```

los pesos son `gamma0 (delta gamma)^t`. Si `delta gamma < 1`, la serie geométrica
da

```text
Gamma = gamma0 / (1 - delta gamma),
V(theta) = Gamma M(e*(theta); theta).
```

Sí: `V` es una especie de valor presente esperado. `delta` descuenta el futuro;
`gamma` reduce la probabilidad de alcanzar rondas futuras. `Gamma` puede superar
uno porque no es una probabilidad: es el número esperado **descontado** de
oportunidades que generan el retorno `M`.

## 7. Cadena de prueba de la Proposición 3

### Lema 1. Concavidad y condición de primer orden

Con

```text
M(e; theta) = alpha Delta sqrt(s e + theta) - e,
```

la derivada interior es

```text
dM/de = alpha Delta s / [2 sqrt(s e + theta)] - 1.
```

La segunda derivada es negativa cuando `alpha`, `Delta` y `s` son positivos.
Por tanto, cualquier solución interior de la condición de primer orden es el
único máximo interior.

### Lema 2. Candidato y dominio interior

La FOC implica

```text
2 sqrt(s e + theta) = alpha Delta s.
```

Ambos lados son no negativos bajo las hipótesis económicas, de modo que se
puede elevar al cuadrado sin introducir una raíz espuria:

```text
4(s e + theta) = alpha^2 Delta^2 s^2.
```

Como `s > 0`, despejar da

```text
e* = alpha^2 Delta^2 s/4 - theta/s.
```

Este candidato es estrictamente positivo si y solo si

```text
theta < alpha^2 Delta^2 s^2/4.
```

Esta condición debe comprobarse por individuo, no solo en promedio.

### Lema 3. Valor interior

La FOC también da

```text
sqrt(s e* + theta) = alpha Delta s/2.
```

Al sustituir en `M` y luego restar `e*`, se obtiene

```text
M(e*; theta) = alpha^2 Delta^2 s/4 + theta/s,
V(theta) = Gamma[alpha^2 Delta^2 s/4 + theta/s].
```

Esta sustitución y la equivalencia de interioridad están comprobadas por Lean.

### Lema 4. Media

Defina

```text
X = alpha^2 Delta^2 s/4,
Y = 1/s.
```

Entonces `V = Gamma(X + theta Y)`. Bajo la independencia asumida,

```text
E[V] = E[Gamma](E[X] + theta E[Y]),
dE[V]/dtheta = E[Gamma] E[1/s] > 0.
```

La desigualdad estricta necesita soporte positivo e integrabilidad.

### Lema 5. Varianza

Expanda primero el cuadrado, sin apelar a intuición:

```text
Var(V)
  = E[Gamma^2 (X + theta Y)^2]
    - E[Gamma(X + theta Y)]^2.
```

La independencia de `Gamma` respecto de `(X,Y)` permite factorizar los momentos.
Después se expande `(X + theta Y)^2` y se usan las independencias entre `alpha`
y `s`. Al agrupar términos se llega a

```text
d Var(V)/dtheta = a0 + 2 theta Var(Gamma/s),

a0 = Delta^2 E[alpha^2]/2
     [E[Gamma^2] - E[Gamma]^2 E[s]E[1/s]].
```

Este es el punto exacto donde las hipótesis de independencia son esenciales.
Con correlación aparecen covarianzas adicionales.

### Lema 6. Qué implica y qué no implica la condición (H)

La condición

```text
E[Gamma^2]/E[Gamma]^2 < E[s]E[1/s]
```

es equivalente a `a0 < 0`. Por ello la varianza cae en `theta=0`.

Si además

```text
q = Var(Gamma/s) > 0,
```

la derivada es una recta de pendiente `2q > 0` y cruza cero una sola vez en

```text
theta* = -a0/(2q) > 0.
```

Pero afirmar que ya es positiva en `theta=1` requiere

```text
theta* < 1
```

o, de forma equivalente,

```text
a0 + 2 Var(Gamma/s) > 0.
```

La condición (H) no implica esta desigualdad adicional. El contraejemplo exacto
del informe de validación produce `theta*=12/5` y derivada `-14/45` en uno.

### Lema 7. No confundir dos varianzas

La ganancia individual respecto del estado sin herramienta es

```text
B(theta) = V(theta) - V(0) = theta Gamma/s.
```

Luego

```text
Var(B(theta)) = theta^2 Var(Gamma/s).
```

Esta varianza sí crece estrictamente para `theta>0` cuando
`Var(Gamma/s)>0`. No contradice que `Var(V(theta))` caiga al principio: una mide
la dispersión de niveles totales y la otra la dispersión de ganancias.

## 8. Cómo leer las proposiciones con rigor

Para cada proposición deben anotarse cuatro columnas antes de interpretar:

| Pregunta de control | Ejemplo para la Proposición 3 |
|---|---|
| ¿Qué hipótesis se usan? | forma funcional, independencia, momentos finitos, interioridad |
| ¿Qué objeto cambia? | calidad exógena `theta` |
| ¿Qué conclusión matemática exacta se obtiene? | signos de derivadas y punto de giro |
| ¿En qué dominio vale? | donde `e*(theta)>0` para los tipos analizados |

Un enunciado económico debe rebajarse al resultado matemático realmente
demostrado si falla cualquiera de esas columnas. En particular:

- “la herramienta reduce esfuerzo” requiere comparar óptimos y controlar
  unicidad/esquinas;
- “la herramienta eleva valor” puede probarse por valor revelado si la acción
  antigua sigue siendo factible y la herramienta mejora débilmente el retorno;
- “la desigualdad es U-shaped” requiere intercepto negativo, pendiente positiva,
  que el giro esté dentro del dominio relevante y que la fórmula de valor siga
  siendo válida allí;
- “la herramienta amplifica juicio de oportunidad” se deriva de que mayor
  `gamma` eleva `Gamma`, siempre que el retorno por oportunidad sea positivo.

## 9. Orden recomendado de estudio

1. Memorizar el diccionario de la Sección 2.
2. Dibujar la secuencia “reconocer oportunidad, elegir acción, implementar”.
3. Derivar `M` y distinguirlo de `V`.
4. Derivar la serie que produce `Gamma`.
5. Probar concavidad, FOC e interioridad antes de usar la fórmula cerrada.
6. Derivar la media de `V`.
7. Expandir la varianza desde `E[V^2]-E[V]^2`.
8. Identificar por separado `a0`, `q` y `theta*`.
9. Comprobar el endpoint y la primera esquina.
10. Solo entonces interpretar sustitución, complementariedad y desigualdad.

Al completar estos diez pasos se puede leer la Proposición 3 sin depender de la
prosa del paper y se está listo para reproducir la *hand derivation* de manera
consciente, no mecánica.
