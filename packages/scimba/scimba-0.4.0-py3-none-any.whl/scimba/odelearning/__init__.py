"""
Classes using the previous networks.
Equation types are splitted: ODE, spatial PDE, space-time and kinetic PDE.
Each equation is described by an abstract class and daughter classes.
PINN classes are used to build a network associated with an equation,
notably to manage derivatives. Each type fo PINNs use a specific trainer
"""
