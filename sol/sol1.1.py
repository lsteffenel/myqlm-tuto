# 1.1 - 50% for value 4 and 50% for value 6


from qat.lang.AQASM import Program
from qat.lang.AQASM import H, X, CNOT, CCNOT

epr_prog = Program()

qbits = epr_prog.qalloc(3)

epr_prog.apply(X,qbits[0])
epr_prog.apply(H,qbits[1])

circuit = epr_prog.to_circ()
%qatdisplay --svg circuit

from qat.qpus import PyLinalg
qpu = PyLinalg()
job = circuit.to_job()
result = qpu.submit(job)

for sample in result:
    print("State", sample.state, "with probability :", sample.probability)