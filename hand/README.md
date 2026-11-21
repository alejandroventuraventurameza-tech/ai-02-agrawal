# Required handwritten check

Add a real phone photo named `prop3-derivation.jpg` to this directory. Do not
replace this requirement with typeset mathematics or an AI-generated image.

Write and photograph these steps:

1. Start from
   $M(e;\theta)=\alpha\Delta\sqrt{se+\theta}-e$.
2. Derive the FOC and solve
   $e^*(\theta)=\alpha^2\Delta^2s/4-\theta/s$.
3. Record the genuine interior condition
   $\theta<\alpha^2\Delta^2s^2/4$.
4. Write
   $V(\theta)=\Gamma(\alpha^2\Delta^2s/4+\theta/s)$.
5. Differentiate the cross-sectional variance:
   $d\operatorname{Var}(V)/d\theta=a_0+2\theta\operatorname{Var}(\Gamma/s)$.
6. Circle the missing implication: $a_0<0$ gives $\theta^*>0$, but the sign at
   $\theta=1$ is positive only if $\theta^*<1$.
7. Separately derive
   $\operatorname{Var}(V(\theta)-V(0))=\theta^2\operatorname{Var}(\Gamma/s)$.

Cross-outs are welcome: the purpose is to show the step that was independently
checked rather than accepted from the model or the LLM.

## Guía completa para la comprobación manuscrita

Esta guía prepara el cálculo que debes reconstruir y comprobar en papel.
No constituye evidencia manuscrita: la foto real sigue pendiente.
Puedes usar dos hojas y fotografiarlas juntas con las ecuaciones legibles.

### Hoja 1: esfuerzo y valor interior

Escribe el título **«Proposición 3: comprobación del esfuerzo y la varianza»**.
Mantén $\alpha>0$, $\Delta>0$, $s>0$, $\theta\ge0$ y
$\Gamma=\gamma_0/(1-\delta\gamma)>0$, con $\delta\gamma<1$.

El agente resuelve

$$
\max_{e\ge0}\; M(e;\theta)=\alpha\Delta\sqrt{se+\theta}-e.
$$

En una solución interior:

$$
M_e=\frac{\alpha\Delta s}{2\sqrt{se+\theta}}-1=0
\quad\Longrightarrow\quad
\sqrt{se^*+\theta}=\frac{\alpha\Delta s}{2}.
$$

Eleva al cuadrado y despeja:

$$
se^*+\theta=\frac{\alpha^2\Delta^2s^2}{4},\qquad
e^*(\theta)=\frac{\alpha^2\Delta^2s}{4}-\frac{\theta}{s}.
$$

Comprueba el máximo y su dominio:

$$
M_{ee}=-\frac{\alpha\Delta s^2}{4(se+\theta)^{3/2}}<0,
\qquad
e^*>0\iff\theta<\frac{\alpha^2\Delta^2s^2}{4}.
$$

Sustituye la FOC en el valor, sin saltarte la resta del esfuerzo:

$$
\begin{aligned}
M(e^*;\theta)
&=\alpha\Delta\frac{\alpha\Delta s}{2}
-\left(\frac{\alpha^2\Delta^2s}{4}-\frac{\theta}{s}\right)\\
&=\frac{\alpha^2\Delta^2s}{4}+\frac{\theta}{s},\\
V(\theta)&=\Gamma\left(\frac{\alpha^2\Delta^2s}{4}
+\frac{\theta}{s}\right).
\end{aligned}
$$

Anota: **«Esta fórmula exige interioridad para cada agente en el intervalo
estudiado»**. Cuando se alcanza la esquina, el esfuerzo es cero y esta fórmula
interior deja de describir el valor.

### Hoja 2: varianza, condición faltante y beneficio individual

La varianza es transversal, entre agentes; $\theta$ es común a todos.
Supón independencia mutua de $\alpha,\gamma_0,\gamma,s$ y los momentos
finitos necesarios para estas varianzas. Define

$$
A=\frac{\Delta^2}{4}\Gamma\alpha^2s,\qquad
C=\frac{\Gamma}{s},\qquad V(\theta)=A+\theta C.
$$

No supongas que $A$ y $C$ son independientes. Expande:

$$
\operatorname{Var}(V(\theta))
=\operatorname{Var}(A)+2\theta\operatorname{Cov}(A,C)
+\theta^2\operatorname{Var}(C).
$$

Calcula los dos términos de la covarianza usando la independencia original:

$$
E[AC]=\frac{\Delta^2}{4}E[\Gamma^2]E[\alpha^2],
$$

$$
E[A]E[C]=\frac{\Delta^2}{4}E[\Gamma]^2E[\alpha^2]E[s]E[1/s].
$$

Por tanto, con $\mu_s=E[s]$ y $q=\operatorname{Var}(\Gamma/s)$:

$$
\begin{aligned}
a_0=2\operatorname{Cov}(A,C)
&=\frac{\Delta^2E[\alpha^2]}{2}
\left(E[\Gamma^2]-E[\Gamma]^2\mu_sE[1/s]\right),\\
\frac{d\operatorname{Var}(V)}{d\theta}&=a_0+2\theta q.
\end{aligned}
$$

La condición de heterogeneidad da solamente el signo inicial:

$$
\frac{E[\Gamma^2]}{E[\Gamma]^2}<\mu_sE[1/s]
\quad\Longrightarrow\quad a_0<0.
$$

Para $q>0$, el cero algebraico de la derivada es

$$
\theta^*=-\frac{a_0}{2q}>0,\qquad
\left.\frac{d\operatorname{Var}(V)}{d\theta}\right|_{\theta=1}>0
\iff a_0+2q>0\iff\theta^*<1.
$$

**Rodea esta conclusión:** «$a_0<0$ no implica $\theta^*<1$. Una U válida
requiere además que el giro ocurra dentro de la región interior».

Comprueba un caso exacto, con dos habilidades igualmente probables:

$$
\alpha=1,\quad\Delta=4,\quad
\gamma_0=\frac45,\quad\gamma=\frac25,\quad\delta=\frac12,
\quad\Gamma=1,\quad s\in\left\{\frac35,1\right\}.
$$

$$
E[s]=\frac45,\quad E[1/s]=\frac43,\quad
1<\frac{16}{15},\quad q=\frac19,\quad
a_0=8\left(1-\frac{16}{15}\right)=-\frac8{15}.
$$

$$
\theta^*=\frac{12}{5}>1,\qquad
\left.\frac{d\operatorname{Var}(V)}{d\theta}\right|_1
=-\frac8{15}+\frac29=-\frac{14}{45}<0.
$$

El primer umbral de esfuerzo es $4(3/5)^2=36/25>1$, así que ambos tipos
permanecen interiores en $[0,1]$. Además,
$\mu_s=4/5>3\sigma_s=3/5$.
El cálculo usa la forma funcional de la Sección 4; no comprueba que la raíz
cuadrada esté acotada por uno como probabilidad literal, una limitación ya
documentada en `formal/VALIDATION_REPORT.md`.

Finalmente, distingue el beneficio individual del valor total:

$$
B(\theta)=V(\theta)-V(0)=\theta\frac{\Gamma}{s},\qquad
\operatorname{Var}(B(\theta))=\theta^2q,
\qquad\frac{d\operatorname{Var}(B)}{d\theta}=2\theta q>0
$$

para $\theta>0$ y $q>0$, dentro de la región interior.

Escribe tu propio veredicto después de comprobar las cuentas: la afirmación
incondicional de una U es incompleta; la condición de heterogeneidad no basta
para garantizar una derivada positiva en uno.

## Foto pendiente

Fotografía tu comprobación real y guarda el archivo como
`hand/prop3-derivation.jpg`. No marques el requisito como cumplido hasta que
la foto exista y se haya revisado su legibilidad y contenido.

