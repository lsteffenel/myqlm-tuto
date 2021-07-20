# 6 - Adder

from qat.lang.AQASM import Program
from qat.lang.AQASM import H, X, CNOT, CCNOT

epr_prog = Program()

N1 = epr_prog.qalloc(4)
N2 = epr_prog.qalloc(4)

## exercice 1.1 - 4/6
epr_prog.apply(X,N1[1])
epr_prog.apply(H,N1[2])

## exercice 1.1 - 2/3
epr_prog.apply(X,N2[2])
epr_prog.apply(H,N2[3])

# adder
epr_prog.apply(CNOT, N1[0], N2[0])
epr_prog.apply(CNOT.ctrl(1), N1[1], N2[1], N2[0])
epr_prog.apply(CNOT, N1[1], N2[1])
epr_prog.apply(CNOT.ctrl(2), N1[2], N2[2], N2[1], N2[0])
epr_prog.apply(CNOT.ctrl(1), N1[2], N2[2], N2[1])
epr_prog.apply(CNOT, N1[2], N2[2]) 



circuit = epr_prog.to_circ()
%qatdisplay --svg circuit

from qat.qpus import PyLinalg
qpu = PyLinalg()
job = circuit.to_job()
result = qpu.submit(job)

for sample in result:
    print("State", sample.state, "with probability :", sample.probability)
    