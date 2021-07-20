# 4 - increment

from qat.lang.AQASM import Program
from qat.lang.AQASM import H, X, CNOT, CCNOT

epr_prog = Program()

qbits = epr_prog.qalloc(4)

## exercice 1.1
epr_prog.apply(X,qbits[1])
epr_prog.apply(H,qbits[2])

# increment
epr_prog.apply(CNOT.ctrl(2),qbits[3],  qbits[2], qbits[1], qbits[0])
epr_prog.apply(CCNOT, qbits[3], qbits[2], qbits[1]) 
epr_prog.apply(CNOT, qbits[3], qbits[2])
epr_prog.apply(X, qbits[3])

circuit = epr_prog.to_circ()
%qatdisplay --svg circuit

from qat.qpus import PyLinalg
qpu = PyLinalg()
job = circuit.to_job()
result = qpu.submit(job)

for sample in result:
    print("State", sample.state, "with probability :", sample.probability)