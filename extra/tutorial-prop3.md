# Tutorial de inmersión: *The Economics of Bicycles for the Mind*

Este tutorial está pensado para poder explicar el paper en voz alta y, al mismo
tiempo, reconstruir la matemática sin saltos. El foco es la Proposición 3 porque
allí se encuentra el mecanismo distributivo más interesante y también el punto
en el que una lectura rápida -humana o de un LLM- es más peligrosa.

## 1. La pregunta, no solo el tema

El tema es “IA, productividad y desigualdad”. La pregunta concreta es:

> Cuando una herramienta cognitiva facilita ejecutar mejoras, ¿reduce el valor
> de las habilidades humanas o amplifica algunas de ellas, y qué implica esa
> interacción para el esfuerzo, la productividad y la desigualdad salarial?

La respuesta corta es que no existe una sola “habilidad humana”. La herramienta
reemplaza parcialmente la capacidad de **implementar**, pero multiplica el valor
de ser capaz de **encontrar oportunidades**. El papel de saber **qué acción genera
valor** puede ser complementario o sustitutivo según el efecto total de la
herramienta sobre la probabilidad de éxito.

## 2. Los tres tipos de capacidad humana

La distinción conceptual más importante del paper es la siguiente.

| Símbolo | Nombre | Pregunta económica |
|---|---|---|
| $s$ | implementation skill | Dado un esfuerzo, ¿qué tan eficazmente lo convierto en implementación? |
| $\alpha$ | payoff judgment | Dado un estado o resultado, ¿sé qué acción extrae valor? |
| $\gamma(t)$ | opportunity judgment | ¿Me doy cuenta de que existe otra mejora que vale la pena intentar? |

Una analogía útil es editar un artículo académico:

- $s$ es la capacidad de ejecutar correctamente una corrección;
- $\alpha$ es saber cuál corrección mejora realmente el argumento;
- $\gamma(t)$ es detectar que todavía hay otra debilidad que corregir.

El modelo es iterativo. En cada ronda primero debe aparecer una oportunidad. Si
aparece, el agente decide cuánto esfuerzo de implementación ejercer. Si no
aparece, el proceso termina.

## 3. El problema estático dentro de cada ronda

Condicional en haber detectado una oportunidad, el agente elige $e_t\ge 0$:

$$
\max_{e_t\ge0}\;M(e_t;\theta)
=p(se_t;\theta)\alpha\Delta-c(e_t;\theta).
$$

Cada factor tiene una función distinta:

1. $p(se_t;\theta)$ es la probabilidad de implementar con éxito.
2. $\alpha$ es la probabilidad de convertir ese éxito técnico en valor.
3. $\Delta$ es el valor incremental si ambos pasos funcionan.
4. $c(e_t;\theta)$ es el costo del esfuerzo.
5. $\theta$ mide la calidad de la herramienta cognitiva.

Si la solución es interior, la condición de primer orden es

$$
p_e(se_t^*;\theta)s\alpha\Delta=c_e(e_t^*;\theta).
$$

Lectura económica: el beneficio marginal de una unidad adicional de esfuerzo,
ajustado por habilidad y juicio, se iguala con su costo marginal.

## 4. Cómo entra la dinámica sin cambiar la elección de esfuerzo

Cuando $\gamma(0)=\gamma_0$ y $\gamma(t)=\gamma$ para $t>0$, el valor esperado es

$$
V(\theta)=\frac{\gamma_0}{1-\delta\gamma}
M(e^*(\theta);\theta)=\Gamma M(e^*(\theta);\theta),
\qquad
\Gamma\equiv\frac{\gamma_0}{1-\delta\gamma}.
$$

El multiplicador $\Gamma$ resume cuántas oportunidades, descontadas, logra
explotar el agente. No modifica el esfuerzo óptimo dentro de una oportunidad
porque el problema de cada ronda es el mismo. Sí amplifica el valor de cualquier
ventaja que el agente tenga dentro de la ronda.

## 5. Proposiciones 1 y 2: qué se puede afirmar en el modelo general

La Definición 1 llama “herramienta cognitiva” a una tecnología que, al aumentar
$\theta$:

- aumenta débilmente $p(se;\theta)$ y/o reduce $c(e;\theta)$;
- reduce estrictamente la razón entre beneficio marginal y costo marginal del
  esfuerzo humano, $p_e/c_e$.

De allí salen dos fuerzas:

- **Menos esfuerzo humano:** el óptimo se desplaza hacia un $e^*$ menor.
- **Mayor valor optimizado:** aun pudiendo imitar el esfuerzo anterior, el agente
  obtiene una probabilidad mayor o un costo menor; optimizar no puede dejarlo peor.

La herramienta siempre complementa el juicio de oportunidad porque $\Gamma$
multiplica la mejora de valor por oportunidad. En cambio, la complementariedad
con $\alpha$ depende de si

$$
p(se^*(1);1)>p(se^*(0);0).
$$

La herramienta mejora directamente la tecnología, pero también induce menos
esfuerzo. Sin una forma funcional adicional no sabemos cuál efecto domina en la
probabilidad de éxito realizada.

## 6. Especialización de la Sección 4

Para estudiar desigualdad, el paper fija

$$
p(se;\theta)=\sqrt{se+\theta},\qquad c(e)=e.
$$

Además supone que $\alpha,\gamma_0,\gamma,s$ son independientes y tienen soporte
positivo. La heterogeneidad de $V(\theta)$ se interpreta como desigualdad
salarial porque el paper identifica salarios con productividad marginal.

### 6.1 Derivación del esfuerzo óptimo

Sustituimos las formas funcionales:

$$
M(e;\theta)=\alpha\Delta\sqrt{se+\theta}-e.
$$

Derivamos con respecto a $e$:

$$
\frac{\partial M}{\partial e}
=\alpha\Delta\frac{s}{2\sqrt{se+\theta}}-1.
$$

La FOC interior es

$$
\alpha\Delta\frac{s}{2\sqrt{se^*+\theta}}=1.
$$

Ahora despejamos sin omitir pasos:

$$
2\sqrt{se^*+\theta}=\alpha\Delta s,
$$

$$
\sqrt{se^*+\theta}=\frac{\alpha\Delta s}{2},
$$

$$
se^*+\theta=\frac{\alpha^2\Delta^2s^2}{4},
$$

$$
\boxed{e^*(\theta)=\frac{\alpha^2\Delta^2s}{4}-\frac{\theta}{s}}.
$$

La segunda derivada es negativa para $se+\theta>0$, por lo que la FOC caracteriza
el máximo interior.

### 6.2 La restricción $e\ge0$ no es un detalle

La fórmula anterior es factible únicamente si

$$
e^*(\theta)>0
\iff
\boxed{\theta<\frac{\alpha^2\Delta^2s^2}{4}}.
$$

En $\theta=1$, esto exige $\Delta>2/(\alpha s)$ para cada agente. Ningún valor
finito de $\Delta$ puede mantener la solución interior para todo
$\theta\in[0,\infty)$. Cuando el umbral se cruza, la solución verdadera es la
esquina $e^*=0$.

Por tanto, el óptimo global es

$$
e^*(\theta)=
\max\left\{\frac{\alpha^2\Delta^2s}{4}-\frac{\theta}{s},0\right\}.
$$

### 6.3 Valor por oportunidad en la región interior

La FOC implica

$$
\sqrt{se^*+\theta}=\frac{\alpha\Delta s}{2}.
$$

Entonces

$$
\begin{aligned}
M(e^*;\theta)
&=\alpha\Delta\sqrt{se^*+\theta}-e^*\\
&=\alpha\Delta\left(\frac{\alpha\Delta s}{2}\right)
-\left(\frac{\alpha^2\Delta^2s}{4}-\frac{\theta}{s}\right)\\
&=\frac{\alpha^2\Delta^2s}{2}
-\frac{\alpha^2\Delta^2s}{4}+\frac{\theta}{s}\\
&=\boxed{\frac{\alpha^2\Delta^2s}{4}+\frac{\theta}{s}}.
\end{aligned}
$$

Multiplicando por las oportunidades:

$$
\boxed{V(\theta)=\Gamma
\left(\frac{\alpha^2\Delta^2s}{4}+\frac{\theta}{s}\right)}.
$$

La expresión separa tres componentes: $\Gamma$ amplifica; el término
$\alpha^2\Delta^2s/4$ favorece a quienes tienen mayor $s$; y $\theta/s$ da una
ventaja mayor a quienes tienen menor $s$.

### 6.4 Valor en la esquina

Si $\theta\ge \alpha^2\Delta^2s^2/4$, entonces $e^*=0$ y

$$
M(0;\theta)=\alpha\Delta\sqrt{\theta},
\qquad
V(\theta)=\Gamma\alpha\Delta\sqrt{\theta}.
$$

En esta región, la habilidad de implementación $s$ desaparece del valor. Por
eso no es válido extrapolar el término interior $\theta/s$ indefinidamente.

## 7. Proposición 3: media y varianza, línea por línea

Definamos

$$
X\equiv\frac{\alpha^2\Delta^2s}{4},
\qquad
Y\equiv\frac1s.
$$

En la región interior, $V(\theta)=\Gamma(X+\theta Y)$.

### 7.1 Media

Por independencia de $\Gamma$ respecto de $(\alpha,s)$:

$$
E[V(\theta)]=E[\Gamma]\{E[X]+\theta E[Y]\}.
$$

Por tanto,

$$
\boxed{\frac{dE[V(\theta)]}{d\theta}=E[\Gamma]E[1/s]>0}.
$$

La media aumenta linealmente mientras la solución se mantiene interior. En la
esquina también aumenta, pero a tasa decreciente, proporcional a
$1/\sqrt\theta$.

### 7.2 Identidad para la varianza de un producto independiente

Si $A$ y $B$ son independientes,

$$
\operatorname{Var}(AB)
=E[A^2]\operatorname{Var}(B)
+\operatorname{Var}(A)E[B]^2.
$$

Se comprueba expandiendo
$E[A^2B^2]-E[AB]^2$ y usando independencia. Aplicada a
$A=\Gamma$ y $B=X+\theta Y$:

$$
\operatorname{Var}(V(\theta))
=E[\Gamma^2]\operatorname{Var}(X+\theta Y)
+\operatorname{Var}(\Gamma)E[X+\theta Y]^2.
$$

### 7.3 Por qué aparece un polinomio cuadrático

Usamos

$$
\operatorname{Var}(X+\theta Y)
=\operatorname{Var}(X)+2\theta\operatorname{Cov}(X,Y)
+\theta^2\operatorname{Var}(Y).
$$

Como $X=(\Delta^2/4)\alpha^2s$ y $Y=1/s$,

$$
XY=\frac{\Delta^2}{4}\alpha^2,
$$

de modo que, usando independencia entre $\alpha$ y $s$,

$$
\operatorname{Cov}(X,Y)
=\frac{\Delta^2E[\alpha^2]}{4}
\left(1-E[s]E[1/s]\right)\le0.
$$

La desigualdad viene de Cauchy-Schwarz o Jensen:
$E[s]E[1/s]\ge1$, con igualdad solo si $s$ es constante. Este término negativo
es el **inverse skill bias**: el impulso $1/s$ es mayor precisamente para quienes
tenían menor productividad base proporcional a $s$.

Al coleccionar términos, la derivada toma la forma

$$
\boxed{
\frac{d\operatorname{Var}(V(\theta))}{d\theta}
=a_0+2\theta\operatorname{Var}(\Gamma/s)},
$$

con

$$
\boxed{
a_0=\frac{\Delta^2E[\alpha^2]}{2}
\left(E[\Gamma^2]-E[\Gamma]^2\mu_sE[1/s]\right)}.
$$

La segunda derivada es

$$
\frac{d^2\operatorname{Var}(V(\theta))}{d\theta^2}
=2\operatorname{Var}(\Gamma/s)\ge0.
$$

### 7.4 Qué hace exactamente la condición de heterogeneidad

La condición del paper es

$$
\frac{E[\Gamma^2]}{E[\Gamma]^2}<\mu_sE[1/s]. \tag{H}
$$

(H) equivale a $a_0<0$. Por ello garantiza que la varianza cae en
$\theta=0$. Si $\operatorname{Var}(\Gamma/s)>0$, la pendiente de la derivada es
positiva y existe un único cero algebraico:

$$
\boxed{\theta^*=-\frac{a_0}{2\operatorname{Var}(\Gamma/s)}>0}.
$$

Hasta aquí, la prueba es correcta dentro de la región interior.

## 8. La trampa de esta semana

### 8.1 ¿La varianza de qué?

Es $\operatorname{Var}(V(\theta))$ **a través de personas**. Mide dispersión de
productividad/valor y se interpreta como desigualdad salarial. No es:

- la varianza de las respuestas de una IA;
- la incertidumbre que enfrenta una persona;
- la varianza del beneficio individual de adoptar la herramienta.

### 8.2 ¿La U es incondicional?

No. Se requieren al menos tres capas:

1. (H) para obtener una pendiente inicial negativa;
2. $\operatorname{Var}(\Gamma/s)>0$ para una curvatura estrictamente positiva;
3. que el punto donde se afirma el giro pertenezca a la región interior.

Además, decir que la derivada es positiva en $\theta=1$ exige

$$
a_0+2\operatorname{Var}(\Gamma/s)>0
\iff
\boxed{\theta^*<1}.
$$

(H) solo da $\theta^*>0$; no da $\theta^*<1$.

### 8.3 ¿Qué ocurre con la varianza del beneficio individual?

Definamos el beneficio de la herramienta para una persona como

$$
B(\theta)=V(\theta)-V(0).
$$

En la región interior,

$$
B(\theta)=\theta\frac{\Gamma}{s}.
$$

Por tanto,

$$
\boxed{\operatorname{Var}(B(\theta))
=\theta^2\operatorname{Var}(\Gamma/s)}
$$

y

$$
\frac{d\operatorname{Var}(B(\theta))}{d\theta}
=2\theta\operatorname{Var}(\Gamma/s)>0
$$

para $\theta>0$ y heterogeneidad no degenerada. La dispersión del beneficio
individual aumenta aunque la dispersión del nivel total $V(\theta)$ esté
cayendo. No hay contradicción: la covarianza negativa entre productividad base
y ganancia puede comprimir los niveles al comienzo.

## 9. Un contraejemplo exacto al signo en $\theta=1$

Tome $\gamma_0=0.8$, $\gamma=0.4$, $\delta=0.5$ (de modo que
$\Gamma=1$), $\alpha=1$, $\Delta=4$, y dos tipos de habilidad igualmente
probables:

$$
s\in\{0.6,1\}.
$$

Se cumplen:

- soporte positivo;
- $\mu_s=0.8>3\sigma_s=0.6$;
- (H), pues $1<0.8\times(4/3)=16/15$;
- interioridad en todo $\theta\in[0,1]$, porque el tipo $s=0.6$ tiene umbral
  $\alpha^2\Delta^2s^2/4=1.44$.

En la fórmula interior,

$$
V(\theta,s)=4s+\frac\theta s.
$$

La varianza se minimiza en $\theta^*=2.4$. Por ello sigue cayendo en
$\theta=1$, aun cuando (H) se cumple. Esta es una refutación directa de la
segunda desigualdad de la ecuación (32), no del hecho más débil de que la
cuadrática tiene eventualmente una rama creciente.

## 10. Deslices internos documentables

### Desliz 1: el signo en $\theta=1$

La Proposición 3(b) escribe simultáneamente
$V'(0)<0$ y $V'(1)>0$ para la derivada de la varianza bajo (H). La prueba solo
establece una intersección positiva $\theta^*>0$. Falta $\theta^*<1$.

### Desliz 2: interioridad global

La Sección 4 deja $\theta\in[0,\infty)$ y usa una expresión interior que se hace
negativa para cada agente cuando $\theta$ es suficientemente grande. La
restricción $e\ge0$ obliga a una función por tramos. En consecuencia, la
cuadrática no describe globalmente la varianza.

### Desliz 3: el papel de $\alpha$ en la nota 14

La nota 14 afirma que, por ser independiente de la herramienta, $\alpha$ no
afecta la desigualdad absoluta. Sin embargo, $V(\theta)$ contiene
$\alpha^2\Delta^2s/4$, y tanto $a_0$ como $\theta^*$ contienen $E[\alpha^2]$.
Lo preciso es que el **tool boost directo** $\theta/s$ no contiene $\alpha$ en
esta forma funcional; no que $\alpha$ sea irrelevante para la varianza total.

## 11. Las cinco preguntas de lectura

### 1. ¿Cuál es la pregunta?

¿Qué capacidades humanas sustituye o complementa una herramienta cognitiva y
cómo esas interacciones determinan el esfuerzo, la productividad y la
desigualdad?

### 2. ¿Cuál es la respuesta?

La herramienta reduce el esfuerzo y la ventaja de la habilidad de
implementación, aumenta el valor de encontrar oportunidades y tiene una relación
ambigua con el juicio de payoff. La productividad media aumenta; la desigualdad
puede caer inicialmente y aumentar después, pero esa U es condicional y la
formulación publicada sobrestima lo que sus condiciones garantizan.

### 3. ¿Cómo llegan a la conclusión y se sigue de su análisis?

Construyen un modelo teórico de mejoras iterativas. Resuelven un problema estático
por oportunidad, lo multiplican por la secuencia esperada de oportunidades y
luego introducen heterogeneidad. La sustitución de esfuerzo y el aumento del
valor optimizado sí se siguen de la definición del instrumento, sujetas a
condiciones de interioridad y unicidad. La Proposición 3 se obtiene de una forma
funcional cuadrática muy útil para intuición, pero el signo en $\theta=1$ y la
extrapolación global no se siguen de los supuestos declarados.

No se estima el modelo ni se usan datos propios. La evidencia empírica citada se
usa para interpretar mecanismos, no para identificar por separado $s$, $\alpha$
y $\gamma$.

### 4. ¿Cuál es la contribución marginal?

Frente a la literatura de tareas y automatización, la contribución es separar
la cognición humana en implementación y dos tipos de juicio dentro de un modelo
iterativo de augmentation. Eso permite explicar con un solo lenguaje por qué una
herramienta puede comprimir brechas de ejecución y simultáneamente amplificar
brechas de juicio.

Predecesores inmediatos:

- Agrawal, Gans y Goldfarb (2019), sobre predicción versus juicio;
- Agrawal, Gans y Goldfarb (2023), *The Turing Transformation*, sobre
  automatización, augmentation y skill premia;
- Acemoglu y Autor (2011), como base del enfoque de tareas y habilidades.

Continuaciones relacionadas:

- Agrawal, McHale y Oettl (2026) desarrollan modelos de tareas donde la IA
  aumenta productividad sin automatizar tareas;
- Gans y Goldfarb (2026), *O-Ring Automation*, estudian complementariedades y
  cuellos de botella entre tareas.

### 5. ¿Qué no convence?

Primero, el resultado distributivo central depende de independencia mutua entre
cuatro capacidades que económicamente parecen correlacionadas. Correlacionar
juicio y habilidad agrega términos de covarianza que pueden desplazar o eliminar
el giro.

Segundo, la Proposición 3 mezcla un resultado local válido con una afirmación
global más fuerte: (H) entrega una caída inicial, pero no el signo en uno ni la
validez de la fórmula después de que esfuerzo llega a cero. Esta no es una
objeción de gusto; es una brecha algebraica reproducible.

## 12. Cómo explicarlo en cinco minutos

1. Abra con las tres capacidades y diga que “skill” no es un escalar único.
2. Muestre el problema del agente y el multiplicador $\Gamma$.
3. Presente $V(\theta)=\Gamma(K\alpha^2s+\theta/s)$ como la ecuación que contiene
   todo el mecanismo distributivo.
4. Distinga nivel total de beneficio individual.
5. Cierre con el veredicto: U condicional; condición faltante en $\theta=1$;
   esquina omitida para herramientas muy buenas.


## 13. Extensión exacta de este repositorio: la esquina elimina la U en el ejemplo

Una vez imponemos \(e\ge0\), el óptimo de cada tipo es
\(e^*(\theta,s)=\max\{4s-\theta/s,0\}\). Por tanto, el tipo
\(s_L=3/5\) llega a la esquina en \(36/25=1.44\), mientras
\(s_H=1\) llega a ella en \(\theta=4\).

Sea \(D(\theta)=V_H(\theta)-V_L(\theta)\). Al sustituir el valor
interior cuando el tipo trabaja y \(V_s(\theta)=4\sqrt{\theta}\)
cuando tiene esfuerzo cero, obtenemos

$$
D(\theta)=
\begin{cases}
\frac85-\frac{2\theta}{3}, &0\le\theta\le36/25,\\
(\sqrt{\theta}-2)^2,&36/25\le\theta\le4,\\
0,&\theta\ge4.
\end{cases}
$$

En el primer tramo, \(D'=-2/3\). En el segundo,
\(D'=1-2/\sqrt\theta\le0\). Como \(D\ge0\),
la varianza entre ambos tipos es \(D^2/4\): **cae hasta cero
y después permanece constante**. El giro \(12/5\) pertenece
solo a una extrapolación inválida de la fórmula interior.

No ocurre lo mismo con la *dispersión de los beneficios individuales*.
La diferencia inicial de valores es \(D(0)=8/5\), de modo que

$$
\operatorname{Var}\big(V(\theta)-V(0)\big)
=\frac14\big(D(\theta)-8/5\big)^2.
$$

Esta última **aumenta hasta \(16/25\)** y luego permanece constante,
aunque la dispersión de los niveles totales esté disminuyendo.
La explicación es que el instrumento beneficia más al tipo
inicialmente rezagado y termina igualando niveles, no ganancias.

**Limitación indispensable:** al alcanzar el óptimo interior,
\(p^*=\alpha\Delta s/2=2s\), de modo que \(p^*>1\)
para ambos tipos. Este ejercicio es una extensión algebraica
del índice \(\sqrt{se+\theta}\), no una calibración admisible
de una verdadera probabilidad de éxito. Una normalización
de \(p\) exige resolver nuevamente el problema.
