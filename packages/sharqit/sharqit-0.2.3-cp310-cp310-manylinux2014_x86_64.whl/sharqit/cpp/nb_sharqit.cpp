/**
 * @file nb_sharqit.cpp
 * @brief definition of python-wrapper using nanobind
 */

#include <nanobind/nanobind.h>
#include <nanobind/operators.h>
#include <nanobind/stl/string.h>
#include <nanobind/stl/vector.h>
#include <nanobind/stl/tuple.h>
#include <nanobind/stl/map.h>
#include <nanobind/stl/pair.h>
#include <nanobind/stl/set.h>
#include <nanobind/stl/list.h>
#include <nanobind/stl/optional.h>
#include <nanobind/stl/bind_vector.h>

namespace nb = nanobind;

#include "sharqit.h"

NB_MODULE(sharqit_base, m) {
  nb::class_<Sharqit::Phase>(m, "Phase")
    .def(nb::init<const int32_t>())
    .def(nb::init<const int32_t, const int32_t>())
    .def(nb::init<const std::string&>())
    .def("to_string", &Sharqit::Phase::to_string, nb::arg("pi_str") = false,
	 "get a string of the Phase.")
    .def("__str__", &Sharqit::Phase::to_string, nb::arg("pi_str") = false)
    .def(nb::self + nb::self)
    .def(nb::self - nb::self)
    .def(nb::self += nb::self)
    .def(nb::self -= nb::self)
    .def(nb::self *= int32_t())
    .def(nb::self /= int32_t())
    .def(int() * nb::self)
    .def(nb::self * int())
    .def(nb::self / int())
    .doc() = "Phase of rotation gate"
    ;
  nb::enum_<Sharqit::QGateKind>(m, "QGateKind")
    .value("X", Sharqit::QGateKind::X,
	   "Pauli-X gate")
    .value("Z", Sharqit::QGateKind::Z,
	   "Pauli-X gate")
    .value("S", Sharqit::QGateKind::S,
	   "S gate")
    .value("Sdg", Sharqit::QGateKind::Sdg,
	   "Hermitian conjugate of S gate")
    .value("T", Sharqit::QGateKind::T,
	   "T gate")
    .value("Tdg", Sharqit::QGateKind::Tdg,
	   "Hermitian conjugate of T gate")
    .value("H", Sharqit::QGateKind::H,
	   "Hadamard gate")
    .value("RZ", Sharqit::QGateKind::RZ,
	   "RZ gate")
    .value("CX", Sharqit::QGateKind::CX,
	   "CNOT gate")
    .value("CZ", Sharqit::QGateKind::CZ,
	   "controlled RZ gate")
    .value("Id", Sharqit::QGateKind::Id,
	   "single qubit identity gate")
    .value("Id2", Sharqit::QGateKind::Id2,
	   "two qubit identity gate")
    .export_values();
  nb::class_<Sharqit::QGate>(m, "QGate")
    .def(nb::init<const Sharqit::QGateKind, const std::vector<uint32_t>&, const Sharqit::Phase&,
	 const std::vector<uint32_t>>(), nb::arg("kind") = Sharqit::QGateKind::Id,
	 nb::arg("qid") = std::vector<uint32_t>(1, 0),
	 nb::arg("phase") = Sharqit::Phase(0),
	 nb::arg("pol") = std::vector<uint32_t>(0))
    .def(nb::init<const std::string&>(), nb::arg("qgate_str"))
    .def("to_string", &Sharqit::QGate::to_string, nb::arg("pi_str") = false,
	 "get a string of the QGate.")
    .def("__str__", &Sharqit::QGate::to_string, nb::arg("pi_str") = false)
    .def("name", &Sharqit::QGate::name, nb::arg("pi_str") = false,
	 "get a string of the QGate name.")
    .def_prop_rw("kind",
		 [](Sharqit::QGate& qgate) { return qgate.kind() ; },
		 [](Sharqit::QGate& qgate, Sharqit::QGateKind kind) { qgate.kind(kind) ; },
		 "kind of the QGate.")
    .def_prop_rw("qid",
		 [](Sharqit::QGate& qgate) { return qgate.qid() ; },
		 [](Sharqit::QGate& qgate, std::vector<uint32_t>& qid) { qgate.qid(qid) ; },
		 "qubit indexes of the QGate")
    .def_prop_rw("phase",
		 [](Sharqit::QGate& qgate) { return qgate.phase() ; },
		 [](Sharqit::QGate& qgate, Sharqit::Phase& phase) { qgate.phase(phase) ; },
		 "phase of the rotation gate.")
    .def_prop_rw("pol",
		 [](Sharqit::QGate& qgate) { return qgate.pol() ; },
		 [](Sharqit::QGate& qgate, std::vector<uint32_t>& pol) { qgate.pol(pol) ; },
		 "polarities of control qubits.")
    .doc() = "Quantum Gate"
     ;
  nb::class_<Sharqit::QCirc>(m, "QCirc")
    .def(nb::init<>())
    .def("to_string", &Sharqit::QCirc::to_string, nb::arg("width") = 100,
	 "show the quantum circuit diagram as an ascii string.")
    .def("__str__", &Sharqit::QCirc::to_string, nb::arg("width") = 100)
    .def("show", &Sharqit::QCirc::show, nb::arg("width") = 100,
	 "show the quantum circuit diagram as an ascii string.")
    .def("print_qcirc", &Sharqit::QCirc::print_qcirc,
	 "print the QCirc.")
    .def("print_stats", &Sharqit::QCirc::print_stats,
	 "print stats of the QCirc.")
    .def("is_equal", [](Sharqit::QCirc& qc, Sharqit::QCirc& other) { return qc.is_equal(other); },
      "is the quantum circuit equal to the other.")
    .def("save", &Sharqit::QCirc::save, nb::arg("file_name"),
	 "save the quantum circuit to a file.")
    .def("load", &Sharqit::QCirc::load, nb::arg("file_name"),
	 "load the quantum circuit from a file.")
    .def("id", &Sharqit::QCirc::id, nb::arg("q"),
	 "add an identity gate to the quantum circuit.")
    .def("x", &Sharqit::QCirc::x, nb::arg("q"),
	 "add a pauli-X gate to the quantum circuit.")
    .def("z", &Sharqit::QCirc::z, nb::arg("q"),
	 "add a pauli-Z gate to the quantum circuit")
    .def("s", &Sharqit::QCirc::s, nb::arg("q"),
	 "add a S gate to the quantum circuit.")
    .def("sdg", &Sharqit::QCirc::sdg, nb::arg("q"),
	 "add a S+ (Hermitian conjugate of the S gate) gate to the quantum circuit.")
    .def("t", &Sharqit::QCirc::t, nb::arg("q"),
	 "add a T gate to the quantum circuit.")
    .def("tdg", &Sharqit::QCirc::tdg, nb::arg("q"),
	 "add a T+ (Hermitian conjugate of the T gate) gate to the quantum circuit.")
    .def("h", &Sharqit::QCirc::h, nb::arg("q"),
	 "add an H (hadamard) gate to the quantum circuit.")
    .def("rz", &Sharqit::QCirc::rz, nb::arg("q"), nb::arg("phase") = Sharqit::Phase(0),
	 "add a RZ gate to the quantum circuit.")
    .def("id2", &Sharqit::QCirc::id2, nb::arg("q0"), nb::arg("q1"),
	 "add a two-qubit identity gate.")
    .def("cx", &Sharqit::QCirc::cx, nb::arg("con"), nb::arg("tar"), nb::arg("pol") = std::vector<uint32_t>(1,0),
	 "add a CX (CNOT) gate to the quantum circuit.")
    .def("cz", &Sharqit::QCirc::cz, nb::arg("con"), nb::arg("tar"), nb::arg("pol") = std::vector<uint32_t>(1,0),
	 "add a CZ gate to the quantum circuit.")
    .def("rx", &Sharqit::QCirc::rx, nb::arg("q"), nb::arg("phase") = Sharqit::Phase(0),
	 "add a CX (CNOT) gate to the quantum circuit.")
    .def("y", &Sharqit::QCirc::y, nb::arg("q"),
	 "add a pauli-Y gate to the quamtum circuit.")
    .def("sx", &Sharqit::QCirc::sx, nb::arg("q"),
	 "add a sqrt-X (squre root of pauli-X) gate to the quantum circuit.")
    .def("sxdg", &Sharqit::QCirc::sxdg, nb::arg("q"),
	 "add a sqrt-X+ (squre root of pauli-X) gate to the quantum circuit.")
    .def("ry", &Sharqit::QCirc::ry, nb::arg("q"), nb::arg("phase") = Sharqit::Phase(0),
	 "add a RY gate to the quantum circuit.")
    .def("p", &Sharqit::QCirc::p, nb::arg("q"), nb::arg("phase") = Sharqit::Phase(0),
	 "add a P (phase shift) gate to the quantum circuit.")
    .def("cy", &Sharqit::QCirc::cy, nb::arg("con"), nb::arg("tar"),
	 "add a CY (controlled-Y) gate to the quantum circuit.")
    .def("csx", &Sharqit::QCirc::csx, nb::arg("con"), nb::arg("tar"),
	 "add a controlled-sqrt-X gate to the quantum circuit.")
    .def("csxdg", &Sharqit::QCirc::csxdg, nb::arg("con"), nb::arg("tar"),
	 "add a hermitian conjugate of controlled-sqrt-X gate to the quantum circuit.")
    .def("ch", &Sharqit::QCirc::ch, nb::arg("con"), nb::arg("tar"),
	 "add a CH (controlled-hadamard) gate to the quantum circuit.")
    .def("cs", &Sharqit::QCirc::cs, nb::arg("con"), nb::arg("tar"),
	 "add a CS (controlled-S) gate to the quantum circuit.")
    .def("csdg", &Sharqit::QCirc::csdg, nb::arg("con"), nb::arg("tar"),
	 "add a CS+ (hermitian conjugate of controlled-S) gate to the quantum circuit.")
    .def("ct", &Sharqit::QCirc::ct, nb::arg("con"), nb::arg("tar"),
	 "add a CT (controlled-T) gate to the quantum circuit.")
    .def("ctdg", &Sharqit::QCirc::ctdg, nb::arg("con"), nb::arg("tar"),
	 "add a CT+ (hermitian conjugate of controlled-T) gate to the quantum circuit.")
    .def("crx", &Sharqit::QCirc::crx, nb::arg("con"), nb::arg("tar"), nb::arg("phase") = Sharqit::Phase(0),
	 "add a controlled-RX gate to the quantum circuit.")
    .def("cry", &Sharqit::QCirc::cry, nb::arg("con"), nb::arg("tar"), nb::arg("phase") = Sharqit::Phase(0),
	 "add a controlled-RY gate to the quantum circuit.")
    .def("crz", &Sharqit::QCirc::crz, nb::arg("con"), nb::arg("tar"), nb::arg("phase") = Sharqit::Phase(0),
	 "add a controlled-RZ gate to the quantum circuit.")
    .def("cp", &Sharqit::QCirc::cp, nb::arg("con"), nb::arg("tar"), nb::arg("phase") = Sharqit::Phase(0),
	 "add a controlled-P gate to the quantum circuit.")
    .def("rxx", &Sharqit::QCirc::rxx, nb::arg("q0"), nb::arg("q1"), nb::arg("phase") = Sharqit::Phase(0),
	 "add a ising coupling gate (XX-interaction) to the quantum circuit.")
    .def("ryy", &Sharqit::QCirc::ryy, nb::arg("q0"), nb::arg("q1"), nb::arg("phase") = Sharqit::Phase(0),
	 "add a ising coupling gate (YY-interaction) to the quantum circuit.")
    .def("rzz", &Sharqit::QCirc::rzz, nb::arg("q0"), nb::arg("q1"), nb::arg("phase") = Sharqit::Phase(0),
	 "add a ising coupling gate (ZZ-interaction) to the quantum circuit.")
    .def("sw", &Sharqit::QCirc::sw, nb::arg("q0"), nb::arg("q1"),
	 "add a swap gate to the quantum circuit.")
    .def("csw", &Sharqit::QCirc::csw, nb::arg("con"), nb::arg("q0"), nb::arg("q1"),
	 "add a controlled swap (fredkin) gate to the quantum circuit.")
    .def("ccx", &Sharqit::QCirc::ccx, nb::arg("c0"), nb::arg("c1"), nb::arg("tar"),
	 nb::arg("pol") = std::vector<uint32_t>(2, 0),
	 "add a controlled cnot (toffoli) gate to the quantum circuit.")
    .def("ccz", &Sharqit::QCirc::ccz, nb::arg("c0"), nb::arg("c1"), nb::arg("tar"),
	 nb::arg("pol") = std::vector<uint32_t>(2, 0),
	 "add a controlled CZ gate to the quantum circuit.")
    .def("x_count", &Sharqit::QCirc::x_count,
	 "get a number of pauli-X gates in the quantum circuit.")
    .def("z_count", &Sharqit::QCirc::z_count,
	 "get a number of pauli-Z gates in the quantum circuit.")
    .def("h_count", &Sharqit::QCirc::h_count,
	 "get a number of H gates in the quantum circuit.")
    .def("s_count", &Sharqit::QCirc::s_count,
	 "get a number of S and S+ gates in the quantum circuit.")
    .def("t_count", &Sharqit::QCirc::t_count,
	 "get a number of T and T+ gates in the quantum circuit.")
    .def("rz_count", &Sharqit::QCirc::rz_count,
	 "get a number of RZ gates in the quantum circuit.")
    .def("cx_count", &Sharqit::QCirc::cx_count,
	 "get a number of CX (CNOT) gates in the quantum circuit.")
    .def("cz_count", &Sharqit::QCirc::cz_count,
	 "get a number of CZ gates in the quantum circuit.")
    .def("twoq_count", &Sharqit::QCirc::twoq_count,
	 "get a number of two-qubit gates in the quantum circuit.")
    .def("ccx_count", &Sharqit::QCirc::ccx_count,
	 "get a number of CCX gates in the quantum circuit.")
    .def("ccz_count", &Sharqit::QCirc::ccz_count,
	 "get a number of CCZ gates in the quantum circuit.")
    .def("tof_count", &Sharqit::QCirc::tof_count,
	 "get a number of Toffoli gates (CCX and CCZ gates) in the quantum circuit.")
    .def("gate_count", &Sharqit::QCirc::gate_count,
	 "get a number of the quantum gates except to identity gates.")
    .def("depth", &Sharqit::QCirc::depth,
	 "get a depth of the quantum circuit.")
    .def("qubit_num", [](Sharqit::QCirc& qc) { return qc.qubit_num(); },
	 "get a number of the qubits.")
    .def("add_random", &Sharqit::QCirc::add_random_str, nb::arg("qubit_num"), nb::arg("qgate_num"), nb::arg("probs"),
	 "add a random quantum circuit to the quantum circuit.")
    .def("add_qgate", nb::overload_cast<const std::string&>(&Sharqit::QCirc::add_qgate), nb::arg("qgate_str"),
	 "add a quantum gate to the quantum circuit.")
    .def("add_qgate", nb::overload_cast<const Sharqit::QGate&>(&Sharqit::QCirc::add_qgate), nb::arg("qgate"),
	 "add a quantum gate to the quantum circuit.")
    .def("add_qgate", nb::overload_cast<const Sharqit::QGateKind, const std::vector<uint32_t>&,
	 const Sharqit::Phase&, const std::vector<uint32_t>&>(&Sharqit::QCirc::add_qgate),
	 nb::arg("kind"), nb::arg("qid"), nb::arg("phase") = Sharqit::Phase(0),
	 nb::arg("pol") = std::vector<uint32_t>(0), 
	 "add a quantum gate to the quantum circuit.")
    .def("add_qcirc", &Sharqit::QCirc::add_qcirc, nb::arg("qc"),
	 "add a quantum circuit to the quantum circuit.")
    .def("get_qgate", &Sharqit::QCirc::get_qgate, nb::arg("i"),
	 "get a quantum gate.")
    .def("get_qgates", &Sharqit::QCirc::get_qgates,
	 "get a list of quantum gates.")
    .def("inverse", &Sharqit::QCirc::inverse,
	 "inverse gates.")
    .def("decomp_tof", &Sharqit::QCirc::decomp_tof,
	 "decompose Toffoli gates.")
    .def(nb::self + nb::self)
    .def(nb::self += nb::self)
    .doc() = "Quantum Circuit"
    ;
  nb::class_<Sharqit::Optimizer>(m, "Optimizer")
    .def(nb::init<>())
    .def("show", &Sharqit::Optimizer::show,
	 "show the optimizing result.")
    .def("proc_time", &Sharqit::Optimizer::get_proc_time,
	 "get the processing time (sec).")
    .def("reduce_gates", &Sharqit::Optimizer::reduce_gates, nb::arg("qc"), nb::arg("method") = "zx",
	 "reduce the gate count.")
    .doc() = "Quantum Optimizer"
    ;
}
