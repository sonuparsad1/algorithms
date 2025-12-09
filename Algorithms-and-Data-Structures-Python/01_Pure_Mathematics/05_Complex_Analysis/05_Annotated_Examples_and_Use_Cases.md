# Complex Analysis: Annotated Examples and Use Cases

## 1. Electrical Engineering: AC Circuits

**Concept**: Impedance.
*   Resistors: Real. $R$.
*   Inductors: Imaginary. $j\omega L$.
*   Capacitors: Imaginary negative. $1/(j\omega C)$.
*   **Ohm's Law**: $V = I Z$ (Complex numbers).
*   Greatly simplifies differential equations to algebraic equations.

## 2. Fluid Dynamics: Potential Flow

**Concept**: Modeling ideal (inviscid, incompressible) flow in 2D.
*   Velocity Potential $\phi$. Stream Function $\psi$.
*   Complex Potential: $w(z) = \phi + i \psi$.
*   Velocity vector field is $\overline{w'(z)}$.
*   **Joukowski Transform**: Maps circle to airfoil shape. Foundational for early aeronautics.

## 3. Quantum Mechanics

**Wavefunction**: $\Psi(x, t)$ is complex-valued.
*   Probability: $|\Psi|^2$.
*   Phase is physically meaningful (Interference).
*   Schrödinger Equation involves $i$: $i \hbar \frac{\partial}{\partial t} \Psi = \hat{H} \Psi$.

## 4. Control Theory: Root Locus

**Problem**: Stability of feedback systems.
**poles**: Roots of denominator of Transfer Function $H(s)$.
**Condition**: System is stable if all poles have **negative real part** (Left Half Plane).
**Nyquist Plot**: Contour integral of transfer function to count poles around origin.
