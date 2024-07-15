from problog.program import PrologString
from problog import get_evaluatable

p = PrologString("""
% Define as variáveis aleatórias como estocásticas
0.9::street_condition(true).
0.1::street_condition(false).

0.4::flywheel_worn(true).
0.6::flywheel_worn(false).

0.4::light_bulb_ok(true).
0.6::light_bulb_ok(false).

0.99::cable_ok(true).
0.01::cable_ok(false).

% Define as probabilidades condicionais para 'dynamo_sliding'
% P(dynamo_sliding | street_condition, flywheel_worn)
0.05::dynamo_sliding(true) :- street_condition(true), flywheel_worn(true).
0.0  ::dynamo_sliding(true) :- street_condition(true), flywheel_worn(false).
0.6  ::dynamo_sliding(true) :- street_condition(false), flywheel_worn(true).
0.05 ::dynamo_sliding(true) :- street_condition(false), flywheel_worn(false).
dynamo_sliding(false) :- \+dynamo_sliding(true).

% Define as probabilidades condicionais para 'dynamo_shows_voltage'
% P(dynamo_shows_voltage | dynamo_sliding)
0.04::dynamo_shows_voltage(true) :- dynamo_sliding(true).
0.99::dynamo_shows_voltage(true) :- dynamo_sliding(false).
dynamo_shows_voltage(false) :- \+dynamo_shows_voltage(true).

% Define as probabilidades condicionais para 'light_is_on'
% P(light_is_on | dynamo_shows_voltage, light_bulb_ok, cable_ok)
light_is_on :- dynamo_shows_voltage(true), light_bulb_ok(true), cable_ok(true).
\+light_is_on :- \+dynamo_shows_voltage(true).
\+light_is_on :- \+light_bulb_ok(true).
\+light_is_on :- \+cable_ok(true).

% Consulta: P(dynamo_shows_voltage(true) | street_condition(true))
query(dynamo_shows_voltage(true)).
""")

result = get_evaluatable().create_from(p).evaluate()
print(result)
