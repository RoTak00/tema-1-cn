import sympy as sp

x = sp.Symbol("x")
y = sp.Symbol("y")

a,b = sp.symbols("a,b")
f = x**2 + 2 * x + 5
g = x ** 2 + y **3 + 2 * x* y

print(f'f(1) = {f.subs(x, 1)}')

print(f'g(1, 2) = {sp.simplify(g.subs({x:x+1, y:x+2}))}')
print(f'g(1, 2) = {g.subs([(x,1),(y,2)])}')

print(f'g(1, 2) = {(g.expand({x:x+1, y:x+2}))}')
sp.pprint(g.subs({x:x+1, y:x+2}))

sp.pprint(g.diff(x))

t = sp.Symbol("xi")
exp = sp.sin(x) * t

sp.pprint(exp.diff(x))