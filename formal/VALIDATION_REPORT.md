# Informe de validación

## Veredicto

La parte algebraica central de la Proposición 3 ha quedado validada de forma
independiente en Lean y con aritmética racional exacta. La validación confirma
los siguientes resultados, siempre dentro de la región en la que la solución
de esfuerzo es interior:

1. el candidato de esfuerzo y su condición de interioridad son correctos;
2. la sustitución del candidato produce la fórmula cerrada del valor;
3. la ganancia individual es `theta Gamma / s`;
4. la derivada de la varianza total es afín en `theta` y tiene un único cero
   positivo si su intercepto es negativo y su pendiente es positiva;
5. la condición de heterogeneidad del paper solo hace negativo el intercepto;
6. para afirmar que la derivada ya es positiva en `theta = 1` hace falta además
   `theta* < 1`, equivalentemente `a0 + 2 Var(Gamma/s) > 0`;
7. existe un contraejemplo racional que satisface las condiciones listadas por
   el paper y mantiene esfuerzo interior en `[0, 1]`, pero cuya derivada en uno
   es negativa.

Por tanto, la conclusión rigurosa es una U **algebraica y condicional**: la
varianza cae inicialmente y gira en `theta*` si la fórmula interior sigue siendo
válida hasta ese punto. Las hipótesis declaradas no garantizan que el giro ocurra
antes de `theta = 1`.

## Fuente fijada

- Agrawal, Gans y Goldfarb (2025), *The Economics of Bicycles for the Mind*,
  NBER Working Paper 34034, 53 páginas.
- Página oficial: <https://www.nber.org/papers/w34034>
- SHA-256 de la copia examinada:
  `11B8F4EDA55480FCB1EAF4EE42598CE9C6640DA535ED0FA551FC7597EE7BAE8D`.

El hash fija el documento fuente: una versión posterior del working paper debe
volver a compararse contra este registro.

## Ledger: fuente, formalización y evidencia

| Objeto del paper | Declaración formal | Evidencia exacta | Estado |
|---|---|---|---|
| Candidato interior de esfuerzo, ecuación (58) | `effortCandidate` | evaluación por ambos tipos | validado |
| Condición de esfuerzo positivo derivada de (58) | `effortCandidate_pos_iff` | primera esquina `36/25 > 1` | validado |
| Identidad del input efectivo en el FOC | `effectiveInput_at_candidate` | comprobada para `s=3/5,1` | validado |
| Unicidad de la solución de la FOC despejada | `clearedFOC_iff_effortCandidate` | no necesaria | validado |
| Valor interior, ecuación (59) | `interiorValue_substitution` | comprobado para ambos tipos | validado |
| Valor de continuación, ecuación (60) | `continuationValue` | `Gamma=1` en el ejemplo | definición auditada |
| Ganancia individual `theta Gamma/s` | `individualGain_eq` | varianza de la ganancia `1/9` en `theta=1` | validado |
| Condición (30) y signo del intercepto (83) | `paperCondition_iff_negativeMomentGap`, `derivativeIntercept_neg_of_paperCondition` | `1 < 16/15`, `a0=-8/15` | validado |
| Derivada afín de la varianza, ecuación (81) | `varianceDerivative` | `a0=-8/15`, `q=1/9` | álgebra downstream validada |
| Punto de giro, ecuación (88) y fórmula (94) | `turningPoint_pos_and_zero` | `theta*=12/5` | validado |
| Signo positivo a la derecha del giro | `varianceDerivative_pos_iff_turningPoint_lt` | derivada en uno `-14/45` | validado |
| Varianza de la ganancia individual, derivada en la auditoría | `gainVariance_strictMono` | `Var(V(1)-V(0))=1/9` | validado |
| Afirmación de signo positivo en `theta=1` | `varianceDerivative_at_one_pos_iff` y `exact_counterexample` | falla en el ejemplo | refutada bajo las hipótesis publicadas |

La frase “álgebra downstream validada” es deliberada: Lean recibe `a0` y
`q = Var(Gamma/s)` como escalares reales. La deducción de la ecuación (87) desde
variables aleatorias e independencia se audita en la derivación humana, pero no
está codificada todavía en una teoría de probabilidad.

## Contraejemplo exacto

Se toman

```text
gamma0 = 4/5, gamma = 2/5, delta = 1/2  =>  Gamma = 1
alpha = 1, Delta = 4
s = 3/5 o s = 1, cada uno con probabilidad 1/2
```

Entonces

```text
E[s] = 4/5                       Var(s) = 1/25
E[1/s] = 4/3                     E[s]E[1/s] = 16/15 > 1
Var(Gamma/s) = 1/9               a0 = -8/15
theta* = 12/5                    d Var(V)/d theta |_(theta=1) = -14/45
primera esquina de esfuerzo = 36/25 > 1
Var(V(0)) = 16/25                Var(V(1)) = 49/225
```

El ejemplo satisface la condición de heterogeneidad y no usa la esquina de
esfuerzo en `[0,1]`. Aun así, la varianza total continúa cayendo en ese intervalo.
Esto separa limpiamente la omisión del endpoint de la posterior dificultad de
las soluciones de esquina.

## Qué verificó Lean

`formal/Proposition3.lean` compiló sin errores y no contiene `sorry`, `admit`,
`axiom` ni `native_decide`. Se utilizó una importación focalizada de
`EconCSLib.Foundations.Math.AffineThreshold`, no el agregado completo del
paquete.

Entorno reproducible usado:

```text
Lean                  4.30.0-rc2, commit 3dc1a088...
Lake                  5.0.0-src+3dc1a08
EconCSLib checkout    cf500b748ac63dbff55faf97d989d4935c8eff50
EconCSLib dependency  95fdc7dc863ff83e9d6c3a68fcb2505540462a4d
Mathlib dependency    5450b53e5ddc75d46418fabb605edbf36bd0beb6
```

Comandos de reproducción desde un checkout de EconCSLib con sus dependencias:

```text
lake env lean <ruta-al-repositorio>/formal/Proposition3.lean
python <ruta-al-repositorio>/formal/exact_audit.py
```

## Frontera de la validación

No se debe describir este trabajo como una formalización completa del paper.
Aún no están formalizados en Lean:

- el espacio de probabilidad y las variables aleatorias `alpha`, `Gamma` y `s`;
- el paso de independencia a las identidades de momentos y covarianzas;
- existencia y unicidad global del máximo con la restricción `e >= 0`;
- el cambio de régimen cuando el esfuerzo óptimo llega a cero;
- las Proposiciones 1, 2, 4 y 5;
- la interpretación literal de `sqrt(se+theta)` como probabilidad fuera de un
  dominio que asegure valores entre cero y uno.

Estas exclusiones no debilitan el contraejemplo: este ocurre dentro de `[0,1]`,
con esfuerzo estrictamente positivo. Sí delimitan con precisión qué puede
afirmarse como probado por máquina.

## Archivos de evidencia

- `formal/Proposition3.lean`: teoremas algebraicos comprobados por Lean.
- `formal/exact_audit.py`: contraejemplo con fracciones exactas.
- `sim.py`: exploración numérica y figura de la solución interior y de esquina.
- `extra/reading-roadmap.md`: orden lógico para reconstruir el modelo y sus
  proposiciones.
